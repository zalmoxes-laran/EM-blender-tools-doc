EMtools Structure
=================

The addon is divided into several independent panels that can be moved within
the Blender sidebar (right side of the 3D Viewport). Panels are grouped into
three tab categories, following the authoring workflow from data setup to
export.

Each tab below lists **stable panels** first, then the **experimental
panels** that live in the same sidebar category. Experimental panels are
only visible in Blender when the ``Enable Experimental Features`` flag is
active (see :ref:`EMsetup`) and, where applicable, when Advanced EM mode
is enabled. Their documentation pages are built and deep-linked from the
addon UI but are not shown in the main navigation menu — they are
collected at the bottom of this page for reference.

EM Tab
------

Core functionality: graph loading, stratigraphic exploration, epoch and
activity management, paradata and visualisation.

**Stable panels**:

- :doc:`em_setup` — EM Data Tree: GraphML file management, auxiliary resources, mode switching
- :doc:`stratigraphy_manager` — Stratigraphic unit exploration, filters and containment
- :doc:`epochs_manager` — Epoch management, filtering, custom lighting
- :doc:`activity_manager` — Activity group filtering
- :doc:`paradata_manager` — Paradata exploration and filtering
- :doc:`visual_manager` — Display modes, label tools, color ramps
- :doc:`cronofilter` — Chronological horizons (Landscape mode)

**Experimental panels**:

- :doc:`graph_editor` — Node-editor based graph editing (Node Editor → EM category)
- :doc:`proxy_inflate_manager` — Proxy inflation controls (collapsible section inside Visual Manager)
- :doc:`proxy_to_rm_projection` — RM Coloring / Proxy to RM Projection (inline inside Visual Manager + child panel)
- :doc:`server_panel` — 3D GIS server panel (visible only in 3D GIS mode)

EM Annotator Tab
----------------

Spatial authoring: connecting the graph to Blender scene objects
(representation models, RMSF, proxy boxes, document overlays).

**Stable panels**:

- :doc:`document_manager_3d` — Document Manager: catalog of graph document nodes
- :doc:`rmdoc_manager` — RMDoc: scene objects linked to documents
- :doc:`rm_manager` — Representation Model management
- :doc:`anastylosis_manager` — RMSF (Representation Model Special Find) management
- :doc:`proxy_box_creator` — Measurement-based proxy generation

**Experimental panels**:

- :doc:`surface_areale` — Representation Model to Proxy + Surface Areale

EM Bridge Tab
-------------

Export and integrations with external pipelines.

**Stable panels**:

- :doc:`export_manager` — CSV and Heriverse export

**Experimental panels**:

- :doc:`stratiminer` — StratiMiner: unified ``em_data.xlsx`` workflow (prompt copy, build and merge)
- :doc:`export_statistics` — Per-object mesh statistics CSV export
- :doc:`tapestry_integration` — AI-powered photorealistic reconstruction via Tapestry server

Other
-----

- :doc:`keyboard_shortcuts` — Keyboard shortcuts reference


.. toctree::
   :maxdepth: 2
   :caption: EM Tab

   em_setup
   stratigraphy_manager
   epochs_manager
   activity_manager
   paradata_manager
   visual_manager
   cronofilter

.. toctree::
   :maxdepth: 2
   :caption: EM Annotator Tab

   document_manager_3d
   rmdoc_manager
   rm_manager
   anastylosis_manager
   proxy_box_creator

.. toctree::
   :maxdepth: 2
   :caption: EM Bridge Tab

   export_manager

.. toctree::
   :maxdepth: 2
   :caption: Other

   keyboard_shortcuts


.. Experimental / not-yet-stable panels.
   Pages are built (so deep links from the addon UI continue to work) but
   hidden from the user-visible navigation until each panel is promoted to
   stable in a future release.

.. toctree::
   :hidden:

   graph_editor
   proxy_inflate_manager
   proxy_to_rm_projection
   server_panel
   surface_areale
   stratiminer
   export_statistics
   tapestry_integration
