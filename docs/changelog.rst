Changelog
=========

Version History
---------------

This page contains the detailed changelog for all EM Tools releases. For the latest changes, see the `CHANGELOG.md <https://github.com/zalmoxes-laran/EM-blender-tools/blob/main/CHANGELOG.md>`_ file.

v1.5.0 (2025-01-15)
^^^^^^^^^^^^^^^^^^^

Major Release - Extension Format Migration

**Added**
   - Blender Extension format support
   - Automatic dependency management
   - GitHub Actions for automated releases
   - Heriverse export functionality
   - GPU instancing support
   - Development scripts for contributors

**Changed**
   - Configuration uses ``blender_manifest.toml``
   - Simplified installation process
   - Updated to Blender 4.0 minimum
   - Modernized Python dependencies

**Removed**
   - Manual dependency installation UI
   - Legacy external modules installer

**Fixed**
   - Blender 4.x compatibility issues
   - Python dependency conflicts
   - Large dataset export errors

v1.4.0 (2024-05-20)
^^^^^^^^^^^^^^^^^^^

Feature Release

**Added**
   - Time branch management
   - Property density visualization
   - XLSX import for stratigraphic data
   - Batch export capabilities
   - Volume calculation tools

**Changed**
   - Enhanced GraphML parser
   - Improved memory management
   - Updated CIDOC-CRM mapping

**Fixed**
   - Period manager synchronization
   - Label creation in orthographic views
   - Proxy model visibility

v1.3.2 (2024-02-15)
^^^^^^^^^^^^^^^^^^^

Patch Release

**Fixed**
   - Critical epoch management bug
   - GraphML import for hierarchies
   - Memory leak in paradata streaming

v1.3.1 (2024-01-10)
^^^^^^^^^^^^^^^^^^^

Patch Release

**Added**
   - Paradata streaming mode
   - Real-time synchronization
   - Enhanced error reporting

**Changed**
   - Optimized 3D view updates
   - Improved collection management

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
   * - 1.5.x
     - 4.0+
     - 3.11
     - Active
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

Migration Guides
----------------

Migrating from 1.4 to 1.5
^^^^^^^^^^^^^^^^^^^^^^^^^

The main change is the move to Blender Extension format:

1. **Uninstall old addon**::

      # Remove from Blender preferences
      Edit → Preferences → Add-ons → EM Tools → Remove

2. **Install new extension**::

      # Download .blext file
      # Install via: Edit → Preferences → Add-ons → Install from Disk

3. **Update scripts**: No API changes, scripts should work as-is

Migrating from 1.3 to 1.4
^^^^^^^^^^^^^^^^^^^^^^^^^

Key changes include new time branch APIs:

1. **Update time branch code**::

      # Old API
      graph.set_branch(branch_id)
      
      # New API
      graph.time_branches.activate(branch_id)

2. **Update property access**::

      # Old API
      node.properties['density']
      
      # New API
      node.get_property('density', namespace='em')