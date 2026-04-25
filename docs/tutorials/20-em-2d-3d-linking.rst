.. badge:: Intermediate
   :color: orange

Linking EM to Your 2D and 3D Documentation
==========================================

An EM graph becomes useful only when its nodes are tied to the
*things* they describe — drawings, photographs, photogrammetric
models, sections. This tutorial shows how to wire those connections
so that, in Blender, every stratigraphic unit can be inspected
spatially *and* the inverse — selecting an object on screen surfaces
its graph entry.

It also explains the difference between **document references**
(``Document`` nodes, used for any source) and **3D documents**
(handled by the :doc:`../panels/document_manager_3d`), which add
spatial-temporal placement.

Learning objectives
-------------------

By the end you will be able to:

- attach 2D drawings (sections, plans, orthophotos) to the units
  they document, with the right source metadata;
- bind a 3D mesh — proxy or high-resolution — to a stratigraphic
  unit so that selection works in both directions
  (graph ↔ viewport);
- place a *3D document* in the scene (a camera + image plane) so
  that historic photographs sit in the same coordinate system as
  the reconstruction;
- decide when to use a ``Document`` node, when to use a *3D
  document*, and when to use both.

Prerequisites
-------------

- :doc:`19-manual-em-construction` — the small graph you authored
  there is the starting point of this tutorial.
- A scene with at least one mesh (proxy or photogrammetric) loaded
  into Blender.
- One section drawing in PNG/SVG and one historic photograph (any
  format Blender can import as image plane).

Dataset
-------

We extend the *Casa di Esempio / Trench A* example: section drawing
of the east face, an orthophoto of the floor, two historic
photographs, and a small photogrammetric mesh of one wall.

.. todo::
   Companion files in preparation. Use your own equivalent dataset
   in the meantime — the structure of the steps does not change.

The walk-through
----------------

**Step 1 — Document references for the 2D drawings**

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - section drawing PNG; metadata
     - yEd
     - Add a ``Document`` node, fill ``id``, ``title``, ``year``, ``file_path`` (relative to DosCo); link to the units it documents.
     - The section is now reachable from every unit it shows.

**Step 2 — Bind proxies to units**

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - the mesh; the active US
     - :doc:`../panels/proxy_box_creator`
     - 7-point pick on the mesh, name = US human ID.
     - Proxy aligned to the mesh, named to match the graph node.
   * - all proxies
     - :doc:`../panels/em_setup`
     - *Reload*.
     - Selecting the proxy highlights the US in the Stratigraphy Manager and vice versa.

**Step 3 — 3D documents (camera + image plane)**

For documents that have a *position in space and time* — historic
photographs, archival drawings with a known viewpoint — use the
:doc:`../panels/document_manager_3d`.

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - photograph + capture date + estimated viewpoint
     - :doc:`../panels/document_manager_3d`
     - Create a 3D document; align the camera; set image plane.
     - The photograph appears in the scene from the right angle and is bound to its temporal anchor.

**Step 4 — Cross-walk: from graph to viewport and back**

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - any unit selected in the graph
     - :doc:`../panels/stratigraphy_manager`
     - Click the focus button on the row.
     - Camera flies to the proxy; related sources highlight.
   * - any proxy selected in 3D
     - :doc:`../panels/paradata_manager`
     - Enable *Filter Paradata*.
     - Properties / extractors / documents filter to the selected unit.

Self-check
----------

#. Selecting any of the eight units from Step 1 of
   :doc:`19-manual-em-construction` reveals the linked drawings
   *or* the 3D document, as appropriate.
#. Two-way selection (graph ↔ viewport) works on every unit that
   has a proxy.
#. The historic photograph appears in the scene at its correct
   location, oriented as it was taken.

Common pitfalls
---------------

- ``file_path`` on Document nodes is **relative to DosCo**, not
  absolute. Absolute paths break as soon as the project moves
  machines.
- A proxy that does not exactly match the US human ID will not
  link automatically — name them identically (case-sensitive).
- 3D documents need a date or epoch reference, otherwise they
  cannot participate in epoch filtering.

Where to go next
----------------

- :doc:`21-sources-metadata` — make the source attachments richer
  with extractors, combiners, and property nodes.
- :doc:`../panels/visual_manager` — drive proxy colours from
  graph properties.
- :doc:`../panels/document_manager_3d` for the full 3D-document
  reference.
