Creating an Extended Matrix from Different Sources
==================================================

The Extended Matrix (EM) can be created through several pathways, each suited to different project needs and workflows. This guide covers all supported methods, from manual GraphML editing to AI-assisted extraction from archaeological reports.

.. contents::
   :local:
   :depth: 2

Overview
--------

Three main approaches are available for creating an Extended Matrix:

1. **From GraphML** — Manual creation using graph editors like yEd
2. **From Excel** — Structured tabular input using standardized templates
3. **AI-Assisted Extraction** — Using AI models to extract stratigraphy from PDF reports, field notes, and images

The Excel and AI approaches use a **two-file workflow**:

- **stratigraphy.xlsx** (core) — Contains stratigraphic nodes, relationships, chronologies, and paradata. This file generates the GraphML.
- **site_properties.xlsx** (auxiliary) — Contains site-specific properties (definitions, materials, techniques, etc.). This file is imported as an auxiliary to enrich the graph nodes.

.. figure:: img/workflow_two_excel.png
   :width: 600
   :align: center

   The two-Excel workflow: core stratigraphy generates the GraphML, site properties enrich it as auxiliary data.


From GraphML (yEd)
-------------------

The traditional method for creating an EM is to use the `yEd Graph Editor <https://www.yworks.com/products/yed>`_ to manually build the GraphML file. This approach gives full control over the graph structure and is well-suited for:

- Small to medium stratigraphic sequences
- Projects where the stratigrapher directly builds the graph
- Fine-tuning and validation of automatically generated graphs

For details on the GraphML structure and node types, see :doc:`EMstructure`.


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


Import into EMtools
~~~~~~~~~~~~~~~~~~~

1. Prepare your ``stratigraphy.xlsx`` file following the template
2. Use s3Dgraphy's ``MappedXLSXImporter`` with the mapping ``excel_to_graphml_mapping`` to generate a GraphML file
3. Import the GraphML into EMtools via **File > Import EM file**


From Excel (Site Properties — Auxiliary)
-----------------------------------------

The second Excel file contains site-specific properties that enrich the graph nodes with detailed attributes. This file is imported as an **auxiliary file** in EMtools using the auxiliary file system.

Template Download
~~~~~~~~~~~~~~~~~

- **template_site_properties.xlsx** — Empty template with 15 common property columns

The template uses a sheet named **"Properties"** with data starting from row 2.

Column Reference
~~~~~~~~~~~~~~~~

.. list-table:: Site Properties Columns (15)
   :header-rows: 1
   :widths: 5 15 75

   * - Col
     - Header
     - Description
   * - A
     - ID
     - Must match an existing node ID in the stratigraphy
   * - B
     - DEFINITION
     - Synthetic definition (e.g., Wall, Floor, Fill, Cut)
   * - C
     - INTERPRETATION
     - Functional interpretation in archaeological context
   * - D
     - BUILDING_TECHNIQUE
     - Construction technique (e.g., opus reticulatum, dry stone)
   * - E
     - INORGANIC_COMPONENTS
     - Inorganic materials (stone, mortar, brick, etc.)
   * - F
     - ORGANIC_COMPONENTS
     - Organic materials (wood, bone, charcoal, etc.)
   * - G
     - MEASURES
     - Dimensions (free format or LxWxH)
   * - H
     - MATERIAL
     - Primary material
   * - I
     - COLOR
     - Color (Munsell or descriptive)
   * - J
     - CONSERVATION_STATE
     - State of conservation
   * - K
     - SITE
     - Archaeological site name
   * - L
     - AREA
     - Excavation area/sector/room
   * - M
     - SOURCE_PDF
     - Source PDF filename
   * - N
     - SOURCE_PAGE
     - Page number in source PDF
   * - O
     - NOTES
     - Additional notes

Customizing Columns
~~~~~~~~~~~~~~~~~~~

This template is a starting point. Projects with specialized needs can add or remove columns. For example, the Montebelluna metallurgical project added columns like ``METALLURGICAL_EVIDENCE``, ``SLAG_IDS``, and ``ROOM_OR_FUNCTIONAL_UNIT``.

When customizing columns, create a corresponding mapping JSON following the format in ``s3dgraphy/mappings/emdb/site_properties_mapping.json``.

Import as Auxiliary File
~~~~~~~~~~~~~~~~~~~~~~~~

1. Import your GraphML into EMtools
2. In the EM Setup panel, add an auxiliary file
3. Select file type **EMdb Excel**
4. Choose the mapping **site_properties_mapping**
5. Select your ``site_properties.xlsx`` file
6. Click **Import** — properties are added to matching nodes

.. tip::
   Enable **Auto-reload on EM update** to automatically re-import the auxiliary file whenever the GraphML is reloaded.


AI-Assisted Extraction
-----------------------

AI models (Claude, ChatGPT, Gemini, etc.) can extract stratigraphic data directly from archaeological reports, field notes, and even images. This dramatically accelerates the creation of an Extended Matrix from existing documentation.

The Prompt
~~~~~~~~~~

A ready-to-use, two-part prompt is available in the s3Dgraphy repository:

``s3Dgraphy/docs/AI_EXTRACTION_PROMPT.md``

- **Part A** extracts core stratigraphy (24 columns) into a table compatible with ``stratigraphy.xlsx``
- **Part B** extracts site properties (15+ columns) into a table compatible with ``site_properties.xlsx``

Workflow
~~~~~~~~

1. Open your AI assistant (Claude, ChatGPT, etc.)
2. Paste the **Part A prompt** from ``AI_EXTRACTION_PROMPT.md``
3. Upload or paste the archaeological document
4. Copy the AI's output table into ``stratigraphy.xlsx``
5. Paste the **Part B prompt**
6. Copy the second table into ``site_properties.xlsx``
7. Import into EMtools following the steps above

Working with Existing GraphML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When enriching an existing GraphML with new document data, add this instruction to the prompt::

   I already have a GraphML with the following units: [list IDs].
   Match extracted units to existing ones where possible.
   Mark new units that are not in the current graph.

This was successfully used in the Montebelluna project, where AI-extracted data from multiple PDF reports was integrated with a pre-existing (but incomplete) GraphML, resulting in a significantly enriched stratigraphic sequence.

Best Practices
~~~~~~~~~~~~~~

- Process documents one at a time for accuracy
- Review AI output before importing — check relationship symmetry and type assignments
- Use the EXTRACTOR column to track which AI model produced each row
- For large projects, build incrementally: start with a core set of units, then add from additional documents


From Existing Databases
------------------------

EMtools supports import from archaeological database systems via s3Dgraphy's mapping system.

pyArchInit
~~~~~~~~~~

`pyArchInit <https://pyarchinit.readthedocs.io/>`_ databases (SQLite format) can be imported using the ``pyarchinit`` mapping type. The mapping file ``pyarchinit_us_mapping.json`` handles the translation from pyArchInit's table schema to s3Dgraphy nodes.

To import:

1. Add the SQLite database as an auxiliary file in EMtools
2. Select file type **pyArchInit**
3. Choose the appropriate mapping
4. Click **Import**

Custom Database Formats
~~~~~~~~~~~~~~~~~~~~~~~

For other database formats, create a custom mapping JSON in the ``emdb/`` or ``pyarchinit/`` directories. The s3Dgraphy mapping system supports:

- **xlsx** — Excel files with custom column layouts
- **sqlite** — SQLite databases with custom table schemas

See the s3Dgraphy mapping documentation for details on creating custom mappings.
