import os
import json
import logging
import requests
import time
from abc import ABC, abstractmethod
from appdirs import user_cache_dir
from dotenv import load_dotenv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
dotenv_path = os.path.join(project_root, ".env")
load_dotenv(dotenv_path)

logger = logging.getLogger(__name__)
logger.error(f"ABConnect User: {os.getenv('ABCONNECT_USERNAME')}")

class TokenStorage(ABC):
    identity_url = 'https://login.abconnect.co/connect/token'
    
    def _calc_expires_at(self, expires_in: int, buffer: int = 300) -> float:
        return time.time() + expires_in - buffer
    
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

# TODO
class SessionTokenStorage(TokenStorage):
    def __init__(self, request):
        self.request = request

    def get_token(self):
        return self.request.session.get("abc_token")['access_token']

    def set_token(self, token):
        self.request.session["abc_token"] = token

    def _get_creds_from_env(self):
        # TODO mixin oauth flow
        return None

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
                with open(self.path, 'r') as f:
                    data = json.load(f)
                    self._token = data.get("access_token")
                    self._refresh = data.get("refresh_token")
            except Exception as e:
                print(f"Error reading token file: {e}")
        if self.expired:
            if not self.refresh_token():
                self._login()

    def _save_token(self):
        try:
            with open(self.path, 'w') as f:
                json.dump({"token": self._token}, f)
        except Exception as e:
            print(f"Error writing token file: {e}")

    def _get_creds_from_env(self):
        username = os.getenv("ABCONNECT_USERNAME")
        password = os.getenv("ABCONNECT_PASSWORD")
        if username and password:
            return {"username": username, "password": password}
        return None

    def _identity_body(self):
        return {
            'rememberMe': True,
            'scope': 'offline_access',
            'client_id': os.getenv("ABC_CLIENT_ID"),
            'client_secret': os.getenv("ABC_CLIENT_SECRET")
        }

    def _login(self):
        data = {
            'grant_type': 'password',
            **self._get_creds_from_env(),
            **self._identity_body()
        }
        r = requests.post(self.identity_url, data=data)
        if r.ok:
            resp = r.json()
            self.set_token(resp)


    def refresh_token(self):
        if not self._token or "refresh_token" not in self._token:
            return False
        
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self._token["refresh_token"],
            **self._identity_body()
        }
        
        r = requests.post(self.identity_url, data=data)
        if r.ok:
            resp = r.json()
            self.set_token(resp)
            return True
        return False

    def get_token(self):
        if self.expired:
            if not self.refresh_token():
                self._login()

        if not self.expired:
            return self._token["access_token"]

        raise Exception("Unable to retrieve a valid token. Login and refresh both failed.")

    def set_token(self, token):
        token['expires_at'] = self._calc_expires_at(token['expires_in'])
        self._token = token
        self._save_token()

    @property
    def expired(self) -> bool:
        if not self._token:
            return True
        expires_at = self._token.get("expires_at")
        if not expires_at:
            return True
        return time.time() >= expires_at