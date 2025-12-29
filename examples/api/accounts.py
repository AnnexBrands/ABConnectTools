from ABConnect import ABConnectAPI

abapi = ABConnectAPI()
from ABConnect.api import models

# DELETE_PAYMENTSOURCE
# GET_PROFILE
# GET_VERIFYRESETTOKEN
# POST_CONFIRM


# POST_FORGOT

requestModel = models.ForgotLoginModel
forgotlogin = models.ForgotLoginModel(
    user_name="training",
    email="abconnect@annexbrands.com",
    forgot_type=models.ForgotType.USERNAME # ForgotType.PASSWORD
)

responseModel = models.ServiceBaseResponse
r = abapi.account.post_forgot(forgotlogin)
print(isinstance(r, models.ServiceBaseResponse))
print(r)

# POST_REGISTER
# POST_RESETPASSWORD
# POST_SEND_CONFIRMATION
# POST_SETPASSWORD
# PUT_PAYMENTSOURCE

