.. _CronoFilter:

CronoFilter
===========

The CronoFilter panel manages custom chronological horizons (time periods) that can be used for temporal filtering and exported with Heriverse context data. The panel appears in the **EM** tab when **Landscape mode** is active.

Panel Layout
------------

**Header**:

- Label: ``Chronological Horizons``

**Operations**:

- ``Auto from Epochs`` button: automatically generates horizons from the epoch data of all loaded graphs
- ``Save`` button: exports horizons to a ``.cf.json`` file
- ``Load`` button: imports horizons from a previously saved ``.cf.json`` file

**Horizons List**:

Each row in the list displays:

- **Enabled checkbox**: toggle whether the horizon is included in exports
- **Color swatch**: click to change the horizon color
- **Label**: editable name of the horizon
- **Time range**: ``start_time - end_time`` displayed on the right

List controls on the right side:

- ``+`` button: add a new empty horizon
- ``-`` button: remove the selected horizon
- Up/Down arrows: reorder horizons in the list

**Edit Selected Horizon** (when an item is selected):

- ``Label`` text field
- ``Start Time`` and ``End Time`` integer fields (negative values for BC dates)
- ``Color`` picker and ``Enabled`` checkbox

**Status**:

- Shows the count of enabled horizons vs total: ``Status: N/M horizons enabled``

Workflow
--------

**Auto-generating horizons from epochs:**

1. Load one or more GraphML files in Landscape mode (each may contain EpochNodes with time boundaries)
2. Click ``Auto from Epochs``
3. The system collects all epoch time boundaries, creates breakpoints, and generates a horizon for each interval
4. Each horizon is assigned a label and color from the best-matching epoch
5. Edit labels, colors, and time boundaries as needed

**Manually creating horizons:**

1. Click the ``+`` button to add a new horizon
2. Set the label, start time, end time, and color in the edit area
3. Toggle the enabled checkbox to include or exclude the horizon

**Saving and loading:**

- Click ``Save`` to export all horizons to a ``.cf.json`` file
- Click ``Load`` to import horizons from a file, replacing the current list
- The file format stores version, type, and all horizon data (label, start, end, color as hex, enabled status)
