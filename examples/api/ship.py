
import json
from ABConnect.api import ABConnectAPI

api = ABConnectAPI()

JOBID = 4675063
# ratesKey, choices = api.jobs.ship._get_choices(JOBID, "UPS12")
# ratesKey = ''
# print(f"Rates Key: {ratesKey}")
# print(f"Rates: {json.dumps(choices, indent=2, default=str)}")

# choose = api.jobs.freightproviders.post_freightproviders_ratequote(
#     optionIndex=4,
#     jobDisplayId=JOBID,
#     data={
#             "ratesKey": "",
#             "carrierCode": "",
#             "active": True
#         }
# )

# print(choose)
import datetime
print(datetime.datetime.now().isoformat())
data = {
  "quoteOptionIndex": 0,
  "shipOutDate": "2025-10-20T00:06:20.944Z",
  "documentByteCodeRequired": True
}