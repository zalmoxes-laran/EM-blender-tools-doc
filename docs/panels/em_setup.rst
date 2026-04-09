.. _EMsetup:

EM Data Tree
============

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


In this panel (:numref:`Fig. %s <EMsetup_02FIG>`) users can also link the path to the *DosCo* folder, where sources are stored.
To locate sources, users must follow the same guidelines previously outlined for the localization of the EM file.

If the EM graph presents a connection with and external database, EMTools allows to import databases to maintain data connection also within Blender.

To establish the connection with EMtools:

- expand the ``Auxiliary files`` section and press ``Add``;
- select the type (Generic Excel, PyArchInit, EMdb Excel);
- indicate the exact location of the Auxiliary file and click on the ``Accept`` button.

.. note::
   When **EMdb Excel** type is selected a ``Format`` menu appears, select the correct format from the list.

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

A third section, the ``Utilities & Settings`` one, is included within the EM Data Tree panel.
Here, users can: convert an EM made with an old version of the formalism, rename Proxies and enable Experimental Features.

In the first case EMtools will automatically convert US and USV nodes to the latest version of the formalism (**NB**: this function will not affect groups).

Within this section, EMtools includes also a button, ``Create Standard Collections``, that allows to automatically create the set of default collections (Proxy, RM, CAMS) related to a reconstruction process with Extended Matrix.

In the second case, by pressing ``Manage Proxies' Prefixes`` button, EMtools will automatically rename Proxies according to the GraphML ID (**NB**: this step is mandatory to mutually connect GraphML and Proxies. User must select geometries before applying the tool).

In the third case, by pressing the ``Enable Experimental Features`` button, a set of Experimental Features will be activated within the sections of the EM Data Tree panel (:numref:`Fig. %s <EMsetup_03_editFIG>`).

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

     The panel also provides **template download** buttons and an **AI Extraction Prompt** section with a language selector and a one-click **Copy AI Prompt to Clipboard** button. See :doc:`../creating_em` for the full workflow.

     **Warning**: This feature is experimental. Always verify the generated GraphML before using it in production.

.. _EMsetup_04abcFIG:

.. figure:: ../img/EMsetup_04abc.jpg
   :width: 400
   :align: center

   3D GIS mode
