"""
Views API Examples - Dashboard views and dataset stored procedures

Usage:
    python views.py                 # Run all examples
    python views.py datasetsp       # Run a single example
    python views.py help            # List available examples
"""

from _base import ExampleRunner


class ViewExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Views API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("datasetsp", "Get a specific dataset stored procedure", self.get_datasetsp)

    def get_datasetsp(self):
        res = self.api.views.get_datasetsp('dashboard.agentDonan')
        print(res)


if __name__ == "__main__":
    ViewExamples().run()
