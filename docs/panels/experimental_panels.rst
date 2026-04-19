Experimental Panels
===================

Panels under active development. They are only visible in Blender when
the ``Enable Experimental Features`` flag is active in :ref:`EMsetup`
and, where applicable, when Advanced EM mode is enabled. Always work on
a backup before using them on production data.

Every panel title ends with the ``(Experimental)`` suffix so it is easy
to spot in the Blender sidebar.

**EM Tab**:

- :doc:`graph_editor` — Graph Editor (Experimental): node-based graph editing in the Node Editor
- :doc:`proxy_inflate_manager` — Proxy Inflate Manager (Experimental): solidify-based thickness, inside Visual Manager
- :doc:`proxy_to_rm_projection` — RM Coloring / Proxy to RM Projection (Experimental)
- :doc:`server_panel` — Server Panel (Experimental): TCP remote control (3D GIS mode only)

**EM Annotator Tab**:

- :doc:`surface_areale` — Surface Areale (Experimental): Representation Model to Proxy + Surface Areale

**EM Bridge Tab**:

- :doc:`stratiminer` — StratiMiner (Experimental): unified ``em_data.xlsx`` workflow (prompt copy, build and merge)
- :doc:`export_statistics` — Export Statistics (Experimental): per-object mesh statistics CSV
- :doc:`tapestry_integration` — Tapestry Integration (Experimental): AI-powered photorealistic reconstruction

.. toctree::
   :maxdepth: 1
   :hidden:

   graph_editor
   proxy_inflate_manager
   proxy_to_rm_projection
   server_panel
   surface_areale
   stratiminer
   export_statistics
   tapestry_integration
