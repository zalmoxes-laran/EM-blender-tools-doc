.. _Proxy_to_RM_Projection:

RM Coloring (Proxy to RM Projection)
=====================================

The RM Coloring system transfers proxy material colors onto Representation Model (RM) objects based on volumetric intersections. This allows visualizing which stratigraphic units contribute to the composition of each RM object.

.. warning::
   This is an **experimental feature**. It requires:

   - Advanced EM mode enabled
   - Experimental Features enabled in :ref:`EMsetup`
   - RM temporal sync active (in the :ref:`Visual_Manager`)

The controls appear as a collapsible sub-panel within the :ref:`Visual_Manager`.

Controls
--------

**When projection is inactive**:

- ``Apply Projection`` button (large, green): calculates vertex intersections and applies colors
- Prerequisites status: shows whether all requirements are met, or lists missing prerequisites (e.g., no active epoch selected, no proxy objects, no RM objects)

**When projection is active**:

- ``Clear Projection`` button: removes all coloring and restores original materials
- ``Update`` button: re-applies the projection with current settings (useful after changing epoch or proxy colors)
- ``Toggle`` button: toggles the projection visibility on and off

**Projection Settings**:

- ``Auto Update`` toggle: automatically updates the projection when proxy colors change
- ``Method`` dropdown: ``Vertex Paint`` or ``Node Shader`` (two different approaches for applying the colors)
- ``Strength`` slider (0.0 - 1.0): blends between original materials and projected colors
- ``Hide Non-Intersected Areas`` toggle: makes non-intersected parts of the RM transparent

**Advanced Settings** (collapsible):

- ``Precision`` slider: controls ray-casting accuracy (higher values are slower but more accurate)
- ``Max Distance``: maximum ray distance for intersection detection
- ``Batch Size``: number of vertices processed at once (affects memory vs speed)
- ``Override Linked Materials`` toggle: allows modifying materials on linked RM objects

**Debug Tools** (experimental only):

- ``Run Diagnosis`` button: validates the system status and displays a diagnostic report

Workflow
--------

1. Ensure the prerequisites are met: RM sync is active, an epoch is selected, proxies and RM objects are present
2. Click ``Apply Projection`` to calculate intersections and apply colors
3. Adjust the ``Strength`` slider to control the blend between original and projected colors
4. Toggle ``Hide Non-Intersected Areas`` to focus on the intersected regions
5. When the epoch or proxy colors change, click ``Update`` (or enable ``Auto Update``)
6. Click ``Clear Projection`` to restore the original materials
