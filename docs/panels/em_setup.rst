.. _EMsetup:

EM Data Tree
============

.. seealso::

   In the Extended Matrix language manual:

   - `Extended Matrix — language manual <https://docs.extendedmatrix.org/en/1.5/index.html>`_
     — overview of the formal notation feeding the ``.graphml`` files loaded here.
   - `EM workspace preparation <https://docs.extendedmatrix.org/en/1.5/em_workspace_preparation.html>`_
     — DosCo folder layout and iteration pattern.

.. _EMsetupFIG:

.. figure:: ../img/EMsetup.png
   :width: 400
   :align: center

   EM Data Tree Panel

This panel (:numref:`Fig. %s <EMsetupFIG>`)  allows to create the first connection between Blender and the Extended Matrix (.graphml file).
Press the ``Add GraphML`` and locate the ``.graphml`` file wiin the ``Path`` section (**NB**: before closing the path window remember to uncheck ``relative path`` within the settings.
Alternatively, it is possible to paste the entire path within the empty line).


.. _EMsetup_02FIG:

.. figure:: ../img/EMsetup_02.png
   :width: 400
   :align: center

   GraphML import

When a GraphML is loaded (:numref:`Fig. %s <EMsetup_02FIG>`), on the left side of the EM Data Tree window the GraphML ID will appear (for example, the ID: GT16).
On the same line, on the right side, a green square will show up.
The green color cofirms that a connection between the GraphML and EMtools has been established.

.. note::

   To correctly link the ``.graphml`` file with the ``EM Data Tree`` panel it is mandaotry to insert, at least, the GraphML ID on the title of the ``Swimlane node`` (**1.5 dev4 palette**); the first node that needs to be imported in the yEd space to start the creation of an Extended Matrix (:numref:`Fig. %s <EM_TITLEFIG>`).

   Example:

   Context name [ID:xx;ORCID:xx;LICENSE:CC-BY-ND]

   Great Temple [ID:GT16;LICENSE:CC-BY-ND]

   .. _EM_TITLEFIG:

   .. figure:: ../img/EM_TITLE.png
      :width: 400
      :align: center

      EM graphml file title example





Next to the green (or red) square, three buttons complete the right side of the line (:numref:`Fig. %s <EMsetup_02FIG>`): the ``Update`` button allows to refresh the ``.graphml`` file, if changes have been applied on the EM graph during the modelling session; the ``Activate EM`` button consent to explore only the selected GraphML; and the ``pubblish`` button appears when the multigraph mode is enabled.

This version of EMtools allows to activate the ``Multigraph Mode``, this option consent to upload and visualize multiple graphs.
To upload a new graph and explore its information user can follow all the steps already explained.

.. note::

  This version of EMtools include **info boxes**.
  When the info button is selected an info box will appears with more information related to that specific part of the tool.


   .. _EM_info_buttonFIG:

   .. figure:: ../img/EM_info_button.png
      :width: 400
      :align: center

      Example of EM info box


Once the connection has been established, EMTools will summarize the most important information (US/USV; Epochs; Properties; Sources) within a simple table under the ``Path`` section (:numref:`Fig. %s <EMsetup_02FIG>`).

The ``Remove GraphML`` button allows to remove one or more EMs from the EM Data Tree list.


.. _em-tools-aux-load:

.. note::

   **Loading DosCo documents into the graph**

   The panel commands described below load documents from your DosCo
   folder into the EM graph as nodes. The link between the file on
   disk and the graph node is preserved; if you re-iterate your
   DosCo (add new entries, update existing ones), reload from this
   panel to surface the changes. For the DosCo concept, folder layout
   and iteration pattern, see `Iterating the DosCo
   <https://docs.extendedmatrix.org/en/1.5/em_workspace_preparation.html#enrich-dosco-iterative>`_
   in the Extended Matrix language manual.

In this panel (:numref:`Fig. %s <EMsetup_02FIG>`) users can also link the path to the *DosCo* folder, where sources are stored.
To locate sources, users must follow the same guidelines previously outlined for the localization of the EM file.

If the EM graph presents a connection with and external database, EMTools allows to import databases to maintain data connection also within Blender.

To establish the connection with EMtools:

- expand the ``Auxiliary files`` section and press ``Add``;
- select the type (Generic Excel, PyArchInit, EMdb Excel);
- indicate the exact location of the Auxiliary file and click on the ``Accept`` button.

.. note::
   When **EMdb Excel** type is selected a ``Format`` menu appears, select the correct format from the list.

.. _aux-files-concept:

Auxiliary files — concept
~~~~~~~~~~~~~~~~~~~~~~~~~

Auxiliary files are **not** part of the EM graph's core structure.
The graph (``.graphml``) defines stratigraphy, proxies, sources and
their logical relations; auxiliary files provide *additional,
tabular* information that EMtools attaches to existing graph nodes
at import time. They live outside the graph and can be re-imported,
re-mapped or detached without altering the topology of the
reconstruction.

The three currently supported auxiliary types behave the same way
conceptually but differ in their source format:

- **Generic Excel** — any ``.xlsx`` with a header row; mapping is
  defined by the user.
- **pyArchInit** — a pyArchInit SQLite database; mapping is
  pre-configured for the pyArchInit US table (see
  :doc:`/tutorials/15-pyarchinit-external-data`).
- **EMdb Excel** — a tabular database structured according to the
  *EMdb* conventions; mapping is driven by a **JSON mapping file**
  (see :ref:`aux-json-mapping` below).

.. important::

   Auxiliary files in this sense (tabular data attached at import
   time via a mapping) must not be confused with **auxiliary
   stratigraphic nodes** in the EM language — *Continuity* and
   related node types that belong to the formal notation. The
   former is a *data plumbing* feature of EMtools; the latter is a
   *modelling primitive* of the language. See the EM language
   manual for the latter.

Typical use cases:

- enrich existing US/USV nodes with material qualia, dating
  ranges, excavator notes that live in a separate spreadsheet;
- link photo paths and metadata to stratigraphic units without
  redrawing the graph in yEd
  (see :ref:`link-photos-aux` for the step-by-step procedure);
- merge field-database records (pyArchInit) into an already
  authored graph.

.. _aux-json-mapping:

JSON mapping template
~~~~~~~~~~~~~~~~~~~~~

For the **EMdb Excel** (and **Generic Excel**) auxiliary types,
EMtools consumes a JSON mapping file that declares how each column
of the spreadsheet should be projected onto graph properties.
A minimal mapping has the following shape:

.. code-block:: json

   {
     "version": "1.0",
     "sheet_name": "Stratigraphy",
     "start_row": 2,
     "id_column": "A",
     "mappings": [
       {"column": "A", "target": "human_id",      "type": "identifier"},
       {"column": "B", "target": "node_type",     "type": "node_type"},
       {"column": "C", "target": "epoch",         "type": "epoch"},
       {"column": "D", "target": "material",      "type": "qualia"},
       {"column": "E", "target": "photo_path",    "type": "document_link"}
     ]
   }

Each row of the spreadsheet (from ``start_row`` onward) is matched
against an existing graph node via ``id_column``. For each entry
in ``mappings``, EMtools writes the value of the indicated column
onto the target property of the matched node (or creates the
property if absent). Supported ``type`` values mirror the kinds of
data the EM language recognises (``identifier``, ``node_type``,
``epoch``, ``qualia``, ``document_link``, …); the exact list
depends on the importer in use and is documented alongside the
operator in :doc:`/api_reference`.

.. todo::

   Ship a canonical ``emdb_mapping.template.json`` next to the
   addon and reference it here once finalised. Until then the
   shape above is the reference; live working examples can be
   inspected in the *Basilica Iulia* dataset used by
   :doc:`/tutorials/16-mapping-tool-excel`.

.. seealso::

   - :doc:`/tutorials/16-mapping-tool-excel` — bulk import via the
     JSON mapping tool, end-to-end on a 2 000+ row dataset.
   - :doc:`/tutorials/15-pyarchinit-external-data` — pyArchInit as
     auxiliary file (live link to the field database).
   - :ref:`link-photos-aux` — link photos as auxiliary files.

Starting from version 1.5, EMtools allows to link external resource folders containing photos, 3D scans, documents and other media files to your Extended Matrix project.
This feature is particularly useful when working with large image collections that need to be referenced and previewed directly from within Blender.


Setting Up Resource Folders
----------------------------

To link a resource folder to your Extended Matrix:

1. Expand the ``Auxiliary files`` section in the EM Data Tree panel

2. Select an existing auxiliary file or press ``Add`` to create a new one

3. In the ``Resources:`` field, click the folder icon and navigate to your media folder

4. **Important**: Before confirming the path, make sure to check the ``Relative Path`` option in the file browser settings


.. warning::

   Always use **relative paths** when setting up resource folders!

   - Correct: ``//Resources`` or ``//../../SharedFolder/Photos``
   - Wrong: ``C:\Users\YourName\Project\Resources`` (Windows-specific)
   - Wrong: ``/Users/yourname/Project/Resources`` (macOS-specific)

   Relative paths ensure that your project works correctly when:

   - Opening the file on different computers
   - Syncing through cloud services (OneDrive, Dropbox, Google Drive)
   - Sharing the project with collaborators
   - Moving the project to a different location


If a warning appears in red indicating that the path is absolute, reconfigure the path using the relative format.

The Thumbnail System
---------------------

Once a resource folder is configured, EMtools can automatically generate thumbnail previews of all images in that folder.
The thumbnail system creates a local cache that speeds up image browsing and reduces memory usage.

**How it works:**

- Thumbnails are stored in a folder named ``EM_thumbs/`` next to your ``.blend`` file
- Each resource folder gets its own subfolder (e.g., ``Resources_abc12345``)
- The system remembers which images have been processed to avoid duplicates
- If you sync your project via cloud storage, thumbnails are automatically shared across computers


Generating Thumbnails
----------------------

1. In the Auxiliary Files panel, locate the text ``Thumbnails for the resource folder? Click below.``

2. Click the ``(Re)generate thumbnails`` button

3. EMtools will scan all images in the resource folder (including subfolders) and create previews

4. Progress information is displayed in the Blender console

5. The line ``Thumbs: Resources_xxxxxxxx`` shows the name of the cache folder that was created


.. note::

   Supported image formats: JPG, PNG, BMP, TIFF, PDF (first page)

   The generation process only creates thumbnails for new or modified images.
   If you click ``(Re)generate`` again, existing thumbnails are skipped automatically.


Viewing Thumbnail Cache
-------------------------

You can verify that thumbnails were created correctly:

- The ``Thumbs: Resources_xxxxxxxx`` line displays the cache folder name
- Click the folder icon next to this line to open the cache folder in your file manager
- Inside you'll find the ``index.json`` file and thumbnail images organized in subfolders


Using Thumbnails in EMtools
-----------------------------

Once thumbnails are generated, they are automatically displayed when:

- Browsing DocumentNodes linked to images
- Using the US/USV Manager to view associated documentation
- Working with the Stratigraphy visualization tools

The thumbnail preview provides quick access to your images without having to open them in external applications.


Working Across Multiple Computers
-----------------------------------

If you use cloud storage to sync your project:

1. **First computer**: Set up resource folders using relative paths and generate thumbnails

2. Wait for cloud sync to complete (the ``EM_thumbs/`` folder will be uploaded)

3. **Second computer**: Open the same ``.blend`` file

4. Thumbnails are automatically recognized and ready to use - no need to regenerate them!


.. tip::

   If you work on multiple computers, make sure that:

   - The ``.blend`` file and resource folders maintain the same relative structure
   - Cloud sync is complete before opening the project
   - You always use the ``//`` prefix for relative paths


Best Practices
----------------

- **Keep resources organized**: Use clear folder names like ``Photos``, ``3DScans``, ``Documents``
- **Generate thumbnails periodically**: After adding many new images, regenerate to update the cache
- **Check the hash**: The ``Thumbs: Resources_xxxxxxxx`` code should be identical on all your computers if using relative paths
- **Backup regularly**: Include both the ``.blend`` file and the ``EM_thumbs/`` folder in your backups


.. note::

   For more advanced usage and technical details about the thumbnail system, click the help icon (?) next to the ``Thumbs:`` line in the interface.


Troubleshooting
-----------------

**Thumbnails not appearing**
   - Verify that the resource folder path is correct and accessible
   - Click ``(Re)generate thumbnails`` to rebuild the cache
   - Check the Blender console for error messages

**Warning about absolute path**
   - Reconfigure the resource folder using a relative path with ``//`` prefix
   - Example: change ``C:\Project\Resources`` to ``//Resources``

**Different cache folder on another computer**
   - This happens when using absolute paths instead of relative paths
   - Solution: reconfigure all resource folders using relative paths
   - The hash (``Thumbs: Resources_xxxxxxxx``) should match across computers

**Thumbnails folder not syncing**
   - Check that your cloud storage service is actively syncing the ``EM_thumbs/`` folder
   - Some cloud services may need manual folder selection for sync

Utils sub-panel
---------------

A third section, the ``Utils`` sub-panel (labelled *Utilities & Settings*
in older builds), is included within the EM Data Tree panel.
Here, users can: convert an EM made with an old version of the formalism,
create the default collections, rename Proxies and enable Experimental
Features.

In the first case (``Convert 1.x->1.5`` button) EMtools will normalise
older GraphML files authored with the 1.x palette to the 1.5 visual
conventions — see :ref:`convert-legacy-em-graph` below for details.

Within this section, EMtools includes also a button, ``Create Standard Collections``, that allows to automatically create the set of default collections (Proxy, RM, CAMS) related to a reconstruction process with Extended Matrix.

By pressing ``Manage Proxies' Prefixes`` button, EMtools will automatically rename Proxies according to the GraphML ID (**NB**: this step is mandatory to mutually connect GraphML and Proxies. User must select geometries before applying the tool).

By pressing the ``Enable Experimental Features`` button, a set of Experimental Features will be activated within the sections of the EM Data Tree panel (:numref:`Fig. %s <EMsetup_03_editFIG>`).

.. _convert-legacy-em-graph:

Convert 1.x->1.5
~~~~~~~~~~~~~~~~

The ``Convert 1.x->1.5`` button in the EM Data Tree → **Utils**
sub-panel migrates older Extended Matrix GraphML files (authored
with the 1.x generation of the yEd palette) to the **1.5** visual
conventions used by the current importer and tooling.

What it does
^^^^^^^^^^^^

The button drives the ``graphml.convert_borders`` operator, which
reads a ``.graphml`` file and rewrites its node visual attributes
in-place on a new file:

- Sets the **border width** to ``4.0`` for the EM target shapes
  (rectangle, hexagon, ellipse, octagon, parallelogram).
- Applies the **1.5 canonical border colours** based on shape type
  and background:

  - rectangle → ``#9B3333`` (US / negative units)
  - hexagon → ``#31792D`` (USV)
  - ellipse → ``#31792D`` (USV variants)
  - parallelogram → ``#248FE7`` (documents / extractors)
  - octagon → ``#D8BD30`` (Special Find) when on a light background,
    ``#B19F61`` (Virtual Special Find) when on a black background.

The result is written next to the original file with a
``_converted.graphml`` suffix; the source file is left untouched.

How to use
^^^^^^^^^^

1. Expand the ``Utils`` sub-panel in the EM Data Tree.
2. Click ``Convert 1.x->1.5`` — Blender's file browser opens.
3. Select the legacy ``.graphml`` file and confirm. EMtools
   produces ``<name>_converted.graphml`` in the same folder and
   reports the output path in the Blender status bar.
4. Load the converted file with ``Add GraphML`` as you would any
   other graph (see the *Loading DosCo documents into the graph*
   note above for the load workflow).

What it does NOT do
^^^^^^^^^^^^^^^^^^^

The operator is a **visual / palette normaliser**, not a full
datamodel migration. In particular:

- It does not invent or upgrade paradata. If the older graph lacked
  ``family`` / ``is_series`` attributes on extractors and combiners,
  the converted file reflects the same absence.
- It does not rename relation edges whose semantics changed between
  releases (e.g. ``is_after`` direction canonicalisation introduced
  in v1.5.3). Such edges are preserved as-is and may surface as
  importer warnings.
- It does not re-link external documents. DosCo references in the
  original are preserved as identifiers; ensure the corresponding
  files are reachable in your DosCo folder.
- For projects authored **before EM 1.0** (pre-formalisation,
  free-form yEd), conversion is not reliable: the original is best
  used as a visual reference for manually rebuilding the graph in
  the current palette.

For the missing pieces above, the importer side picks up some of
the slack: ``s3dgraphy.importer.import_graphml`` is forgiving on
older label conventions and re-maps known legacy types on the fly
during import, and the post-import passes in ``s3dgraphy.transforms``
(``hoist_propagative_metadata``, ``prune_redundant_propagative_edges``,
``compact_propagative_metadata``) can be used to normalise paradata
attribution programmatically.

Roadmap
^^^^^^^

A single, end-to-end ``s3dgraphy.utils.convert_legacy_em_graph``
wrapper that combines the palette-normalisation step performed by
this button with the in-memory cleanup transforms is on the
s3dgraphy roadmap. Until it lands, the procedure above (button →
load → optional transforms → re-export) is the recommended path.
The anchor for this section (``convert-legacy-em-graph``) is
stable and will continue to point here when the wrapper is
published.

.. _EMsetup_03_editFIG:

.. figure:: ../img/EMsetup_03_edit.png
   :width: 400
   :align: center

   Experimental Features enabled (red rectangles with numbers 1-3)



.. note::

   As highlighted in the red warning, this set of features is experimental and it should not be used within the regular documentation process of the EM (:numref:`Fig. %s <EMsetup_03_editFIG>`).



Here a brief presentation of the Experimental Features, the numebers on the list refer to the numbers specified in :numref:`Fig. %s <EMsetup_04abcFIG>`:

1. On the upper part of the panel the ``Switch to 3D GIS`` button allows to instantly switch from the ``EM mode`` to a ``3D GIS mode`` where users can link an external database to EMtools (:numref:`Fig. %s <EMsetup_04abcFIG>`). The activation of the ``3D GIS mode`` consents to connect an External database to the 3D environment of Blender via EMtools. User have three different type of external databases (*Generic Excel*, *PyArchInit*, *EMdb Excel*) to choose from. By pressing the corresponding button a diverse set of options will appear. After setting all the required information the external db will be import within EMtools.

2. Within the ``DosCo Folder`` section (:numref:`Fig. %s <EMsetup_03_editFIG>`) the ``More option`` menu appears, this new part of the add-on permits to populate Extractors, documents and Combiners using DosCo files.

3. In the ``Utilities & Settings`` (:numref:`Fig. %s <EMsetup_03_editFIG>`) the activation of the ``Enable Experimental Features`` button activates the ``Experimental Tools`` section with ``Rebuild Graph Indices``, ``Benchmark Property Functions``, and the collapsible **Create a GraphML** wizard.

   - **Create a GraphML**: A 3-step panel-based wizard for generating Extended Matrix GraphML files from Excel data — either filled manually using downloadable templates or produced by AI-assisted extraction from archaeological reports. The wizard works entirely in memory until export:

     - **Step 1 — Convert Stratigraphy**: Loads ``stratigraphy.xlsx`` (24-column template) and creates an s3dgraphy graph in memory.
     - **Step 2 — Enrich with Paradata** (optional): Loads ``em_paradata.xlsx`` and adds per-property provenance chains (PropertyNode → ExtractorNode → DocumentNode) to matching nodes.
     - **Step 3 — Export GraphML**: Saves the graph to a ``.graphml`` file. Import this file via **File > Import EM file** to populate the Blender scene.

     The panel also provides **template download** buttons and an **AI Extraction Prompt** section with a language selector and a one-click **Copy AI Prompt to Clipboard** button.

     **Warning**: This feature is experimental. Always verify the generated GraphML before using it in production.

.. _EMsetup_04abcFIG:

.. figure:: ../img/EMsetup_04abc.jpg
   :width: 400
   :align: center

   3D GIS mode


.. _graphml_warnings:

GraphML Warnings
----------------

When a GraphML file is imported, EMtools validates its structure and content. Any issues are surfaced in a collapsible **GraphML Warning** box below the graph entry.

Common warnings:

- **Missing site ID** — the swimlane header does not contain the mandatory ``ID:`` field (for example ``Great Temple [ID:GT16]``). Fix this in yEd before reloading.
- **Placeholder epoch dates** — an epoch still contains the ``xx`` placeholder in its start/end fields. Replace with real dates.
- **Structural issues** — malformed nodes, dangling edges, unknown node types reported by the importer. Each message indicates the offending node ID.

The warnings are read-only: they describe what the importer detected. To clear them, fix the ``.graphml`` file in yEd and reload with the ``File Refresh`` button in the EM Data Tree list. The ``Data Funnel guide`` button links to the Extended Matrix manual section with authoring best-practices.


.. _graphml_merge_conflict:

GraphML Merge Conflict Resolution
---------------------------------

When an XLSX stratigraphy file is merged into an already-loaded graph (for example, to incrementally add units discovered in a later season), the EM Setup panel performs a diff and surfaces **conflicts** — nodes where the incoming data and the existing graph disagree.

The **Conflict Resolution** panel appears in the EM tab while a merge is active. For each conflict the user can choose:

- **Keep Existing** — ignore the incoming value for this node.
- **Use Incoming** — overwrite the existing value.
- **Per-Field Choice** — accept some fields from the existing graph and others from the incoming XLSX, useful when only a subset of attributes has changed.

Epoch compatibility is verified before merge: if the XLSX references epochs that do not exist in the graph (or have incompatible ranges), a blocking **Epoch Report** is shown at the top of the panel. Fix the XLSX (or adjust graph epochs) and retry.

``Apply Merge`` commits the choices into the graph; ``Cancel Merge`` discards them.
