from ABConnect import ABConnectAPI

# abapi = ABConnectAPI(env='staging', username='instaquote')
abapi = ABConnectAPI(username='Brett')

token = abapi._request_handler.token_storage.get_token()

print(token['access_token'])