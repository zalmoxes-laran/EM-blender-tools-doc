.. badge:: Quick Start
   :color: green
.. badge:: Full Course
   :color: blue

Creating Your First Extended Matrix
===================================

.. todo::

   **Embed YouTube video** — placeholder slug ``13_em_first_matrix``.
   Once the recording is uploaded, replace this todo with a
   ``.. raw:: html`` iframe pointing at the real YouTube video ID.
   Working title: *Creating Your First Extended Matrix (~~4 min)*.

| **Clip:** 13  |  **Duration:** ~4 min  |  **Recording segment:** ~1:03:00 → 1:07:14

----

Prerequisites
-------------

:doc:`12-install-yed-blender`

Overview
--------

Create a minimal Extended Matrix from scratch: drag the canvas from the yEd palette, fill in metadata (human ID, author, ORCID, licence, embargo), add two SU nodes and connect them, save as GraphML, then import into Blender and verify the nodes appear in the Stratigraphic Manager.

.. figure:: /_static/screenshots/clip_13/0001_yed_drag_canvas_palette.jpg
   :alt: yEd: dragging the EM canvas node from the palette onto the workspace.
   :width: 90%

   yEd: dragging the EM canvas node from the palette onto the workspace.

Key Concepts
------------

- Always start with the canvas: drag it from the palette onto the yEd workspace.
- Fill metadata before adding nodes — it propagates to all children.
- Save as GraphML (.graphml) — this is the native EM file format.
- Import into Blender via the EM panel → add GraphML slot → browse to file.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_13/0002_yed_fill_metadata_name.jpg
   :alt: Filling in the canvas metadata: human ID, site name, author.
   :width: 90%

   Filling in the canvas metadata: human ID, site name, author.

.. figure:: /_static/screenshots/clip_13/0005_yed_save_graphml.jpg
   :alt: yEd: File → Save as GraphML.
   :width: 90%

   yEd: File → Save as GraphML.

.. figure:: /_static/screenshots/clip_13/0006_blender_em_panel_import.jpg
   :alt: Blender EM panel: adding a GraphML slot and browsing to the file.
   :width: 90%

   Blender EM panel: adding a GraphML slot and browsing to the file.

.. figure:: /_static/screenshots/clip_13/0007_strat_manager_nodes.jpg
   :alt: The Stratigraphic Manager in Blender showing the imported EM nodes.
   :width: 90%

   The Stratigraphic Manager in Blender showing the imported EM nodes.

Try It Yourself
---------------

Create an EM for a real or fictional site with at least four SU nodes and import it into Blender.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`Multi-Temporal 3D Visualization Demo <14-multitemporal-visualization>`

