"""Swagger/Route lookup utilities.

Example usage:
    python examples/swagger.py /job/{jobDisplayId}/parcelitems
    python examples/swagger.py parcelitems
    python examples/swagger.py GET /contacts
"""

from ABConnect.api.routes import SCHEMA, Route


def lookup_path(path: str, method: str = None) -> list[tuple[str, str, Route]]:
    """Look up a path in the SCHEMA and return matching routes.

    Args:
        path: Full path (e.g., '/job/{jobDisplayId}/parcelitems') or partial match
        method: Optional HTTP method filter (GET, POST, PUT, DELETE, PATCH)

    Returns:
        List of (tag, route_name, route) tuples
    """
    results = []
    path_lower = path.lower().strip("/")

    for tag, routes in SCHEMA.items():
        for route_name, route in routes.items():
            route_path_lower = route.path.lower().strip("/")

            # Exact match or partial match
            if path_lower in route_path_lower or route_path_lower in path_lower:
                if method is None or route.method.upper() == method.upper():
                    results.append((tag, route_name, route))

    return results


def display_route(tag: str, route_name: str, route: Route) -> None:
    """Display route details including request and response models."""
    print(f"\n{'='*60}")
    print(f"Tag:      {tag}")
    print(f"Route:    {route_name}")
    print(f"Method:   {route.method}")
    print(f"Path:     {route.path}")
    print(f"Request:  {route.request_model or '(none)'}")
    print(f"Response: {route.response_model or '(none)'}")
    print(f"{'='*60}")


def lookup_and_display(path: str, method: str = None) -> None:
    """Look up a path and display all matching routes."""
    results = lookup_path(path, method)

    if not results:
        print(f"No routes found matching: {path}" + (f" [{method}]" if method else ""))
        return

    print(f"\nFound {len(results)} route(s) matching: {path}" + (f" [{method}]" if method else ""))

    for tag, route_name, route in results:
        display_route(tag, route_name, route)


def list_tags() -> None:
    """List all available tags and route counts."""
    print("\nAvailable tags:")
    print("-" * 40)
    for tag in sorted(SCHEMA.keys()):
        count = len(SCHEMA[tag])
        print(f"  {tag}: {count} routes")


def list_routes_for_tag(tag: str) -> None:
    """List all routes for a specific tag."""
    tag_upper = tag.upper()
    if tag_upper not in SCHEMA:
        print(f"Tag not found: {tag}")
        list_tags()
        return

    print(f"\nRoutes for {tag_upper}:")
    print("-" * 60)
    for route_name, route in SCHEMA[tag_upper].items():
        req = f" <- {route.request_model}" if route.request_model else ""
        resp = f" -> {route.response_model}" if route.response_model else ""
        print(f"  {route_name}: {route.method} {route.path}{req}{resp}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python examples/swagger.py <path>           # Search for path")
        print("  python examples/swagger.py <method> <path>  # Search with method filter")
        print("  python examples/swagger.py --tags           # List all tags")
        print("  python examples/swagger.py --tag <TAG>      # List routes for tag")
        print("\nExamples:")
        print("  python examples/swagger.py parcelitems")
        print("  python examples/swagger.py GET /contacts")
        print("  python examples/swagger.py --tag JOB")
        sys.exit(0)

    if sys.argv[1] == "--tags":
        list_tags()
    elif sys.argv[1] == "--tag" and len(sys.argv) > 2:
        list_routes_for_tag(sys.argv[2])
    elif len(sys.argv) == 2:
        lookup_and_display(sys.argv[1])
    elif len(sys.argv) >= 3:
        # Check if first arg is a method
        if sys.argv[1].upper() in ("GET", "POST", "PUT", "DELETE", "PATCH"):
            lookup_and_display(sys.argv[2], sys.argv[1])
        else:
            lookup_and_display(sys.argv[1])
