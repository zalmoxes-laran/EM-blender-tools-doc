.. _StratiMiner:

StratiMiner (Experimental)
==========================

.. seealso::

   In the Extended Matrix language manual:

   - :doc:`em-doc:em_data` — the formal ``em_data`` data model that
     StratiMiner serialises and round-trips through Excel.
   - :doc:`em-doc:draw_the_matrix` — the yEd-based authoring path
     StratiMiner aims to short-circuit by letting authors stay in a
     tabular tool.

The **StratiMiner** panel drives the unified ``em_data.xlsx`` workflow for
building an Extended Matrix graph from archaeological documents. It
replaces the legacy two-file wizard (``stratigraphy.xlsx`` +
``em_paradata.xlsx``) with a single five-sheet schema (``Units``,
``Epochs``, ``Claims``, ``Authors``, ``Documents``) that can be produced
either by an AI assistant or by hand from an existing database.

.. warning::
   This is an **experimental feature**. It requires Experimental
   Features enabled in the :ref:`EMsetup` panel and is only visible when
   Advanced EM mode is active. Always work on a backup before using it
   on production data.

The panel is located in the **EM Bridge** tab under the label
``StratiMiner (Experimental)``.

Panel layout
------------

The panel is organised into two logical blocks — **Create** and
**Use** — that are independent: pick the action that matches the
current session.

Block 1 — CREATE ``em_data.xlsx``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two alternative paths to obtain an ``em_data.xlsx`` file.

**Option A — AI-assisted**:

- ``Output language`` dropdown: language in which the AI should return
  labels and descriptions
- ``Documents folder``: folder that contains the source PDFs the AI
  will parse
- ``DosCo in-place`` toggle: when enabled, the DosCo layout is written
  directly inside the documents folder; when disabled, a
  ``Target DosCo folder`` field appears to redirect the output
- ``AI has filesystem access`` toggle: declares whether the assistant
  can read the PDFs directly (Claude Projects, ChatGPT with uploaded
  files, Gemini) or only via pasted text
- ``Include validation instructions`` toggle
- ``Include checklist`` toggle
- ``Stratigraphy-only prompt`` toggle: emits a reduced prompt limited
  to stratigraphic relations (no paradata)
- ``Copy StratiMiner Prompt`` button: copies the v5.2 extraction prompt
  to the clipboard, ready to be pasted into Claude, ChatGPT or Gemini
  together with the PDFs. The assistant returns a single
  ``em_data.xlsx`` with the 5 typed sheets.

**Option B — Manual (empty template)**:

- ``Save em_data.xlsx Template`` button: writes an empty 5-sheet
  workbook to disk so it can be filled by hand. This is the
  recommended entry point when migrating a pre-existing
  archaeological database that already contains explicit
  stratigraphic relations.

Block 2 — USE ``em_data.xlsx``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once an ``em_data.xlsx`` exists (via Option A or B), it can be
consumed in two independent ways.

- ``em_data.xlsx`` file path: selects the workbook to use for the
  actions below.

**Path A — Build a new GraphML**:

- ``Also write .graphml on import`` toggle: when enabled, the graph is
  exported to disk right after it is built in memory
- ``Output .graphml`` file path: destination of the optional export
  (the ``.graphml`` extension is added automatically if missing)
- ``Build GraphML from em_data.xlsx`` button: parses the xlsx with the
  ``UnifiedXLSXImporter``, registers the resulting graph in the
  MultiGraphManager, and — if enabled — writes out the ``.graphml``
  file. Node/edge counts of the freshly built graph are shown below
  the button.

**Path B — Merge into active GraphML**:

- ``Merge into Active Graph...`` button: launches the merge
  conflict-resolution flow against the currently loaded GraphML.
  Disabled until a GraphML is active in the :ref:`EMsetup` tree.

Import warnings
~~~~~~~~~~~~~~~

When the importer reports warnings (missing authors, orphan claims,
unknown epochs, etc.), a collapsible ``Import Warnings (N)`` box is
appended at the bottom of the panel with a per-entry list and a clear
button.

Workflow
--------

1. Enable Experimental Features in the :ref:`EMsetup` panel and
   activate Advanced EM mode.
2. Open **EM Bridge → StratiMiner (Experimental)**.
3. Choose how to produce the ``em_data.xlsx``:

   - *AI path*: set the documents folder, adjust the DosCo and prompt
     toggles, click ``Copy StratiMiner Prompt``, paste it into the
     assistant along with the PDFs, save the returned workbook.
   - *Manual path*: click ``Save em_data.xlsx Template`` and fill the
     5 sheets by hand.

4. Point the ``em_data.xlsx`` field to the file produced at step 3.
5. Either click ``Build GraphML from em_data.xlsx`` (optionally
   writing the ``.graphml`` to disk) or ``Merge into Active Graph...``
   to integrate it into the currently loaded graph.
6. Inspect the ``Import Warnings`` box and reconcile anything flagged
   before treating the result as final.

Related operators
-----------------

- ``stratiminer.copy_prompt`` — copies the v5.2 extraction prompt to
  the clipboard.
- ``stratiminer.import_em_data`` — Action A: build a new in-memory
  graph from ``em_data.xlsx`` with optional ``.graphml`` export.
- ``em.merge_xlsx_start`` — Action B: merge an ``em_data.xlsx`` into
  the active graph through the Conflict Resolution panel.
- ``emtools.save_em_data_template`` — writes the empty 5-sheet
  workbook.
