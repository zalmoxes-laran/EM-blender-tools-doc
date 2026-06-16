Installation
============

EM Tools is a Blender extension. The recommended install path is the
**drag-and-drop card** on the Extended Matrix website, which sets up
the EM Blender repository for you and installs the extension in one
gesture. This page also covers the offline / manual path for users
on restricted networks, the development setup, and the yEd palette
note (since the palette is part of the EM language toolchain, not of
this manual).

.. contents::
   :local:
   :depth: 1


Quick install (recommended)
---------------------------

Open the install card at
`extendedmatrix.org/tools/em-tools <https://www.extendedmatrix.org/tools/em-tools/#install>`__.
The card picks the right build for your OS and Blender version, and
exposes a drag-and-drop handle:

1. **Drag the handle into the Blender window**. The first drop adds
   the *Extended Matrix* repository to Blender's Extensions list.
2. **Drop a second time**. EM Tools installs from the repository.
3. **Tick the checkbox** next to *EM Tools* in the Extensions panel
   to enable it. The EM Tools panels appear in the 3D Viewport
   sidebar.

Future EM Tools releases arrive as automatic updates from the
repository — no further action needed.


System requirements
-------------------

- **Blender** 4.4 LTS or later.
- **OS**: Windows (x64), macOS (Apple Silicon / arm64), macOS (Intel
  x64, Blender 4.4 / 4.5 only — Blender 5.x dropped Intel binaries),
  Linux (x64).
- 4 GB RAM (8 GB recommended), 500 MB free disk for the extension
  and its bundled wheels.

The extension installs all Python dependencies automatically.


Offline / manual install
------------------------

For restricted networks, mirrored installations, or if you prefer to
pin a specific build:

1. Visit the
   `GitHub Releases page <https://github.com/zalmoxes-laran/EM-blender-tools/releases>`_
   and download the ``.zip`` matching your Blender version and OS.
   Different ``.zip`` builds exist per OS × Blender ABI; the
   filename encodes the combination (for example
   ``em_tools-v1.5.3-macosx-arm64-blender51.zip`` for Blender 5.1 on
   Apple Silicon).
2. In Blender, open ``Edit → Preferences → Get Extensions → Install
   from Disk…`` and select the downloaded ``.zip``.
3. Tick the box next to *EM Tools* to enable it.

The extension installs Python dependencies automatically; no manual
``pip install`` is needed.


Updating EM Tools
-----------------

* **Quick install path**: Blender follows the *Extended Matrix*
  repository for you; updates arrive automatically on Blender's
  next ``Check for Updates`` cycle (configurable under ``Get
  Extensions → ⚙ → Online``).
* **Offline / manual path**: download the new ``.zip``, uninstall
  the previous version in Blender's Extensions panel, restart
  Blender, and re-install from disk.


Importing the EM palette in yEd
-------------------------------

The yEd palette is part of the **EM language** toolchain, not of EM
Tools. The canonical walkthrough lives in the EM language manual:

* `Setting up the yEd palette
  <https://docs.extendedmatrix.org/en/1.5/mini_tutorials/setup_yed_palette.html>`__
  — concept page, palette download link, and step-by-step yEd
  ``Edit → Manage Palette → Import Section…`` walkthrough.

The palette is required only when you author or edit an EM graph in
yEd. EM Tools itself reads any standard EM ``.graphml`` regardless of
whether the authoring used yEd, the unified ``em_data.xlsx`` flow, or
AI-assisted generation via StratiMiner.


Development setup
-----------------

Contributors and developers should follow :doc:`development_setup`
instead — it covers the dev-venv setup, the wheel pipeline used by
``em.sh``, and the s3dgraphy editable-install pattern for working
against the in-development library.

