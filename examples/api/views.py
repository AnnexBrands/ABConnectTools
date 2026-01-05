from ABConnect import ABConnectAPI, models

api = ABConnectAPI(env='staging', username='instaquote')

# all_sps = api.views.get_datasetsps()
res = api.views.get_datasetsp('dashboard.agentDonan')