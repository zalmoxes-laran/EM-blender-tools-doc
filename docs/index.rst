Welcome to the EM Tools Documentation
=====================================

**EM Tools** is a Blender extension that creates a connection between the Extended Matrix (.graphml file) and the 3D environment of Blender (proxy files). With EM Tools users can import, manage, visualize, modify, represent and export all the information (geometries, data and paradata) concerning micro and macro scale contexts, single objects or collection of objects.

The extension has been developed by E. Demetrescu at CNR-ISPC (Rome, former CNR-ITABC).

.. note::
   Starting from version 1.5, EM Tools is distributed as a Blender Extension (.zip file) 
   which automatically manages all Python dependencies.

Quick Start
-----------

- **For Users**: Download the latest release and install via Blender's preferences
- **For Developers**: Clone the repository and follow the development setup guide
- **Community**: Join our `Telegram group <https://t.me/UserGroupEM>`_ for support and discussions

For detailed instructions, see the :doc:`installation` section.

What's New
----------

**Version 1.5.0** (in development)
   - **Landscape mode**: manage multiple archaeological graphs simultaneously in a single Blender scene
   - **CronoFilter**: chronological horizons manager for landscape mode with horizon-based filtering and coloring
   - **Stratigraphy Manager**: complete rewrite (formerly US/USV Manager) with containment filters, instance chain tracking, and associated documents
   - **Anastylosis Manager (RMSF)**: link 3D objects to SpecialFind nodes with LOD management
   - **3D Document Manager**: spatial-temporal document management with camera and image plane support
   - **Graph Editor**: node-based graph visualization in the Node Editor
   - **Proxy Box Creator**: 7-point measurement tool with optional paradata enrichment
   - **Tapestry Integration**: AI-powered photorealistic reconstruction (experimental)
   - Blender Extension format with automatic dependency management
   - Heriverse export functionality
   - See full :doc:`changelog` for details

**Development Tracking**
   - Visit `dev.extendedmatrix.org <https://dev.extendedmatrix.org/dev-projects>`_ for progress and feature requests
   - See our :doc:`roadmap` for future plans

.. admonition:: Documentation Status

   This documentation is continuously updated. If you find any issues or have suggestions, 
   please contribute via `GitHub <https://github.com/zalmoxes-laran/EM-blender-tools>`_.

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
   export_guide

.. Experimental / non-stable long-form pages. Built but hidden from nav
   so the addon can still deep-link to them.

.. toctree::
   :hidden:

   creating_em

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
- **Extended Matrix Website**: `extendedmatrix.org <https://www.extendedmatrix.org>`_
- **ATON Framework**: `GitHub <https://github.com/phoenixbf/aton>`_
- **Video Tutorials**: `YouTube Channel <https://www.youtube.com/extendedmatrix>`_

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :hidden:

   EMstructure

