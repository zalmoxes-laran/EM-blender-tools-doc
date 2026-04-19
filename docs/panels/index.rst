EMtools Structure
=================

The addon is divided into several independent panels that can be moved within
the Blender sidebar (right side of the 3D Viewport). Panels are grouped into
three tab categories — **EM**, **EM Annotator**, **EM Bridge** — following
the authoring workflow from data setup to export.

For navigation, the documentation sorts the same panels into two
groups: **Stable Panels** (production-ready) and **Experimental Panels**
(only visible in Blender when the ``Enable Experimental Features`` flag
is active in :ref:`EMsetup` — all experimental titles end with
``(Experimental)``).

Stable Panels
-------------

**EM Tab** (core functionality):

- :doc:`em_setup` — EM Data Tree: GraphML file management, auxiliary resources, mode switching
- :doc:`stratigraphy_manager` — Stratigraphic unit exploration, filters and containment
- :doc:`epochs_manager` — Epoch management, filtering, custom lighting
- :doc:`activity_manager` — Activity group filtering
- :doc:`paradata_manager` — Paradata exploration and filtering
- :doc:`visual_manager` — Display modes, label tools, color ramps
- :doc:`cronofilter` — Chronological horizons (Landscape mode)

**EM Annotator Tab** (spatial authoring):

- :doc:`document_manager_3d` — Document Manager: catalog of graph document nodes
- :doc:`rmdoc_manager` — RMDoc: scene objects linked to documents
- :doc:`rm_manager` — Representation Model management
- :doc:`anastylosis_manager` — RMSF (Representation Model Special Find) management
- :doc:`proxy_box_creator` — Measurement-based proxy generation

**EM Bridge Tab** (export / integrations):

- :doc:`export_manager` — CSV and Heriverse export

**Other**:

- :doc:`keyboard_shortcuts` — Keyboard shortcuts reference

Experimental Panels
-------------------

Only visible when ``Enable Experimental Features`` is active in
:ref:`EMsetup`. Use on backups only.

**EM Tab**:

- :doc:`graph_editor` — Graph Editor (Experimental): node-based graph editing in the Node Editor
- :doc:`proxy_inflate_manager` — Proxy Inflate Manager (Experimental): solidify-based thickness inside Visual Manager
- :doc:`proxy_to_rm_projection` — RM Coloring / Proxy to RM Projection (Experimental)
- :doc:`server_panel` — Server Panel (Experimental): TCP remote control (3D GIS mode only)

**EM Annotator Tab**:

- :doc:`surface_areale` — Surface Areale (Experimental): Representation Model to Proxy + Surface Areale

**EM Bridge Tab**:

- :doc:`stratiminer` — StratiMiner (Experimental): unified ``em_data.xlsx`` workflow (prompt copy, build and merge)
- :doc:`export_statistics` — Export Statistics (Experimental): per-object mesh statistics CSV
- :doc:`tapestry_integration` — Tapestry Integration (Experimental): AI-powered photorealistic reconstruction


.. toctree::
   :maxdepth: 2
   :caption: Stable Panels

   em_setup
   stratigraphy_manager
   epochs_manager
   activity_manager
   paradata_manager
   visual_manager
   cronofilter
   document_manager_3d
   rmdoc_manager
   rm_manager
   anastylosis_manager
   proxy_box_creator
   export_manager
   keyboard_shortcuts

.. toctree::
   :maxdepth: 2
   :caption: Experimental Panels

   graph_editor
   proxy_inflate_manager
   proxy_to_rm_projection
   server_panel
   surface_areale
   stratiminer
   export_statistics
   tapestry_integration
