EMtools Structure
=================

The addon is divided into several independent panels that can be moved within
the Blender sidebar (right side of the 3D Viewport). Panels are grouped into
three tab categories, following the authoring workflow from data setup to
export.

Pages listed under each tab below are the **stable** ones: they are built
into the documentation and linked from the navigation menu. Pages for
experimental panels are built but hidden from navigation — see the note at
the end of this page.

Stable panels
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
- :doc:`surface_areale` — Surface Areale: RM-to-Proxy contour extraction

**EM Bridge Tab** (export / integrations):

- :doc:`export_manager` — CSV and Heriverse export

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
   rmdoc_manager
   rm_manager
   anastylosis_manager
   proxy_box_creator
   surface_areale

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

   export_statistics
   graph_editor
   proxy_inflate_manager
   proxy_to_rm_projection
   server_panel
   tapestry_integration
