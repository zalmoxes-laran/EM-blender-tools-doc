EMtools Structure
=================

The addon is divided into several independent panels that can be easily moved within the dedicated space on the sidebar of Blender (left side of the Viewport).

Panels are organized into three tab categories:

**EM Tab** (Core Functionality):

- :doc:`em_setup` - EM Data Tree: GraphML file management, mode switching, resource folders
- :doc:`visual_manager` - Display modes, label tools, color ramps
- :doc:`activity_manager` - Activity group filtering
- :doc:`epochs_manager` - Epoch management, filtering, custom lighting
- :doc:`stratigraphy_manager` - Stratigraphic unit exploration and filtering
- :doc:`cronofilter` - Chronological horizons (Landscape mode)
- :doc:`proxy_inflate_manager` - Proxy thickness management (Experimental)

**EM Annotator Tab**:

- :doc:`anastylosis_manager` - RMSF (Representation Model Special Find) management
- :doc:`rm_manager` - Representation Model management
- :doc:`document_manager_3d` - Spatial-temporal document management
- :doc:`proxy_box_creator` - Measurement-based proxy generation

**EM Bridge Tab**:

- :doc:`paradata_manager` - Paradata exploration and filtering
- :doc:`export_manager` - CSV and Heriverse export
- :doc:`export_statistics` - Volume and weight statistics export
- :doc:`server_panel` - TCP remote control
- :doc:`tapestry_integration` - AI-powered reconstruction (Experimental)

**Other**:

- :doc:`graph_editor` - Node-based graph visualization (Node Editor)
- :doc:`keyboard_shortcuts` - Keyboard shortcuts reference

.. toctree::
   :maxdepth: 2
   :caption: EM Tab

   em_setup
   visual_manager
   activity_manager
   epochs_manager
   stratigraphy_manager
   cronofilter
   proxy_inflate_manager

.. toctree::
   :maxdepth: 2
   :caption: EM Annotator Tab

   anastylosis_manager
   rm_manager
   document_manager_3d
   proxy_box_creator

.. toctree::
   :maxdepth: 2
   :caption: EM Bridge Tab

   paradata_manager
   export_manager
   export_statistics
   server_panel
   tapestry_integration

.. toctree::
   :maxdepth: 2
   :caption: Other

   graph_editor
   keyboard_shortcuts
