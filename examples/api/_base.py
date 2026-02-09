"""Base class for API example runners.

Provides a consistent way to register, list, and run examples
individually or all at once from the command line.

Usage:
    class MyExamples(ExampleRunner):
        def __init__(self):
            super().__init__("My API", api_kwargs=dict(env='staging', username='instaquote'))
            self.add("get", "Get a resource by ID", self.get_resource)
            self.add("search", "Search for resources", self.search_resources)

        def get_resource(self):
            result = self.api.endpoint.get(ID)
            print(result)

        def search_resources(self):
            result = self.api.endpoint.search(query="test")
            print(result)

    if __name__ == "__main__":
        MyExamples().run()
"""

import sys
from ABConnect import ABConnectAPI


class ExampleRunner:
    """Base class for organizing and running API examples.

    Supports running a single example by name or all examples sequentially.
    When run from the command line, accepts an optional example name argument.

    Args:
        title: Display title for this example group
        api_kwargs: Keyword arguments passed to ABConnectAPI()
    """

    def __init__(self, title: str, api_kwargs: dict = None):
        self.title = title
        self._examples = []
        self._api = None
        self._api_kwargs = api_kwargs or {}

    @property
    def api(self) -> ABConnectAPI:
        """Lazy-initialized API client shared across all examples."""
        if self._api is None:
            self._api = ABConnectAPI(**self._api_kwargs)
        return self._api

    def add(self, name: str, description: str, func: callable):
        """Register an example function.

        Args:
            name: Short name used to select this example from the CLI
            description: One-line description shown in the help listing
            func: Callable that runs the example
        """
        self._examples.append({"name": name, "description": description, "func": func})

    def list(self):
        """Print available examples."""
        print(f"Available examples for {self.title}:\n")
        for ex in self._examples:
            print(f"  {ex['name']:30s} {ex['description']}")
        print(f"\nUsage: python {sys.argv[0]} [example_name]")
        print("  Omit example_name to run all examples.")

    def run(self, names: list[str] = None):
        """Run examples by name, or parse sys.argv if names is None.

        Args:
            names: List of example names to run. None reads from sys.argv.
                   An empty list or ["all"] runs every registered example.
        """
        if names is None:
            args = sys.argv[1:]
            if args and args[0] in ("-h", "--help", "help"):
                self.list()
                return
            names = args

        if not names or names == ["all"]:
            self._run_all()
        else:
            for name in names:
                self._run_one(name)

    def _run_all(self):
        """Run every registered example."""
        print(f"{'=' * 60}")
        print(f" {self.title} Examples")
        print(f"{'=' * 60}\n")
        for i, ex in enumerate(self._examples):
            if i > 0:
                print()
            self._run_example(ex)

    def _run_one(self, name: str):
        """Run a single example by name."""
        for ex in self._examples:
            if ex["name"] == name:
                self._run_example(ex)
                return
        print(f"Unknown example: {name!r}\n")
        self.list()

    def _run_example(self, ex: dict):
        """Run one example with header formatting."""
        print(f"--- {ex['name']}: {ex['description']} ---\n")
        try:
            ex["func"]()
        except Exception as e:
            print(f"Error: {e}")
