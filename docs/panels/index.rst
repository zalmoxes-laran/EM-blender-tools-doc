EMtools Structure
=================

The addon is divided into several independent panels that can be easily moved within the dedicated space on the sidebar of Blender (left side of the Viewport).

Panels are organized into three tab categories, following the authoring workflow from data setup to export:

**EM Tab** (Core Functionality):

- :doc:`em_setup` — EM Data Tree: GraphML file management, auxiliary resources, mode switching
- :doc:`stratigraphy_manager` — Stratigraphic unit exploration, filters and containment
- :doc:`epochs_manager` — Epoch management, filtering, custom lighting
- :doc:`activity_manager` — Activity group filtering
- :doc:`paradata_manager` — Paradata exploration and filtering
- :doc:`visual_manager` — Display modes, label tools, color ramps
- :doc:`cronofilter` — Chronological horizons (Landscape mode)

**EM Annotator Tab**:

- :doc:`document_manager_3d` — Document manager and RMDoc (spatialized documents)
- :doc:`rm_manager` — Representation Model management
- :doc:`anastylosis_manager` — RMSF (Representation Model Special Find) management
- :doc:`proxy_box_creator` — Measurement-based proxy generation

**EM Bridge Tab**:

- :doc:`export_manager` — CSV and Heriverse export
- :doc:`export_statistics` — Volume and weight statistics export

**Other**:

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
   rm_manager
   anastylosis_manager
   proxy_box_creator

.. toctree::
   :maxdepth: 2
   :caption: EM Bridge Tab

   export_manager
   export_statistics

.. toctree::
   :maxdepth: 2
   :caption: Other

   keyboard_shortcuts


.. Experimental / not-yet-stable panels — kept as build targets for deep links
   from the addon UI, but hidden from the user-visible navigation until they
   are promoted to stable in a future release.

.. toctree::
   :hidden:

   graph_editor
   proxy_inflate_manager
   server_panel
   tapestry_integration
