.. _export_manager:

.. _Export_Manager:

Export Manager
==============

.. _EM_Export_ManagerFIG:

.. figure:: ../img/EM_Export_Manager.png
   :width: 400
   :align: center

   Export Manager panel

The **Export Manager** lives in the *EM Bridge* tab of the 3D Viewport
sidebar and groups every exporter EM Tools ships with into a single
panel. Each exporter is rendered as a collapsible sub-section with its
own help-button pointing to its dedicated documentation page.

This page documents the **Tabular Export** section only. For the
Heriverse publishing pipeline see :doc:`heriverse_export`.

.. _tabular-export:

Tabular Export
--------------

The Tabular Export section dumps the Extended Matrix graph(s) into
plain tabular files for downstream analysis, archival, or ingestion in
external tools (spreadsheets, statistical software, databases).

Two output formats are available:

- **em_data.xlsx** — the 5-sheet canonical workbook containing the
  stratigraphic units (US/USV), Sources, Extractors, and the relational
  tables that link them together. This is the recommended deliverable
  when the goal is to hand over the graph as a self-contained
  spreadsheet.
- **CSV** — a flat dump of individual node groups (US/USV, Sources,
  Extractors). Useful when only one slice of the graph is needed, or
  when integrating with a CSV-only pipeline.

To use the section:

1. Pick the desired table format with the radio toggle
   (``table_type``).
2. Press the ``EM (csv)`` button to export the active graph in the
   chosen format.

The output files are saved next to the current ``.blend`` file unless
a custom path is configured upstream.

.. seealso::

   :doc:`heriverse_export` — for publishing the reconstruction to the
   Heriverse platform (proxies, RM, RB, animations, paradata).
