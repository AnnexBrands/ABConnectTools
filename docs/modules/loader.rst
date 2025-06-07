Loader Module
=============

The Loader module provides robust file loading capabilities for various formats with automatic encoding detection.

.. automodule:: ABConnect.Loader
   :members:
   :undoc-members:
   :show-inheritance:

FileLoader
----------

.. autoclass:: ABConnect.Loader.FileLoader
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__
   :noindex:

Supported Formats
-----------------

* **CSV** - Comma-separated values files
* **JSON** - JavaScript Object Notation files
* **XLSX/XLS** - Excel spreadsheet files

Features
--------

* Automatic encoding detection for text files
* Character encoding cleanup
* Support for multiple Excel sheets
* Robust error handling

Usage Examples
--------------

Loading CSV Files
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ABConnect.Loader import FileLoader
   
   loader = FileLoader()
   
   # Load CSV with automatic encoding detection
   df = loader.load('data.csv')
   
   # Load with specific encoding
   df = loader.load('data.csv', encoding='utf-8')

Loading Excel Files
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Load specific sheet
   df = loader.load('data.xlsx', sheet_name='Sheet1')
   
   # Load all sheets
   sheets = loader.load('data.xlsx', sheet_name=None)
   
   # Access individual sheets
   sheet1_df = sheets['Sheet1']

Loading JSON Files
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Load JSON data
   data = loader.load('data.json')
   
   # Works with nested structures
   config = loader.load('config.json')
   api_key = config['api']['key']

Error Handling
--------------

.. code-block:: python

   from ABConnect.exceptions import ABConnectError
   
   try:
       data = loader.load('nonexistent.csv')
   except ABConnectError as e:
       print(f"Failed to load file: {e}")

Character Encoding
------------------

The loader automatically handles various character encoding issues:

* BOM (Byte Order Mark) removal
* Invalid character replacement
* Smart encoding detection using chardet