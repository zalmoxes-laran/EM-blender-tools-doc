Welcome to the EM Tools Documentation
=====================================

**EM Tools** is a Blender extension that creates a connection between the Extended Matrix (``.graphml`` file) and the 3D environment of Blender (proxy files). With EM Tools you can import, manage, visualize, modify, represent and export all the information (geometries, data and paradata) concerning micro and macro scale contexts, single objects or collections of objects.

The extension is developed by E. Demetrescu at CNR-ISPC (Rome, former CNR-ITABC).

.. admonition:: First time here?
   :class: tip

   If this is your very first contact with the Extended Matrix project, the recommended landing page is `extendedmatrix.org <https://www.extendedmatrix.org>`__ — it explains *what* EM is, *who* it is for, and *which* of the manuals you should open next. The page you are reading now is the **EM Tools manual**: the practical guide to the Blender add-on. The complementary `language manual <https://docs.extendedmatrix.org>`__ is where the formal notation is defined.

.. figure:: img/EM_workflow_blender.svg
   :width: 100%
   :align: center

   *EM Tools at a glance: the five moments your work will move through, from importing the graph and the 3D content to exporting a publishable reconstruction. The panels in the addon follow this order.*

EM, EM Tools, 3DSC: who is who
------------------------------

A new user often meets three names at once. The distinction matters because each one solves a different problem:

.. list-table::
   :header-rows: 1
   :widths: 22 38 40

   * - Name
     - What it is
     - Where to learn it
   * - **Extended Matrix (EM)**
     - The *formal language* used to document stratigraphy and reconstruction processes. Drawn in yEd or produced from ``em_data.xlsx``.
     - `extendedmatrix.org docs <https://docs.extendedmatrix.org>`_
   * - **EM Tools**
     - The *Blender add-on* that connects an EM graph to 3D content (this manual).
     - You are here.
   * - **3DSC**
     - A complementary Blender environment for high-quality 3D survey processing that can feed EM Tools.
     - `3D-survey-collection docs <https://docs.extendedmatrix.org/projects/3D-survey-collection>`_
   * - **Heriverse**
     - The *Heritage Science Metaverse* — web-based publication and collaborative VR for EM-aware scenes. The natural endpoint of what you author here.
     - `Heriverse docs <https://docs.extendedmatrix.org/projects/heriverse/en/latest/>`__

If you are unsure which one you need: start from EM (the language) if you have *evidence to organize*; come to EM Tools if you have *3D content to annotate*; reach for 3DSC if you have *raw survey data to clean and align*; open Heriverse when your work is *ready to be published on the web*.

Start here
----------

Pick the entry that fits you best. Each path is short and ends back at the panels reference.

.. admonition:: I work with sources, stratigraphy and reconstruction logic
   :class: tip

   Begin with the formal language at `the EM language docs <https://docs.extendedmatrix.org>`__, then come back here for :doc:`installation`, the :doc:`tutorials/12-install-yed-blender` walkthrough, and the :doc:`tutorials/13-first-matrix-creation` exercise. The :doc:`panels/stratigraphy_manager` is where most of your work will happen.

.. admonition:: I build and texture 3D models and want to enrich them with EM data
   :class: tip

   Go straight to :doc:`installation`, then follow :doc:`tutorials/12-install-yed-blender` and :doc:`tutorials/13-first-matrix-creation`. From there, :doc:`panels/em_setup`, :doc:`panels/proxy_box_creator` and :doc:`panels/visual_manager` cover the daily authoring loop. Export options are in :doc:`export_guide`.

.. admonition:: I want to extend EM Tools, integrate it, or contribute code
   :class: tip

   Read :doc:`development_setup` and :doc:`api_reference`, then :doc:`contributing` for the workflow. The s3Dgraphy library — bundled inside the addon — is what you will most often touch; its source lives in the `EM-blender-tools repo <https://github.com/zalmoxes-laran/EM-blender-tools>`_.

.. note::
   Starting from version 1.5, EM Tools is distributed as a Blender Extension (``.zip`` file)
   which automatically manages all Python dependencies.

Quick Start
-----------

- **For users** — download the latest release and install via Blender's preferences. See :doc:`installation`.
- **For developers** — clone the repository and follow :doc:`development_setup`.
- **Community** — join the `Telegram group <https://t.me/UserGroupEM>`_ for support and discussions.

What's New
----------

**Version 1.5 (development snapshot — building toward 1.5.0 stable)**
   - **Landscape mode**: manage multiple archaeological graphs simultaneously in a single Blender scene
   - **CronoFilter**: chronological horizons manager for landscape mode with horizon-based filtering and coloring
   - **Stratigraphy Manager**: complete rewrite (formerly US/USV Manager) with containment filters, instance chain tracking, and associated documents
   - **Anastylosis Manager (RMSF)**: link 3D objects to SpecialFind nodes with LOD management
   - **3D Document Manager**: spatial-temporal document management with camera and image plane support
   - **Graph Editor**: node-based graph visualization in the Node Editor
   - **Proxy Box Creator**: 7-point measurement tool with optional paradata enrichment
   - **Conservation Workflow / TSU**: Transformation Stratigraphic Units for documenting decay, restoration and thematic surveys (see :doc:`panels/conservation_workflow`)
   - **Tapestry Integration**: AI-powered photorealistic reconstruction (experimental)
   - Blender Extension format with automatic dependency management
   - Heriverse export functionality
   - See full :doc:`changelog` for details

**Development tracking**
   - Visit `dev.extendedmatrix.org <https://dev.extendedmatrix.org/dev-projects>`_ for progress and feature requests
   - See the :doc:`roadmap` for future plans

.. admonition:: Documentation status
   :class: important

   This documentation describes EM Tools **1.5 (development snapshot)** and is rebuilt continuously
   from the ``main`` branch. The downloadable PDF carries the same release string on its cover
   (``Extended Matrix tool 1.5.0-dev``). If you land on a page whose header says ``1.4`` you are
   reading the previous stable release; switch the version selector at the bottom-left of the page
   to the version you actually need. Issues and suggestions: please open them on
   `GitHub issues <https://github.com/zalmoxes-laran/EM-blender-tools/issues>`__.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   usage_examples

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   panels/index
   workflows
   creating_em
   export_guide

.. toctree::
   :maxdepth: 2
   :caption: Developer Guide

   api_reference
   contributing
   development_setup

.. toctree::
   :maxdepth: 2
   :caption: Project Information

   roadmap
   changelog
   license

.. toctree::
   :maxdepth: 1
   :caption: Community

   support
   faq
   showcase

.. toctree::
   :maxdepth: 2
   :caption: Tutorials

   tutorials/index

Additional Resources
--------------------

- **GitHub Repository**: `EM-blender-tools <https://github.com/zalmoxes-laran/EM-blender-tools>`_
- **Extended Matrix website**: `extendedmatrix.org <https://www.extendedmatrix.org>`_
- **EM language docs**: `docs.extendedmatrix.org <https://docs.extendedmatrix.org>`_
- **3DSC docs**: `3D-survey-collection <https://docs.extendedmatrix.org/projects/3D-survey-collection>`_
- **Heriverse docs**: `Heritage Science Metaverse <https://docs.extendedmatrix.org/projects/heriverse/en/latest/>`__
- **ATON Framework**: `phoenixbf/aton on GitHub <https://github.com/phoenixbf/aton>`__
- **Video tutorials**: `YouTube Channel <https://www.youtube.com/extendedmatrix>`_

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :hidden:

   EMstructure
