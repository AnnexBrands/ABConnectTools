from ABConnect.api.models.account import ForgotLoginModel
from ABConnect.api.models.shared import ServiceBaseResponse

from ABConnect import ABConnectAPI

abapi = ABConnectAPI()
m = abapi.models

# DELETE_PAYMENTSOURCE
# GET_PROFILE
# GET_VERIFYRESETTOKEN
# POST_CONFIRM


# POST_FORGOT

requestModel = ForgotLoginModel
forgotlogin = ForgotLoginModel(
    user_name="training",
    email="abconnect@annexbrands.com",
    forgot_type=m.ForgotType.USERNAME # ForgotType.PASSWORD
)

responseMopdel = ServiceBaseResponse
r = abapi.account.post_forgot(forgotlogin)
print(isinstance(r, ServiceBaseResponse))
print(r)

# POST_REGISTER
# POST_RESETPASSWORD
# POST_SEND_CONFIRMATION
# POST_SETPASSWORD
# PUT_PAYMENTSOURCE

