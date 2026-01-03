from ABConnect import ABConnectAPI

abapi = ABConnectAPI(env='staging', username='training')

token = abapi._request_handler.token_storage.get_token()

print(token['access_token'])