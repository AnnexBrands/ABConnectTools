from ABConnect import ABConnectAPI

abapi = ABConnectAPI()

token = abapi._request_handler.token_storage.get_token()

print(token['access_token'])