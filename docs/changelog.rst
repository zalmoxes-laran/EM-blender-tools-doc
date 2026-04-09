Changelog
=========

Version History
---------------

This page contains the detailed changelog for all EM Tools releases. For the latest changes, see the `CHANGELOG.md <https://github.com/zalmoxes-laran/EM-blender-tools/blob/main/CHANGELOG.md>`_ file.

Unreleased (in development)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
