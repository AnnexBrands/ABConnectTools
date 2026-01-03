from ABConnect import ABConnectAPI

api = ABConnectAPI(env='staging', username='instaquote')
from ABConnect import models

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
r = api.account.post_forgot(forgotlogin)
print(isinstance(r, models.ServiceBaseResponse))
print(r)

# POST_REGISTER
# POST_RESETPASSWORD
# POST_SEND_CONFIRMATION
# POST_SETPASSWORD
# PUT_PAYMENTSOURCE

