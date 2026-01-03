from ABConnect import ABConnectAPI

api = ABConnectAPI(env='staging', username='instaquote')
from ABConnect import models

f = api.forms.get_hbl(100)

with open(f"/tmp/{f['name']}", "wb") as file:
    file.write(f['data'])
