.. _Proxy_Box_Creator:

Proxy Box Creator
=================

The Proxy Box Creator is a measurement-based tool for generating proxy geometry from 3D reference points. It uses a 7-point recording system to define the dimensions and orientation of a proxy box.

The panel is located in the **EM Annotator** tab.

.. note::
   The paradata enrichment mode (which allows linking source documents to each measurement point) is only available when **Experimental Features** are enabled in Advanced EM mode.

Panel Layout
------------

**Status Box**:

Displays progress counters with status icons (checkmark when complete, error when incomplete):

- Points recorded: X/7
- Documents assigned: X/7 (only in paradata mode)
- Extractors calculated: X/7 (only in paradata mode)

**Create Proxy Button**:

A prominent button that becomes enabled only when all requirements are met. If prerequisites are missing, the button label indicates what is needed (e.g., ``Record All Points First``, ``Assign Documents First``).

**Clear All Points** button: resets the entire workflow.

Settings (Sub-panel)
--------------------

- ``Proxy Name`` text field
- ``Pivot Location`` dropdown: controls the pivot point placement
- ``Use Proxy Collection`` toggle: places the generated proxy in the Proxy collection
- ``Activate paradata enrichment`` checkbox (experimental): enables document assignment and extractor calculation for each point

Workflow (Sub-panel)
--------------------

Instructions are displayed based on the active mode.

**Geometry Only Mode** (paradata enrichment OFF):

1. Position the 3D cursor on the reference model
2. Click the ``Record`` button next to the point
3. Repeat for all 7 points
4. Click ``Create Proxy``

**Paradata-Enriched Mode** (paradata enrichment ON):

1. Position the 3D cursor on the reference model
2. Click the search button to pick a source document
3. Click the ``Record`` button
4. Click the refresh button to calculate the extractor ID
5. Repeat for all 7 points
6. Click ``Create Proxy``

Points (Sub-panel)
------------------

Shows 7 recording boxes, one per measurement point:

.. list-table::
   :widths: 10 40 50
   :header-rows: 1

   * - #
     - Point
     - Purpose
   * - 1
     - Alignment Start
     - Defines the beginning of the main axis
   * - 2
     - Alignment End
     - Defines the end of the main axis
   * - 3
     - Thickness
     - Defines the perpendicular width
   * - 4
     - Quota Min
     - Defines the minimum height
   * - 5
     - Quota Max
     - Defines the maximum height
   * - 6
     - Length Start
     - Defines the start of the axis extent
   * - 7
     - Length End
     - Defines the end of the axis extent

Each point box shows:

- Point label with status icon (checkmark if recorded)
- Coordinates display: ``(x, y, z)`` or ``(not recorded)``
- ``Record`` button: captures the current 3D cursor position

In paradata mode, each box also shows:

- **Document field**: assigned document name with a search button and a copy-down button (copies the document to all remaining points)
- **Extractor field**: auto-calculated extractor ID with a refresh button (only active after a document is assigned)
