from ABConnect import ABConnectAPI

abapi = ABConnectAPI()

f = abapi.forms.get_hbl(100)

with open(f"/tmp/{f['name']}", "wb") as file:
    file.write(f['data'])
