.. badge:: Full Course
   :color: blue
.. badge:: Developer Track
   :color: orange

Creating Proxies and Exporting Your Dataset
===========================================

.. todo::

   **Embed YouTube video** — placeholder slug ``18_em_proxy_export``.
   Once the recording is uploaded, replace this todo with a
   ``.. raw:: html`` iframe pointing at the real YouTube video ID.
   Working title: *Creating Proxies and Exporting Your Dataset (~~4 min)*.

| **Clip:** 18  |  **Duration:** ~4 min  |  **Recording segment:** ~1:29:30 → 1:33:29

----

Prerequisites
-------------

:doc:`13-first-matrix-creation`

Overview
--------

The Proxy Box Creator places a proxy volume on a 3D object by recording two alignment points, measuring wall thickness and length, then generating the volume automatically. The Export Manager packages the full dataset — 3D models, graph nodes, image links, external URLs — as a portable ZIP.

.. figure:: /_static/screenshots/clip_18/0001_proxy_box_creator_panel.jpg
   :alt: The Proxy Box Creator panel in the Blender EM sidebar.
   :width: 90%

   The Proxy Box Creator panel in the Blender EM sidebar.

Key Concepts
------------

- Proxy Box Creator: place the 3D cursor, record two alignment points, generate volume.
- The tool measures quota minimum/maximum, length, and wall thickness automatically.
- Export Manager: select scene elements, set path, configure glTF compression options.
- The ZIP contains all models, metadata, image links, and external URL references.

Screenshots
-----------

.. figure:: /_static/screenshots/clip_18/0002_alignment_point_1.jpg
   :alt: Recording the first alignment point on the wall surface.
   :width: 90%

   Recording the first alignment point on the wall surface.

.. figure:: /_static/screenshots/clip_18/0004_proxy_volume_generated.jpg
   :alt: Proxy volume automatically generated from the two alignment points.
   :width: 90%

   Proxy volume automatically generated from the two alignment points.

.. figure:: /_static/screenshots/clip_18/0005_export_manager_panel.jpg
   :alt: Export Manager panel: element selection and output path settings.
   :width: 90%

   Export Manager panel: element selection and output path settings.

.. figure:: /_static/screenshots/clip_18/0007_export_zip_contents.jpg
   :alt: Export result: ZIP archive containing models, metadata, and links.
   :width: 90%

   Export result: ZIP archive containing models, metadata, and links.

Try It Yourself
---------------

Use the Proxy Box Creator on two walls in the playground dataset and export the scene as a ZIP archive.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`EM Data Architecture and Python Library <em-doc:learn-em/tutorials/11-data-architecture>`

