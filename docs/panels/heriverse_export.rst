.. _heriverse_export:

Heriverse Export
================

The **Heriverse Export** provider lives in the *EM Bridge → Export
Manager* panel and produces a complete Heriverse project from the
current Blender scene. Heriverse is the 3D-web publishing platform of
the Extended Matrix ecosystem: it ingests a folder containing the
graph (JSON), the supporting documents (DosCo), the proxies, the
Representation Models (RM) and the Reality-Based (RB) geometries, and
serves them as an interactive online scene with paradata fully
browsable next to the 3D content.

This page documents the panel options, the produced project structure,
the threaded variant, the publishing workflow, and common
troubleshooting. For the tabular dump of the graph (em_data.xlsx,
CSV), see :doc:`export_manager`.

.. seealso::

   - `Heriverse docs <https://docs.extendedmatrix.org/projects/heriverse/en/1.5/>`__
     — full documentation of the Heriverse publishing platform.
   - `Publishing a reconstruction via Heriverse
     <https://docs.extendedmatrix.org/projects/heriverse/en/1.5/user_dashboard.html#publish-via-heriverse>`__
     — the upload step (creating a Heriverse scene and pushing the
     exported bundle online).
   - :doc:`export_manager` — for Tabular export (em_data.xlsx, CSV).

Overview
--------

A Heriverse export bundles, into a single output folder, every asset a
Heriverse scene needs:

- the **graph JSON** describing the Extended Matrix (US/USV nodes,
  epochs, relations, paradata);
- the **DosCo** folder with the source documents referenced by the
  graph;
- the **Proxies** — lightweight stand-ins for each stratigraphic unit,
  organised by epoch;
- the **Representation Models (RM)** — the high-quality reconstruction
  geometries — and their documentation variants (**RM Doc**) and
  Special Find variants (**RM SF**);
- optional **panorama** (``defsky.jpg``) and a **ZIP** archive of the
  whole bundle for distribution.

Only graphs explicitly marked as **Publishable** in the EM Setup panel
are included in the export. This is signalled in the UI by an info
line right below the project name fields.

Prerequisites
-------------

Before running an export, please verify that:

- every Representation Model and Reality-Based geometry is assigned to
  the correct **epoch(s)** through an Activity NodeGroup — see
  :doc:`em-doc:activity` in the EM language manual for the underlying
  concept;
- 3D objects live in the appropriate Blender **collection** (``RM`` for
  Representation Models, ``RB`` for Reality-Based, ``Proxy`` for
  stratigraphic proxies);
- at least one graph is marked as **Publishable** in the EM Setup
  panel;
- the destination folder is writable and the project name does not
  collide with an existing export (the exporter will overwrite by
  default).

Panel Options
-------------

The panel is split into a **basic** area, always visible, and an
**Advanced Options** area that toggles open via the ``TRIA`` arrow.

Basic
~~~~~

**Export Path** (``scene.heriverse_export_path``)
   Destination folder where the Heriverse project will be written.
   Defaults to empty — the user must set it before exporting.

**Project Name** (``scene.heriverse_project_name``)
   Name of the project folder created inside the export path.

**Export JSON** (``heriverse_overwrite_json``)
   Write/overwrite the graph JSON for every Publishable graph.

**Export DosCo** (``heriverse_export_dosco``)
   Copy the DosCo folder (source documents) into the project.

**Export Proxies** (``heriverse_export_proxies``)
   Export the Proxy collection — one proxy per stratigraphic unit.

**Export RM** (``heriverse_export_rm``)
   Export the Representation Models geometry.

**Export RM Doc** (``heriverse_export_rmdoc``)
   Export the RM Documentation variants (paradata-attached models).

**Export RM SF** (``heriverse_export_rmsf``)
   Export the RM Special Find variants.

**Create ZIP** (``heriverse_create_zip``)
   Pack the produced project folder into a ``.zip`` archive next to it,
   ready for upload.

**Add Panorama** (``scene.heriverse_export_panorama``, default ``True``)
   Copy the default panorama (``defsky.jpg``) into the project.

.. note::

   If **Export JSON** is enabled while **Export RM** is not, the panel
   shows a warning: ``Warning: JSON export without RM export!``. The
   produced JSON will still reference the RM nodes, but the link
   between RM nodes in the graph and the actual 3D models on disk will
   be missing. To fix it, enable **Export RM** as well, or disable the
   JSON re-export when re-running an export that only touches geometry.

Advanced
~~~~~~~~

The advanced area gathers GLB compression, texture handling, animation
export, paradata-specific options and Cesium tilesets.

**Use Draco Compression** (``heriverse_use_draco``)
   Apply Draco mesh compression to the exported glTF assets. When
   enabled, exposes:

   **Compression Level** (``heriverse_draco_level``)
      Draco compression level. Higher = smaller files but slower decode.

**Separate Textures** (``heriverse_separate_textures``)
   Export textures as separate files instead of embedding them into the
   glTF. When enabled, exposes a **Texture Compression** block on the
   scene:

   **Enable Compression** (``scene.heriverse_enable_compression``,
   default ``True``)
      Toggle JPEG re-encoding of textures.

   **Max Size** (``scene.heriverse_texture_max_res``,
   default ``4096``, range 512–8192)
      Maximum edge length of exported textures, in pixels.

   **Quality** (``scene.heriverse_texture_quality``,
   default ``80``, range 10–100)
      JPEG quality. ``100`` is lossless, ``80`` is the recommended
      default, ``60`` is compressed, ``40`` is heavily compressed.

**Use GPU Instancing** (``heriverse_use_gpu_instancing``)
   Pack repeated meshes as GPU-instanced nodes in the glTF.

**Export Animations** (``heriverse_export_animations``)
   Export Blender animations (armatures, bones, and keyframe data).
   When enabled, exposes:

   **All Animations** (``heriverse_export_all_animations``)
      Export every animation track on the selected armatures.

   **Frame Range Only** (``heriverse_animation_frame_range``)
      Restrict the exported animation to the scene frame range.

**ParaData Export Options** (visible when **Export RM Doc** is on)
   **Preserve Transforms for each RMDoc**
   (``scene.heriverse_preserve_rmdoc_transform``, default ``True``)
      Save and restore the original position, rotation and scale of
      each ParaData (RM Doc) object so it is exported in place rather
      than at the world origin.

   **Compress Textures**
   (``scene.heriverse_paradata_texture_compression``, default
   ``True``)
      Toggle JPEG re-encoding of ParaData textures. When enabled,
      exposes:

      **Max Size** (``scene.heriverse_rmdoc_texture_max_res``,
      default ``2048``, range 512–8192)
         Maximum edge length of ParaData textures, in pixels.

      **Quality** (``scene.heriverse_rmdoc_texture_quality``,
      default ``60``, range 10–100)
         JPEG quality for ParaData textures.

**Cesium Tileset Options**
   **Skip Extracted Tilesets** (``heriverse_skip_extracted_tilesets``)
      When the scene contains a Cesium tileset that has already been
      extracted, skip re-exporting it. Useful for large RB tilesets
      that don't change between runs.

Running the Export
------------------

When the options are set, press **Export Heriverse Project** at the
bottom of the section. The exporter runs the following steps:

1. Validates the scene (collections, publishable flag, export path).
2. For each Publishable graph, writes the corresponding JSON.
3. Copies the DosCo folder, if enabled.
4. Exports the Proxy, RM, RM Doc and RM SF objects as glTF/GLB into
   the appropriate sub-folders (applying Draco, texture separation and
   GPU instancing per the advanced options).
5. Optionally copies the default panorama.
6. Optionally zips the result.

The resulting folder layout, inside ``<Export Path>/<Project Name>/``,
mirrors the Heriverse scene contract: a top-level JSON per graph, the
``DosCo/`` folder, the ``proxies/``, ``RM/``, ``RMDoc/`` and ``RMSF/``
sub-folders, plus the optional panorama and ZIP archive.

Threaded export
~~~~~~~~~~~~~~~

A threaded variant of the exporter is also available
(``export.heriverse_threaded``, defined in ``export_threaded.py``). It
performs the same export pipeline in a background thread so the Blender
UI remains responsive on large scenes — useful when the project
contains many RM/RB objects, heavy textures, or when Draco compression
significantly slows down the synchronous path. Behaviour and panel
options are identical to the synchronous variant.

Publishing
----------

Once the export is complete, the project folder (or its ZIP) is ready
to be uploaded to a Heriverse instance. The upload step itself —
creating a Heriverse scene from your user dashboard and pushing the
exported bundle online — is documented on the Heriverse side:

`Publishing a reconstruction via Heriverse
<https://docs.extendedmatrix.org/projects/heriverse/en/1.5/user_dashboard.html#publish-via-heriverse>`__.

Troubleshooting
---------------

**Missing linked libraries**
   The exporter logs a warning when an RM or RB collection links a
   ``.blend`` library that cannot be resolved at export time. Fix the
   library path in *File → External Data → Find Missing Files* and
   re-run the export.

**DosCo paths broken**
   Source documents referenced by the graph but not present in the
   DosCo folder will be skipped, leaving dangling references in the
   exported JSON. Verify that the DosCo folder configured for the
   active graph matches the file system before exporting.

**RM/JSON link inconsistencies**
   If you re-exported the JSON but not the RM (or vice-versa), the
   Heriverse scene will display nodes without their geometry, or
   geometry that the graph cannot reach. Enable both **Export JSON**
   and **Export RM** when in doubt — the panel raises a yellow warning
   for this exact case.

**Animations not visible in Heriverse**
   Make sure the source object has its own armature and that **Export
   Animations** is enabled. If only a single take is needed, restrict
   it via **Frame Range Only**; if every action should be shipped,
   enable **All Animations**.

**Heavy ZIP, slow upload**
   Lower the texture **Max Size** / **Quality** values in the
   advanced section and/or enable **Use Draco Compression**. For
   ParaData (RM Doc), the dedicated ParaData texture knobs are
   typically more aggressive than the RM ones.
