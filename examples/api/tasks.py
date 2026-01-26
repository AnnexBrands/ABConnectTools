from ABConnect import ABConnectAPI, models
from _constants import JOB_DISPLAY_ID, START

api = ABConnectAPI(env='staging', username='instaquote')

r = api.jobs.timeline.delete(JOB_DISPLAY_ID, models.TaskCodes.STORAGE)
print(r)
r = api.jobs.timeline._2(JOB_DISPLAY_ID, START)
print(r)
