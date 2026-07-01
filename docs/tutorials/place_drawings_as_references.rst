.. _place-drawings-as-refs:

Placing 2D Drawings as 3D References
====================================

.. include:: ../_includes/golden_twelve_card.rst

A common authoring step is to import a 2D drawing — a section, a
plan, an excavation orthophoto — into Blender and bring it to the
correct **position**, **orientation** and **scale** so that proxies,
RMs and stratigraphic units can be built or aligned against it. The
same procedure applies to graphic documents handled through the
:ref:`rmdoc_manager` panel: in both cases the drawing has to live in
the same coordinate system as the rest of the reconstruction.

This mini-tutorial walks through the workflow using the **metric
scale bar visible on the drawing itself** as the reference for
scaling. The technique is independent of any addon and only uses
core Blender features (Images as Planes import, the 3D Cursor, and
parent/unparent with *Keep Transformation*).

Learning objectives
-------------------

By the end you will be able to:

- import a raster drawing as a plane in the 3D viewport;
- rotate it so a section stands vertically or a plan lies flat;
- rescale it metrically using a scale bar drawn on the image;
- align the drawing to known reference points in the scene.

Prerequisites
-------------

- Blender 4.x with the **Import Images as Planes** addon enabled
  (``Edit > Preferences > Add-ons > Import-Export: Images as Planes``).
- A raster drawing (PNG / JPG / TIFF) that contains a **visible
  metric scale bar** of known length.
- A target scene where the drawing has to live. For the
  ``RMDoc`` use case, see :ref:`rmdoc_manager`.

.. _place-drawings-import:

Step 1 — Import the drawing as a plane
--------------------------------------

Use ``File > Import > Images as Planes`` and pick the drawing
file. Leave the default material settings; the plane is created at
the world origin, on the XY plane, with the texture mapped to its
UV.

.. TODO: screenshot — File > Import > Images as Planes dialog with the drawing selected; show the right-hand options panel (Import method, Shadeless, Alpha) at default.

.. image:: /_static/tutorials/place_drawings/01_import_dialog.png
   :width: 90%
   :align: center
   :alt: Images as Planes import dialog with the drawing about to be imported.

.. note::

   An equivalent alternative is ``Add > Image > Reference``
   (creates an *Image Empty*). The procedure below works the same
   way: substitute "the image plane" with "the image empty" — both
   are transformable Blender objects and both honour the parent
   workflow described later.

.. _place-drawings-orientation:

Step 2 — Rough orientation
--------------------------

The drawing is loaded flat on the world XY plane. Rotate and
translate it so it sits in the role it documents:

- **section drawings** must be brought to a vertical plane —
  typically a 90° rotation around X (or Y, depending on the
  section's intended facing) so the drawing reads upright in the
  XZ or YZ plane;
- **plan / orthophoto drawings** stay horizontal on XY; only
  rotation around Z is needed to align the drawing's north with
  the scene's north.

Translate the plane to the approximate location it documents. Do
not worry about precision yet — scale comes next.

.. TODO: screenshot — viewport with the imported plane after rough rotation/translation; include the N gizmo for orientation context and the object name in the outliner.

.. image:: /_static/tutorials/place_drawings/02_rough_orientation.png
   :width: 90%
   :align: center
   :alt: Imported image after rough rotation/translation.

.. _place-drawings-scaling:

Step 3 — Scale using a metric reference on the drawing
------------------------------------------------------

The drawing carries a scale bar. We use it as the only metric
reference. The trick is to create a temporary helper mesh of known
size, parent the drawing to it, and then resize the helper.

**3.1 — Snap the 3D Cursor to the start of the scale bar**

Click in the viewport, or use ``Shift+S > Cursor to Selected`` after
picking a vertex/empty already placed at the start of the bar, so
that the 3D Cursor sits exactly at the bar's origin (the ``0`` tick).

.. TODO: screenshot — close-up of the drawing's scale bar with the 3D Cursor aligned to the bar's zero tick.

.. image:: /_static/tutorials/place_drawings/03_cursor_and_helper.png
   :width: 90%
   :align: center
   :alt: 3D Cursor placed at the start of the scale bar; a 1x1 m helper plane has been added there.

**3.2 — Add a 1 × 1 m helper mesh at the cursor**

``Add > Mesh > Plane`` (or ``Add > Mesh > Cube``) creates a default
1 m object. Make sure the option ``Add > Origin: 3D Cursor`` is
active, or use ``Shift+S > Selection to Cursor`` right after the
add. The helper has to lie in the same plane as the drawing
(rotate it to match if needed).

At this point the helper is **1 m long** by construction, regardless
of how big the drawing currently looks in the viewport.

**3.3 — Read the scale**

Compare the helper's length with the scale bar on the drawing.
Example: the helper visually spans only 20 cm of the drawing, but
the scale bar declares 10 m. The drawing is therefore 50× too
small; rather than computing the factor manually, let Blender do
the arithmetic in the next step.

**3.4 — Parent the drawing to the helper**

Select the drawing **first**, then ``Shift``-select the helper (so
the helper becomes the active object), and press
``Ctrl + P > Object``. The drawing is now a child of the helper.

.. TODO: screenshot — Outliner showing the parent relationship (helper as parent, drawing as child) and the Object Properties > Relations panel with Parent: <helper>.

.. image:: /_static/tutorials/place_drawings/04_parent_relation.png
   :width: 90%
   :align: center
   :alt: Outliner / Object Properties showing the drawing parented to the helper mesh.

**3.5 — Resize the helper to the real scale-bar length**

With the helper still selected, set its dimension on the relevant
axis (X or Y, depending on how the scale bar is oriented on the
drawing) to the value the bar declares — e.g. ``10 m``. Use the
``N`` panel ``Item > Dimensions`` field, not a free ``S`` drag, to
get an exact figure.

The drawing follows because it is parented. Visually, the scale
bar on the drawing should now match the helper edge length.

**3.6 — Unparent with *Keep Transformation***

Select only the drawing and press
``Alt + P > Clear and Keep Transformation``. The parent link is
removed but the inherited scale stays on the drawing. Check
``Item > Dimensions`` on the drawing: the values now reflect the
true metric size.

.. TODO: screenshot — N panel Item > Dimensions of the drawing after Clear and Keep Transformation, showing real-world metres.

.. image:: /_static/tutorials/place_drawings/05_dimensions_post_unparent.png
   :width: 90%
   :align: center
   :alt: Item > Dimensions of the drawing after Clear and Keep Transformation.

**3.7 — Delete the helper**

The helper mesh is no longer needed. Select it and delete
(``X``). Apply ``Object > Apply > All Transforms`` on the drawing
if you want to bake the scale into the object data; this is
optional but recommended before further alignment.

.. _place-drawings-alignment:

Step 4 — Final alignment
------------------------

With the drawing now in metric units, perform the final placement
against the scene.

- **For a section drawing**, align it to the corresponding section
  node if the project defines one, or to the wall face it
  documents. Use ``Snap > Vertex`` with a known corner as anchor;
  rotate around Z until the section reads parallel to its wall.
- **For a plan drawing**, place it at the elevation that matches
  the surface it documents (floor level of the relevant epoch);
  align the plan's reference points (georeferenced markers,
  known corners) to their 3D counterparts using a standard
  three-point alignment.

.. TODO: screenshot — final view of the drawing aligned in the scene next to proxies/RMs that confirm the placement (orthographic side view for a section, top view for a plan).

.. image:: /_static/tutorials/place_drawings/06_final_alignment.png
   :width: 90%
   :align: center
   :alt: Final view with the drawing aligned to the reconstruction.

.. seealso::

   - :ref:`rmdoc_manager` — once the drawing is in place, bind it
     to a graph document node so its provenance travels with the
     scene.
   - :doc:`20-em-2d-3d-linking` — the broader workflow of linking
     EM nodes to 2D/3D documentation.
