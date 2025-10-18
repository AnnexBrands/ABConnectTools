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


def cmd_address(args):
    """Validate address information."""
    api = ABConnectAPI()
    try:
        # Validate address
        params = {}
        if args.line1:
            params['line1'] = args.line1
        if args.city:
            params['city'] = args.city
        if args.state:
            params['state'] = args.state
        if args.zip:
            params['zip'] = args.zip

        if not params:
            print("Error: Provide address components to validate (--line1, --city, --state, --zip)")
            sys.exit(1)

        address = api.address.get_isvalid(**params)

        print(json.dumps(address, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_company(args):
    """Get company information."""
    api = ABConnectAPI()
    try:
        # Use the new convenience method
        code_or_id = args.code or args.id
        details = args.details if hasattr(args, 'details') else 'short'

        company = api.companies.get(code_or_id, details=details)

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


def cmd_swagger(args):
    """Show swagger API structure hierarchically."""
    import json
    from pathlib import Path
    from collections import defaultdict
    
    # Load swagger.json
    swagger_path = Path(__file__).parent / "base" / "swagger.json"
    with open(swagger_path, 'r') as f:
        swagger = json.load(f)
    
    # Extract information
    schemas = swagger.get('components', {}).get('schemas', {})
    paths = swagger.get('paths', {})
    
    # Group endpoints by tags
    tag_endpoints = defaultdict(list)
    tag_methods = defaultdict(set)
    tag_descriptions = {}
    
    for path, methods in paths.items():
        for method, spec in methods.items():
            tags = spec.get('tags', ['Untagged'])
            for tag in tags:
                endpoint_info = {
                    'method': method.upper(),
                    'path': path,
                    'summary': spec.get('summary', ''),
                    'description': spec.get('description', ''),
                    'operationId': spec.get('operationId', '')
                }
                tag_endpoints[tag].append(endpoint_info)
                tag_methods[tag].add(method.upper())
    
    # Handle specific tag request
    if args.tag:
        tag = args.tag
        if tag not in tag_endpoints:
            print(f"❌ Tag '{tag}' not found")
            print(f"Available tags: {', '.join(sorted(tag_endpoints.keys()))}")
            sys.exit(1)
        
        endpoints = tag_endpoints[tag]
        methods = sorted(tag_methods[tag])
        
        print(f"📂 {tag} Tag - Complete Endpoint List")
        print("=" * 60)
        print(f"Total endpoints: {len(endpoints)}")
        print(f"HTTP methods: {', '.join(methods)}")
        print()
        
        for i, endpoint in enumerate(sorted(endpoints, key=lambda x: (x['path'], x['method'])), 1):
            print(f"{i:2}. {endpoint['method']} {endpoint['path']}")
            if endpoint['summary'] and args.verbose:
                print(f"    📝 {endpoint['summary']}")
            if endpoint['operationId'] and args.verbose:
                print(f"    🔧 Operation: {endpoint['operationId']}")
            if args.verbose:
                print()
        return
    
    if args.schemas:
        # Show schemas grouped by inferred categories
        print(f"📋 SWAGGER SCHEMAS ({len(schemas)} total)")
        print("=" * 60)
        
        # Group schemas by category (inferred from name patterns)
        schema_groups = defaultdict(list)
        for schema_name in schemas.keys():
            name_lower = schema_name.lower()
            if 'company' in name_lower:
                schema_groups['Companies'].append(schema_name)
            elif 'job' in name_lower:
                schema_groups['Jobs'].append(schema_name)
            elif 'contact' in name_lower:
                schema_groups['Contacts'].append(schema_name)
            elif 'address' in name_lower:
                schema_groups['Addresses'].append(schema_name)
            elif 'user' in name_lower:
                schema_groups['Users'].append(schema_name)
            elif any(word in name_lower for word in ['request', 'response', 'model']):
                schema_groups['Common Models'].append(schema_name)
            else:
                schema_groups['Other'].append(schema_name)
        
        for group, schema_list in sorted(schema_groups.items()):
            print(f"\n🏷️  {group} ({len(schema_list)} schemas)")
            for schema in sorted(schema_list)[:10]:  # Show first 10
                print(f"   {schema}")
            if len(schema_list) > 10:
                print(f"   ... and {len(schema_list) - 10} more")
    
    elif args.tags:
        # Show just tag summary
        print(f"🏷️  SWAGGER TAGS ({len(tag_endpoints)} total)")
        print("=" * 60)
        for tag in sorted(tag_endpoints.keys()):
            endpoint_count = len(tag_endpoints[tag])
            methods = sorted(tag_methods[tag])
            print(f"{tag:30} {endpoint_count:3} endpoints  [{', '.join(methods)}]")
    
    else:
        # Show full hierarchical structure
        print(f"🌳 SWAGGER API STRUCTURE")
        print("=" * 60)
        print(f"📊 Summary: {len(schemas)} schemas, {len(tag_endpoints)} tags, {sum(len(eps) for eps in tag_endpoints.values())} endpoints")
        print()
        
        for tag in sorted(tag_endpoints.keys()):
            endpoints = tag_endpoints[tag]
            methods = sorted(tag_methods[tag])
            
            print(f"📂 {tag} ({len(endpoints)} endpoints)")
            print(f"   Methods: {', '.join(methods)}")
            
            if args.verbose:
                for endpoint in sorted(endpoints, key=lambda x: (x['path'], x['method']))[:15]:  # Show first 15
                    print(f"   ├─ {endpoint['method']} {endpoint['path']}")
                if len(endpoints) > 15:
                    print(f"   └─ ... and {len(endpoints) - 15} more")
            else:
                # Show just a few examples
                for endpoint in sorted(endpoints, key=lambda x: (x['path'], x['method']))[:3]:
                    print(f"   ├─ {endpoint['method']} {endpoint['path']}")
                if len(endpoints) > 3:
                    print(f"   └─ ... and {len(endpoints) - 3} more")
            print()


def cmd_jobs(args):
    """Handle jobs package commands with submodules."""
    if not hasattr(args, 'submodule'):
        # Show help for jobs package
        print("📂 JOBS PACKAGE")
        print("=" * 60)
        print("The jobs package contains multiple submodules:")
        print()
        print("  agent      - Agent operations (OA/DA changes)")
        print("  job        - Core job operations")
        print("  email      - Job email operations")
        print("  form       - Job form operations")
        print("  timeline   - Timeline and task operations")
        print("  rfq        - Job RFQ operations")
        print("  shipment   - Job shipment operations")
        print("  status     - Job status operations")
        print()
        print("Usage examples:")
        print("  ab jobs agent oa 2000000 JM          # Change OA to JM")
        print("  ab jobs agent da 2000000 ABC         # Change DA to ABC")
        print("  ab jobs job get 2000000              # Get job details")
        print("  ab jobs timeline get 2000000         # Get job timeline")
        return

    api = ABConnectAPI()
    submodule = args.submodule
    method_name = getattr(args, 'method', None)

    # Get the submodule from jobs package
    if not hasattr(api.jobs, submodule):
        print(f"❌ Unknown jobs submodule: {submodule}")
        print("Available submodules: agent, job, email, form, timeline, rfq, shipment, status")
        sys.exit(1)

    endpoint = getattr(api.jobs, submodule)

    if not method_name:
        # Show methods for submodule
        print(f"📂 jobs.{submodule} endpoint")
        print("=" * 60)
        methods = [m for m in dir(endpoint) if not m.startswith('_') and callable(getattr(endpoint, m))]
        print(f"Available methods: {', '.join(methods)}")
        return

    # Execute the method
    if not hasattr(endpoint, method_name):
        print(f"❌ Method '{method_name}' not found on jobs.{submodule}")
        available_methods = [m for m in dir(endpoint) if not m.startswith('_') and callable(getattr(endpoint, m))]
        print(f"Available methods: {', '.join(available_methods)}")
        sys.exit(1)

    method = getattr(endpoint, method_name)
    method_params = getattr(args, 'params', [])

    try:
        if method_params:
            # Convert numeric parameters if needed
            converted_params = []
            for param in method_params:
                if param.isdigit():
                    converted_params.append(int(param))
                else:
                    converted_params.append(param)
            print(f"🔄 Executing jobs.{submodule}.{method_name}({', '.join(map(str, converted_params))})...")
            result = method(*converted_params)
        else:
            print(f"🔄 Executing jobs.{submodule}.{method_name}()...")
            result = method()

        print("✅ Method executed successfully")
        print(json.dumps(result, indent=2) if isinstance(result, (dict, list)) else str(result))
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def cmd_endpoint_help(args):
    """Show help for a specific endpoint or execute endpoint method."""
    endpoint_name = args.endpoint_name
    method_name = getattr(args, 'method_name', None)
    
    # Map of endpoint names to their info
    endpoint_info = {
        'account': ('AccountEndpoint', '/api/account', 'Account management and authentication'),
        'address': ('AddressEndpoint', '/api/address', 'Address validation and property types'),  
        'admin': ('AdminEndpoint', '/api/admin', 'Administrative settings and configurations'),
        'companies': ('CompaniesEndpoint', '/api/companies', 'Company management operations'),
        'company': ('CompanyEndpoint', '/api/company', 'Single company operations'),
        'contacts': ('ContactsEndpoint', '/api/contacts', 'Contact management operations'),
        'dashboard': ('DashboardEndpoint', '/api/dashboard', 'Dashboard data and analytics'),
        'documents': ('DocumentsEndpoint', '/api/documents', 'Document management'),
        'email': ('EmailEndpoint', '/api/email', 'Email operations'),
        'job': ('JobEndpoint', '/api/job', 'Job management operations'),
        'jobs': ('JobEndpoint', '/api/job', 'Job management operations (alias for job)'),
        'jobintacct': ('JobintacctEndpoint', '/api/jobintacct', 'Job integration with Intacct'),
        'lookup': ('LookupEndpoint', '/api/lookup', 'Master data lookups'),
        'note': ('NoteEndpoint', '/api/note', 'Note management'),
        'reports': ('ReportsEndpoint', '/api/reports', 'Reporting endpoints'),
        'rfq': ('RfqEndpoint', '/api/rfq', 'Request for Quote operations'),
        'shipment': ('ShipmentEndpoint', '/api/shipment', 'Shipment operations'),
        'smstemplate': ('SmstemplateEndpoint', '/api/SmsTemplate', 'SMS template management'),
        'users': ('UsersEndpoint', '/api/users', 'User management'),
        'views': ('ViewsEndpoint', '/api/views', 'Grid view configurations'),
        'webhooks': ('WebhooksEndpoint', '/api/webhooks', 'Webhook handling'),
    }
    
    if endpoint_name not in endpoint_info:
        print(f"❌ Unknown endpoint: {endpoint_name}")
        print(f"Available endpoints: {', '.join(sorted(endpoint_info.keys()))}")
        sys.exit(1)
    
    class_name, api_path, description = endpoint_info[endpoint_name]
    
    # If method name provided, execute the method
    if method_name:
        try:
            # Initialize API client
            api = ABConnectAPI(enable_generic=False)
            # Map CLI endpoint names to API endpoint names
            api_endpoint_name = endpoint_name.replace('smstemplate', 'sms_template')
            endpoint = getattr(api, api_endpoint_name)
            
            if not hasattr(endpoint, method_name):
                print(f"❌ Method '{method_name}' not found on {endpoint_name} endpoint")
                available_methods = [m for m in dir(endpoint) if not m.startswith('_') and callable(getattr(endpoint, m))]
                print(f"Available methods: {', '.join(available_methods)}")
                sys.exit(1)
            
            # Get method and check if it needs parameters
            method = getattr(endpoint, method_name)
            import inspect
            sig = inspect.signature(method)

            # Get parameters from command line
            method_params = getattr(args, 'params', [])

            # Analyze method signature
            param_list = [p for p in sig.parameters.values() if p.name != 'self']
            required_params = [p for p in param_list if p.default == inspect.Parameter.empty]

            # Check if we have enough parameters
            if len(method_params) < len(required_params):
                if required_params:
                    print(f"❌ Method '{method_name}' requires {len(required_params)} parameter(s): {[p.name for p in required_params]}")
                    print(f"Method signature: {method_name}{sig}")
                    print(f"Provided: {len(method_params)} parameter(s)")
                    sys.exit(1)

            # Check if we have too many parameters
            if len(method_params) > len(param_list):
                print(f"❌ Method '{method_name}' accepts at most {len(param_list)} parameter(s)")
                print(f"Method signature: {method_name}{sig}")
                print(f"Provided: {len(method_params)} parameter(s)")
                sys.exit(1)

            # Execute method with parameters
            if method_params:
                print(f"🔄 Executing {endpoint_name}.{method_name}({', '.join(method_params)})...")
                result = method(*method_params)
            else:
                print(f"🔄 Executing {endpoint_name}.{method_name}()...")
                result = method()
            
            print("✅ Method executed successfully")
            print(json.dumps(result, indent=2) if isinstance(result, (dict, list)) else str(result))
            
        except Exception as e:
            print(f"❌ Error executing {endpoint_name}.{method_name}(): {e}")
            sys.exit(1)
        
        return
    
    print(f"📂 {endpoint_name.upper()} ENDPOINT")
    print("=" * 60)
    print(f"Class: {class_name}")
    print(f"API Path: {api_path}")
    print(f"Description: {description}")
    print()
    
    # Get actual endpoint methods using swagger
    from pathlib import Path
    
    swagger_path = Path(__file__).parent / "base" / "swagger.json"
    with open(swagger_path, 'r') as f:
        swagger = json.load(f)
    
    # Find all endpoints for this API path
    matching_endpoints = []
    for path, methods in swagger['paths'].items():
        if path.startswith(api_path) or (endpoint_name == 'jobs' and path.startswith('/api/job')):
            for method, spec in methods.items():
                matching_endpoints.append({
                    'method': method.upper(),
                    'path': path,
                    'summary': spec.get('summary', ''),
                    'operationId': spec.get('operationId', '')
                })
    
    if matching_endpoints:
        print(f"📋 Available Methods ({len(matching_endpoints)} total):")
        print()
        
        for i, endpoint in enumerate(sorted(matching_endpoints, key=lambda x: (x['path'], x['method'])), 1):
            print(f"{i:2}. {endpoint['method']} {endpoint['path']}")
            if endpoint['summary']:
                print(f"    📝 {endpoint['summary']}")
            if args.verbose and endpoint['operationId']:
                print(f"    🔧 Operation: {endpoint['operationId']}")
            print()
        
        print("💡 Usage Examples:")
        print(f"   # 🎯 Preferred: Use friendly endpoint commands when available")
        print(f"   ab {endpoint_name} method_name")
        print(f"   # ⚠️  Fallback: Use raw API only when friendly commands don't support parameters")
        print(f"   ab api raw get {api_path}/{{id}} id=your-id-here")
        print(f"   ab api raw post {api_path} data='{{...}}'")
        print()
        print(f"🔗 For all endpoints: ab swagger {endpoint_name.title()}")
    else:
        print("No endpoints found for this module.")


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

    Supports three access patterns (in order of preference):
    1. Friendly endpoint commands: ab smstemplate get_notificationtokens
    2. Tagged endpoints: ab api companies get-details --id=123  [NOT YET IMPLEMENTED]
    3. Raw API (last resort): ab api raw get /api/companies/{id} id=123

    Use friendly endpoint commands when available, fallback to raw API only when needed.
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
            # Tagged endpoint access - not supported yet
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
    company_parser.add_argument("--details", choices=["short", "full", "details"],
                               default="short", help="Level of detail (default: short)")
    company_parser.set_defaults(func=cmd_company)

    # Address command
    address_parser = subparsers.add_parser("address", help="Validate address information")
    address_parser.add_argument("--line1", help="Address line 1")
    address_parser.add_argument("--city", help="City")
    address_parser.add_argument("--state", help="State")
    address_parser.add_argument("--zip", help="ZIP code")
    address_parser.set_defaults(func=cmd_address)

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

    # Swagger command
    swagger_parser = subparsers.add_parser("swagger", help="Show swagger API structure hierarchically")
    swagger_parser.add_argument(
        "tag", nargs="?", help="Show all endpoints for specific tag (e.g., 'Companies', 'Jobs')"
    )
    swagger_group = swagger_parser.add_mutually_exclusive_group()
    swagger_group.add_argument(
        "--schemas", "-s", action="store_true", help="Show schemas grouped by category"
    )
    swagger_group.add_argument(
        "--tags", "-t", action="store_true", help="Show only tag summary"
    )
    swagger_parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show more details (summaries, operation IDs)"
    )
    swagger_parser.set_defaults(func=cmd_swagger)

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

    # Jobs command with submodules
    jobs_parser = subparsers.add_parser("jobs", help="Jobs package with submodules")
    jobs_subparsers = jobs_parser.add_subparsers(dest="submodule", help="Jobs submodules")

    # Agent submodule
    agent_parser = jobs_subparsers.add_parser("agent", help="Agent operations (OA/DA changes)")
    agent_parser.add_argument("method", nargs="?", help="Method name (oa, da, change)")
    agent_parser.add_argument("params", nargs="*", help="Method parameters")

    # Job submodule
    job_parser = jobs_subparsers.add_parser("job", help="Core job operations")
    job_parser.add_argument("method", nargs="?", help="Method name")
    job_parser.add_argument("params", nargs="*", help="Method parameters")

    # Email submodule
    email_parser = jobs_subparsers.add_parser("email", help="Job email operations")
    email_parser.add_argument("method", nargs="?", help="Method name")
    email_parser.add_argument("params", nargs="*", help="Method parameters")

    # Form submodule
    form_parser = jobs_subparsers.add_parser("form", help="Job form operations")
    form_parser.add_argument("method", nargs="?", help="Method name")
    form_parser.add_argument("params", nargs="*", help="Method parameters")

    # Timeline submodule
    timeline_parser = jobs_subparsers.add_parser("timeline", help="Timeline and task operations")
    timeline_parser.add_argument("method", nargs="?", help="Method name")
    timeline_parser.add_argument("params", nargs="*", help="Method parameters")

    # RFQ submodule
    rfq_parser = jobs_subparsers.add_parser("rfq", help="Job RFQ operations")
    rfq_parser.add_argument("method", nargs="?", help="Method name")
    rfq_parser.add_argument("params", nargs="*", help="Method parameters")

    # Shipment submodule
    shipment_parser = jobs_subparsers.add_parser("shipment", help="Job shipment operations")
    shipment_parser.add_argument("method", nargs="?", help="Method name")
    shipment_parser.add_argument("params", nargs="*", help="Method parameters")

    # Status submodule
    status_parser = jobs_subparsers.add_parser("status", help="Job status operations")
    status_parser.add_argument("method", nargs="?", help="Method name")
    status_parser.add_argument("params", nargs="*", help="Method parameters")

    jobs_parser.set_defaults(func=cmd_jobs)

    # Dynamic endpoint help commands (avoid conflicts with existing commands)
    existing_commands = {'config', 'me', 'company', 'quote', 'lookup', 'load', 'endpoints', 'swagger', 'api', 'address', 'jobs'}
    endpoint_names = [
        'account', 'address', 'admin', 'companies', 'contacts',
        'dashboard', 'documents', 'email', 'job', 'jobintacct',
        'note', 'reports', 'rfq', 'shipment', 'smstemplate', 'users', 'views', 'webhooks'
    ]

    for endpoint_name in endpoint_names:
        # Skip if conflicts with existing command
        if endpoint_name in existing_commands:
            continue

        # Create help description
        help_text = f"Show help for {endpoint_name} endpoint"

        endpoint_parser = subparsers.add_parser(endpoint_name, help=help_text)
        endpoint_parser.add_argument(
            "method_name", nargs="?", help="Method name to execute (e.g., get_profile)"
        )
        endpoint_parser.add_argument(
            "params", nargs="*", help="Method parameters as positional arguments"
        )
        endpoint_parser.add_argument(
            "--verbose", "-v", action="store_true", help="Show operation IDs and details"
        )
        endpoint_parser.set_defaults(func=cmd_endpoint_help, endpoint_name=endpoint_name)

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
