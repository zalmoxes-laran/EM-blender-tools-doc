Creating an Extended Matrix from Different Sources
==================================================

The Extended Matrix (EM) can be created through several pathways, each
suited to different project needs and workflows. This guide covers the
supported methods, focusing on the unified ``em_data.xlsx`` flow
introduced in EMtools 1.5 / s3Dgraphy 1.6.

.. contents::
   :local:
   :depth: 2


The Knowledge Tree
------------------

The Extended Matrix knowledge system works like a **tree**: the GraphML
file is the **trunk**, providing the stratigraphic sequence, chronological
scaffolding, and fundamental relationships between units. The leaves are
the detailed, granular data that give richness to each stratigraphic
unit: definitions, interpretations, materials, measurements, dating
evidence, and so on.

A single ``em_data.xlsx`` file carries **both the trunk and the leaves**
for a given graph. It is consumed in one pass by the ``UnifiedXLSXImporter``
to produce a complete s3Dgraphy graph, ready to be written as GraphML
(for yEd editing) or merged into an already-loaded GraphML (conflict
resolution).

.. seealso::

   For a full explanation of this architecture, see
   `The Knowledge Tree <https://docs.extendedmatrix.org/en/1.6/knowledge_tree.html>`_
   in the Extended Matrix documentation.


Overview
--------

Three parallel paths are supported for creating and evolving an EM
graph:

1. **From GraphML (yEd)** — Manual creation or editing of the GraphML
   file with the yEd graph editor. Full control over the graph
   structure, traditional stratigrapher-driven workflow.
2. **From em_data.xlsx** — Structured tabular input using the unified
   5-sheet schema. Two sub-paths:

   a. **AI-assisted** — copy the StratiMiner prompt into Claude /
      ChatGPT / Gemini, attach the PDFs, paste the returned xlsx.
   b. **Manual** — save the empty template and fill it by hand,
      ideal for migrating pre-existing archaeological databases with
      explicit stratigraphic relations.

3. **From existing databases** — Import from pyArchInit and other
   tabular sources via the s3Dgraphy mapping system. See
   `From Existing Databases`_ at the end of this page.

Paths 1 and 2 converge on the same in-memory graph and can be mixed
freely in the same project.


From GraphML (yEd)
------------------

The traditional method for creating an EM is to use the
`yEd Graph Editor <https://www.yworks.com/products/yed>`_ to manually
build the GraphML file. This approach gives full control over the
graph structure and is well-suited for:

- Small to medium stratigraphic sequences;
- Projects where the stratigrapher directly builds the graph;
- Fine-tuning and validation of automatically generated graphs.

For details on the GraphML structure and node types, see
:doc:`panels/em_setup`.

.. note::

   For a comprehensive guide on the Extended Matrix formal language,
   node types, and how to construct a valid EM graph, refer to the
   `Extended Matrix documentation <https://docs.extendedmatrix.org/en/1.6/>`_.
   The `nodes introduction <https://docs.extendedmatrix.org/en/1.6/nodes_intro.html>`_
   and `stratigraphic nodes <https://docs.extendedmatrix.org/en/1.6/stratigraphic_nodes.html>`_
   pages are particularly useful for understanding what each node type
   represents.


From em_data.xlsx (Unified schema)
-----------------------------------

The unified xlsx format is a **single file** with five typed sheets
that together describe both the stratigraphic skeleton and its full
paradata chain. It replaces the legacy two-file workflow
(``stratigraphy.xlsx`` + ``em_paradata.xlsx``) used by earlier EMtools
versions.

The StratiMiner panel in the EMtools EM Bridge tab offers both paths
to **create** an ``em_data.xlsx`` and both paths to **use** one.

.. image:: img/stratiminer_panel.png
   :alt: StratiMiner panel in EM Bridge tab
   :align: center


Create em_data.xlsx
~~~~~~~~~~~~~~~~~~~

**Option A — AI-assisted**

1. Open **EM Bridge → StratiMiner (Experimental)** (requires the
   *Experimental Features* flag).
2. Under **CREATE em_data.xlsx**, set the *Language* (default: the same
   as the source document) and the *Documents folder* pointing at the
   directory that holds the source PDFs.
3. Select the optional toggles:

   - **Validation script** — includes a Python snippet the AI must run
     on its output to catch duplicates, missing references, missing
     ``COMBINER_REASONING`` and stratigraphic cycles. Strongly
     recommended.
   - **End-of-session checklist** — the AI-side QA list for the final
     handoff.
   - **Include stratigraphy-only mode** — appends an extra section
     describing the reduced flow for legacy databases with no paradata
     attribution. Enable only if your source data matches that case.

4. Click **Copy StratiMiner Prompt**. The prompt is placed in the
   clipboard, with the documents-folder path injected and all the
   toggles applied.
5. Paste the prompt into your AI assistant (Claude, ChatGPT, Gemini)
   together with the PDFs. The AI returns a single ``em_data.xlsx``.

**Option B — Manual**

1. Click **Save em_data.xlsx Template** under *Option B*. A Save dialog
   opens; choose a directory. An empty ``em_data_template.xlsx`` is
   copied from the s3Dgraphy package.
2. Open the template in Excel or LibreOffice. Every header cell carries
   a tooltip that describes the expected content.
3. Fill the five sheets (see `The 5-sheet schema`_ below). The minimal
   required content is: at least one row in ``Units``, ``Authors`` and
   ``Claims``.

Both options produce the same file format and are interchangeable.


Use em_data.xlsx
~~~~~~~~~~~~~~~~

**Path A — Build a brand-new GraphML**

1. Under **USE em_data.xlsx**, pick the ``em_data.xlsx`` file.
2. Optionally tick *Also write .graphml on import* and pick the output
   path. (The panel auto-suggests one next to the xlsx.)
3. Click **Build GraphML from em_data.xlsx**. The xlsx is parsed by
   ``UnifiedXLSXImporter`` into a fresh in-memory graph, and (if you
   enabled it) immediately written out as ``.graphml``.
4. The resulting ``.graphml`` can be opened in yEd for visual editing,
   or imported back into EMtools via the standard *Import EM file*
   flow.

**Path B — Merge into an already-loaded GraphML**

1. Make sure a GraphML is loaded and active in the EM tree tab.
2. Under **USE em_data.xlsx → Merge into active GraphML**, click
   **Merge into Active Graph…**.
3. A file picker opens — select the ``em_data.xlsx``. The merger
   auto-detects the unified 5-sheet schema (falls back to the legacy
   stratigraphy.xlsx format for backward compatibility) and compares it
   with the active graph.
4. Differences surface in the *Conflict Resolution* panel: qualia
   added, qualia value changed, new per-claim attribution sources,
   added authors / documents / epochs, relation-edge attribution
   changes. You accept or reject each conflict.
5. Apply the resolutions; accepted changes are written into the active
   in-memory graph. Save the graph with *Save GraphML* / *Save As…* to
   persist the merged state to disk.


The 5-sheet schema
~~~~~~~~~~~~~~~~~~

An ``em_data.xlsx`` file has exactly five sheets, in this order:

**1. Units** — the stratigraphic skeleton

.. list-table::
   :header-rows: 1
   :widths: 10 10 30

   * - Column
     - Required
     - Description
   * - ``ID``
     - Yes
     - Unique unit id (``C01``, ``SU001``, ``USV100``, ``TM_USM01`` …)
   * - ``TYPE``
     - Yes
     - Stratigraphic class: ``US``, ``USVs``, ``USVn``, ``SF``, ``VSF``,
       ``USD``, ``serSU``, ``serUSD``, ``serUSVn``, ``serUSVs``,
       ``TSU``, ``SE``, ``BR``
   * - ``NAME``
     - No
     - Short human label. Falls back to ``ID`` when empty

Units only declares the existence of a node. Every fact about it
(dimensions, materials, datation, relationships) goes into the
``Claims`` sheet.

**2. Epochs** — swimlanes and non-overlapping phases

.. list-table::
   :header-rows: 1
   :widths: 10 10 30

   * - Column
     - Required
     - Description
   * - ``ID``
     - Yes
     - Short phase code (``E1``, ``PH0``, ``PH2`` …)
   * - ``NAME``
     - Yes
     - Human-readable name (``II A.D.``, ``PH2 – Temple construction``)
   * - ``START``
     - Yes
     - Start year as an integer (negative = BCE)
   * - ``END``
     - Yes
     - End year as an integer
   * - ``COLOR``
     - No
     - Swimlane fill colour (``#RRGGBB``)

Epochs **must be non-overlapping**. If a unit spans multiple phases,
it is a *single* ``belongs_to_epoch`` claim pointing at its primary
phase; additional survival spans are handled by ``survive_in_epoch``
edges added by the downstream chronology resolver.

**3. Claims** — the long-table, one row per asserted fact

Every piece of information about a unit (or an epoch) lives here. A
row carries one of four kinds of content:

- **Scalar qualia** — ``PROPERTY_TYPE`` ∈ ``definition``,
  ``material_type``, ``length``, ``width``, ``height``, ``shape``,
  ``conservation_state``, ``interpretation``, ``comparanda``, …
- **Temporal qualia** — ``absolute_time_start`` /
  ``absolute_time_end``. Feed the DP-32 chronology resolver.
- **Epoch membership** — ``belongs_to_epoch`` with ``TARGET2_ID``
  pointing at an ``Epochs.ID``.
- **Stratigraphic relation** — ``overlies``, ``cuts``, ``fills``,
  ``abuts``, ``bonded_to``, ``equals``, ``is_after`` …; ``TARGET_ID``
  is the source endpoint, ``TARGET2_ID`` the target endpoint.

Each row also carries its own **per-claim attribution**:

.. list-table::
   :header-rows: 1
   :widths: 15 15 40

   * - Column group
     - Fields
     - Meaning
   * - Attribution #1
     - ``EXTRACTOR_1`` / ``DOCUMENT_1`` / ``AUTHOR_1`` /
       ``AUTHOR_KIND_1``
     - The verbatim excerpt (``EXTRACTOR_1``) from the source
       document (``DOCUMENT_1``), asserted by ``AUTHOR_1``. The
       ``AUTHOR_KIND_1`` column distinguishes facts **transcribed**
       from the document author (``author``) from facts **newly
       derived** by an AI extractor (``extractor``).
   * - Attribution #2 (optional)
     - ``EXTRACTOR_2`` / ``DOCUMENT_2`` / ``AUTHOR_2`` /
       ``AUTHOR_KIND_2``
     - Second converging source. When both #1 and #2 are populated,
       ``COMBINER_REASONING`` must describe how the two sources are
       combined (concordance, divergence, canonical choice).

**4. Authors** — the normalized author catalog

.. list-table::
   :header-rows: 1
   :widths: 10 10 40

   * - Column
     - Required
     - Description
   * - ``ID``
     - Yes
     - ``A.01``, ``A.02``, ... for humans. ``AI.01``, ``AI.02``, ...
       for AI agents (the prefix matters)
   * - ``KIND``
     - Yes
     - ``author`` (human, AuthorNode) or ``extractor`` (AI,
       AuthorAINode). Must agree with the ID prefix.
   * - ``DISPLAY_NAME``
     - No
     - Human-readable display (``"Demetrescu, Emanuele"`` or
       ``"StratiMiner-v1"``)
   * - ``ORCID``
     - No
     - ORCID for humans; model version / pipeline id for AI agents
   * - ``AFFILIATION``
     - No
     - Institutional affiliation

**5. Documents** — the normalized source catalog

.. list-table::
   :header-rows: 1
   :widths: 10 10 40

   * - Column
     - Required
     - Description
   * - ``ID``
     - Yes
     - ``D.01``, ``D.02``, ...
   * - ``FILENAME``
     - Yes
     - Filename on disk
   * - ``TITLE``
     - No
     - Full bibliographic title
   * - ``YEAR``
     - No
     - Publication year
   * - ``AUTHOR_IDS``
     - No
     - Comma-separated ``Authors.ID`` list for the document authors
       (distinct from the per-claim authors!)


Why the distinction between author and extractor matters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every claim is traceable to *one specific agent*: either the person who
wrote the source document (``KIND=author``) or the agent who derived
the claim from the document (``KIND=extractor``, typically the AI
StratiMiner).

The s3Dgraphy **diagnostics layer** uses this distinction to route
chronology paradoxes and stratigraphic cycles to the right reviewer.
When the resolver detects that unit ``Y`` declares an
``absolute_time_start = 130`` that contradicts its stratigraphic
position, the warning names the specific extractor / author that made
the offending claim — so you know whether to re-read the PDF or
re-prompt the AI.

See :doc:`panels/em_setup` for details on the *Conflict Resolution*
panel that surfaces these diagnostics.


From Existing Databases
-----------------------

EMtools supports import from archaeological database systems via
s3Dgraphy's mapping system.

pyArchInit
~~~~~~~~~~

`pyArchInit <https://pyarchinit.readthedocs.io/>`_ is an archaeological
information system based on QGIS.

.. _pyarchinit-architecture:

Architecture
^^^^^^^^^^^^

The integration uses three independent layers — each one can be
maintained, upgraded, or replaced without breaking the others.

.. code-block:: text

   +------------------------------------------------------------------+
   |                                                                  |
   |   PyArchInit project (QGIS plugin)                               |
   |   - Stratigraphic records, 2D GIS data                           |
   |   - Maintained by Luca Mandolesi and the PyArchInit community    |
   |                                                                  |
   +-----------------------------+------------------------------------+
                                 |
                                 |  s3Dgraphy library (mapping layer)
                                 |  - Reads the PyArchInit database
                                 |  - Either references records live,
                                 |    or bakes them into the EM graph
                                 |  - pyarchinit_us_mapping is the
                                 |    canonical mapping for the US table
                                 |
                                 v
   +------------------------------------------------------------------+
   |                                                                  |
   |   EM-Tools (Blender add-on)                                      |
   |   - Consumes the s3Dgraphy graph                                 |
   |   - Drives the Extended Matrix workflow                          |
   |                                                                  |
   +------------------------------------------------------------------+

Two integration modes
"""""""""""""""""""""

**Connection mode (recommended for live projects)** — the PyArchInit
database stays the source of truth for stratigraphic records.
s3Dgraphy reads it on demand. Changes in PyArchInit propagate to EM
on the next read.

**Bake mode** — the PyArchInit records are imported once into the EM
graph as auxiliary nodes. Subsequent edits happen on the EM side.
Useful for archive projects or for finalised excavations.

.. seealso::

   - :doc:`tutorials/15-pyarchinit-external-data` — full how-to
   - `PyArchInit project <https://github.com/pyarchinit/pyarchinit>`_
   - `s3Dgraphy on PyPI <https://pypi.org/project/s3dgraphy/>`_
   - `Extended Matrix cookbook recipe <https://docs.extendedmatrix.org/en/1.6/cookbook/pyarchinit_integration.html>`_

Operational workflow
^^^^^^^^^^^^^^^^^^^^

There are **two ways** to use pyArchInit data with the Extended Matrix:

**1. Generate GraphML from pyArchInit (creating the trunk)**

pyArchInit has a built-in tool that can export stratigraphic data
directly as a GraphML file in Extended Matrix format. This is the
recommended approach when you want to create a new EM graph from an
existing pyArchInit database. See the
`pyArchInit documentation on the HerRIS Matrix for Extended Matrix Tool
<https://pyarchinit.readthedocs.io/it/latest/novit%C3%A0.html#herris-matrix-per-extended-matrix-tool>`_
(in Italian).

**2. Import pyArchInit as auxiliary file (adding leaves)**

When you already have a GraphML and want to enrich it with property
data from a pyArchInit database, you can add it as an **auxiliary
file** in EMtools. In this mode, the pyArchInit SQLite database is
imported using the ``pyarchinit`` mapping type, and properties are
added to existing graph nodes (matched by unit ID). The graph
structure is not modified.

To import as auxiliary:

1. Import your GraphML into EMtools first
2. In the EM Data Tree panel, add an auxiliary file
3. Select file type **pyArchInit**
4. Select the SQLite database file
5. Choose the appropriate mapping (``pyarchinit_us_mapping``)
6. Click **Import** — properties from the database are added to
   matching nodes


Legacy two-file workflow (deprecated)
-------------------------------------

Before EMtools 1.5 the AI-assisted flow produced **two** files
(``stratigraphy.xlsx`` + ``em_paradata.xlsx``) that had to be imported
in separate steps. That workflow is deprecated but still usable for
backward compatibility:

- The ``MappedXLSXImporter`` + ``QualiaImporter`` pair is still shipped
  and registered.
- The ``em.merge_xlsx_start`` operator auto-detects the legacy schema
  (sheet named ``Stratigraphy``) and falls back to the old importer
  path.
- Legacy xlsx files can be converted to the unified schema by: import
  with the legacy pair → resulting graph exported to
  ``em_data.xlsx`` via ``UnifiedXLSXExporter``.

New projects should use the unified ``em_data.xlsx`` schema from the
start.
