from .Loader import FileLoader
from .Builder import APIRequestBuilder
from .Quoter import Quoter
from .api import ABConnectAPI

# Create models alias for convenient imports
# Usage: from ABConnect.models import ChangeJobAgentRequest
import sys
from .api import models
from .api import routes
sys.modules['ABConnect.models'] = models
sys.modules['ABConnect.routes'] = routes

__all__ = ["FileLoader", "APIRequestBuilder", "Quoter", "ABConnectAPI", "models", "routes"]

__version__ = "0.2.1"
VERSION = "0.2.1"