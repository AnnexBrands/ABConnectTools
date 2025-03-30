class ABConnectError(Exception):
    """Base class for exceptions in this module."""

    pass


class RequestError(ABConnectError):
    """Exception raised for errors in the request."""

    def __init__(self, status_code, message, response=None):
        self.status_code = status_code
        self.message = message
        self.response = response
        super().__init__(f"HTTP {status_code} Error: {self.message}")


class NotLoggedInError(ABConnectError):
    """Exception raised when a user is not logged in."""

    def __init__(self, message="User is not logged in."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"
