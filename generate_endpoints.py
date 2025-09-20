#!/usr/bin/env python3
"""Generate all endpoint modules from swagger paths.

This script creates the 25 endpoint modules based on API directory structure,
maintaining BaseEndpoint inheritance and adding type safety.
"""

import json
import re
from pathlib import Path
from collections import defaultdict


def to_pascal_case(snake_str: str) -> str:
    """Convert snake_case to PascalCase."""
    return ''.join(word.capitalize() for word in snake_str.replace('-', '_').split('_'))


def to_snake_case(camel_str: str) -> str:
    """Convert camelCase/PascalCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def sanitize_method_name(operation_id: str, method: str, path: str) -> str:
    """Generate a clean Python method name."""
    if operation_id:
        # Use operation ID as base
        method_name = to_snake_case(operation_id)
    else:
        # Generate from method and path
        path_parts = [p for p in path.split('/') if p and not p.startswith('{')]
        if len(path_parts) > 2:  # Skip 'api' and module name
            action = '_'.join(path_parts[2:])
        else:
            action = method.lower()
        method_name = f"{method.lower()}_{action}"
    
    # Ensure valid Python identifier
    method_name = re.sub(r'[^a-zA-Z0-9_]', '_', method_name).lower()
    method_name = re.sub(r'_+', '_', method_name).strip('_')
    
    # Handle reserved keywords
    if method_name in ['class', 'def', 'import', 'from', 'type', 'list']:
        method_name = f"{method_name}_api"
    
    return method_name


def generate_endpoint_module(module_name: str, paths: list, swagger_data: dict) -> str:
    """Generate endpoint module code."""
    class_name = f"{to_pascal_case(module_name)}Endpoint"
    api_path = f"/api/{module_name}"
    
    # Extract all methods for this module
    methods = []
    imports = {'BaseEndpoint'}
    
    for path_info in paths:
        path = path_info['path']
        method = path_info['method']
        spec = path_info['spec']
        
        operation_id = spec.get('operationId', '')
        summary = spec.get('summary', '')
        description = spec.get('description', '')
        
        method_name = sanitize_method_name(operation_id, method, path)
        
        # Generate method signature
        path_params = []
        query_params = []
        
        # Extract path parameters
        path_param_matches = re.findall(r'\{([^}]+)\}', path)
        for param in path_param_matches:
            path_params.append(f"{param}: str")
        
        # Extract query/body parameters from spec
        parameters = spec.get('parameters', [])
        for param in parameters:
            if param.get('in') == 'query':
                param_name = to_snake_case(param['name'])
                param_type = "str"  # Simplified for now
                required = param.get('required', False)
                if not required:
                    param_type = f"Optional[{param_type}]"
                    imports.add('Optional')
                query_params.append(f"{param_name}: {param_type} = None")
        
        # Build method
        all_params = path_params + query_params
        if spec.get('requestBody'):
            all_params.append("data: dict = None")
        
        param_str = ", ".join(all_params)
        if param_str:
            param_str = ", " + param_str
        
        # Create relative path for internal use
        relative_path = path.replace(f'/api/{module_name}', '') or '/'
        
        method_code = f'''    def {method_name}(self{param_str}) -> dict:
        """{summary or f'{method} {path}'}
        
        {description}
        
        Returns:
            dict: API response data
        """
        path = "{relative_path}"'''
        
        # Handle path parameters
        if path_param_matches:
            for param in path_param_matches:
                method_code += f'''
        path = path.replace("{{{param}}}", {param})'''
        
        # Handle query parameters
        if query_params or spec.get('requestBody'):
            method_code += '''
        kwargs = {}'''
            
        if query_params:
            method_code += '''
        params = {}'''
            for param in parameters:
                if param.get('in') == 'query':
                    param_name = to_snake_case(param['name'])
                    orig_name = param['name']
                    method_code += f'''
        if {param_name} is not None:
            params["{orig_name}"] = {param_name}'''
            method_code += '''
        if params:
            kwargs["params"] = params'''
        
        if spec.get('requestBody'):
            method_code += '''
        if data is not None:
            kwargs["json"] = data'''
        
        method_code += f'''
        return self._make_request("{method}", path, **kwargs)'''
        
        methods.append(method_code)
    
    # Generate module code
    import_lines = []
    if 'Optional' in imports:
        import_lines.append('from typing import Optional')
    import_lines.append('from .base import BaseEndpoint')
    
    module_code = f'''"""{to_pascal_case(module_name)} API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to {api_path}/* endpoints.
"""

{chr(10).join(import_lines)}


class {class_name}(BaseEndpoint):
    """{to_pascal_case(module_name)} API endpoint operations.
    
    Handles all API operations for {api_path}/* endpoints.
    Total endpoints: {len(paths)}
    """
    
    api_path = "{api_path}"

{chr(10).join(methods)}
'''
    
    return module_code


def main():
    """Generate all 25 endpoint modules."""
    print("🔄 Generating endpoint modules from swagger paths...")
    
    # Load swagger
    swagger_path = Path("ABConnect/base/swagger.json")
    with open(swagger_path, 'r') as f:
        swagger_data = json.load(f)
    
    # Group paths by API module
    api_modules = defaultdict(list)
    paths = swagger_data.get('paths', {})
    
    for path, methods in paths.items():
        if path.startswith('/api/'):
            segments = path.split('/')
            if len(segments) > 2:
                module_name = segments[2]
                if not module_name.startswith('{'):
                    for method, spec in methods.items():
                        api_modules[module_name].append({
                            'path': path,
                            'method': method.upper(),
                            'spec': spec
                        })
    
    print(f"📊 Found {len(api_modules)} API modules to generate")
    
    # Backup existing endpoints
    endpoints_dir = Path("ABConnect/api/endpoints")
    if endpoints_dir.exists():
        backup_dir = endpoints_dir.with_suffix('.backup')
        if backup_dir.exists():
            import shutil
            shutil.rmtree(backup_dir)
        endpoints_dir.rename(backup_dir)
        print(f"📦 Backed up existing endpoints to {backup_dir}")
    
    endpoints_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy base.py from backup
    base_backup = backup_dir / "base.py"
    if base_backup.exists():
        import shutil
        shutil.copy2(base_backup, endpoints_dir / "base.py")
        print("📝 Restored enhanced base.py")
    
    # Generate all endpoint modules
    generated_modules = []
    for module_name, module_paths in sorted(api_modules.items()):
        if not module_paths:
            continue
            
        print(f"📝 Generating {module_name}.py ({len(module_paths)} endpoints)")
        
        module_code = generate_endpoint_module(module_name, module_paths, swagger_data)
        module_file = endpoints_dir / f"{module_name}.py"
        
        with open(module_file, 'w') as f:
            f.write(module_code)
        
        generated_modules.append(module_name)
    
    # Generate __init__.py
    init_file = endpoints_dir / "__init__.py"
    with open(init_file, 'w') as f:
        f.write('''"""ABConnect API endpoints package.

Auto-generated from swagger.json specification.
Contains endpoint classes for all API modules.
"""

from .base import BaseEndpoint

''')
        
        # Import all endpoint classes
        for module in sorted(generated_modules):
            class_name = f"{to_pascal_case(module)}Endpoint"
            f.write(f'from .{module} import {class_name}\n')
        
        f.write('\n# Export all endpoint classes\n__all__ = [\n    "BaseEndpoint",\n')
        for module in sorted(generated_modules):
            class_name = f"{to_pascal_case(module)}Endpoint"
            f.write(f'    "{class_name}",\n')
        f.write(']\n')
    
    print(f"✅ Generated {len(generated_modules)} endpoint modules")
    print(f"📁 Endpoints available in: {endpoints_dir}")


if __name__ == "__main__":
    main()