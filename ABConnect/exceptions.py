class ABConnectError(Exception):
    """Base exception class for all ABConnect errors."""

    def __init__(self, message: str, *, code: str = None, details: dict = None):
        self.code = code
        self.details = details or {}
        super().__init__(message)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.args[0]}"

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} code={self.code!r} "
            f"message={self.args[0]!r} details={self.details!r}>"
        )

    def no_traceback(self):
        return self.with_traceback(None)

    def to_dict(self):
        return {
            "error": self.__class__.__name__,
            "code": self.code,
            "message": self.args[0],
            "details": self.details,
        }


class RequestError(ABConnectError):
    """Exception raised for HTTP request errors."""

    def __init__(self, status_code, message, response=None, *, code="REQUEST_ERROR"):
        details = {
            "status_code": status_code,
            "response": getattr(response, "text", str(response)),
        }
        super().__init__(
            f"HTTP {status_code} Error: {message}", code=code, details=details
        )
        self.status_code = status_code
        self.response = response


class NotLoggedInError(ABConnectError):
    """Exception raised when a user is not logged in."""

    def __init__(
        self, message="User is not logged in.", *, code="NOT_LOGGED_IN", details=None
    ):
        super().__init__(message, code=code, details=details)


class LoginFailedError(ABConnectError):
    """Exception raised when login fails."""

    def __init__(self, message="Login failed.", *, code="LOGIN_FAILED", details=None):
        super().__init__(message, code=code, details=details)
