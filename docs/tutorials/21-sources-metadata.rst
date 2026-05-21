.. badge:: Intermediate
   :color: orange

Managing Sources, Paradata and Metadata
=======================================

The point of an EM graph is not the units, it is the *reasoning chain*
behind each unit: which sources support it, what was extracted from
each source, how partial extractions were combined, and what
properties the combination justifies. This tutorial shows how to
build that chain cleanly, how to expose it to the user in Blender,
and how to keep your DosCo folder tidy enough that the chain still
works two years from now.

Learning objectives
-------------------

By the end you will be able to:

- structure a DosCo folder so every source has a stable, citeable
  path;
- author a complete paradata chain
  (``Document → Extractor → Combiner → Property``) that travels
  with the unit;
- decide when an extractor is justified and when a property can be
  attached directly;
- review and audit paradata in Blender via the
  :doc:`../panels/paradata_manager`.

Prerequisites
-------------

- :doc:`20-em-2d-3d-linking` — you have units bound to drawings,
  meshes and 3D documents.
- A handful of source PDFs that justify *interpretive* (not just
  observational) properties — i.e. things you cannot read off the
  drawing directly.
- Familiarity with the EM paradata vocabulary
  (`EM language docs — Paradata Nodes
  <https://docs.extendedmatrix.org/en/1.5/paradata_nodes.html>`_).

DosCo discipline
----------------

DosCo (*Documentation Source Collection*) is the folder where every
source the graph references lives. The contract is simple:

- one folder per *kind* of source (``photographs``, ``reports``,
  ``drawings``, ``analyses``);
- file names that match the ``id`` of the corresponding Document
  node (``DOC.012.pdf``, ``DOC.012_p4_detail.png``, …);
- never reference files outside DosCo from a Document node — copy
  them in;
- never rename files after they are referenced, only add.

If the contract holds, the :doc:`../panels/em_setup` *DosCo path*
field is the only setting that ever needs updating when the project
moves.

The walk-through
----------------

We continue with the *Casa di Esempio / Trench A* example. Pick
one US whose interpretation rests on more than one source — for
instance, *US.A.005* whose dating rests on a coin, a stratigraphic
position, and an analogous context elsewhere.

**Step 1 — Document nodes for each source**

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - the three sources for US.A.005
     - yEd
     - Add three Document nodes (``DOC.005a``, ``DOC.005b``, ``DOC.005c``); fill metadata; place in DosCo.
     - Three Document nodes resolvable to files on disk.

**Step 2 — Extractors per source**

An *Extractor* records *what you actually pulled* from a source. If
the report says "the layer contained a coin of Hadrian and a
fragment of late-Antonine sigillata", the **extraction** is *terminus
post quem 138 CE* — not the whole report.

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - each Document
     - yEd
     - Add an Extractor node per source; fill ``method`` (e.g. ``temporal_tpq``), ``value``, ``confidence``; connect Document → Extractor.
     - Three extractions, each citing exactly one source.

When *not* to use an extractor: if the property is directly
*observable* from the source (e.g. a measured length on a drawing),
attach the property to the Document directly. Reserve extractors
for *interpretive* steps.

**Step 3 — Combine the extractions**

When several extractions converge on the same property, a
**Combiner** records the act of synthesising them.

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - the three Extractors
     - yEd
     - Add one Combiner node; connect all three Extractors into it; fill ``rationale``.
     - One node that says "these three together imply X".

**Step 4 — Attach the property**

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - the Combiner
     - yEd
     - Add a Property node (``dating``, value ``2nd c. CE``, confidence ``high``); connect Combiner → Property → US.
     - The unit now has a justified property whose chain you can audit.

**Step 5 — Audit in Blender**

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - the loaded graph
     - :doc:`../panels/paradata_manager`
     - Select US.A.005; enable *Filter Paradata*.
     - The three Documents, three Extractors, the Combiner and the Property surface in a connected list.

Self-check
----------

#. Every property on US.A.005 has a chain that ends in at least one
   Document.
#. No Document referenced in the graph is missing from DosCo.
#. The :doc:`../panels/paradata_manager`'s filter view shows the
   chain in the expected order.
#. Removing one of the three sources (in a *copy* of the graph)
   visibly weakens the chain — the Combiner ``rationale`` should
   make this auditable.

Common pitfalls
---------------

- Stuffing everything into one Document node ("the report") instead
  of one per logical citation. The chain becomes opaque.
- Skipping the Extractor and connecting Document directly to
  Property when the inference is non-trivial — you lose the
  *what was actually extracted* layer.
- Combiners with one input. If only one extraction supports the
  property, attach the property to the Extractor; reserve Combiners
  for genuine syntheses.

Where to go next
----------------

- :doc:`22-complete-case-study` — see this discipline applied
  to a whole site.
- :doc:`17-paradata-graph-viz` — visualise the chains you just
  authored as a node graph.
