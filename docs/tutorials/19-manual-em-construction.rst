.. badge:: Intermediate
   :color: orange

Building an Extended Matrix Manually, Unit by Unit
==================================================

This tutorial walks you through authoring a small EM graph from a
written stratigraphic report — no AI extraction, no pre-existing
xlsx — so you can feel the formal language with your hands and
recognise its parts when they appear in larger projects.

It is the natural follow-up to
:doc:`13-first-matrix-creation`: that one shows the *mechanics* of
yEd; this one shows the *reasoning*.

Learning objectives
-------------------

By the end you will be able to:

- read a stratigraphic report and translate it into EM nodes (US,
  USV, USD, SF) with correct typing;
- model the most common stratigraphic relationships
  (``stratigraphic_above``, ``contemporary_with``,
  ``cuts``, ``filled_by``) using EM connectors;
- attach paradata (sources, extractors, properties) to a unit and
  trace the inference chain back to the source;
- recognise when a piece of evidence does *not* fit any node type
  and decide what to do (discuss, defer, or document the gap).

Prerequisites
-------------

- :doc:`12-install-yed-blender` — yEd installed with the EM palette.
- :doc:`13-first-matrix-creation` — you know how to create the canvas
  and save GraphML.
- A basic understanding of stratigraphic reading
  (`EM language docs — A stratigraphic approach
  <https://docs.extendedmatrix.org/en/1.5.0dev/stratigraphic_approach.html>`_).

Dataset
-------

We use a small, self-contained example: the **east cross-section of
Trench A** at the *Casa di Esempio* training site. The dataset
contains:

- the report PDF (~3 pages, 8 stratigraphic units, 2 special finds);
- the section drawing in PNG and SVG;
- the source PDFs for two of the units.

.. todo::
   Dataset is being prepared. Until then, use any small report with
   8–12 units. The instructions below assume 8 US/USD/SF nodes —
   adapt the count to your material.

The walk-through
----------------

We approach each step with the four-column rhythm of
:doc:`../workflows`.

**Step 1 — Set the canvas and metadata**

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - your project info
     - yEd canvas
     - Drag the EM canvas, fill *site code*, *author*, *ORCID*, *licence*, *embargo*.
     - Empty graph with the metadata frontmatter set.

**Step 2 — Catalogue the units before drawing anything**

On a sheet of paper (or in a side document), list every stratigraphic
unit in the report and decide its type:

- **US** — a real, observed body of matter;
- **USD** — a documentary unit (something you read about but don't
  see physically);
- **USV** — a virtual unit, supported by an in-situ anchor;
- **USVn** — a typological reference (no anchor on this site);
- **SF** / **VSF** — a special find or a virtual special find.

If you don't know which one a unit is, *write it down* — you will
ask someone or come back to it.

**Step 3 — Place the nodes**

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - the typed list from Step 2
     - yEd palette + canvas
     - Drag one node per unit; set the *human ID* (e.g. ``CDE.A.US.001``).
     - One labelled node per unit, no connectors yet.

**Step 4 — Draw the relations**

Go through the report a second time, this time looking only for
*verbs of stratigraphic relation*: "covers", "is cut by", "fills",
"contemporary with", … For each, pick the matching connector from
the EM palette (see `EM language docs — Connectors
<https://docs.extendedmatrix.org/en/1.5.0dev/connectors.html>`_)
and draw the arrow.

**Step 5 — Attach the sources**

For at least two units, drag a *Document* node, fill its metadata
(``DOC.001``, title, year, page range, file path inside DosCo), and
connect it to the unit with the *has source* connector. We will
come back to richer paradata in :doc:`20-em-2d-3d-linking`.

**Step 6 — Save and load in Blender**

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - the GraphML you just saved
     - :doc:`../panels/em_setup`
     - Set graph + DosCo paths; *Reload*.
     - Your 8 units appear in the Stratigraphy Manager, sources auto-linked.

Self-check
----------

Before moving on, confirm:

#. Every node has a unique human ID and the right type.
#. Every relation in the report is represented by exactly one
   connector — no duplicates, no missing arrows.
#. The two units with sources show those sources in the
   :doc:`../panels/paradata_manager` after reload.
#. Saving and reloading the GraphML produces no validation warnings
   in the EM Setup panel.

Common pitfalls
---------------

- Mixing **USV** and **USVn**: USV must have an in-situ anchor on
  *this* site; USVn does not. If in doubt, USVn.
- Forgetting the canvas metadata: it is the only place where
  ``site_code``, ``author`` and ``licence`` live. Without it, every
  export will be incomplete.
- Drawing the same relation twice (e.g. a forward and a reverse
  connector): EM relations are directional and one-way is enough.

Where to go next
----------------

- :doc:`20-em-2d-3d-linking` — connect the units you just authored
  to the section drawing and to a 3D model.
- :doc:`21-sources-metadata` — turn the two source nodes into a
  proper paradata chain with extractors and combiners.
- :doc:`22-complete-case-study` — see the full life cycle of an EM
  on a real site.
