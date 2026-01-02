import os
import json
import logging
import requests
import time
from abc import ABC, abstractmethod
from ABConnect.exceptions import LoginFailedError
from ABConnect.config import Config, get_config
from appdirs import user_cache_dir

logger = logging.getLogger(__name__)


class TokenStorage(ABC):
    @property
    def identity_url(self):
        return Config.get_identity_url()

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

    def _identity_body(self):
        return {
            "rememberMe": True,
            "scope": "offline_access",
            "client_id": get_config("ABC_CLIENT_ID"),
            "client_secret": get_config("ABC_CLIENT_SECRET"),
        }

    def _call_login(self, data):
        r = requests.post(self.identity_url, data=data)
        if r.ok:
            resp = r.json()
            self.set_token(resp)
            logger.info(
                f"Login successful for user {data.get('username')} using grant_type {data.get('grant_type')}"
            )
        else:
            msg = f"Login failed for {data.get('username')}: {r.status_code} {r.text}"
            logger.error(msg)
            raise LoginFailedError(msg).no_traceback()

    def _login(self):
        data = {
            "grant_type": "password",
            **self._get_creds(),
            **self._identity_body(),
        }
        self._call_login(data)

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

    @abstractmethod
    def _get_creds(self):
        """Return dict with 'username' and 'password' keys for credential login."""
        pass


class SessionTokenStorage(TokenStorage):
    def __init__(self, *args, **kwargs):
        self._token = None
        self.request = kwargs["request"]
        self._load_token()

    def _load_token(self):
        if "abc_token" in self.request.session:
            self._token = self.request.session["abc_token"]
            if not self.expired:
                logger.info(f"From ABConnect.api.auth._load_token() -- Success")
                return
        if (
            hasattr(self.request.user, "refresh_token")
            and self.request.user.refresh_token
        ):
            self._token = {"refresh_token": self.request.user.refresh_token}
            if self.refresh_token():
                return
        self._login()

    def _get_creds(self):
        if "username" in self._creds and "password" in self._creds:
            return {
                "username": self._creds["username"],
                "password": self._creds["password"],
            }
        else:
            if (
                hasattr(self.request, "user")
                and hasattr(self.request.user, "username")
                and hasattr(self.request.user, "pw")
            ):
                return {
                    "username": self.request.user.username,
                    "password": self.request.user.pw,
                }

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

    def refresh_token(self):
        if self._token and "refresh_token" in self._token:
            refresh_token = self._token["refresh_token"]
        elif self.request.user.refresh_token:
            refresh_token = self.request.user.refresh_token
        else:
            return False

        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            **self._identity_body(),
        }
        try:
            self._call_login(data)
            return True
        except LoginFailedError:
            logger.info(
                "Refresh token expired or invalid, will attempt credential login"
            )
            return False


class FileTokenStorage(TokenStorage):
    def __init__(self, *args, **kwargs):
        self._resolve_creds(**kwargs)
        cache_dir = user_cache_dir("ABConnect")
        os.makedirs(cache_dir, exist_ok=True)

        # Include environment in filename to separate staging/production tokens
        env_suffix = "_staging" if Config._env == "staging" else ""
        self.path = os.path.join(cache_dir, f"token_{self.creds['username']}{env_suffix}.json")
        self._token = None
        self._load_token()

        if not self._token:
            raise RuntimeError("Failed to load or obtain a valid access token.")

    def _resolve_creds(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")

        if username and password:
            username = username.lower()
        elif username:
            username = username.lower()
            password = get_config(f"AB_USER_{username.upper()}")
            if not password:
                raise LoginFailedError(f"No password configured for user '{username}'")
        else:
            username = get_config("ABCONNECT_USERNAME")
            password = get_config("ABCONNECT_PASSWORD")
            if not (username and password):
                raise LoginFailedError("Default credentials (ABCONNECT_USERNAME/PASSWORD) not set")

        self.creds = {"username": username.lower(), "password": password}
    
    def _get_creds(self):
        return self.creds

    def _load_token(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r") as f:
                    self._token = json.load(f)
            except Exception as e:
                logger.error(f"Error reading token file: {e}")
        self.get_token()

    def get_token(self):
        if self.expired:
            logger.info(f"Token expired")
            if not self.refresh_token():
                self._login()
        return self._token

    def set_token(self, token):
        token["expires_at"] = self._calc_expires_at(token["expires_in"])
        self._token = token
        try:
            with open(self.path, "w") as f:
                json.dump(self._token, f)
        except Exception as e:
            print(f"Error writing token file: {e}")

    def refresh_token(self):
        if not self._token or "refresh_token" not in self._token:
            return False

        data = {
            "grant_type": "refresh_token",
            "refresh_token": self._token["refresh_token"],
            **self._identity_body(),
        }

        try:
            self._call_login(data)
            return True
        except LoginFailedError:
            logger.info(
                f"Refresh token failed for {self.creds['username']}"
            )
            return False
