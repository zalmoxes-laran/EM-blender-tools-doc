.. _panel-georeferencing:

Georeferencing
==============

.. seealso::

   In the Extended Matrix language manual:

   - :doc:`em-doc:location` — how spatial anchoring (CRS, shift values)
     is described in the formal notation this panel materialises in
     Blender.

The **Georeferencing panel** (tab ``EM``, sidebar of the 3D Viewport) is
the single place where you anchor your EM scene to a real-world
coordinate reference system (CRS). It exposes four canonical values —
``EPSG``, ``Shift X``, ``Shift Y``, ``Shift Z`` — which are stored on
the Blender scene (``scene.em_georef``) and propagated, when present,
to the companion add-ons that consume them:

- `BlenderGIS <https://github.com/domlysz/BlenderGIS>`_ for vector and
  raster GIS data, basemaps, terrain.
- `3D Survey Collection (3DSC) <https://github.com/zalmoxes-laran/3D-survey-collection>`_
  for georeferenced DXF/point cloud import and Cesium 3D Tiles export.

When neither add-on is installed, the Georeferencing panel is still the
authoritative record of your scene's CRS — the values persist inside
the ``.blend`` file and travel with the project.

.. admonition:: When to use it
   :class: tip

   Open this panel **before** importing GIS layers, georeferenced DXF
   files, or aligning proxies to surveyed coordinates. Setting the
   CRS afterwards forces a manual reconciliation against geometry
   that is already in the scene.

Panel controls
--------------

Editable fields
~~~~~~~~~~~~~~~

- **EPSG** — the EPSG code of the projected CRS (e.g. ``32633`` for
  UTM 33N, ``3003`` for Monte Mario Italy 1, ``4326`` for WGS84
  geographic). Stored as a string; do not prefix with ``EPSG::``.
- **Shift X / Y / Z** — the Easting, Northing and Elevation offsets
  applied to the scene origin, in CRS units (typically meters). The
  typical archaeological convention is to subtract a "false origin"
  close to the site to keep Blender working with values below 10,000 m.

Sync status (semaforic indicators)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A small box reports the alignment between EM Tools and each companion
add-on:

- **green** — add-on installed and its state matches the EM Tools
  values (within a 1 mm tolerance).
- **yellow** — add-on installed but has no CRS / no origin set yet.
- **red** — add-on installed and its values diverge from EM Tools.
- **grey** — add-on not installed (or not detected). The panel still
  lists which integrations *would* become available when present.

Actions
~~~~~~~

- **Import shift.txt / Export shift.txt** — read or write the 3DSC
  ``shift.txt`` file (format ``EPSG::NNNN X Y Z``) so the same shift
  travels with a folder of meshes.
- **Propagate coordinates** — push the EM Tools values to every
  detected companion add-on.
- **Pull from BGIS / Pull from 3DSC** — re-read each add-on's state
  into EM Tools, useful after editing the BGIS GeoScene or 3DSC
  scene properties directly.
- **Push to GeoNode** — write the current values into the
  ``GeoPositionNode`` of the active graph, so the absolute position
  travels with the GraphML when exported.

Advanced
~~~~~~~~

A collapsible section exposes two opt-in toggles:

- **Move objects on origin change** — when editing the shift, also
  translate existing top-level objects. *Off by default*: most
  archaeological scenes already contain shifted geometry, and the
  origin edit is a metadata change, not a transform.
- **Compute lat/lon (needs PyProj)** — also derive scene lat/lon
  from the projected origin via BlenderGIS reprojection. Requires
  GDAL or PyProj inside Blender's Python; *off by default*.

.. _import-gis-blendergis:

BlenderGIS integration tutorial
-------------------------------

`BlenderGIS <https://github.com/domlysz/BlenderGIS>`_ is a third-party
Blender add-on that adds GIS data import, basemap visualization, and
geospatial operations directly inside Blender. It is the recommended
companion add-on for any EM workflow that involves **territorial
context** — landscapes, multi-site projects, or any reconstruction
that needs to sit on a real terrain.

This tutorial walks through how to bring BlenderGIS layers into a
georeferenced EM scene.

Step 1 — Install BlenderGIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the latest release from
`github.com/domlysz/BlenderGIS <https://github.com/domlysz/BlenderGIS>`_
and install as a regular Blender add-on (``Edit → Preferences →
Add-ons → Install…``). Enable it.

Once enabled, the EM Tools Georeferencing panel will detect it and
the BlenderGIS sync indicator will turn yellow (installed, no values
yet) or green (installed, values already coincide with EM Tools).

Step 2 — Configure the EM scene georeferencing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the **Georeferencing panel** of EM Tools, set the four canonical
values:

- **EPSG** of your project (e.g. ``32633`` for UTM 33N,
  ``3003`` for Italian Monte Mario zone).
- **Shift X / Y / Z** — typically the Easting / Northing / Elevation
  you subtract from absolute coordinates to keep your scene around
  the world origin.

These four values are the contract that BlenderGIS will honour when
projecting incoming layers into your scene. With the panel update
callback in place, simply editing them pushes the values into the
BlenderGIS GeoScene automatically (no manual sync needed). If the
sync dot stays red, click **Propagate coordinates** to force-push.

Step 3 — Import GIS layers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use BlenderGIS's native import flows:

- **Shapefile** (``.shp``) → ``GIS → Import → Vector``
- **GeoTIFF rasters** (terrain DEM, orthophoto) → ``GIS → Import →
  Georaster``
- **Web map services** (Bing, OSM, Mapbox, …) → ``GIS → Web geodata``
  (network required, plus an access key for some providers).

BlenderGIS reads the source CRS from each file (or asks you to
specify it for shapefiles without a ``.prj`` sidecar) and reprojects
on import into the scene's EPSG, applying the origin offset you set
in EM Tools.

Step 4 — Integrate with EM proxies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that your scene carries georeferenced layers, your EM proxies
(walls, structures, surfaces) are positioned in absolute coordinates.
Typical follow-up moves:

- Use orthophotos as visual references for re-modelling existing
  structures.
- Build proxies that align with surveyed terrain elevations sampled
  from a DEM.
- Cross-reference findings from multiple sites within the same
  territorial context, by overlapping their proxies on the same
  BlenderGIS basemap.

When you export the scene to Heriverse or to a GraphML for
documentation, the georeferencing travels with the project — the
``GeoPositionNode`` (push via the **Push to GeoNode** button) is the
canonical place in the graph where the CRS+shift live.

Notes
~~~~~

- BlenderGIS is maintained by an external community, not by the EM
  team. For tool-specific issues (failed imports, CRS conflicts,
  performance with large rasters), consult the BlenderGIS
  documentation or its issue tracker.
- The EM **Georeferencing panel** is the *source of truth* for the
  scene's CRS. If BlenderGIS suggests reprojecting to a different
  CRS, prefer to keep BlenderGIS aligned to the EM panel's EPSG
  rather than changing the EM-side reference (which would shift
  every existing proxy).
- For non-UTM CRS reprojection, BlenderGIS needs ``GDAL`` or
  ``PyProj`` installed inside Blender's Python. The
  **Compute lat/lon** toggle in the Advanced section relies on the
  same dependency.

Related recipes
---------------

- :doc:`/panels/em_setup` — connect the .graphml to the scene.
- The 3DSC CAD/DXF import recipe — see the 3D Survey Collection
  manual.
- The EM cookbook on the language manual — landscape-scale workflows
  and cross-tool integrations.
