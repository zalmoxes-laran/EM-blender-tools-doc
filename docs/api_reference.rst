API Reference
=============

This section documents the main APIs and modules in EM Tools.

Core Modules
------------

em_graph Module
^^^^^^^^^^^^^^^

The central module for graph management.

.. py:class:: EMGraph

   Main class for Extended Matrix graph operations.

   .. py:method:: load_graphml(filepath)
   
      Load a GraphML file into the EM system.
      
      :param filepath: Path to the GraphML file
      :type filepath: str
      :returns: True if successful
      :rtype: bool
      
   .. py:method:: get_nodes_by_type(node_type)
   
      Retrieve all nodes of a specific type.
      
      :param node_type: Type of nodes to retrieve
      :type node_type: str
      :returns: List of matching nodes
      :rtype: list
      
   .. py:method:: find_connected_nodes(node_id, edge_type=None)
   
      Find nodes connected to a given node.
      
      :param node_id: ID of the source node
      :type node_id: str
      :param edge_type: Optional edge type filter
      :type edge_type: str
      :returns: List of connected nodes
      :rtype: list

Visual Manager API
^^^^^^^^^^^^^^^^^^

.. py:function:: update_display_mode(mode)

   Update the visualization mode for all proxies.
   
   :param mode: Display mode ('EM' or 'PERIODS')
   :type mode: str

.. py:function:: create_labels(objects, camera)

   Create labels for selected objects.
   
   :param objects: List of objects to label
   :type objects: list
   :param camera: Camera for label orientation
   :type camera: bpy.types.Object

Operators
---------

Import Operators
^^^^^^^^^^^^^^^^

.. py:class:: IMPORT_OT_graphml

   Import GraphML file operator.
   
   :bl_idname: import_scene.graphml
   :bl_label: Import GraphML
   
   .. py:method:: execute(context)
   
      Execute the import operation.

.. py:class:: IMPORT_OT_emdb

   Import EM database operator.
   
   :bl_idname: import_scene.emdb
   :bl_label: Import EMdb

Export Operators
^^^^^^^^^^^^^^^^

.. py:class:: EXPORT_OT_heriverse

   Export to Heriverse format.
   
   :bl_idname: export_scene.heriverse
   :bl_label: Export Heriverse
   
   Properties:
      - ``export_path``: Output directory path
      - ``use_draco``: Enable Draco compression
      - ``export_textures``: Export textures separately

.. py:class:: EXPORT_OT_emviq

   Export to EMviq web format.
   
   :bl_idname: export_scene.emviq
   :bl_label: Export EMviq

Property Groups
---------------

EM Settings
^^^^^^^^^^^

.. py:class:: EMAddonSettings

   Global addon settings.
   
   Properties:
      - ``preserve_web_url``: Preserve URLs from GraphML
      - ``overwrite_url_with_dosco_filepath``: Use DosCo paths
      - ``dosco_options``: Show DosCo options

.. py:class:: ExportVars

   Export settings property group.
   
   Properties:
      - ``format_file``: Export format selection
      - ``heriverse_use_draco``: Draco compression toggle
      - ``heriverse_draco_level``: Compression level

Utility Functions
-----------------

Graph Utilities
^^^^^^^^^^^^^^^

.. py:function:: find_proxy_by_node(node_id)

   Find Blender object corresponding to a graph node.
   
   :param node_id: Node identifier
   :type node_id: str
   :returns: Blender object or None
   :rtype: bpy.types.Object

.. py:function:: update_proxy_material(proxy, color)

   Update proxy object material color.
   
   :param proxy: Proxy object
   :type proxy: bpy.types.Object
   :param color: RGB color tuple
   :type color: tuple

Data Management
^^^^^^^^^^^^^^^

.. py:function:: populate_em_list(context)

   Populate the EM elements list from graph data.
   
   :param context: Blender context
   :type context: bpy.types.Context

.. py:function:: stream_paradata(node_id, streaming_mode)

   Stream paradata for a specific node.
   
   :param node_id: Node identifier
   :type node_id: str
   :param streaming_mode: Enable/disable streaming
   :type streaming_mode: bool

Constants and Enumerations
--------------------------

Node Types
^^^^^^^^^^

.. py:data:: NODE_TYPES

   Dictionary of supported node types::
   
      NODE_TYPES = {
          'US': 'Stratigraphic Unit',
          'USV': 'Virtual Stratigraphic Unit',
          'SF': 'Special Find',
          'USD': 'Documentary Stratigraphic Unit',
          'serSU': 'Series of Stratigraphic Unit',
          'serUSD': 'Series of Documentary Stratigraphic Unit',
          'serUSVn': 'Series of Non-Structural Virtual Stratigraphic Unit',
          'serUSVs': 'Series of Structural Virtual Stratigraphic Unit',
          'DOC': 'Document',
          'PROP': 'Property',
          'COMB': 'Combiner',
          'EXT': 'Extractor'
      }

Edge Types
^^^^^^^^^^

.. py:data:: EDGE_TYPES

   Dictionary of supported edge types::
   
      EDGE_TYPES = {
          'CONT': 'Contemporary',
          'LATER': 'Later Than',
          'PART_OF': 'Part Of',
          'PROP_OF': 'Property Of',
          'DOC_OF': 'Document Of'
      }

Display Modes
^^^^^^^^^^^^^

.. py:data:: DISPLAY_MODES

   Available display modes::
   
      DISPLAY_MODES = [
          ('EM', 'Extended Matrix', 'Color by node type'),
          ('PERIODS', 'Periods', 'Color by chronological period'),
          ('PROPERTIES', 'Properties', 'Color by property values')
      ]

Callbacks and Handlers
----------------------

Update Callbacks
^^^^^^^^^^^^^^^^

.. py:function:: em_graph_update_callback(scene)

   Called when the EM graph needs updating.
   
   :param scene: Current Blender scene
   :type scene: bpy.types.Scene

.. py:function:: proxy_selection_callback(scene)

   Handles proxy selection synchronization.
   
   :param scene: Current Blender scene
   :type scene: bpy.types.Scene

Event Handlers
^^^^^^^^^^^^^^

.. py:function:: on_graphml_loaded(filepath)

   Event handler for GraphML file loading.
   
   :param filepath: Path to loaded file
   :type filepath: str

.. py:function:: on_export_complete(format, filepath)

   Event handler for export completion.
   
   :param format: Export format used
   :type format: str
   :param filepath: Output file path
   :type filepath: str

Extension Points
----------------

Custom Node Types
^^^^^^^^^^^^^^^^^

To add a custom node type::

   from em_tools import node_registry
   
   @node_registry.register('CUSTOM')
   class CustomNode:
       def __init__(self, id, data):
           self.id = id
           self.data = data
       
       def get_display_name(self):
           return f"Custom: {self.id}"
       
       def get_color(self):
           return (1.0, 0.5, 0.0)  # Orange

Custom Exporters
^^^^^^^^^^^^^^^^

To add a custom exporter::

   from em_tools import export_registry
   
   @export_registry.register('custom', 'Custom Format')
   class CustomExporter:
       def __init__(self, context, filepath):
           self.context = context
           self.filepath = filepath
       
       def export(self):
           # Implementation here
           pass

Integration APIs
----------------

ATON Integration
^^^^^^^^^^^^^^^^

.. py:class:: ATONExporter

   Integration with ATON framework.
   
   .. py:method:: setup_project(project_name, user_name)
   
      Setup ATON project configuration.
      
      :param project_name: Name of the project
      :type project_name: str
      :param user_name: ATON username
      :type user_name: str
   
   .. py:method:: export_scene(scene_name, include_metadata=True)
   
      Export scene to ATON format.
      
      :param scene_name: Name for the exported scene
      :type scene_name: str
      :param include_metadata: Include EM metadata
      :type include_metadata: bool

Heriverse Integration
^^^^^^^^^^^^^^^^^^^^^

.. py:class:: HeriverseExporter

   Export to Heriverse format.
   
   .. py:method:: configure(options)
   
      Configure export options.
      
      :param options: Dictionary of export options
      :type options: dict
   
   .. py:method:: export_graph(graph_id, output_path)
   
      Export specific graph to Heriverse.
      
      :param graph_id: Graph identifier
      :type graph_id: str
      :param output_path: Output directory
      :type output_path: str

Error Handling
--------------

Exception Classes
^^^^^^^^^^^^^^^^^

.. py:exception:: EMGraphError

   Base exception for graph-related errors.

.. py:exception:: EMImportError

   Raised when import operations fail.

.. py:exception:: EMExportError

   Raised when export operations fail.

.. py:exception:: EMValidationError

   Raised when data validation fails.

Error Codes
^^^^^^^^^^^

.. py:data:: ERROR_CODES

   Standard error codes::
   
      ERROR_CODES = {
          'E001': 'Invalid GraphML format',
          'E002': 'Missing required node attribute',
          'E003': 'Circular reference detected',
          'E004': 'Export path not writable',
          'E005': 'Unsupported file format'
      }

Best Practices
--------------

Performance Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Batch Operations**: Use batch operations when updating multiple proxies::

      with context.temp_override(selected_objects=objects):
          bpy.ops.em.batch_update()

2. **Lazy Loading**: Load graph data on demand::

      graph = EMGraph(lazy_load=True)
      graph.load_nodes_by_type('US')  # Load only US nodes

3. **Memory Management**: Clear unused data::

      graph.clear_cache()
      bpy.ops.em.purge_unused_data()

Thread Safety
^^^^^^^^^^^^^

EM Tools operations should be called from the main thread::

   import bpy
   
   def thread_safe_operation():
       def actual_operation():
           # Your code here
           pass
       
       bpy.app.timers.register(actual_operation)

Debugging
^^^^^^^^^

Enable debug logging::

   import logging
   from em_tools import logger
   
   logger.setLevel(logging.DEBUG)
   
   # Debug specific modules
   logging.getLogger('em_tools.graph').setLevel(logging.DEBUG)

Version Compatibility
---------------------

API Versioning
^^^^^^^^^^^^^^

Check API version::

   from em_tools import __api_version__
   
   if __api_version__ >= (1, 5):
       # Use new features
       pass
   else:
       # Fallback to old API
       pass

Deprecation Warnings
^^^^^^^^^^^^^^^^^^^^

Handle deprecated features::

   import warnings
   
   with warnings.catch_warnings():
       warnings.simplefilter("ignore", DeprecationWarning)
       # Use deprecated feature
       old_function()

Further Reading
---------------

- :doc:`/installation` - Installation and setup
- :doc:`/usage_examples` - Practical examples
- :doc:`/panels/index` - UI and structure overview
- `GitHub Repository <https://github.com/zalmoxes-laran/EM-blender-tools>`_ - Source code