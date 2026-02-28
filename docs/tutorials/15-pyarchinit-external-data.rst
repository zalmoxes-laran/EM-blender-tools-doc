.. badge:: Full Course
   :color: blue
.. badge:: Developer Track
   :color: orange

Auxiliary Resources: pyArchInit and External Data Connections
=============================================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 15_em_pyarchinit -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_15_em_pyarchinit"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ Auxiliary Resources: pyArchInit and External Data Connections (~~4 min)</em></p>

| **Clip:** 15  |  **Duration:** ~4 min  |  **Recording segment:** ~1:16:00 → ~1:20:30

----

Prerequisites
-------------

:doc:`13-first-matrix-creation`

Overview
--------

Auxiliary resources connect live external databases to the EM. The pyArchInit connection pulls excavator records, images, and site data directly from the field database into the EM graph. Document Resources link local photo folders as document nodes. Multiple GraphML files can coexist in a single Blender scene.

.. figure:: /_static/screenshots/clip_15/0001_data_tree_multiple_graphml.jpg
   :alt: Data tree panel showing multiple GraphML files in a single Blender scene.
   :width: 90%

   Data tree panel showing multiple GraphML files in a single Blender scene.

Key Concepts
------------

- Auxiliary resources are live connections — data updates when the external source changes.
- Multiple GraphML files can coexist (different site areas or survey campaigns).
- pyArchInit integration: excavator records, images, and measurements flow into EM automatically.
- Document Resources: link a local folder of photos as a document node batch.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_15/0003_auxiliary_resources_panel.jpg
   :alt: Auxiliary Resources panel in the Blender EM sidebar.
   :width: 90%

   Auxiliary Resources panel in the Blender EM sidebar.

.. figure:: /_static/screenshots/clip_15/0005_live_data_ingestion.jpg
   :alt: Live data ingestion from pyArchInit: excavator info and images flow into the EM.
   :width: 90%

   Live data ingestion from pyArchInit: excavator info and images flow into the EM.

.. figure:: /_static/screenshots/clip_15/0006_document_resources_photos.jpg
   :alt: Document Resources: linking a local photo folder as document nodes.
   :width: 90%

   Document Resources: linking a local photo folder as document nodes.

Try It Yourself
---------------

Add a Document Resource to the playground EM that points to a local folder of photos.

.. note::

   The video for this tutorial is available on the StratiGraph private YouTube channel.
   Clip filename: ``15_em_pyarchinit.mp4``

.. seealso::

   :doc:`Basilica Iulia: Excel Mapping Tool <16-mapping-tool-excel>`

