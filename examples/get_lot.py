from ABConnect import ABConnectAPI
from ABConnect.api.models.catalog import LotDataDto

api = ABConnectAPI()
customerid = "225165902"
lotid = "625279"
lot = api.catalog.lots._get(lotid)

print(lot)
