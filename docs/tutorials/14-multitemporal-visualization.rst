.. badge:: Full Course
   :color: blue

Multi-Temporal 3D Visualization Demo
====================================

.. todo::

   **Embed YouTube video** — placeholder slug ``14_em_multitemporal``.
   Once the recording is uploaded, replace this todo with a
   ``.. raw:: html`` iframe pointing at the real YouTube video ID.
   Working title: *Multi-Temporal 3D Visualization Demo (~~9 min)*.

| **Clip:** 14  |  **Duration:** ~9 min  |  **Recording segment:** 1:07:14 → ~1:16:00

----

Prerequisites
-------------

:doc:`13-first-matrix-creation`

Overview
--------

Live demo with the Great Temple dataset: switching between epochs, assigning different 3D models to different time periods, identifying modern restorations vs. original fabric, using the Visual Manager to control proxy display, and syncing colour changes between yEd and Blender.

.. figure:: /_static/screenshots/clip_14/0001_great_temple_initial.jpg
   :alt: Great Temple dataset loaded in Blender: initial state.
   :width: 90%

   Great Temple dataset loaded in Blender: initial state.

Key Concepts
------------

- Assign a 3D model to an epoch via the Representation Model Manager.
- The same 3D object can show a different model in each epoch.
- Modern restorations vs. original fabric: separate them as different SUs in different epochs.
- Colour changes in yEd propagate to Blender after pressing Shift+F5.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_14/0002_gif_epoch_switch.gif
   :alt: Switching between epochs: 20th century → 2nd century → post-antiquity.
   :width: 90%

   Switching between epochs: 20th century → 2nd century → post-antiquity.

.. figure:: /_static/screenshots/clip_14/0003_repmodel_manager.jpg
   :alt: Representation Model Manager: assigning a photogrammetric model to an epoch.
   :width: 90%

   Representation Model Manager: assigning a photogrammetric model to an epoch.

.. figure:: /_static/screenshots/clip_14/0007_visual_manager_proxy.jpg
   :alt: Visual Manager: controlling proxy visibility and alpha levels.
   :width: 90%

   Visual Manager: controlling proxy visibility and alpha levels.

Try It Yourself
---------------

In the Great Temple dataset, assign a different epoch colour to the Ottoman-period elements and verify the change in Blender.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`EM Language: Canvas, Metadata and Epochs <em-doc:learn-em/tutorials/07-canvas-metadata-epochs>`

