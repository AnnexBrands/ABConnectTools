#!/usr/bin/env python3
"""Command line interface for ABConnect.

This module provides the 'ab' command for interacting with ABConnect tools.
"""

import argparse
import sys
import json
from typing import Optional
from ABConnect import __version__
from ABConnect.api import ABConnectAPI
from ABConnect.config import Config
from ABConnect.Quoter import Quoter
from ABConnect.Loader import FileLoader


def cmd_version(args):
    """Show version information."""
    print(f"ABConnect version {__version__}")


def cmd_config(args):
    """Show or set configuration."""
    if args.show:
        config = Config()
        print(f"Environment: {config.get_env()}")
        print(f"API URL: {config.get_api_base_url()}")
        print(f"Config file: {config._env_file}")
    elif args.env:
        # Set environment
        if args.env in ["staging", "production"]:
            Config.load(force_reload=True)
            print(f"Environment set to: {args.env}")
        else:
            print("Error: Environment must be 'staging' or 'production'")
            sys.exit(1)


def cmd_me(args):
    """Get current user information."""
    api = ABConnectAPI()
    try:
        user = api.users.me()
        print(json.dumps(user, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_company(args):
    """Get company information."""
    api = ABConnectAPI()
    try:
        if args.code:
            company = api.companies.get(args.code)
        elif args.id:
            company = api.companies.get_id(args.id)
        else:
            print("Error: Provide either --code or --id")
            sys.exit(1)

        print(json.dumps(company, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_quote(args):
    """Get a quote."""
    quoter = Quoter(
        env=Config.get_env(),
        type=args.type,
        auto_book=args.auto_book,
    )

    # Build quote parameters
    params = {
        "customer_id": args.customer_id,
        "origin_zip": args.origin_zip,
        "destination_zip": args.destination_zip,
    }

    # Add optional parameters
    if args.weight:
        params["weight"] = args.weight
    if args.pieces:
        params["pieces"] = args.pieces

    try:
        if args.type == "qq":
            result = quoter.qq(**params)
        else:
            result = quoter.qr(**params)

        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_lookup(args):
    """Lookup master constant values."""
    api = ABConnectAPI()
    try:
        result = api.raw.get(f"lookup/{args.key}")

        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            # Table format
            if isinstance(result, list):
                for item in result:
                    if isinstance(item, dict):
                        name = item.get("name", item.get("value", ""))
                        id_val = item.get("id", "")
                        print(f"{name:<30} {id_val}")
                    else:
                        print(item)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_load(args):
    """Load and display a file."""
    loader = FileLoader()
    try:
        data = loader.load(args.file)

        if args.format == "json":
            # Convert to JSON if it's a DataFrame
            if hasattr(data, "to_dict"):
                data = data.to_dict(orient="records")
            print(json.dumps(data, indent=2))
        else:
            print(data)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_endpoints(args):
    """List available API endpoints."""
    api = ABConnectAPI()

    if args.endpoint:
        # Show details for specific endpoint
        try:
            info = api.get_endpoint_info(args.endpoint)
            print(f"Endpoint: {info['name']}")
            print(f"Type: {info['type']}")
            print(f"Methods: {', '.join(info['methods'])}")

            # Special display for lookup endpoint
            if "lookup_endpoints" in info:
                print(
                    f"\nAvailable lookup endpoints ({len(info['lookup_endpoints'])}):"
                )
                for endpoint in info["lookup_endpoints"]:
                    print(f"  /api/lookup/{endpoint}")

            if "master_constant_keys" in info:
                print(
                    f"\nMaster constant keys for {{masterConstantKey}} endpoint ({len(info['master_constant_keys'])}):"
                )
                print("Usage: ab lookup <key>")
                print("Available keys:")
                for i, key in enumerate(info["master_constant_keys"]):
                    if i < 10:  # Show first 10
                        print(f"  {key}")
                if len(info["master_constant_keys"]) > 10:
                    print(f"  ... and {len(info['master_constant_keys']) - 10} more")

            if "paths" in info and args.verbose:
                print("\nAPI Paths:")
                for path_info in info["paths"]:
                    print(f"  {path_info['path']}")
                    print(f"    Methods: {', '.join(path_info['methods'])}")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        # List all endpoints
        endpoints = api.available_endpoints

        if args.format == "json":
            # JSON format with details
            endpoint_list = []
            for endpoint in endpoints:
                try:
                    info = api.get_endpoint_info(endpoint)
                    endpoint_list.append(
                        {
                            "name": endpoint,
                            "type": info["type"],
                            "methods": info["methods"],
                        }
                    )
                except:
                    pass
            print(json.dumps(endpoint_list, indent=2))
        else:
            # Table format
            print(f"Available endpoints ({len(endpoints)} total):\n")

            # Separate by type
            manual = []
            generic = []

            for endpoint in endpoints:
                if endpoint in [
                    "users",
                    "companies",
                    "contacts",
                    "docs",
                    "forms",
                    "items",
                    "jobs",
                    "tasks",
                ]:
                    manual.append(endpoint)
                else:
                    generic.append(endpoint)

            if manual:
                print("Manual endpoints:")
                for endpoint in sorted(manual):
                    print(f"  {endpoint}")

            if generic:
                print(f"\nGeneric endpoints ({len(generic)}):")
                for endpoint in sorted(generic):
                    print(f"  {endpoint}")


def cmd_api(args):
    """Execute API commands.

    Supports three access patterns:
    1. Raw: ab api raw get /api/companies/{id} --id=123
    2. Tagged: ab api companies get-details --id=123
    3. Friendly: ab api companies get-by-code ABC123
    """
    api = ABConnectAPI()

    try:
        if (hasattr(args, "raw") and args.raw) or getattr(
            args, "api_type", None
        ) == "raw":
            # Raw API call
            # For raw subparser, method should be a positional argument
            # But there might be conflicts, so let's be defensive
            method = getattr(args, 'method', None)
            path = getattr(args, 'path', None)
            
            if not method or not path:
                print("Error: Raw API requires method and path")
                print("Usage: ab api raw <method> <path> [params...]")
                sys.exit(1)

            # Parse parameters
            params = {}
            data = None

            if args.params:
                for param in args.params:
                    if "=" in param:
                        key, value = param.split("=", 1)
                        if key == "data" and value.startswith("@"):
                            # Load data from file
                            with open(value[1:], "r") as f:
                                data = json.load(f)
                        else:
                            params[key] = value

            # Make the call
            result = api.raw.call(method.upper(), path, data=data, **params)

        else:
            # Tagged or friendly access - not supported yet
            print("Error: Non-raw API access not implemented yet")
            print("Use: ab api raw <method> <path> [params...]")
            sys.exit(1)

        # Output result
        if args.format == "json" or isinstance(result, (dict, list)):
            print(json.dumps(result, indent=2))
        else:
            print(result)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="ab", description="ABConnect CLI - Tools for Annex Brands data processing"
    )

    parser.add_argument(
        "--version", "-v", action="store_true", help="Show version information"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Config command
    config_parser = subparsers.add_parser("config", help="Configuration management")
    config_parser.add_argument(
        "--show", action="store_true", help="Show current configuration"
    )
    config_parser.add_argument(
        "--env", choices=["staging", "production"], help="Set environment"
    )
    config_parser.set_defaults(func=cmd_config)

    # Me command
    me_parser = subparsers.add_parser("me", help="Get current user information")
    me_parser.set_defaults(func=cmd_me)

    # Company command
    company_parser = subparsers.add_parser("company", help="Get company information")
    company_group = company_parser.add_mutually_exclusive_group(required=True)
    company_group.add_argument("--code", help="Company code")
    company_group.add_argument("--id", help="Company ID (UUID)")
    company_parser.set_defaults(func=cmd_company)

    # Quote command
    quote_parser = subparsers.add_parser("quote", help="Get a quote")
    quote_parser.add_argument("customer_id", help="Customer ID")
    quote_parser.add_argument("origin_zip", help="Origin ZIP code")
    quote_parser.add_argument("destination_zip", help="Destination ZIP code")
    quote_parser.add_argument(
        "--type", choices=["qq", "qr"], default="qq", help="Quote type"
    )
    quote_parser.add_argument("--weight", type=float, help="Total weight")
    quote_parser.add_argument("--pieces", type=int, help="Number of pieces")
    quote_parser.add_argument(
        "--auto-book", action="store_true", help="Automatically book the quote"
    )
    quote_parser.set_defaults(func=cmd_quote)

    # Lookup command
    lookup_parser = subparsers.add_parser(
        "lookup", help="Lookup master constant values"
    )
    lookup_parser.add_argument("key", help="Master constant key (e.g., CompanyTypes)")
    lookup_parser.add_argument(
        "--format", choices=["table", "json"], default="table", help="Output format"
    )
    lookup_parser.set_defaults(func=cmd_lookup)

    # Load command
    load_parser = subparsers.add_parser("load", help="Load and display a file")
    load_parser.add_argument("file", help="File path to load")
    load_parser.add_argument(
        "--format", choices=["json", "raw"], default="raw", help="Output format"
    )
    load_parser.set_defaults(func=cmd_load)

    # Endpoints command
    endpoints_parser = subparsers.add_parser(
        "endpoints", help="List available API endpoints"
    )
    endpoints_parser.add_argument(
        "endpoint", nargs="?", help="Show details for specific endpoint"
    )
    endpoints_parser.add_argument(
        "--format", choices=["table", "json"], default="table", help="Output format"
    )
    endpoints_parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show verbose output"
    )
    endpoints_parser.set_defaults(func=cmd_endpoints)

    # API command
    api_parser = subparsers.add_parser("api", help="Execute API calls")
    api_subparsers = api_parser.add_subparsers(dest="api_type", help="API access type")

    # Raw API access
    raw_parser = api_subparsers.add_parser("raw", help="Raw API access")
    raw_parser.add_argument(
        "method", choices=["get", "post", "put", "patch", "delete"], help="HTTP method"
    )
    raw_parser.add_argument("path", help="API path (e.g., /api/companies/{id})")
    raw_parser.add_argument("params", nargs="*", help="Parameters as key=value pairs")
    raw_parser.add_argument(
        "--format", choices=["json", "raw"], default="json", help="Output format"
    )
    raw_parser.set_defaults(func=cmd_api, raw=True)

    # Tagged/Friendly API access
    # These are handled differently when not using 'raw' subcommand
    # We'll handle these in the cmd_api function based on positional args

    # Parse arguments
    args = parser.parse_args()

    # Handle version flag
    if args.version:
        cmd_version(args)
        sys.exit(0)

    # Handle commands
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
