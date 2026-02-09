Creating an Extended Matrix from Different Sources
==================================================

The Extended Matrix (EM) can be created through several pathways, each suited to different project needs and workflows. This guide covers all supported methods, from manual GraphML editing to AI-assisted extraction from archaeological reports.

.. contents::
   :local:
   :depth: 2

The Knowledge Tree
------------------

The Extended Matrix knowledge system works like a **tree**: the GraphML file is the **trunk**, providing the stratigraphic sequence, chronological scaffolding, and fundamental relationships between units. The core properties (node types, relationships, epochs) are the **main branches** — they are part of the graph structure itself.

The **leaves** are the detailed, granular data that come from auxiliary tabular files: definitions, interpretations, materials, construction techniques, measurements, and all those properties that give richness to each stratigraphic unit.

This separation is deliberate: the graph (trunk) is best managed by the project leader and changes infrequently, while the tables (leaves) can be updated continuously by the working group using familiar tools like Excel or databases. Thanks to s3Dgraphy and EMtools, these two worlds merge on-the-fly into a unified knowledge graph.

.. seealso::

   For a full explanation of this architecture, see `The Knowledge Tree <https://docs.extendedmatrix.org/en/1.5.0/knowledge_tree.html>`_ in the Extended Matrix documentation.


Overview
--------

Three main approaches are available for creating an Extended Matrix:

1. **From GraphML** — Manual creation using graph editors like yEd
2. **From Excel** — Structured tabular input using standardized templates
3. **AI-Assisted Extraction** — Using AI models to extract stratigraphy from PDF reports, field notes, and images

The Excel and AI approaches use a **two-file workflow**:

- **stratigraphy.xlsx** (core) — Contains stratigraphic nodes, relationships, and chronologies. This generates the GraphML (the trunk and main branches).
- **em_paradata.xlsx** (enrichment) — Contains per-property provenance data with full data lineage (extractor text → source document). This is imported to enrich the graph with paradata chains.


From GraphML (yEd)
-------------------

The traditional method for creating an EM is to use the `yEd Graph Editor <https://www.yworks.com/products/yed>`_ to manually build the GraphML file. This approach gives full control over the graph structure and is well-suited for:

- Small to medium stratigraphic sequences
- Projects where the stratigrapher directly builds the graph
- Fine-tuning and validation of automatically generated graphs

For details on the GraphML structure and node types, see :doc:`EMstructure`.

.. note::

   For a comprehensive guide on the Extended Matrix formal language, node types, and how to construct a valid EM graph, refer to the `Extended Matrix documentation <https://docs.extendedmatrix.org/en/1.5.0/>`_. The `nodes introduction <https://docs.extendedmatrix.org/en/1.5.0/nodes_intro.html>`_ and `stratigraphic nodes <https://docs.extendedmatrix.org/en/1.5.0/stratigraphic_nodes.html>`_ pages are particularly useful for understanding what each node type represents.


From Excel (Standard Stratigraphy)
-----------------------------------

The Excel-based approach uses a standardized template with 24 columns that map directly to the s3Dgraphy graph model.

Template Download
~~~~~~~~~~~~~~~~~

Download the empty template from the s3Dgraphy repository:

- **template_stratigraphy.xlsx** — Empty template with 24 column headers
- **example_stratigraphy.xlsx** — Example with 5 sample stratigraphic units

The template uses a sheet named **"Stratigraphy"** with data starting from row 2.

Column Reference
~~~~~~~~~~~~~~~~

.. list-table:: Stratigraphy Columns (24)
   :header-rows: 1
   :widths: 5 15 10 70

   * - Col
     - Header
     - Required
     - Description
   * - A
     - ID
     - Yes
     - Unique identifier for the stratigraphic unit (e.g., US001, USM01)
   * - B
     - TYPE
     - Yes
     - Node type: US, USVs, USVn, SF, VSF, USD, serSU, serUSD, serUSVn, serUSVs, TSU, SE, BR
   * - C
     - DESCRIPTION
     - Yes
     - Detailed textual description of the unit
   * - D
     - PERIOD
     - No
     - Historical period (e.g., Roman, Medieval, Modern)
   * - E
     - PERIOD_START
     - No
     - Start year of the period (negative for BCE)
   * - F
     - PERIOD_END
     - No
     - End year of the period
   * - G
     - PHASE
     - No
     - Chronological phase within the period
   * - H
     - PHASE_START
     - No
     - Start year of the phase
   * - I
     - PHASE_END
     - No
     - End year of the phase
   * - J
     - SUBPHASE
     - No
     - Finer chronological subdivision
   * - K
     - SUBPHASE_START
     - No
     - Start year of the subphase
   * - L
     - SUBPHASE_END
     - No
     - End year of the subphase
   * - M
     - OVERLIES
     - No
     - Comma-separated IDs of units this one covers
   * - N
     - OVERLAIN_BY
     - No
     - Comma-separated IDs of units resting on this one
   * - O
     - CUTS
     - No
     - Comma-separated IDs of units cut by this one
   * - P
     - CUT_BY
     - No
     - Comma-separated IDs of units that cut this one
   * - Q
     - FILLS
     - No
     - Comma-separated IDs of units this one fills
   * - R
     - FILLED_BY
     - No
     - Comma-separated IDs of units that fill this one
   * - S
     - ABUTS
     - No
     - Comma-separated IDs of units this one abuts
   * - T
     - ABUTTED_BY
     - No
     - Comma-separated IDs of units abutting this one
   * - U
     - BONDED_TO
     - No
     - Comma-separated IDs of units physically bonded (contemporary)
   * - V
     - EQUALS
     - No
     - Comma-separated IDs of physically equal units (same fabric)
   * - W
     - EXTRACTOR
     - Yes
     - Who/what extracted the data (e.g., Claude, GPT-4, Manual)
   * - X
     - DOCUMENT
     - Yes
     - Source document filename


Import into EMtools (3-Step Wizard)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EMtools provides a panel-based wizard in the **Experimental Tools** section for converting Excel data into a GraphML file. The wizard keeps the graph in memory until you export it, so you can optionally enrich it with paradata before saving.

1. **Enable Experimental Features** in the EM Setup panel (Utilities & Settings section)
2. Expand **Create a GraphML**

**Step 1 — Convert Stratigraphy**

- Select your ``stratigraphy.xlsx`` file
- Choose the mapping (default: ``excel_to_graphml_mapping``)
- Click **Convert to Graph** — the graph is created in memory and a summary is shown

**Step 2 — Enrich with Paradata** (optional)

- Select your ``em_paradata.xlsx`` file
- Click **Enrich Graph** — provenance chains (PropertyNode → ExtractorNode → DocumentNode) are added to matching nodes

**Step 3 — Export GraphML**

- Choose the output file path
- Click **Export GraphML** — the graph is saved to disk

After exporting, import the GraphML into EMtools via **File > Import EM file** to populate the Blender lists and scene.

.. tip::
   Download empty templates directly from the wizard panel using the **Save Stratigraphy Template** and **Save Paradata Template** buttons.


From Excel (Paradata Enrichment)
---------------------------------

The second Excel file (``em_paradata.xlsx``) contains per-property provenance data in **long format**: one row per (unit, property) pair. Each row records the property value, the specific text extracted from a source document, and which document it came from.

This file is used in **Step 2** of the wizard to enrich the in-memory graph with full data lineage.

Template Download
~~~~~~~~~~~~~~~~~

- **template_em_paradata.xlsx** — Empty template with the paradata column schema

The template uses a sheet named **"Paradata"** with data starting from row 2.

Column Reference
~~~~~~~~~~~~~~~~

.. list-table:: Paradata Columns
   :header-rows: 1
   :widths: 5 20 10 65

   * - Col
     - Header
     - Required
     - Description
   * - A
     - US_ID
     - Yes
     - Must match an existing node ID in the stratigraphy
   * - B
     - PROPERTY_TYPE
     - Yes
     - Property type (e.g., Height, Material, Conservation State)
   * - C
     - VALUE
     - Yes
     - The property value (e.g., "2.5m", "opus reticulatum")
   * - D
     - COMBINER_REASONING
     - No
     - Reasoning combining multiple sources (leave empty for single-source)
   * - E
     - EXTRACTOR_1
     - Yes
     - Text extracted from the first source document
   * - F
     - DOCUMENT_1
     - Yes
     - Filename of the first source document
   * - G
     - EXTRACTOR_2
     - No
     - Text extracted from a second source (multi-source only)
   * - H
     - DOCUMENT_2
     - No
     - Filename of the second source document

Additional ``EXTRACTOR_N`` / ``DOCUMENT_N`` column pairs can be added for properties derived from more than two sources. The importer detects all pairs automatically via column name pattern matching.

Provenance Chains
~~~~~~~~~~~~~~~~~

Each row creates a provenance chain in the Extended Matrix graph:

**Single-source** (COMBINER_REASONING empty)::

   PropertyNode → ExtractorNode → DocumentNode

**Multi-source** (COMBINER_REASONING filled)::

   PropertyNode → CombinerNode → ExtractorNode₁ → DocumentNode₁
                                → ExtractorNode₂ → DocumentNode₂

Property Type Vocabulary
~~~~~~~~~~~~~~~~~~~~~~~~

Common property types include: Height, Width, Length, Thickness, Depth, Material, Conservation State, Construction Technique, Primary Function, Artistic Style, Definition, Interpretation, Absolute Start Date, Absolute End Date, Dating Method. Custom property types in Title Case are also accepted.


AI-Assisted Extraction
-----------------------

AI models (Claude, ChatGPT, Gemini, etc.) can extract stratigraphic data directly from archaeological reports, field notes, and even images. This dramatically accelerates the creation of an Extended Matrix from existing documentation.

The Prompt
~~~~~~~~~~

A ready-to-use, two-part prompt is bundled inside the s3Dgraphy package and can be copied to clipboard directly from the EMtools panel:

- **Part A** extracts core stratigraphy (24 columns) into a table compatible with ``stratigraphy.xlsx``
- **Part B** extracts per-property provenance data into a table compatible with ``em_paradata.xlsx``

The prompt is also available in the s3Dgraphy repository at ``s3Dgraphy/docs/AI_EXTRACTION_PROMPT.md``.

Copy from Blender
~~~~~~~~~~~~~~~~~

In the **Create a GraphML** wizard panel (Experimental Tools), the **AI Extraction Prompt** section provides:

1. A **Language** field — set the target language for descriptions (default: same as the source document)
2. A **Copy AI Prompt to Clipboard** button — copies the full prompt (Part A + Part B) with the language instruction prepended

This is the fastest way to get the prompt ready: paste it into your AI assistant alongside the archaeological documents.

Workflow
~~~~~~~~

1. In EMtools, expand **Create a GraphML** → **AI Extraction Prompt**
2. Set the output language if needed
3. Click **Copy AI Prompt to Clipboard**
4. Open your AI assistant (Claude, ChatGPT, Gemini, etc.)
5. Paste the prompt, then upload or paste the archaeological document
6. Copy the AI's **Part A** output table into ``stratigraphy.xlsx`` (sheet: "Stratigraphy")
7. Copy the AI's **Part B** output table into ``em_paradata.xlsx`` (sheet: "Paradata")
8. Use the 3-step wizard to convert, enrich, and export

Working with Existing GraphML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When enriching an existing GraphML with new document data, add this instruction to the prompt::

   I already have a GraphML with the following units: [list IDs].
   Match extracted units to existing ones where possible.
   Mark new units that are not in the current graph.

Best Practices
~~~~~~~~~~~~~~

- Process documents one at a time for accuracy
- Review AI output before importing — check relationship symmetry and type assignments
- Use the EXTRACTOR columns to track the specific text extracted by the AI from each source
- For large projects, build incrementally: start with a core set of units, then add from additional documents


From Existing Databases
------------------------

EMtools supports import from archaeological database systems via s3Dgraphy's mapping system.

pyArchInit
~~~~~~~~~~

`pyArchInit <https://pyarchinit.readthedocs.io/>`_ is an archaeological information system based on QGIS. There are **two ways** to use pyArchInit data with the Extended Matrix:

**1. Generate GraphML from pyArchInit (creating the trunk)**

pyArchInit has a built-in tool that can export stratigraphic data directly as a GraphML file in Extended Matrix format. This is the recommended approach when you want to create a new EM graph from an existing pyArchInit database. See the `pyArchInit documentation on the HerRIS Matrix for Extended Matrix Tool <https://pyarchinit.readthedocs.io/it/latest/novit%C3%A0.html#herris-matrix-per-extended-matrix-tool>`_ (in Italian).

**2. Import pyArchInit as auxiliary file (adding leaves)**

When you already have a GraphML and want to enrich it with property data from a pyArchInit database, you can add it as an **auxiliary file** in EMtools. In this mode, the pyArchInit SQLite database is imported using the ``pyarchinit`` mapping type, and properties are added to existing graph nodes (matched by unit ID). The graph structure is not modified.

To import as auxiliary:

1. Import your GraphML into EMtools first
2. In the EM Setup panel, add an auxiliary file
3. Select file type **pyArchInit**
4. Select the SQLite database file
5. Choose the appropriate mapping (``pyarchinit_us_mapping``)
6. Click **Import** — properties from the database are added to matching nodes

Custom Database Formats
~~~~~~~~~~~~~~~~~~~~~~~

For other database formats, create a custom mapping JSON in the ``emdb/`` or ``pyarchinit/`` directories. The s3Dgraphy mapping system (``MappingRegistry``) supports:

- **xlsx** — Excel files with custom column layouts
- **sqlite** — SQLite databases with custom table schemas

Custom mapping directories can be added with priority-based search, allowing project-specific mappings to override built-in ones. See the s3Dgraphy mapping documentation for details on creating custom mappings.
