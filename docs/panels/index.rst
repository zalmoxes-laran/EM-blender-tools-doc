EMtools Structure
=================

The addon is divided into several independent panels that can be moved
within the Blender sidebar (right side of the 3D Viewport). Panels are
grouped into three tab categories — **EM**, **EM Annotator**,
**EM Bridge** — following the authoring workflow from data setup to
export.

The list below mirrors the order in which the panels appear in Blender.

EM tab — core
-------------

.. toctree::
   :maxdepth: 1

   em_setup
   stratigraphy_manager
   epochs_manager
   activity_manager
   paradata_manager
   visual_manager
   cronofilter
   georeferencing

EM Annotator tab — spatial authoring
------------------------------------

.. toctree::
   :maxdepth: 1

   document_manager_3d
   rm_manager
   anastylosis_manager
   rmdoc_manager
   proxy_box_creator
   surface_areale
   conservation_workflow

EM Bridge tab — export & integrations
-------------------------------------

.. toctree::
   :maxdepth: 1

   export_manager
   heriverse_export

Reference
---------

.. toctree::
   :maxdepth: 1

   keyboard_shortcuts

Experimental
------------

Panels under active development. They appear in Blender only when
``Enable Experimental Features`` is on (and where applicable, when
Advanced EM mode is enabled). Always work on a backup before using them
on production data. Their titles end with ``(Experimental)`` so they are
easy to spot in the sidebar.

.. toctree::
   :maxdepth: 1

   graph_editor
   proxy_inflate_manager
   proxy_to_rm_projection
   server_panel
   stratiminer
   export_statistics
   tapestry_integration
