.. badge:: Full Course
   :color: blue
.. badge:: Developer Track
   :color: orange

Bulk Import via the Excel Mapping Tool
======================================

.. raw:: html

   <!-- Replace VIDEO_ID with the actual YouTube video ID for 16_em_mapping_tool -->
   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
   <iframe src="https://www.youtube.com/embed/VIDEO_ID_16_em_mapping_tool"
           style="position:absolute;top:0;left:0;width:100%;height:100%;"
           frameborder="0" allowfullscreen></iframe>
   </div>
   <p><em>▶ Bulk Import via the Excel Mapping Tool (~~4 min)</em></p>

| **Clip:** 16  |  **Duration:** ~4 min  |  **Recording segment:** ~1:20:30 → 1:24:55

----

Prerequisites
-------------

:doc:`15-pyarchinit-external-data`

Overview
--------

Import thousands of SUs from an Excel spreadsheet using a JSON mapping file. The mapping file defines which Excel column maps to which EM property (human ID, material qualia, epoch, etc.). Demonstrated with the Basilica Iulia dataset: 2,039 SUs and 1,088 properties imported in seconds.

.. figure:: /_static/screenshots/clip_16/0001_basilica_iulia_2039_sus.jpg
   :alt: Basilica Iulia dataset overview: 2,039 stratigraphic units.
   :width: 90%

   Basilica Iulia dataset overview: 2,039 stratigraphic units.

Key Concepts
------------

- The mapping file is JSON: version, sheet name, start row, and column-to-property mappings.
- Any Excel column can map to: human ID, epoch, node type, or a qualia property.
- The import creates nodes, connects them, and assigns all mapped qualia automatically.
- After import, the Visual Manager can filter by any mapped property (e.g., material type).

Screenshots
-----------

.. figure:: /_static/screenshots/clip_16/0003_json_mapping_file.jpg
   :alt: The JSON mapping file: version, sheet, start row, column definitions.
   :width: 90%

   The JSON mapping file: version, sheet, start row, column definitions.

.. figure:: /_static/screenshots/clip_16/0004_column_mapping_detail.jpg
   :alt: Column mapping: Excel column → EM property (human ID, material qualia).
   :width: 90%

   Column mapping: Excel column → EM property (human ID, material qualia).

.. figure:: /_static/screenshots/clip_16/0005_import_result_1088_props.jpg
   :alt: Import result: 1,088 properties created in the graph.
   :width: 90%

   Import result: 1,088 properties created in the graph.

.. figure:: /_static/screenshots/clip_16/0006_visual_manager_material_filter.jpg
   :alt: Visual Manager filtering by material type after import.
   :width: 90%

   Visual Manager filtering by material type after import.

Try It Yourself
---------------

Create a mapping file for a 10-row sample spreadsheet and import it into a new EM.

.. note::

   A video walkthrough for this tutorial will be available on the Extended Matrix YouTube channel.

.. seealso::

   :doc:`EM Nodes: Stratigraphic Units and Paradata <em-doc:learn-em/tutorials/08-nodes-paradata-qualia>`

