"""Views API Examples - Working with saved views and datasets.

This example demonstrates getting views data and dataset stored procedures.
"""

from ABConnect import ABConnectAPI, models
from _helpers import save_fixture

api = ABConnectAPI(username='instaquote')

# =====================================================================
# 1. Get all views
# =====================================================================
print("=== 1. get_all ===")
views = api.views.get_all()
print(f"  Views count: {len(views)}")
save_fixture(views, "ViewsAll")

# =====================================================================
# 2. Get dataset stored procedures
# =====================================================================
print("\n=== 2. get_datasetsps ===")
datasetsps = api.views.get_datasetsps()
print(f"  Stored procedures count: {len(datasetsps)}")
save_fixture(datasetsps, "ViewsDatasetSps")

# =====================================================================
# 3. Get a specific dataset stored procedure's columns
# =====================================================================
print("\n=== 3. get_datasetsp ===")
if datasetsps:
    sp_name = datasetsps[0]
    print(f"  Using SP: {sp_name}")
    columns = api.views.get_datasetsp(sp_name)
    print(f"  Columns count: {len(columns)}")
    for col in columns[:5]:
        print(f"    {col}")
    save_fixture(columns, "ViewsDatasetSp")

print("\nDone.")
