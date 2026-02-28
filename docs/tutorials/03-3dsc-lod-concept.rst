.. badge:: Full Course
   :color: blue

3D Survey Collection: Level of Detail in Blender
================================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 03_3dsc_lod_concept -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_03_3dsc_lod_concept"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ 3D Survey Collection: Level of Detail in Blender (~~6 min)</em></p>

| **Clip:** 03  |  **Duration:** ~6 min  |  **Recording segment:** 11:43 → ~18:00

----

Prerequisites
-------------

Blender 3.x or later installed.

Overview
--------

The 3D Survey Collection (3DSC) add-on solves the problem of working with very large photogrammetric models in Blender. The LOD (Level of Detail) generator creates four resolution versions of any mesh, allowing real-time switching between detail levels while working on site-scale datasets.

.. figure:: /_static/screenshots/clip_03/0001_3dsc_panel_location.jpg
   :alt: The 3D Survey Collection panel in the Blender N-panel sidebar.
   :width: 90%

   The 3D Survey Collection panel in the Blender N-panel sidebar.

Key Concepts
------------

- Large photogrammetric models (10M+ polygons) are impractical on standard hardware.
- The LOD generator creates four resolution levels from a single source mesh.
- LOD levels can be switched at runtime — no scene reload required.
- The 3DSC panel lives in the Blender sidebar (press N to open).

Screenshots
-----------

.. figure:: /_static/screenshots/clip_03/0003_single_element_lod3_10k.jpg
   :alt: Single architectural element at LOD Level 3: 10,000 polygons.
   :width: 90%

   Single architectural element at LOD Level 3: 10,000 polygons.

.. figure:: /_static/screenshots/clip_03/0004_original_resolution_10M.jpg
   :alt: Same element at original resolution: 10 million polygons.
   :width: 90%

   Same element at original resolution: 10 million polygons.

.. figure:: /_static/screenshots/clip_03/0005_lod_generator_interface.jpg
   :alt: The LOD generator interface with resolution parameters.
   :width: 90%

   The LOD generator interface with resolution parameters.

.. figure:: /_static/screenshots/clip_03/0006_gif_lod_switch.gif
   :alt: Switching between LOD levels in real time in the Blender viewport.
   :width: 90%

   Switching between LOD levels in real time in the Blender viewport.

Try It Yourself
---------------

Apply the LOD generator to the sample mesh in the playground dataset and verify all four LOD levels load correctly.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`Site-Scale LOD and Data Preparation <04-3dsc-site-scale>`

