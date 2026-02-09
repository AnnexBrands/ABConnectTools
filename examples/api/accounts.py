"""
Account API Examples - Login, registration, and password operations

Usage:
    python accounts.py              # Run all examples
    python accounts.py forgot       # Run a single example
    python accounts.py help         # List available examples
"""

from ABConnect import models
from _base import ExampleRunner


class AccountExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Account API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("forgot", "Post a forgot-username request", self.post_forgot)

    def post_forgot(self):
        forgotlogin = models.ForgotLoginModel(
            user_name="training",
            email="abconnect@annexbrands.com",
            forgot_type=models.ForgotType.USERNAME
        )
        r = self.api.account.post_forgot(forgotlogin)
        print(f"isinstance ServiceBaseResponse: {isinstance(r, models.ServiceBaseResponse)}")
        print(r)


if __name__ == "__main__":
    AccountExamples().run()
