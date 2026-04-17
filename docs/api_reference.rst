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

Graphs are managed by the external ``s3dgraphy`` library. EM Tools exposes the
top-level helpers directly, while ``load_graph_from_file`` lives under
``s3dgraphy.multigraph.multigraph``.

.. code-block:: python

   from s3dgraphy import get_graph, remove_graph, get_all_graph_ids
   from s3dgraphy.multigraph.multigraph import load_graph_from_file

   # Load a graph from a GraphML file (returns the graph identifier / name)
   graph_id = load_graph_from_file(filepath)

   # Fetch a graph already loaded in memory, by name
   graph = get_graph(graph_id)

   # List all loaded graph IDs
   for gid in get_all_graph_ids():
       g = get_graph(gid)

   # Drop a graph from memory
   remove_graph(graph_id)

EM Tools tracks the set of GraphML files the user has imported in
``scene.em_tools.graphml_files`` (see :ref:`api-prop-em-tools`). The name of
each file in that collection matches the graph ID used by ``get_graph``.

Import Operators
----------------

.. py:class:: EM_import_GraphML

   Import an Extended Matrix GraphML file.

   :bl_idname: ``import.em_graphml``
   :bl_label: Import EM GraphML
   :file: ``import_operators/importer_graphml.py``

.. py:class:: EM_OT_import_3dgis_database

   Import an external database (Generic Excel, PyArchInit, or EMdb Excel). The
   import type is read from ``scene.em_tools.mode_3dgis_import_type``
   (``generic_xlsx`` / ``pyarchinit`` / ``emdb_xlsx``).

   :bl_idname: ``em.import_3dgis_database``
   :bl_label: Import 3D GIS Database
   :file: ``import_operators/import_EMdb.py``

Importer Registry
^^^^^^^^^^^^^^^^^

EM Tools uses a registry so new importer back-ends can be plugged in without
touching the operator:

.. code-block:: python

   from import_operators.importer_registry import (
       IMPORTER_REGISTRY,
       create_importer,
       get_supported_formats,
       get_required_params,
   )

   # Supported importer types (keys of IMPORTER_REGISTRY):
   #   'generic_xlsx'  - Generic Excel spreadsheet (GenericXLSXImporter)
   #   'emdb_xlsx'     - EMdb Excel format (s3dgraphy.MappedXLSXImporter)
   #   'pyarchinit'    - PyArchInit SQLite database (s3dgraphy.PyArchInitImporter)

   # Build an importer. ``settings`` is a dict carrying at least the required
   # parameters for that type (see get_required_params(import_type)).
   settings = {
       'filepath': '/path/to/file.xlsx',
       'sheet_name': 'Sheet1',
       'id_column': 'ID',
       'desc_column': 'Description',  # optional
   }
   importer = create_importer('generic_xlsx', settings, existing_graph=None)

:file: ``import_operators/importer_registry.py``

Export Operators
----------------

.. py:class:: EXPORT_OT_heriverse

   Main Heriverse project export: GLTF geometry, DosCo documents, RM and SF
   models, and the Heriverse JSON descriptor. Options are read from
   ``scene.heriverse_*`` and ``context.window_manager.export_vars``.

   :bl_idname: ``export.heriverse``
   :bl_label: Export Heriverse Project
   :file: ``export_operators/heriverse/operator.py``

.. py:class:: EXPORT_OT_heriverse_threaded

   Threaded / background variant of the Heriverse export that drives the same
   GLTF pipeline via a background job queue. Uses
   ``export_operators.heriverse.gltf.export_gltf_with_animation_support``
   internally.

   :bl_idname: ``export.heriverse_threaded``
   :file: ``export_threaded.py``

.. py:class:: HERIVERSE_OT_export_json

   JSON-only export of publishable graphs (skips geometry / textures). The
   Python class was previously named ``JSON_OT_exportEMformat``; it was renamed
   during the Heriverse split so the class name no longer clashes with the
   removed EMviq operator. The Blender ``bl_idname`` is unchanged, so existing
   callers of ``bpy.ops.export.heriversejson(...)`` keep working.

   :bl_idname: ``export.heriversejson``
   :bl_label: Export Heriverse JSON
   :file: ``export_operators/heriverse/json_export.py``

.. py:class:: HERIVERSE_OT_make_collections_visible

   Convenience operator that unhides every collection containing at least one
   RM object (i.e. any object with ``EM_ep_belong_ob`` entries). Useful before
   launching an export so all publishable RMs are selectable.

   :bl_idname: ``heriverse.make_collections_visible``
   :file: ``export_operators/heriverse/collections_op.py``

.. py:class:: EM_export_GraphML

   Write the currently active graph back to its original ``.graphml`` file.
   Invoked from the EM Data Tree header, not from the Export panel.

   :bl_idname: ``export.graphml_update``
   :file: ``export_operators/exporter_graphml.py``

.. py:class:: EM_export_GraphML_SaveAs

   Save the active graph to a new ``.graphml`` file chosen by the user.

   :bl_idname: ``export.graphml_saveas``
   :file: ``export_operators/exporter_graphml.py``

.. py:class:: EMExportCSV

   Experimental CSV export of per-object mesh statistics (volume, weight,
   surface areas) driven by ``scene.em_properties``.

   :bl_idname: ``export_mesh.csv``
   :file: ``em_statistics/operators.py``

.. py:class:: OBJECT_OT_ExportUUSS / ExportuussData

   Tabular CSV export of Stratigraphic Units, Sources or Extractors. The
   first operator simply opens the second via ``INVOKE_DEFAULT``; the second
   does the actual file writing. Driven by
   ``context.window_manager.export_tables_vars.table_type``.

   :bl_idname: ``export.uuss_export`` / ``export.uuss_data``
   :file: ``export_manager/providers/tabular/operators.py``

Export Provider Registry
^^^^^^^^^^^^^^^^^^^^^^^^

The Export Manager panel is plugin-style: every collapsible section is an
``ExportProvider`` registered into a central list that the panel iterates.
Adding a new exporter UI section does not require modifying the panel.

.. code-block:: python

   from export_manager.registry import (
       ExportProvider,
       register_provider,
       unregister_provider,
       get_providers,
   )

   def _poll(context):
       return context.scene.em_tools.mode_em_advanced

   def _draw(box, context):
       box.row().operator("export.my_exporter", text="Run My Export")

   PROVIDER = ExportProvider(
       id="my_exporter",       # must match the `{id}_expanded` attr on ExportVars
                               # if you want a collapsible toggle (optional)
       label="My Exporter",
       order=30,
       icon='EXPORT',
       poll=_poll,
       draw=_draw,
   )

   def register():
       register_provider(PROVIDER)

   def unregister():
       unregister_provider(PROVIDER.id)

:file: ``export_manager/registry.py``

Currently shipped providers live under ``export_manager/providers/``:

- ``tabular`` — CSV exports of US/USV, Sources, Extractors
- ``heriverse`` — UI for ``export.heriverse`` (Advanced mode only)

Property Groups
---------------

EMAddonSettings
^^^^^^^^^^^^^^^

Global addon settings, stored in the addon preferences
(``bpy.context.preferences.addons[__package__].preferences``).

:file: ``__init__.py``

Properties:

- ``preserve_web_url`` (BoolProperty, default ``True``): Preserve URLs from GraphML nodes
- ``overwrite_url_with_dosco_filepath`` (BoolProperty, default ``True``): Use DosCo folder paths instead of web URLs
- ``dosco_options`` (BoolProperty, default ``False``): Show DosCo options in the UI
- ``dosco_advanced_options`` (BoolProperty, default ``False``): Show advanced DosCo import options
- ``verbose_logging`` (BoolProperty, computed): Enable detailed console logging. Backed by addon preferences via a getter/setter pair

ExportVars
^^^^^^^^^^

Export UI settings. Attached to ``bpy.types.WindowManager`` as
``window_manager.export_vars``.

:file: ``__init__.py``

Expand toggles (used by the Export panel provider loop):

- ``tabular_expanded`` (BoolProperty, default ``True``)
- ``heriverse_expanded`` (BoolProperty, default ``False``)
- ``emviq_expanded`` (BoolProperty, default ``False``) — legacy flag, EMviq exporter was removed
- ``heriverse_advanced_options`` (BoolProperty)

Heriverse pipeline flags (consumed by ``EXPORT_OT_heriverse``):

- ``heriverse_overwrite_json`` / ``heriverse_export_dosco``
- ``heriverse_export_proxies`` / ``heriverse_export_rm``
  / ``heriverse_export_rmdoc`` / ``heriverse_export_rmsf``
- ``heriverse_create_zip``
- ``heriverse_use_draco`` / ``heriverse_draco_level`` (1–10)
- ``heriverse_separate_textures`` / ``heriverse_use_gpu_instancing``
- ``heriverse_skip_extracted_tilesets``
- ``heriverse_export_animations`` / ``heriverse_export_all_animations``
  / ``heriverse_animation_frame_range``

Generic format selector (legacy EMviq-era):

- ``format_file`` (EnumProperty: ``gltf`` / ``obj`` / ``fbx``, default ``gltf``)

Texture / path settings live on the Scene, not on ``ExportVars`` (see below).

ExportTablesVars
^^^^^^^^^^^^^^^^

Settings for the Tabular CSV export provider.

:file: ``__init__.py``

Properties:

- ``table_type`` (EnumProperty: ``US/USV`` / ``Sources`` / ``Extractors``)

Scene-level Heriverse settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Registered by the Heriverse provider when the provider loads. Attached to
``bpy.types.Scene``:

- ``heriverse_export_path`` (StringProperty, DIR_PATH)
- ``heriverse_project_name`` (StringProperty)
- ``heriverse_export_panorama`` (BoolProperty)
- ``heriverse_enable_compression`` (BoolProperty)
- ``heriverse_texture_max_res`` (IntProperty, 512–8192)
- ``heriverse_texture_quality`` (IntProperty, 10–100)
- ``heriverse_paradata_texture_compression`` (BoolProperty)
- ``heriverse_paradata_texture_quality`` (IntProperty, 10–100)
- ``heriverse_rmdoc_texture_max_res`` (IntProperty, 512–8192)
- ``heriverse_rmdoc_texture_quality`` (IntProperty, 10–100)
- ``heriverse_preserve_rmdoc_transform`` (BoolProperty)

:file: ``export_manager/providers/heriverse/properties.py``

.. _api-prop-em-tools:

EM_Tools
^^^^^^^^

Main container for all EM Tools scene-level state. Attached to
``bpy.types.Scene`` as ``scene.em_tools``. Every manager exposes its state
through a ``PointerProperty`` on this container.

:file: ``em_props.py``

Manager pointers:

- ``stratigraphy`` (``StratigraphyManagerProps``)
- ``epochs`` (``EpochManagerProps``)
- ``visual`` (``VisualManagerProps``)
- ``anastylosis`` (``AnastylosisManagerProps``)
- ``rm`` (``RMManagerProps``)
- ``proxy_box`` (``ProxyBoxSettings``)
- ``tapestry`` (``TapestryManagerProps``)
- ``surface_areale`` (``SurfaceArealeSettings``)

GraphML file management:

- ``graphml_files`` (CollectionProperty of ``GraphMLFileItem``) — all loaded graphs
- ``active_file_index`` (IntProperty, default ``-1``)

Global settings and mode flags:

- ``mode_em_advanced`` (BoolProperty, default ``True``) — switch between 3D GIS and EM Advanced UIs
- ``experimental_features`` (BoolProperty, default ``False``) — gates the experimental panels (see below)
- ``show_advanced_tools`` (BoolProperty)
- ``show_collection_manager`` (BoolProperty)
- ``exp_create_graphml_expanded`` (BoolProperty)
- ``mode_3dgis_import_type`` (EnumProperty: ``generic_xlsx`` / ``pyarchinit`` / ``emdb_xlsx``)

Anastylosis LOD helpers
^^^^^^^^^^^^^^^^^^^^^^^

Public helpers exported by ``anastylosis_manager`` (useful for scripts that
need to introspect LOD variants without going through operators):

.. code-block:: python

   from anastylosis_manager import detect_lod_variants
   from anastylosis_manager.lod_utils import (
       LOD_MIN_LEVEL, LOD_MAX_LEVEL,
       _resolve_lod_with_fallback,
       _switch_linked_mesh_lod,
   )

   variants = detect_lod_variants("MyProxy")   # [(lod_level, obj_name), ...]

:file: ``anastylosis_manager/lod_utils.py``

Proxy inflate hooks
^^^^^^^^^^^^^^^^^^^

``proxy_inflate_manager`` also exposes pre/post export hooks so callers can
temporarily solidify proxies around an export:

.. code-block:: python

   from proxy_inflate_manager import (
       auto_inflate_for_export,
       cleanup_auto_inflate,
       export_pre_hook,
       export_post_hook,
   )

:file: ``proxy_inflate_manager/helpers.py``

Panels Reference
----------------

Principal Blender panels registered by EM Tools. All sit in
``VIEW_3D > UI`` unless stated otherwise.

+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| Class                           | bl_label                    | bl_category           | File                                |
+=================================+=============================+=======================+=====================================+
| ``EM_SetupPanel``               | EM Data Tree {version}      | EM                    | ``em_setup/ui.py``                  |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_visual_panel``      | Visual Manager              | EM                    | ``visual_manager/ui.py``            |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_ToolsPanel``        | Stratigraphy Manager        | EM                    | ``stratigraphy_manager/ui.py``      |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_BasePanel``         | Epochs Manager              | EM                    | ``epoch_manager/ui.py``             |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_activity_manager``  | Activity Manager            | EM                    | ``activity_manager/ui.py``          |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_RM_Manager``        | Representation Model (RM)   | EM Annotator          | ``rm_manager/ui.py``                |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_Anastylosis_Manager``| Anastylosis (RMSF)         | EM Annotator          | ``anastylosis_manager/ui.py``       |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_ParadataPanel``     | Paradata Manager            | EM                    | ``paradata_manager/ui.py``          |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_3DDocumentManager`` | Document Manager            | EM Annotator          | ``document_manager/ui.py``          |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_RMDoc_Manager``     | Representation Model Document (RMDoc) | EM Annotator | ``document_manager/ui.py``          |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_ExportPanel``       | Export Manager              | EM Bridge             | ``export_manager/panel.py``         |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_graphedit_sync``    | EMGraph (Experimental)      | EM                    | ``graph_editor/ui.py``              |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``CF_PT_cronofilter``           | CronoFilter                 | EM                    | ``cronofilter/ui.py``               |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+
| ``VIEW3D_PT_ServerPanel``       | EM Server                   | EM                    | ``server.py``                       |
+---------------------------------+-----------------------------+-----------------------+-------------------------------------+

Experimental panels (gated behind ``scene.em_tools.experimental_features``):

+---------------------------------+--------------------------------------+-----------------------+-------------------------------------------+
| Class                           | bl_label                             | Location              | File                                      |
+=================================+======================================+=======================+===========================================+
| ``EM_PT_ExportPanel``           | Export statistics (Experimental)     | EM Bridge             | ``em_statistics/ui.py``                   |
+---------------------------------+--------------------------------------+-----------------------+-------------------------------------------+
| ``VIEW3D_PT_ProxyInflatePanel`` | Proxy Inflate Manager                | Child of Visual Mgr   | ``proxy_inflate_manager/ui.py``           |
+---------------------------------+--------------------------------------+-----------------------+-------------------------------------------+
| ``VIEW3D_PT_proxy_projection_panel`` | Proxy to RM Projection (Experimental) | EM             | ``proxy_to_rm_projection/ui.py``          |
+---------------------------------+--------------------------------------+-----------------------+-------------------------------------------+
| ``VIEW3D_PT_graphml_wizard_bridge`` | GraphML Wizard (Experimental)   | EM                    | ``em_setup/ui.py``                        |
+---------------------------------+--------------------------------------+-----------------------+-------------------------------------------+

.. note::
   "RM Coloring (Experimental)" is **not** a separate panel: it is drawn inline
   inside Visual Manager by ``visual_manager.ui.VisualManager.draw_rm_coloring``.
   Its backend operators (``proxy_projection.apply``, ``proxy_projection.clear``,
   ``proxy_projection.update``, ``proxy_projection.toggle``, …) live in
   ``proxy_to_rm_projection/operators.py``.

.. note::
   The "Proxy Inflate Manager (Experimental)" collapsible box visible inside
   Visual Manager is also an *inline* rendering, produced by
   ``visual_manager.ui.VisualManager.draw_proxy_inflate_tools``. It exposes the
   same operators as ``VIEW3D_PT_ProxyInflatePanel`` (the standalone
   sub-panel); the inline version adds the red header and the
   ``(Experimental)`` suffix, the standalone sub-panel uses the plain label.

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
   │   ├── __init__.py             # Register hub
   │   ├── data.py                 # RMListItem + RM PropertyGroups
   │   ├── handlers.py             # load_post + depsgraph handlers
   │   ├── operators.py            # RM list CRUD + epoch selection + LOD
   │   └── ui.py                   # VIEW3D_PT_RM_Manager + UIList + menus
   ├── paradata_manager/           # Paradata Manager panel
   │   ├── __init__.py             # Register hub
   │   ├── data.py                 # ParadataImageProps + paradata list items
   │   ├── operators.py            # Document/Extractor/Combiner operators
   │   └── ui.py                   # Panels (documents / extractors / combiners)
   ├── document_manager/           # 3D Document Manager panel
   │   ├── __init__.py             # Register hub
   │   ├── data.py                 # 3D document PropertyGroups
   │   ├── handlers.py             # Scene-update handlers
   │   ├── operators.py            # Document CRUD + link-to-epoch operators
   │   ├── ui.py                   # Panel + UIList
   │   └── validators.py           # Document data validation helpers
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
   ├── cronofilter/                # CronoFilter panel (custom chronological horizons)
   │   ├── __init__.py             # Register hub
   │   ├── properties.py           # CF_ChronologicalHorizon + CF_CronoFilterSettings + Scene.cf_settings
   │   ├── operators.py            # Add / Remove / Move / Save / Load / AutoHorizons
   │   ├── ui.py                   # CF_UL_HorizonList + CF_PT_CronoFilterPanel
   │   ├── integration.py          # Runtime integration helpers (preview / validation)
   │   └── json_exporter_patch.py  # Patch wiring custom horizons into the JSON exporter
   ├── graph_editor/               # Graph Editor panels (node-based graph visualization)
   │   ├── __init__.py             # Register hub
   │   ├── properties.py           # GraphEditor PropertyGroups
   │   ├── data.py                 # Internal data structures
   │   ├── nodes.py                # Node type definitions
   │   ├── dynamic_nodes.py        # Dynamically generated node classes
   │   ├── socket_generator.py     # Socket factory helpers
   │   ├── layout.py               # Graph layout algorithms
   │   ├── operators.py            # Graph manipulation operators
   │   ├── keymap.py               # Custom keymap bindings
   │   ├── ui.py                   # Editor panel + overlays
   │   └── utils.py                # Shared utilities
   ├── proxy_box_creator/          # Proxy Box Creator panels
   │   ├── __init__.py             # Register hub
   │   ├── data.py                 # ProxyBoxSettings + ProxyBoxPointSettings
   │   ├── create_enhanced.py      # Enhanced proxy-box generation logic
   │   ├── document_picker.py      # Document selection helpers
   │   ├── operators.py            # Creation / editing operators
   │   ├── ui.py                   # Panel UI
   │   └── utils.py                # Geometry helpers
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
   │   ├── __init__.py             # Register hub
   │   ├── properties.py           # Tapestry settings PropertyGroups
   │   ├── operators.py            # Export / submit operators
   │   ├── ui.py                   # Tapestry panel (renamed from ui_panel.py)
   │   ├── graph_bridge.py         # Bridge between EM graph and Tapestry payload
   │   ├── network_client.py       # HTTP client for Tapestry service
   │   ├── render_utils.py         # Render helpers
   │   └── semantic_extractor.py   # Semantic data extraction from the graph
   ├── server.py                   # TCP Server panel (single-file, ~160 lines)
   ├── import_operators/           # Import functionality
   │   ├── __init__.py             # Re-exports
   │   ├── importer_registry.py    # Importer plug-in registry
   │   ├── importer_graphml.py     # GraphML importer
   │   ├── importer_xlsx.py        # XLSX importer
   │   ├── import_EMdb.py          # EMdb importer
   │   └── import_validator.py     # Input validation helpers
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
^^^^^^^^^^^^^^^^^^^^^

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
