.. _link-photos-aux:

Linking Photos as Auxiliary Files
=================================

A frequent enrichment task is attaching **field photos** to the
stratigraphic units they document — without redrawing the graph in
yEd. EMtools supports this through the **Auxiliary files**
sub-panel of the EM Data Tree: a spreadsheet listing one row per
unit, with a column carrying the photo path (or filename), is
imported via a JSON mapping. The result is a set of graph nodes
whose ``photo_path`` (or equivalent) property points at the file on
disk, viewable through the existing thumbnail and document
machinery.

For the conceptual background of auxiliary files (what they are,
why they are tabular, and how the JSON mapping is structured) see
:ref:`aux-files-concept` and :ref:`aux-json-mapping`.

Learning objectives
-------------------

By the end you will be able to:

- prepare a spreadsheet listing photos per US;
- write a minimal JSON mapping that binds the ``photo_path``
  column to a graph property;
- import the spreadsheet as an auxiliary file and verify the
  attachment in the Visual Manager.

Prerequisites
-------------

- A loaded ``.graphml`` graph in EMtools (any version 1.5).
- A photo folder reachable via a **relative path** from the
  ``.blend`` file (see :doc:`/panels/em_setup` — *Setting Up
  Resource Folders*).
- A spreadsheet (``.xlsx``) with one row per US and at least the
  columns: unit ID and photo filename (or relative path).

Step 1 — Prepare the spreadsheet
--------------------------------

Use a simple layout, one US per row. Minimal columns:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Column A
     - Column B
     - Column C
   * - ``human_id``
     - ``photo_path``
     - ``caption``
   * - US001
     - photos/US001_north.jpg
     - North face after cleaning
   * - US002
     - photos/US002_section_a.jpg
     - East–west section A

Keep paths relative to the resource folder (no
``C:\\Users\\...`` or absolute ``/Users/...`` entries).

.. TODO: screenshot — the spreadsheet open in Excel/LibreOffice with the three columns visible and a couple of rows filled.

Step 2 — Write the JSON mapping
-------------------------------

Save the following next to the spreadsheet as
``photos_mapping.json``:

.. code-block:: json

   {
     "version": "1.0",
     "sheet_name": "Photos",
     "start_row": 2,
     "id_column": "A",
     "mappings": [
       {"column": "A", "target": "human_id",   "type": "identifier"},
       {"column": "B", "target": "photo_path", "type": "document_link"},
       {"column": "C", "target": "caption",    "type": "qualia"}
     ]
   }

Adjust ``sheet_name`` to match the tab name in your ``.xlsx``.
``start_row: 2`` skips the header row.

.. TODO: screenshot — JSON file open in a text editor with syntax highlighting, alongside the column letters visible in the spreadsheet for cross-reference.

Step 3 — Add the auxiliary file in EMtools
------------------------------------------

In the EM Data Tree panel:

1. expand the ``Auxiliary files`` section and press ``Add``;
2. choose **EMdb Excel** as the type (the JSON-driven importer);
3. select the spreadsheet from disk;
4. when the ``Format`` menu appears, point it at
   ``photos_mapping.json``;
5. press ``Accept``, then run **Import**.

.. TODO: screenshot — EM Data Tree panel with Auxiliary files expanded, the new entry visible with type EMdb Excel and the mapping file path filled in.

Step 4 — Verify the attachment
------------------------------

After import:

- open the **Stratigraphy Manager** and select a unit that was
  listed in the spreadsheet; the new property (``photo_path``,
  ``caption``) should appear in its property list;
- if the resource folder has thumbnails generated
  (:doc:`/panels/em_setup` — *Generating Thumbnails*), the photo
  preview is reachable from the Visual Manager and from the
  Document Manager;
- check the Blender console for any rows that did not match an
  existing US — these are reported with the offending ``human_id``
  and indicate a typo in the spreadsheet or a missing node in the
  graph.

.. TODO: screenshot — Stratigraphy Manager (or Visual Manager) showing the selected US with the freshly imported photo_path property and the preview thumbnail.

.. seealso::

   - :ref:`aux-files-concept` — what auxiliary files are and how
     they relate to the graph.
   - :ref:`aux-json-mapping` — the JSON mapping schema in
     detail.
   - :doc:`16-mapping-tool-excel` — bulk import with a JSON
     mapping on a larger dataset.
   - :doc:`15-pyarchinit-external-data` — the live-database
     variant of the same idea.
