from ABConnect import ABConnectAPI
from datetime import datetime

start = datetime(2026, 1, 26, 12, 14)
end = datetime(2026, 1, 26, 12, 15)

api = ABConnectAPI()

job = 5649470

api.jobs.agent.oa(job, "9999AZ")
