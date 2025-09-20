"""Swagger-to-Pydantic model generator for ABConnect API.

This module generates Pydantic models from swagger.json specifications,
handling the 293 schemas with proper typing, imports, and organization.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set, Any, Optional, Tuple
from collections import defaultdict
from datetime import datetime


class SwaggerModelGenerator:
    """Generate Pydantic models from swagger schema definitions."""
    
    def __init__(self, swagger_path: str):
        """Initialize generator with swagger file."""
        self.swagger_path = Path(swagger_path)
        self.swagger_data = self._load_swagger()
        self.schemas = self.swagger_data.get('components', {}).get('schemas', {})
        self.enums = {}
        self.models = {}
        self.imports = defaultdict(set)
        self.dependencies = defaultdict(set)
        
    def _load_swagger(self) -> Dict[str, Any]:
        """Load swagger JSON file."""
        with open(self.swagger_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _get_python_type(self, schema: Dict[str, Any], context: str = "") -> Tuple[str, Set[str]]:
        """Convert swagger schema to Python type annotation.
        
        Returns:
            Tuple of (type_string, required_imports)
        """
        imports = set()
        
        # Handle $ref
        if '$ref' in schema:
            ref_path = schema['$ref']
            if ref_path.startswith('#/components/schemas/'):
                ref_name = ref_path.split('/')[-1]
                return ref_name, {ref_name}
        
        # Handle type
        schema_type = schema.get('type', 'object')
        nullable = schema.get('nullable', False)
        
        if schema_type == 'string':
            if 'enum' in schema:
                # Generate enum name from context
                enum_name = f"{context}Enum" if context else "StringEnum"
                self.enums[enum_name] = schema['enum']
                imports.add(enum_name)
                base_type = enum_name
            elif schema.get('format') == 'date-time':
                imports.add('datetime')
                base_type = 'datetime'
            elif schema.get('format') == 'date':
                imports.add('date')
                base_type = 'date'
            else:
                base_type = 'str'
                
        elif schema_type == 'integer':
            if 'enum' in schema:
                enum_name = f"{context}Enum" if context else "IntEnum"
                self.enums[enum_name] = schema['enum']
                imports.add(enum_name)
                base_type = enum_name
            else:
                base_type = 'int'
                
        elif schema_type == 'number':
            base_type = 'float'
            
        elif schema_type == 'boolean':
            base_type = 'bool'
            
        elif schema_type == 'array':
            items_schema = schema.get('items', {})
            item_type, item_imports = self._get_python_type(items_schema, f"{context}Item")
            imports.update(item_imports)
            imports.add('List')
            base_type = f'List[{item_type}]'
            
        elif schema_type == 'object':
            # For object types, check if it has properties
            if 'properties' in schema:
                # This should be a separate model
                model_name = context or 'ObjectModel'
                return model_name, {model_name}
            else:
                # Generic object
                imports.add('Dict')
                imports.add('Any')
                base_type = 'Dict[str, Any]'
        else:
            # Fallback
            imports.add('Any')
            base_type = 'Any'
        
        # Handle nullable
        if nullable:
            imports.add('Optional')
            return f'Optional[{base_type}]', imports
        
        return base_type, imports
    
    def _get_base_class(self, schema_name: str, schema: Dict[str, Any]) -> str:
        """Determine appropriate base class for schema."""
        properties = schema.get('properties', {})
        prop_names = set(properties.keys())
        
        # Check for audit patterns
        has_id = 'id' in prop_names
        has_timestamps = any(prop in prop_names for prop in ['createdDate', 'modifiedDate'])
        has_active = 'isActive' in prop_names
        has_company = any(prop in prop_names for prop in ['companyId', 'companyName'])
        has_job = any(prop in prop_names for prop in ['jobId', 'jobID'])
        
        if has_id and has_timestamps and has_active and has_company:
            return 'CompanyAuditModel'
        elif has_id and has_timestamps and has_active and has_job:
            return 'JobAuditModel'
        elif has_id and has_timestamps and has_active:
            return 'FullAuditModel'
        elif has_timestamps:
            return 'TimestampedModel'
        elif has_id:
            return 'IdentifiedModel'
        elif has_active:
            return 'ActiveModel'
        elif has_company:
            return 'CompanyRelatedModel'
        elif has_job:
            return 'JobRelatedModel'
        else:
            return 'ABConnectBaseModel'
    
    def _generate_field_definition(self, prop_name: str, prop_schema: Dict[str, Any], 
                                 is_required: bool, context: str) -> Tuple[str, Set[str]]:
        """Generate field definition with proper Field() usage."""
        imports = {'Field'}
        
        # Get type
        python_type, type_imports = self._get_python_type(prop_schema, f"{context}{prop_name.title()}")
        imports.update(type_imports)
        
        # Make optional if not required
        if not is_required and not python_type.startswith('Optional'):
            imports.add('Optional')
            python_type = f'Optional[{python_type}]'
        
        # Build Field parameters
        field_params = []
        
        # Default value
        if is_required:
            field_params.append('...')
        else:
            field_params.append('None')
        
        # Alias (convert snake_case to camelCase for swagger compatibility)
        camel_case = self._to_camel_case(prop_name)
        if camel_case != prop_name:
            field_params.append(f'alias="{camel_case}"')
        
        # Description
        description = prop_schema.get('description', '').strip()
        if description:
            # Escape quotes and limit length
            description = description.replace('"', '\\"')[:100]
            field_params.append(f'description="{description}"')
        
        # Validation constraints
        if prop_schema.get('type') == 'string':
            min_length = prop_schema.get('minLength')
            max_length = prop_schema.get('maxLength')
            if min_length is not None:
                field_params.append(f'min_length={min_length}')
            if max_length is not None:
                field_params.append(f'max_length={max_length}')
        
        field_def = f'Field({", ".join(field_params)})'
        
        return f'{prop_name}: {python_type} = {field_def}', imports
    
    def _to_camel_case(self, snake_str: str) -> str:
        """Convert snake_case to camelCase."""
        components = snake_str.split('_')
        return components[0] + ''.join(word.capitalize() for word in components[1:])
    
    def _to_snake_case(self, camel_str: str) -> str:
        """Convert camelCase to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def _sanitize_name(self, name: str) -> str:
        """Sanitize name for Python class/variable."""
        # Handle reserved keywords
        reserved = {'class', 'def', 'if', 'else', 'for', 'while', 'import', 'from', 'type'}
        if name.lower() in reserved:
            name = f'{name}Model'
        
        # Ensure valid Python identifier
        name = re.sub(r'[^a-zA-Z0-9_]', '', name)
        if name and name[0].isdigit():
            name = f'Model{name}'
        
        return name
    
    def generate_model(self, schema_name: str, schema: Dict[str, Any]) -> str:
        """Generate a single Pydantic model from schema."""
        schema_name = self._sanitize_name(schema_name)
        
        # Skip if already processed
        if schema_name in self.models:
            return self.models[schema_name]
        
        # Handle enums
        if 'enum' in schema:
            enum_values = schema['enum']
            enum_type = 'str' if all(isinstance(v, str) for v in enum_values) else 'int'
            
            enum_code = f'class {schema_name}({enum_type}, Enum):\n'
            enum_code += f'    """{schema.get("description", f"{schema_name} enumeration")}"""\n'
            
            for value in enum_values:
                # Create valid Python identifier for enum member
                if isinstance(value, str):
                    member_name = re.sub(r'[^a-zA-Z0-9_]', '_', value.upper())
                    if member_name and member_name[0].isdigit():
                        member_name = f'VALUE_{member_name}'
                    enum_code += f'    {member_name} = "{value}"\n'
                else:
                    member_name = f'VALUE_{value}'
                    enum_code += f'    {member_name} = {value}\n'
            
            self.enums[schema_name] = enum_code
            return enum_code
        
        # Generate regular model
        properties = schema.get('properties', {})
        required = set(schema.get('required', []))
        
        # Get base class
        base_class = self._get_base_class(schema_name, schema)
        imports = {base_class}
        
        # Model header
        model_code = f'class {schema_name}({base_class}):\n'
        model_code += f'    """{schema.get("description", f"{schema_name} model")}"""\n'
        
        # Generate fields
        fields = []
        for prop_name, prop_schema in properties.items():
            # Convert to snake_case for Python field names
            python_field_name = self._to_snake_case(prop_name)
            
            # Skip if base class already provides this field
            base_fields = self._get_base_class_fields(base_class)
            if python_field_name in base_fields:
                continue
            
            is_required = prop_name in required
            field_def, field_imports = self._generate_field_definition(
                python_field_name, prop_schema, is_required, schema_name
            )
            fields.append(field_def)
            imports.update(field_imports)
        
        # Add fields to model
        if fields:
            model_code += '\n'
            for field in fields:
                model_code += f'    {field}\n'
        else:
            model_code += '    pass\n'
        
        self.models[schema_name] = model_code
        self.imports[schema_name] = imports
        
        return model_code
    
    def _get_base_class_fields(self, base_class: str) -> Set[str]:
        """Get fields provided by base class to avoid duplication."""
        base_fields = {
            'IdentifiedModel': {'id'},
            'TimestampedModel': {'created_date', 'modified_date', 'created_by', 'modified_by'},
            'ActiveModel': {'is_active'},
            'CompanyRelatedModel': {'company_id', 'company_name'},
            'JobRelatedModel': {'job_id'},
            'FullAuditModel': {'id', 'created_date', 'modified_date', 'created_by', 'modified_by', 'is_active'},
            'CompanyAuditModel': {'id', 'created_date', 'modified_date', 'created_by', 'modified_by', 'is_active', 'company_id', 'company_name'},
            'JobAuditModel': {'id', 'created_date', 'modified_date', 'created_by', 'modified_by', 'is_active', 'job_id'},
        }
        return base_fields.get(base_class, set())
    
    def generate_all_models(self) -> Dict[str, str]:
        """Generate all models from swagger schemas."""
        for schema_name, schema in self.schemas.items():
            self.generate_model(schema_name, schema)
        
        return self.models
    
    def get_tag_for_schema(self, schema_name: str) -> str:
        """Determine which tag/module a schema belongs to."""
        # Analyze endpoints to see which tags use this schema
        schema_tags = set()
        
        for path, methods in self.swagger_data.get('paths', {}).items():
            for method, spec in methods.items():
                # Check request body
                request_body = spec.get('requestBody', {})
                content = request_body.get('content', {})
                for media_type, media_spec in content.items():
                    schema = media_spec.get('schema', {})
                    if self._schema_references(schema, schema_name):
                        schema_tags.update(spec.get('tags', []))
                
                # Check responses
                responses = spec.get('responses', {})
                for response_code, response_spec in responses.items():
                    response_content = response_spec.get('content', {})
                    for media_type, media_spec in response_content.items():
                        schema = media_spec.get('schema', {})
                        if self._schema_references(schema, schema_name):
                            schema_tags.update(spec.get('tags', []))
        
        # Choose the most specific tag or default
        if not schema_tags:
            # Infer from name
            name_lower = schema_name.lower()
            if 'company' in name_lower:
                return 'Companies'
            elif 'job' in name_lower:
                return 'Job'
            elif 'contact' in name_lower:
                return 'Contacts'
            elif 'address' in name_lower:
                return 'Address'
            elif 'user' in name_lower:
                return 'Users'
            else:
                return 'Shared'
        
        # Return most common tag
        return min(schema_tags) if schema_tags else 'Shared'
    
    def _schema_references(self, schema: Dict[str, Any], target_name: str) -> bool:
        """Check if schema references target schema name."""
        if '$ref' in schema:
            ref_name = schema['$ref'].split('/')[-1]
            return ref_name == target_name
        
        # Check nested schemas
        if 'properties' in schema:
            for prop_schema in schema['properties'].values():
                if self._schema_references(prop_schema, target_name):
                    return True
        
        if 'items' in schema:
            return self._schema_references(schema['items'], target_name)
        
        return False