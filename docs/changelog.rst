Changelog
=========

Version History
---------------

This page contains the detailed changelog for all EM Tools releases. For the latest changes, see the `CHANGELOG.md <https://github.com/zalmoxes-laran/EM-blender-tools/blob/main/CHANGELOG.md>`_ file.

Unreleased (in development)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added — US creation workflow unification (2026-04)**
   - **Unified "Add Stratigraphic Unit" dialog** (``strat.add_us``):
     single floating form used by the Stratigraphy Manager (new
     ``+ Add US`` button under the list), the Proxy Box Creator
     (``+`` next to the Active US picker), and Surface Areas (``+``
     next to the Existing US picker). Fields: Type, Name + gap-aware
     suggest-next, Description, Shared-numbering toggle (default
     ON), Epoch (mandatory, drives the Activity filter), Activity
     (optional, writes ``is_in_activity``), optional stratigraphic
     link. OK optionally saves the graphml and pins the new unit
     as active.
   - **``us_helpers.create_us_node(...)`` factory**: one entry point
     for US creation; writes ``has_first_epoch``, optional
     ``is_in_activity`` (mirrored on the PD nodegroup when created),
     optional stratigraphic relation, and populates the Stratigraphy
     Manager list in one pass.
   - **``us_types.py`` facade**: JSON-driven US type registry
     derived from s3Dgraphy's datamodel v1.5.2 (patch) and its classification
     API (``is_real / is_virtual / is_series`` + ``US_PROPER_TYPES``
     / ``ALL_US_TYPES``).
   - **Activity picker filtered by epoch**:
     ``scene.activity_manager.filtered_activities`` +
     ``ACTIVITY_OT_filter_by_epoch`` + ``draw_activity_picker``
     widget. Shows only activities matching the US's epoch; inline
     refresh icon re-runs the filter.
   - **ParadataNodeGroup per US** (``<US>_PD``): Proxy Box Creator
     wraps every new paradata chain (Document instance clone →
     Extractors → Combiner → PropertyNode) inside a per-US
     container. Inherits ``is_in_activity`` from the US so both sit
     in the same yEd group.
   - **Document instance cloning**: Proxy Box Creator duplicates
     the Step-1 anchor Document into a fresh instance per run so
     extractors never attach to a Document already in another PD
     group.
   - **Chain summary box** in the Proxy Box Creator (collapsible).
   - **Save-after-create toggle** (``persist_after_create``, default
     ON) on both the Add-US dialog and the Proxy Box Creator.
   - **Custom Add-US icon** (``proxies_rows_add``) — visually
     distinct from the dialog-internal ``+`` suggest-next.
   - **Next-number gap-aware from 1**: fills the first unused
     number starting at 1 (was scanning only ``[min(used),
     max(used)]``).
   - **Shared-pool numbering**: counts trailing digits across every
     US type; ``SU001`` ≡ ``US.1`` in the pool. Opt-in via a toggle
     in the dialog; default ON.
   - **Legacy prefix aliases**: Italian ``SU…`` treated as alias
     of English ``US…`` (and ``USNEG`` / ``US_NEG`` as alias of
     ``USN``).
   - **Negative Stratigraphic Unit (USN)**: new canonical type in
     every US picker (dashed border in yEd). Replaces the ad-hoc
     ``US_NEG`` UI placeholder.

**Changed — US creation workflow unification (2026-04)**
   - US creation consolidated to one form; the inline
     ``create_new_us`` toggles in Proxy Box Creator and Surface
     Areas are gone.
   - Proxy Box Creator edge direction/types corrected:
     extractors → Document is ``extracted_from`` (dashed) instead
     of non-canonical ``has_extractor`` (solid); Combiner →
     Extractors is ``combines`` instead of ``is_combined_in``.
   - Proxy Box Creator PropertyNode named after the canonical qualia
     ("Proxy Geometry", ``property_type="proxy_geometry"``, new
     entry in ``em_qualia_types_additions.json``).
   - Centralised hardcoded US-type lists across 10 files (15
     occurrences); three were incomplete — fixed incidentally.

**Removed — US creation workflow unification (2026-04)**
   - ``PROXYBOX_OT_suggest_next_us``, ``EMTOOLS_OT_suggest_next_us``
     operators.
   - Inline ``create_new_us`` branch fields on ``ProxyBoxSettings``
     and ``SurfaceArealeSettings``.
   - ``GENERIC`` placeholder from the Surface Areas US type picker.

**Fixed — US creation workflow unification (2026-04)**
   - Paradata chain edges rendered as solid lines (canonical edge
     types now used — ``extracted_from`` / ``combines`` /
     ``has_data_provenance`` / ``has_property``).
   - Extractor / Combiner NodeLabel positioned as Corner-NorthWest;
     previously ``modelName=Internal, modelPosition=Center``.
   - ParadataNodeGroup positioning anchored to the host US's epoch
     Y (was (0,0) outside any swimlane row); children nested in
     the PD's ``<graph>``.
   - ActivityNodeGroup containment: children with
     ``is_in_activity`` nested inside the Activity's ``<graph>``.
   - Document instance collisions: Proxy Box Creator resolves the
     Step-1 anchor by UUID and clones it locally instead of
     sharing with other PD groups.
   - Activity filter silent-fail: the epoch-change update callback
     used ``bpy.ops.activity.filter_by_epoch`` which Blender
     rejects silently inside update callbacks. Direct populator
     call now.
   - "Add-US dialog not on operator stack" warning when clicking
     the ``+ next number`` button — resolved via shared scene-level
     sentinel.

**Added**
   - **Landscape mode (multi-graph)**: manage 2+ archaeological graphs simultaneously in a single Blender scene
   - **CronoFilter**: chronological horizons manager for landscape mode
   - **Horizon-based filtering**: Stratigraphy Manager filters nodes by temporal overlap with CronoFilter horizons
   - **Horizon-based coloring**: Visual Manager "Horizons" display mode applies CronoFilter colors to 3D proxies
   - **RM visibility sync with horizons**: Representation Models shown/hidden based on epoch overlap with active horizon
   - **Graph badges in Stratigraphy list**: colored icons differentiate nodes from different graphs
   - **Active graph indicator**: Anastylosis Manager and RM Manager show active graph code
   - **Landscape-aware graph reload**: reloading GraphML in landscape mode correctly repopulates lists
   - **Proxy detection in landscape**: uses ``GRAPH_CODE.NODE_NAME`` naming convention (e.g., ``GT16.USM100``)
   - Support for detecting placeholder dates (XX) in epochs
   - Warnings for incomplete or malformed GraphML files in EM Data Tree
   - Flag system for experimental features
   - Improved UI synchronization controls in the Paradata Manager panel

**Changed**
   - Epoch Manager becomes "Horizons" label in Visual Manager when in landscape mode
   - Stratigraphy Manager filter shows "By Horizon" with horizon name in landscape mode
   - CronoFilter simplified: removed filter/reset buttons, now purely a chronology/horizon editor
   - Renamed panel from "US/USV Manager" to "Stratigraphy Manager"
   - Improved robustness of the GraphML import system
   - Reorganized the Stratigraphy Manager panel
   - Separated filter and synchronization controls in the Stratigraphy Manager

**Removed**
   - EMviq exporter from the main UI (moved to experimental features)
   - Proxy inflation tool from the main UI (moved to experimental features)
   - 3D GIS mode from 1.5.0 (moved to 1.6.0)
   - Soloing functionality, toggle reconstruction, and toggle selectable from the Epoch Manager

**Fixed**
   - ``RuntimeError: Object cannot be hidden`` wrapped in try/except
   - ``IndexError`` when disabling horizon filter with stale list index
   - GraphML import bug with "XX" date format
   - Memory Error during UI updates
   - Infinite UI update loops in the Paradata Manager

v1.5.0-dev.71 (2025-01-20)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added**
   - Conversion from Blender add-on to Blender Extension
   - Automatic dependency management via wheels
   - GitHub Actions workflow for automated releases
   - Heriverse export functionality with texture optimization
   - GPU instancing support for improved performance
   - Advanced export options (Draco compression, separate textures)
   - Export of ParaData objects (Documents, Extractors, Combiners)
   - Special Finds model export capability
   - Development scripts for contributors

**Changed**
   - Configuration migrated to ``blender_manifest.toml`` format
   - Simplified installation process
   - Minimum Blender version updated to 4.0
   - Updated Python dependencies (pandas 2.x, numpy 1.26.x)

**Removed**
   - Manual dependency installation UI
   - Legacy external modules installer

**Fixed**
   - Compatibility issues with Blender 4.x series
   - Dependency conflicts with system Python installations
   - Export errors with large archaeological datasets

v1.4.0 (2024-05-20)
^^^^^^^^^^^^^^^^^^^

**Added**
   - XLSX import for stratigraphic data
   - Batch export capabilities
   - Volume calculation tools

**Changed**
   - Improved performance of GraphML parser
   - Better memory handling for large projects
   - Updated CIDOC-CRM mapping

**Fixed**
   - Synchronization issues in period manager
   - Label creation in orthographic views
   - Visibility toggle for proxy models

v1.3.2 (2024-02-15)
^^^^^^^^^^^^^^^^^^^

**Fixed**
   - Critical bug in epoch handling
   - GraphML import for complex hierarchies
   - Memory leak in paradata streaming

v1.3.1 (2024-01-10)
^^^^^^^^^^^^^^^^^^^

**Added**
   - Paradata streaming mode
   - Real-time graph synchronization
   - Improved error reporting

**Changed**
   - Optimized 3D view updates
   - Improved collection management

v1.3.0 (2023-11-30)
^^^^^^^^^^^^^^^^^^^

**Added**
   - EMviq web export functionality
   - ATON framework integration
   - Reconstruction uncertainty visualization
   - Multi-graph support (experimental)

**Changed**
   - Redesigned export manager interface
   - Improved period visualization system

v1.2.0 (2023-07-15)
^^^^^^^^^^^^^^^^^^^

**Added**
   - Support for negative stratigraphic units
   - DosCo folder integration
   - Custom material system for Epochs
   - Soloing mode for epochs

**Changed**
   - Visual manager refactored
   - Updated for Blender 3.6 support

v1.1.0 (2023-03-20)
^^^^^^^^^^^^^^^^^^^

**Added**
   - Basic GraphML import/export
   - US/USV manager
   - Period manager
   - Basic visualization tools

v1.0.0 (2022-12-01)
^^^^^^^^^^^^^^^^^^^

**Added**
   - Initial release
   - Core Extended Matrix functionality
   - Basic 3D visualization
   - Simple export capabilities

Semantic Versioning
-------------------

EM Tools follows `Semantic Versioning <https://semver.org/>`_:

- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality (backwards compatible)
- **PATCH** version for backwards compatible bug fixes

Version Support
---------------

.. list-table:: Version Support Matrix
   :widths: 20 30 30 20
   :header-rows: 1

   * - EM Tools Version
     - Blender Versions
     - Python Version
     - Support Status
   * - 1.5.x (dev)
     - 4.4+
     - 3.13
     - Active Development
   * - 1.4.x
     - 3.6 - 4.1
     - 3.10 - 3.11
     - Maintenance
   * - 1.3.x
     - 3.3 - 3.6
     - 3.10
     - End of Life
   * - 1.2.x
     - 3.0 - 3.3
     - 3.9
     - End of Life
