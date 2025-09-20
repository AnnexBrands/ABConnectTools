#!/usr/bin/env python3
"""Generate all Pydantic models from swagger.json.

This script regenerates all API models from the swagger specification,
organizing them by tags into appropriate modules.
"""

import sys
import os
from pathlib import Path
from collections import defaultdict

# Import the generator without loading the existing package
sys.path.insert(0, str(Path(__file__).parent / "ABConnect" / "api"))
from model_generator import SwaggerModelGenerator


def main():
    """Generate all models and organize into modules."""
    print("🔄 Generating Pydantic models from swagger.json...")
    
    # Initialize generator
    swagger_path = Path("ABConnect/base/swagger.json")
    if not swagger_path.exists():
        print(f"❌ Swagger file not found: {swagger_path}")
        sys.exit(1)
    
    generator = SwaggerModelGenerator(swagger_path)
    
    # Generate all models
    print(f"📊 Found {len(generator.schemas)} schemas to process")
    models = generator.generate_all_models()
    enums = generator.enums
    
    print(f"✅ Generated {len(models)} models and {len(enums)} enums")
    
    # Organize by tags
    tag_models = defaultdict(list)
    tag_enums = defaultdict(list)
    
    for schema_name in generator.schemas.keys():
        tag = generator.get_tag_for_schema(schema_name)
        tag_clean = tag.lower().replace(' ', '_').replace('-', '_')
        
        if schema_name in enums:
            tag_enums[tag_clean].append(schema_name)
        else:
            tag_models[tag_clean].append(schema_name)
    
    # Create models directory structure
    models_dir = Path("ABConnect/api/models")
    
    # Backup existing models
    if models_dir.exists():
        backup_dir = models_dir.with_suffix('.backup')
        if backup_dir.exists():
            import shutil
            shutil.rmtree(backup_dir)
        models_dir.rename(backup_dir)
        print(f"📦 Backed up existing models to {backup_dir}")
    
    models_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate enums module
    _generate_enums_module(models_dir, enums, generator)
    
    # Generate tag-based modules
    all_exports = []
    for tag, model_names in tag_models.items():
        if not model_names:
            continue
            
        module_exports = _generate_tag_module(
            models_dir, tag, model_names, models, generator
        )
        all_exports.extend(module_exports)
    
    # Generate main __init__.py
    _generate_main_init(models_dir, tag_models, tag_enums, all_exports)
    
    print(f"🎉 Successfully generated {len(models)} models in {len(tag_models)} modules")
    print(f"📁 Models available in: {models_dir}")


def _generate_enums_module(models_dir: Path, enums: dict, generator: SwaggerModelGenerator):
    """Generate enums.py module with all enumerations."""
    enums_file = models_dir / "enums.py"
    
    with open(enums_file, 'w') as f:
        f.write('"""Enumeration types for ABConnect API models."""\n\n')
        f.write('from enum import Enum\n\n')
        
        for enum_name, enum_code in enums.items():
            f.write(f'{enum_code}\n\n')
        
        # Export all enums
        enum_names = list(enums.keys())
        f.write(f'__all__ = {enum_names}\n')
    
    print(f"📝 Generated enums module with {len(enums)} enums")


def _generate_tag_module(models_dir: Path, tag: str, model_names: list, 
                        models: dict, generator: SwaggerModelGenerator) -> list:
    """Generate module for a specific tag."""
    module_file = models_dir / f"{tag}.py"
    
    with open(module_file, 'w') as f:
        # Module header
        tag_display = tag.replace('_', ' ').title()
        f.write(f'"""{tag_display} models for ABConnect API."""\n\n')
        
        # Collect all imports
        all_imports = set()
        enum_imports = set()
        base_imports = set()
        
        for model_name in model_names:
            if model_name in generator.imports:
                imports = generator.imports[model_name]
                
                # Separate different types of imports
                for imp in imports:
                    if imp in ['Optional', 'List', 'Dict', 'Any', 'Union']:
                        all_imports.add(imp)
                    elif imp in ['datetime', 'date']:
                        all_imports.add(imp)
                    elif imp.endswith('Enum'):
                        enum_imports.add(imp)
                    elif imp in ['ABConnectBaseModel', 'IdentifiedModel', 'TimestampedModel', 
                               'ActiveModel', 'CompanyRelatedModel', 'JobRelatedModel',
                               'FullAuditModel', 'CompanyAuditModel', 'JobAuditModel']:
                        base_imports.add(imp)
                    elif imp == 'Field':
                        all_imports.add(imp)
        
        # Write imports
        if all_imports:
            typing_imports = [imp for imp in all_imports if imp in ['Optional', 'List', 'Dict', 'Any', 'Union']]
            if typing_imports:
                f.write(f'from typing import {", ".join(sorted(typing_imports))}\n')
            
            if 'datetime' in all_imports:
                f.write('from datetime import datetime\n')
            if 'date' in all_imports:
                f.write('from datetime import date\n')
            
            pydantic_imports = [imp for imp in all_imports if imp in ['Field']]
            if pydantic_imports:
                f.write(f'from pydantic import {", ".join(sorted(pydantic_imports))}\n')
        
        if base_imports:
            f.write(f'from .base import {", ".join(sorted(base_imports))}\n')
        
        if enum_imports:
            f.write(f'from .enums import {", ".join(sorted(enum_imports))}\n')
        
        f.write('\n')
        
        # Write models
        exports = []
        for model_name in sorted(model_names):
            if model_name in models:
                f.write(f'{models[model_name]}\n\n')
                exports.append(model_name)
        
        # Export list
        f.write(f'__all__ = {exports}\n')
    
    print(f"📝 Generated {tag} module with {len(exports)} models")
    return exports


def _generate_main_init(models_dir: Path, tag_models: dict, tag_enums: dict, all_exports: list):
    """Generate main __init__.py for models package."""
    init_file = models_dir / "__init__.py"
    
    with open(init_file, 'w') as f:
        f.write('"""ABConnect API models package.\n\n')
        f.write('Auto-generated from swagger.json specification.\n')
        f.write('Contains Pydantic models for all API schemas.\n')
        f.write('"""\n\n')
        
        # Import from base
        f.write('from .base import *\n')
        
        # Import enums
        if tag_enums:
            f.write('from .enums import *\n')
        
        # Import from tag modules
        for tag in sorted(tag_models.keys()):
            if tag_models[tag]:
                f.write(f'from .{tag} import *\n')
        
        f.write('\n')
        
        # Create comprehensive __all__
        f.write('# Export all models and utilities\n')
        f.write('__all__ = [\n')
        f.write('    # Base classes\n')
        f.write('    "ABConnectBaseModel",\n')
        f.write('    "IdentifiedModel",\n') 
        f.write('    "TimestampedModel",\n')
        f.write('    "ActiveModel",\n')
        f.write('    "CompanyRelatedModel",\n')
        f.write('    "JobRelatedModel",\n')
        f.write('    "FullAuditModel",\n')
        f.write('    "CompanyAuditModel",\n')
        f.write('    "JobAuditModel",\n')
        
        if tag_enums:
            f.write('    # Enums\n')
            for enums in tag_enums.values():
                for enum_name in sorted(enums):
                    f.write(f'    "{enum_name}",\n')
        
        f.write('    # Models\n')
        for model_name in sorted(all_exports):
            f.write(f'    "{model_name}",\n')
        
        f.write(']\n')
    
    print(f"📝 Generated main __init__.py with {len(all_exports)} total exports")


if __name__ == "__main__":
    main()