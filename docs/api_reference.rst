API Reference
=============

This section documents the main modules, operators, and property groups in EM Tools.

.. note::
   EM Tools uses the external `s3dgraphy <https://pypi.org/project/s3dgraphy/>`_ library for graph management.
   Graph classes (nodes, edges, graph operations) are provided by s3dgraphy, not by EM Tools directly.

Architecture Overview
---------------------

EM Tools is structured as a Blender Extension with the following main components:

- **s3dgraphy**: external Python library for Extended Matrix graph operations (GraphML parsing, node/edge management)
- **Blender Operators**: import, export, and UI interaction operators
- **Property Groups**: Blender properties for addon settings, scene state, and UI data
- **Panel modules**: UI panels organized by functional area (em_setup, visual_manager, epoch_manager, etc.)

Graph Access
------------

Graph data is accessed through the s3dgraphy library. The main entry points are:

.. code-block:: python

   from s3dgraphy import multigraph

   # Load a graph from file
   graph = multigraph.load_graph_from_file(filepath)

   # Get a graph by name
   graph = multigraph.get_graph(graph_name)

   # Remove a graph
   multigraph.remove_graph(graph_name)

Import Operators
----------------

.. py:class:: EM_import_GraphML

   Import an Extended Matrix GraphML file.

   :bl_idname: ``import.em_graphml``
   :bl_label: Import EM GraphML
   :file: ``import_operators/importer_graphml.py``

.. py:class:: EM_OT_import_3dgis_database

   Import an external database (Generic Excel, PyArchInit, or EMdb Excel).

   :bl_idname: ``em.import_3dgis_database``
   :bl_label: Import 3D GIS Database
   :file: ``import_operators/import_EMdb.py``

Importer Registry
^^^^^^^^^^^^^^^^^

EM Tools includes a registry for database importers:

.. code-block:: python

   from import_operators.importer_registry import IMPORTER_REGISTRY, create_importer

   # Supported importer types
   # 'generic_xlsx'  - Generic Excel spreadsheet
   # 'emdb_xlsx'     - EMdb Excel format
   # 'pyarchinit'    - PyArchInit database

   # Create an importer instance
   importer = create_importer('generic_xlsx', filepath, options)

:file: ``import_operators/importer_registry.py``

Export Operators
----------------

.. py:class:: EXPORT_OT_heriverse

   Export the project to Heriverse format (3D web viewer based on the ATON Framework).

   :bl_idname: ``export.heriverse``
   :bl_label: Export Heriverse
   :file: ``export_operators/exporter_heriverse.py``

   Exports geometry (GLTF), textures, and EM metadata for the Heriverse web viewer.
   Supports Draco compression and separate texture export.

.. py:class:: JSON_OT_exportEMformat

   Export EM data as JSON for Heriverse.

   :bl_idname: ``export.heriversejson``
   :bl_label: Export Heriverse JSON
   :file: ``export_operators/exporter_heriverse.py``

.. py:class:: EM_export_GraphML

   Reload/update the active GraphML file.

   :bl_idname: ``export.graphml_update``
   :file: ``export_operators/exporter_graphml.py``

.. py:class:: EM_export_GraphML_SaveAs

   Save the graph as a new GraphML file.

   :bl_idname: ``export.graphml_saveas``
   :file: ``export_operators/exporter_graphml.py``

Property Groups
---------------

EMAddonSettings
^^^^^^^^^^^^^^^

Global addon settings, stored in the addon preferences.

:file: ``__init__.py``

Properties:

- ``preserve_web_url`` (BoolProperty): Preserve URLs from GraphML nodes
- ``overwrite_url_with_dosco_filepath`` (BoolProperty): Use DosCo folder paths instead of web URLs
- ``dosco_options`` (BoolProperty): Show DosCo options in the UI
- ``verbose_logging`` (BoolProperty): Enable verbose logging output

ExportVars
^^^^^^^^^^

Export settings property group, stored in the scene.

:file: ``__init__.py``

Properties:

- ``format_file`` (EnumProperty): Export format selection
- ``heriverse_use_draco`` (BoolProperty): Enable Draco mesh compression
- ``heriverse_draco_level`` (IntProperty): Draco compression level

EM_Tools
^^^^^^^^

Main container property group for all EM Tools scene-level settings.

:file: ``em_props.py``

Key properties:

- ``mode_em_advanced`` (BoolProperty): Enable advanced EM mode
- ``experimental_features`` (BoolProperty): Enable experimental features
- ``proxy_display_mode`` (EnumProperty): Current display mode (EM, Epochs, Properties)
- ``proxy_display_alpha`` (FloatProperty): Proxy material transparency

Module Structure
----------------

.. code-block:: text

   EM-blender-tools/
   ├── __init__.py                 # Main entry point, registration
   ├── em_props.py                 # Core property definitions
   ├── em_base_props.py            # Base property groups
   ├── functions.py                # Shared utility functions
   ├── em_setup/                   # EM Data Tree panel
   │   ├── ui.py                   # Panel UI
   │   ├── operators.py            # Setup operators
   │   └── resource_utils.py       # Resource folder utilities
   ├── visual_manager/             # Visual Manager panel
   │   ├── ui.py                   # Panel UI (hosts inline "RM Coloring" experimental section)
   │   ├── operators.py            # Material/display operators
   │   ├── color_ramps.py          # Color scheme definitions
   │   └── label_tools.py          # Label creation
   ├── epoch_manager/              # Epochs Manager panel
   │   ├── ui.py                   # Panel UI
   │   └── operators.py            # Epoch operators
   ├── stratigraphy_manager/       # Stratigraphy Manager panel
   │   ├── ui.py                   # Panel UI
   │   └── data.py                 # Filter data
   ├── activity_manager/           # Activity Manager panel
   │   ├── __init__.py             # Register hub
   │   ├── properties.py           # ActivityItem / ActivityManagerProperties
   │   ├── operators.py            # ACTIVITY_OT_refresh_list
   │   └── ui.py                   # UIList + Panel
   ├── anastylosis_manager/        # Anastylosis / RMSF Manager
   │   ├── __init__.py             # Register hub
   │   ├── properties.py           # PropertyGroups (registered by em_props)
   │   ├── lod_utils.py            # LOD constants + parser + fallback helpers
   │   ├── graph_utils.py          # Graph cleanup + visibility analysis
   │   ├── operators_list.py       # List CRUD operators
   │   ├── operators_link.py       # SF/VSF linking operators
   │   ├── operators_lod.py        # LOD switching operators + menus
   │   └── ui.py                   # UIList + Panel + load_post handler
   ├── rm_manager/                 # RM Manager panel
   ├── paradata_manager/           # Paradata Manager panel
   ├── document_manager/           # 3D Document Manager panel
   ├── em_statistics/              # Mesh statistics CSV export (experimental panel)
   │   ├── __init__.py             # Register hub
   │   ├── materials.py            # CSV loading + material enum items + decimal formatting
   │   ├── metrics.py              # Volume / weight / surface computation
   │   ├── properties.py           # EMSceneProperties + Scene.em_properties
   │   ├── operators.py            # EMExportCSV
   │   └── ui.py                   # EM_PT_ExportPanel (experimental-gated)
   ├── export_manager/             # Export Manager panel (plugin-style providers)
   │   ├── __init__.py             # Register hub + re-export registry API
   │   ├── registry.py             # ExportProvider + register/get_providers
   │   ├── panel.py                # VIEW3D_PT_ExportPanel (loops providers)
   │   └── providers/
   │       ├── __init__.py         # Imports + registers each provider
   │       ├── tabular/            # CSV export section
   │       │   ├── __init__.py
   │       │   ├── ui.py
   │       │   └── operators.py    # OBJECT_OT_ExportUUSS / ExportuussData
   │       └── heriverse/          # Heriverse Export UI section
   │           ├── __init__.py
   │           ├── ui.py
   │           └── properties.py   # Scene.heriverse_* settings
   ├── cronofilter/                # CronoFilter panel
   ├── graph_editor/               # Graph Editor panels
   ├── proxy_box_creator/          # Proxy Box Creator panels
   ├── proxy_inflate_manager/      # Proxy Inflate Manager (experimental)
   │   ├── __init__.py             # Register hub + Scene.proxy_inflate_stats
   │   ├── helpers.py              # get_inflate_name + auto-inflate hooks
   │   ├── operators.py            # Add / Activate / Deactivate / Remove / InflateAll
   │   └── ui.py                   # VIEW3D_PT_ProxyInflatePanel (gated by experimental_features)
   ├── proxy_to_rm_projection/     # RM Coloring backend (experimental)
   │   ├── __init__.py
   │   ├── data.py                 # proxy_projection_settings PropertyGroup
   │   ├── operators.py            # proxy_projection.* operators
   │   ├── ui.py                   # Internal helpers (UI rendered inline in visual_manager/ui.py)
   │   ├── material_override.py    # Shader-node material overrides
   │   └── utils.py                # Projection / vertex paint helpers
   ├── tapestry_integration/       # Tapestry AI integration
   ├── server.py                   # TCP Server panel
   ├── import_operators/           # Import functionality
   ├── export_operators/           # Exporter pool (invoked by export_manager and elsewhere)
   │   ├── __init__.py             # Re-exports from heriverse + exporter_graphml
   │   ├── exporter_graphml.py     # GraphML save / save-as (invoked from EM tree header)
   │   └── heriverse/              # Heriverse exporter subpackage
   │       ├── __init__.py         # Register + re-exports
   │       ├── utils.py            # clean_filename + layer-collection helpers
   │       ├── gltf.py             # export_gltf_with_animation_support wrapper
   │       ├── json_export.py      # HERIVERSE_OT_export_json (export.heriversejson)
   │       ├── collections_op.py   # HERIVERSE_OT_make_collections_visible
   │       └── operator.py         # EXPORT_OT_heriverse (main export.heriverse operator)
   └── s3Dgraphy/                  # Core graph library (bundled)

Experimental Features
~~~~~~~~~~~~~~~~~~~~~

The following panels/sections are gated behind
``scene.em_tools.experimental_features`` and render with a red header plus the
``EXPERIMENTAL`` icon:

- ``em_statistics`` — Export statistics (Experimental)
- ``proxy_inflate_manager`` — Proxy Inflate Manager (Experimental)
- ``proxy_to_rm_projection`` — RM Coloring (Experimental), drawn inline inside
  the Visual Manager panel
- ``export_manager/providers/heriverse`` uses experimental flags for some
  advanced options but the provider itself is not gated

Further Reading
---------------

- :doc:`/installation` - Installation and setup
- :doc:`/usage_examples` - Practical examples
- :doc:`/panels/index` - UI and structure overview
- `GitHub Repository <https://github.com/zalmoxes-laran/EM-blender-tools>`_ - Source code
- `s3dgraphy on PyPI <https://pypi.org/project/s3dgraphy/>`_ - Graph library documentation
