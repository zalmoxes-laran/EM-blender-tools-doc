Installation and Development
============================

This section covers both user installation and developer setup for EM Tools.

User Installation
-----------------

System Requirements
^^^^^^^^^^^^^^^^^^^

* Blender 4.4 or later
* Operating System: Windows (x64), macOS (ARM / Apple Silicon), macOS (Intel x64), Linux (x64)
* At least 4GB RAM (8GB recommended)
* 500MB free disk space

.. note::
   macOS Intel (x64) is supported up to Blender 4.5 (the last version available for Intel Macs).
   From Blender 5.0 onwards, only macOS ARM (Apple Silicon) is supported.

.. important::
   Different ``.zip`` release files are available for different combinations of **Blender version** and **operating system**.
   Make sure to download the correct file for your setup. For example:

   - ``em_tools-v1.5.0-dev.140-blender5.1-windows-x64.zip`` for Blender 5.1 on Windows
   - ``em_tools-v1.5.0-dev.140-blender5.0-macos-arm64.zip`` for Blender 5.0 on macOS Apple Silicon
   - ``em_tools-v1.5.0-dev.140-blender4.5-macos-x64.zip`` for Blender 4.5 on macOS Intel

   Release files with ``-dev.`` in the name are development builds. Stable releases (when available) will not have the ``-dev`` suffix.

Installing from Extension Package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The recommended way to install EM Tools is through the official Blender extension system:

1. **Download the Extension**

   - Visit the `GitHub Releases page <https://github.com/zalmoxes-laran/EM-blender-tools/releases>`_
   - Download the ``.zip`` file matching your Blender version and operating system

2. **Install in Blender**

   - Open Blender
   - Navigate to ``Edit → Preferences... → Get Extensions``
   - Click the ``Install from Disk...`` button
   - Browse to the downloaded ``.zip`` file and select it
   - Press the ``Install from Disk`` button
   - The extension will be installed automatically

3. **Enable the Extension**

   - Find *EM Tools* in the add-ons list
   - Check the box next to it to enable
   - The EM Tools panels will automatically appear in the 3D Viewport sidebar

.. note::
   The extension automatically installs all required Python dependencies.
   No manual dependency installation is needed.

Updating EM Tools
^^^^^^^^^^^^^^^^^

When a new version is available:

1. Uninstall the previous version of EM Tools from Blender (if installed)
2. Restart Blender to ensure all old files are cleared
3. Download the new ``.zip`` file from the `GitHub Releases page <https://github.com/zalmoxes-laran/EM-blender-tools/releases>`_ or the `Download section of the Extended Matrix web site <https://www.extendedmatrix.org/download>`_
4. Install it using the process previously described
5. Blender will automatically update the existing installation

Development Setup
-----------------

This section is for developers who want to contribute to EM Tools or modify it for their needs.

Prerequisites
^^^^^^^^^^^^^

* Blender 4.4 or later
* Python 3.13 (same version as Blender 4.4+)
* Git
* Visual Studio Code (recommended)
* Blender Development extension for VSCode

Setting Up the Development Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Clone the Repository**

   .. code-block:: bash

      git clone https://github.com/zalmoxes-laran/EM-blender-tools.git
      cd EM-blender-tools

2. **Install Development Dependencies**

   Run the setup script to download all required Python wheels:

   .. code-block:: bash

      python scripts/setup_development.py

   This script will:

   - Create a ``wheels`` directory
   - Download all required dependencies for your platform
   - Ensure compatibility with Blender's Python version

3. **Configure for Development**

   Switch to development mode:

   .. code-block:: bash

      python scripts/switch_dev_mode.py dev

   This creates a simplified manifest file optimized for VSCode development.

4. **Open in Visual Studio Code**

   .. code-block:: bash

      code .

5. **Configure VSCode**

   Ensure your ``.vscode/settings.json`` contains:

   .. code-block:: json

      {
          "blender.addon.sourceDirectory": ".",
          "blender.addon.reloadOnSave": true,
          "blender.executable": "/path/to/blender"
      }

6. **Start Development**

   - Press ``Cmd+Shift+P`` (Mac) or ``Ctrl+Shift+P`` (Windows/Linux)
   - Run ``Blender: Start``
   - The addon will load with hot reload enabled

Development Workflow
^^^^^^^^^^^^^^^^^^^^

Daily Development
"""""""""""""""""

1. Make your code changes
2. Save files - the addon will automatically reload in Blender
3. Test your changes in the running Blender instance

.. note::
   You may see "already registered" warnings during hot reload.
   These are normal and can be ignored.

Creating a Release
""""""""""""""""""

1. **Switch to Production Mode**

   .. code-block:: bash

      python scripts/switch_dev_mode.py prod

2. **Update Version**

   - Update version in ``blender_manifest.toml``
   - Update version in ``__init__.py`` (bl_info)

3. **Create Git Tag**

   .. code-block:: bash

      git tag v1.5.0
      git push origin v1.5.0

4. **Automatic Build**

   GitHub Actions will automatically:

   - Download wheels for all platforms
   - Create ``.zip`` packages for each Blender version and platform
   - Create a GitHub release

Project Structure
^^^^^^^^^^^^^^^^^

.. code-block:: text

   EM-blender-tools/
   ├── __init__.py              # Main addon entry point
   ├── blender_manifest.toml    # Extension manifest
   ├── wheels/                  # Dependencies (git-ignored)
   ├── scripts/                 # Development utilities
   │   ├── setup_development.py
   │   ├── switch_dev_mode.py
   │   └── requirements_wheels.txt
   ├── s3Dgraphy/              # Core library
   ├── import_operators/       # Import functionality
   ├── export_operators/       # Export functionality
   └── docs/                   # Documentation

Important Files
^^^^^^^^^^^^^^^

``blender_manifest.toml``
"""""""""""""""""""""""""

The extension manifest file that defines:

- Metadata (name, version, author)
- Dependencies (Python wheels)
- Blender version requirements
- Platform compatibility

``requirements_wheels.txt``
"""""""""""""""""""""""""""

Lists all Python dependencies with specific versions:

.. code-block:: text

   pandas==2.2.3
   numpy==1.26.4
   networkx==3.4.2
   ...

Development Scripts
^^^^^^^^^^^^^^^^^^^

``setup_development.py``
""""""""""""""""""""""""

Downloads all required Python wheels for your platform:

.. code-block:: bash

   python scripts/setup_development.py

``switch_dev_mode.py``
""""""""""""""""""""""

Switches between development and production configurations:

.. code-block:: bash

   # For development with VSCode
   python scripts/switch_dev_mode.py dev

   # For production builds
   python scripts/switch_dev_mode.py prod

Troubleshooting
^^^^^^^^^^^^^^^

Common Issues
"""""""""""""

**Import Errors**
   - Ensure all wheels are downloaded: ``python scripts/setup_development.py``
   - Check that you're using Python 3.13
   - Verify Blender is version 4.4 or later

**VSCode Development Issues**
   - Make sure you're in development mode: ``python scripts/switch_dev_mode.py dev``
   - Check VSCode settings point to correct Blender executable
   - Try restarting VSCode and Blender

**Manifest Errors**
   - Development mode uses a simplified manifest
   - Production builds require the full manifest with wheel declarations

Getting Help
""""""""""""

- Join the `Telegram community <https://t.me/UserGroupEM>`_
- Open an issue on `GitHub <https://github.com/zalmoxes-laran/EM-blender-tools/issues>`_
- Email: emanuel.demetrescu@cnr.it
