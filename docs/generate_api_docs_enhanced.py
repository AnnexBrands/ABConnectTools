#!/usr/bin/env python3
"""Generate enhanced API documentation with Pydantic model integration.

This script creates comprehensive documentation for all API endpoints
with response schemas linked to Pydantic models.
"""

import json
import os
import re
import ast
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Optional, Set
import importlib
import inspect


def get_pydantic_models():
    """Load all Pydantic models from ABConnect.api.models."""
    models = {}
    models_path = Path(__file__).parent.parent / "ABConnect" / "api" / "models"
    
    # Import each module file
    for module_file in models_path.glob("*.py"):
        if module_file.name == "__init__.py":
            continue
            
        module_name = f"ABConnect.api.models.{module_file.stem}"
        try:
            module = importlib.import_module(module_name)
            
            # Get all classes that are Pydantic models
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if hasattr(obj, '__fields__') and obj.__module__ == module_name:
                    models[name] = {
                        'module': module_name,
                        'class': obj,
                        'fields': obj.__fields__,
                        'file': module_file.stem
                    }
        except Exception as e:
            print(f"Warning: Could not import {module_name}: {e}")
    
    return models


def get_endpoint_response_model(endpoint_path: str, method: str) -> Optional[str]:
    """Map endpoint to its response Pydantic model."""
    # Define mappings based on endpoint patterns
    mappings = {
        # Job endpoints
        ('/api/job/{jobDisplayId}', 'GET'): 'Job',
        ('/api/job/search', 'GET'): 'List[Job]',
        ('/api/job/{jobDisplayId}/book', 'POST'): 'Job',
        
        # Company endpoints
        ('/api/companies/{id}', 'GET'): 'CompanyBasic',
        ('/api/companies/{companyId}/details', 'GET'): 'CompanyDetails',
        ('/api/companies/{companyId}/fulldetails', 'GET'): 'CompanyFullDetails',
        ('/api/companies/availableByCurrentUser', 'GET'): 'List[CompanyBasic]',
        ('/api/companies/search', 'GET'): 'List[CompanyBasic]',
        
        # Contact endpoints
        ('/api/contacts/{id}', 'GET'): 'Contact',
        ('/api/contacts', 'POST'): 'Contact',
        ('/api/contacts/{id}', 'PUT'): 'Contact',
        
        # User endpoints
        ('/api/users', 'GET'): 'List[User]',
        ('/api/users/{id}', 'GET'): 'User',
        ('/api/users', 'POST'): 'User',
        
        # Lookup endpoints
        ('/api/lookup/{masterConstantKey}', 'GET'): 'List[LookupValue]',
    }
    
    return mappings.get((endpoint_path, method))


def format_model_reference(model_name: str, models: Dict) -> str:
    """Format a model name as a cross-reference link."""
    # Handle List types
    if model_name.startswith('List[') and model_name.endswith(']'):
        inner_model = model_name[5:-1]
        if inner_model in models:
            model_info = models[inner_model]
            return f"List[:class:`~ABConnect.api.models.{model_info['file']}.{inner_model}`]"
        return model_name
    
    # Handle regular types
    if model_name in models:
        model_info = models[model_name]
        return f":class:`~ABConnect.api.models.{model_info['file']}.{model_name}`"
    
    return model_name


def generate_response_schema_doc(model_name: str, models: Dict, seen: Set[str] = None) -> List[str]:
    """Generate documentation for a response schema."""
    if seen is None:
        seen = set()
    
    doc = []
    
    # Handle List types
    if model_name.startswith('List[') and model_name.endswith(']'):
        inner_model = model_name[5:-1]
        doc.append("**Response Type:** Array of objects")
        doc.append("")
        doc.append(f"Each item in the array is a {format_model_reference(inner_model, models)} object.")
        doc.append("")
        return doc
    
    # Handle regular model types
    if model_name not in models:
        return doc
    
    model_info = models[model_name]
    model_class = model_info['class']
    
    doc.append(f"**Response Type:** {format_model_reference(model_name, models)}")
    doc.append("")
    
    # Don't recurse into already seen models
    if model_name in seen:
        return doc
    
    seen.add(model_name)
    
    # Generate field documentation
    doc.append("**Response Fields:**")
    doc.append("")
    doc.append(".. list-table::")
    doc.append("   :header-rows: 1")
    doc.append("   :widths: 25 25 50")
    doc.append("")
    doc.append("   * - Field")
    doc.append("     - Type")
    doc.append("     - Description")
    
    # Get field information
    for field_name, field_info in model_class.__fields__.items():
        field_type = field_info.annotation
        
        # Format the type
        type_str = str(field_type).replace('typing.', '')
        type_str = type_str.replace("<class '", "").replace("'>", "")
        type_str = type_str.replace("Union[", "").replace(", NoneType]", " | None")
        
        # Check if it's a model type
        type_parts = type_str.split('[')
        base_type = type_parts[0].strip()
        
        if base_type in models:
            type_str = format_model_reference(base_type, models)
        elif 'List[' in type_str:
            # Extract inner type
            inner_match = re.search(r'List\[(\w+)\]', type_str)
            if inner_match:
                inner_type = inner_match.group(1)
                if inner_type in models:
                    type_str = f"List[{format_model_reference(inner_type, models)}]"
        
        # Get field description from docstring or default
        description = field_info.field_info.description or ""
        if not description and hasattr(model_class, '__doc__') and model_class.__doc__:
            # Try to extract from class docstring
            description = ""
        
        doc.append(f"   * - {field_name}")
        doc.append(f"     - {type_str}")
        doc.append(f"     - {description}")
    
    doc.append("")
    
    return doc


def generate_enhanced_endpoint_doc(endpoint: Dict, models: Dict) -> List[str]:
    """Generate enhanced documentation for an endpoint including response schema."""
    from generate_api_docs import (
        format_parameter, format_python_example, format_cli_example,
        format_curl_example, get_endpoint_description, sanitize_anchor
    )
    
    doc = []
    
    path = endpoint['path']
    method = endpoint['method']
    parameters = endpoint.get('parameters', [])
    
    # Get custom descriptions
    custom_summary, custom_description = get_endpoint_description(path, method)
    summary = custom_summary or endpoint.get('summary', '')
    description = custom_description or endpoint.get('description', '')
    
    # Create anchor ID for cross-referencing
    anchor_id = sanitize_anchor(f"{method}-{path}")
    
    # Endpoint title with anchor
    doc.append(f".. _{anchor_id}:")
    doc.append("")
    endpoint_title = f"{method} {path}"
    doc.append(endpoint_title)
    doc.append("~" * len(endpoint_title))
    doc.append("")
    
    # Summary and description
    if summary:
        doc.append(f"**{summary}**")
        doc.append("")
    
    if description:
        doc.append(description)
        doc.append("")
    
    # Parameters
    if parameters:
        doc.append("**Parameters:**")
        doc.append("")
        
        # Group parameters by type
        path_params = [p for p in parameters if p.get('in') == 'path']
        query_params = [p for p in parameters if p.get('in') == 'query']
        header_params = [p for p in parameters if p.get('in') == 'header']
        
        if path_params:
            doc.append("*Path Parameters:*")
            doc.append("")
            for param in path_params:
                doc.append(format_parameter(param))
            doc.append("")
        
        if query_params:
            doc.append("*Query Parameters:*")
            doc.append("")
            for param in query_params:
                doc.append(format_parameter(param))
            doc.append("")
        
        if header_params:
            doc.append("*Header Parameters:*")
            doc.append("")
            for param in header_params:
                doc.append(format_parameter(param))
            doc.append("")
    
    # Example Request with tabs
    doc.append("**Example Request:**")
    doc.append("")
    doc.append(".. tabs::")
    doc.append("")
    
    # Python tab
    doc.append("   .. tab:: Python")
    doc.append("")
    doc.append("      .. code-block:: python")
    doc.append("")
    python_example = format_python_example(endpoint)
    for line in python_example.split('\n'):
        doc.append(f"         {line}")
    doc.append("")
    
    # CLI tab
    doc.append("   .. tab:: CLI")
    doc.append("")
    doc.append("      .. code-block:: bash")
    doc.append("")
    cli_example = format_cli_example(endpoint)
    for line in cli_example.split('\n'):
        doc.append(f"         {line}")
    doc.append("")
    
    # Curl tab
    doc.append("   .. tab:: curl")
    doc.append("")
    doc.append("      .. code-block:: bash")
    doc.append("")
    curl_example = format_curl_example(endpoint)
    for line in curl_example.split('\n'):
        doc.append(f"         {line}")
    doc.append("")
    
    # Response Schema
    response_model = get_endpoint_response_model(path, method)
    if response_model:
        doc.append("**Response Schema:**")
        doc.append("")
        schema_doc = generate_response_schema_doc(response_model, models)
        doc.extend(schema_doc)
    
    # Sample response (collapsible)
    doc.append("**Sample Response:**")
    doc.append("")
    doc.append(".. toggle::")
    doc.append("")
    doc.append("   .. code-block:: json")
    doc.append("      :linenos:")
    doc.append("")
    
    # For now, use existing sample response generation
    from generate_api_docs import generate_sample_response
    sample_response = generate_sample_response(endpoint)
    for line in sample_response.split('\n'):
        doc.append(f"      {line}")
    doc.append("")
    
    return doc


def generate_model_documentation(models: Dict):
    """Generate RST documentation for all Pydantic models."""
    # Group models by module
    modules = defaultdict(list)
    for model_name, model_info in models.items():
        modules[model_info['file']].append((model_name, model_info))
    
    # Create models directory
    models_dir = Path(__file__).parent / "api" / "models"
    models_dir.mkdir(exist_ok=True)
    
    # Generate index file
    index_content = []
    index_content.append("API Models Reference")
    index_content.append("===================")
    index_content.append("")
    index_content.append("Detailed reference for all API data models.")
    index_content.append("")
    index_content.append(".. toctree::")
    index_content.append("   :maxdepth: 2")
    index_content.append("")
    
    # Generate documentation for each module
    for module_name in sorted(modules.keys()):
        index_content.append(f"   {module_name}")
        
        # Generate module documentation
        module_content = []
        module_title = module_name.replace('_', ' ').title()
        module_content.append(module_title)
        module_content.append("=" * len(module_title))
        module_content.append("")
        module_content.append(f".. automodule:: ABConnect.api.models.{module_name}")
        module_content.append("   :members:")
        module_content.append("   :undoc-members:")
        module_content.append("   :show-inheritance:")
        module_content.append("")
        
        # Save module documentation
        module_path = models_dir / f"{module_name}.rst"
        with open(module_path, 'w') as f:
            f.write('\n'.join(module_content))
    
    # Save index
    index_path = models_dir / "index.rst"
    with open(index_path, 'w') as f:
        f.write('\n'.join(index_content))
    
    print(f"Generated model documentation in {models_dir}")


def main():
    """Generate enhanced API documentation with model integration."""
    import sys
    
    # Add parent directory to path so we can import ABConnect
    sys.path.insert(0, str(Path(__file__).parent.parent))
    
    # Load Pydantic models
    print("Loading Pydantic models...")
    models = get_pydantic_models()
    print(f"Loaded {len(models)} models")
    
    # Generate model documentation
    print("Generating model documentation...")
    generate_model_documentation(models)
    
    # Now generate enhanced API documentation
    from generate_api_docs import main as generate_basic_docs
    
    # First generate basic docs
    print("Generating enhanced API documentation...")
    generate_basic_docs()
    
    print("\nEnhanced documentation generation complete!")
    print("\nNext steps:")
    print("1. Update conf.py to include api/models in the toctree")
    print("2. Run 'make html' to build the documentation")
    print("3. The models will be cross-referenced in the API endpoint documentation")


if __name__ == "__main__":
    main()