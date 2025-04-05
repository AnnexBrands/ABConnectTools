import os
import json
import logging
import requests
import time
from abc import ABC, abstractmethod
from ABConnect.exceptions import LoginFailedError
from appdirs import user_cache_dir
from dotenv import dotenv_values

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

env = dotenv_values(".env")


class TokenStorage(ABC):
    identity_url = "https://login.abconnect.co/connect/token"

    def _calc_expires_at(self, expires_in: int, buffer: int = 300) -> float:
        return time.time() + expires_in - buffer

    @property
    def expired(self) -> bool:
        if not self._token:
            return True
        expires_at = self._token.get("expires_at")
        if not expires_at:
            return True
        return time.time() >= expires_at

    @abstractmethod
    def get_token(self):
        """Return the current bearer token."""
        pass

    @abstractmethod
    def set_token(self, token):
        """Store a new token."""
        pass

    @abstractmethod
    def refresh_token(self):
        """Refresh the token if needed and return the updated token."""
        pass


class SessionTokenStorage(TokenStorage):
    def __init__(self, request, creds={}):
        self.request = request
        self._token = None
        self._creds = creds
        self._load_token()

    def _load_token(self):
        # First try to get token from session
        if "abc_token" in self.request.session:
            self._token = self.request.session["abc_token"]
            if not self.expired:
                return

        # Then try to get refresh token from user model
        if (
            hasattr(self.request.user, "refresh_token")
            and self.request.user.refresh_token
        ):
            self._token = {"refresh_token": self.request.user.refresh_token}
            if self.refresh_token():
                return

        # Finally fall back to credential based login
        self._login()

    def _identity_body(self):
        return {
            "rememberMe": True,
            "scope": "offline_access",
            "client_id": os.getenv("ABC_CLIENT_ID"),
            "client_secret": os.getenv("ABC_CLIENT_SECRET"),
        }

    def _call_login(self, data):
        r = requests.post(self.identity_url, data=data)
        if r.ok:
            resp = r.json()
            self.set_token(resp)
        else:
            raise LoginFailedError().no_traceback()

    def _login(self):
        data = {
            "grant_type": "password",
            **self.creds(),
            **self._identity_body(),
        }
        self._call_login(data)

    def refresh_token(self):
        if self._token and "refresh_token" in self._token:
            refresh_token = self._token["refresh_token"]
        elif self.request.user.refresh_token:
            refresh_token = self.request.user.refresh_token
        else:
            return

        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            **self._identity_body(),
        }

        self._call_login(data)

    def get_token(self):
        if self.expired:
            if not self.refresh_token():
                self._login()
        return self._token

    def set_token(self, token):
        token["expires_at"] = self._calc_expires_at(token["expires_in"])
        self._token = token
        self.request.session["abc_token"] = token
        if hasattr(self.request.user, "refresh_token"):
            self.request.user.refresh_token = token.get("refresh_token")
            self.request.user.save()


class FileTokenStorage(TokenStorage):
    def __init__(self, filename=None):
        if filename is None:
            cache_dir = user_cache_dir("ABConnect")
            os.makedirs(cache_dir, exist_ok=True)
            filename = os.path.join(cache_dir, "token.json")
        self.path = filename
        self._token = None
        self._load_token()

        if not self._token:
            raise RuntimeError("Failed to load or obtain a valid access token.")

    def _load_token(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    self._token = json.load(f)
            except Exception as e:
                print(f"Error reading token file: {e}")
        self.get_token()

    def _save_token(self):
        try:
            with open(self.path, "w") as f:
                json.dump({"token": self._token}, f)
        except Exception as e:
            print(f"Error writing token file: {e}")

    def _get_creds(self):
        username = os.getenv("ABCONNECT_USERNAME")
        password = os.getenv("ABCONNECT_PASSWORD")
        return {"username": username, "password": password}

    def _identity_body(self):
        return {
            "rememberMe": True,
            "scope": "offline_access",
            "client_id": os.getenv("ABC_CLIENT_ID"),
            "client_secret": os.getenv("ABC_CLIENT_SECRET"),
        }

    def _login(self):
        data = {
            "grant_type": "password",
            **self._get_creds(),
            **self._identity_body(),
        }
        r = requests.post(self.identity_url, data=data)
        if r.ok:
            resp = r.json()
            self.set_token(resp)
        else:
            raise LoginFailedError().no_traceback()

    def refresh_token(self):
        if not self._token or "refresh_token" not in self._token:
            return False

        data = {
            "grant_type": "refresh_token",
            "refresh_token": self._token["refresh_token"],
            **self._identity_body(),
        }

        r = requests.post(self.identity_url, data=data)
        if r.ok:
            resp = r.json()
            self.set_token(resp)
            return True

    def get_token(self):
        if self.expired:
            if not self.refresh_token():
                self._login()
        return self._token

    def set_token(self, token):
        token["expires_at"] = self._calc_expires_at(token["expires_in"])
        self._token = token
        self._save_token()
