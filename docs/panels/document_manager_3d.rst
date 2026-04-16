.. _Document_Manager_3D:

.. _document_manager:

Document Manager
================

The Document Manager panel lists all document nodes from the loaded graph and lets you navigate between each document and its supporting data: metadata, scene objects linking to it (RM, :ref:`rmdoc_manager`, RMSF), and the graph nodes it documents.

The panel is located in the **EM Annotator** tab and is available in Advanced EM mode.

For the spatial-authoring workflow (linking 3D quads and cameras to document nodes) see the dedicated :ref:`rmdoc_manager` page.

Panel Layout
------------

**Sync Controls**:

- ``Sync from Graph`` button: synchronizes the document list from the loaded graph data
- Document counter: shows the total number of documents

**Summary Bar** (when documents exist):

- Masters count (key documents)
- Dated documents count
- Documents with 3D representation count

**Filter Row**:

- ``Show only masters`` toggle: filters to display only master documents
- ``Show only with 3D`` toggle: filters to documents that have a 3D representation

**Document List**:

Each row displays:

- **Certainty icon** (for master documents): color-coded by certainty level (red = direct, orange = reconstructed, yellow = hypothetical, gray = unknown)
- **Name**: with date if available for master documents
- **3D state icons**: mesh icon if it has a quad, camera icon (clickable) if it has a camera
- **Description**

**Detail Panel** (when a document is selected):

- Document name and badge (Master or Instance)
- Description (if available)
- Chronology section (for masters): start date and linked epoch
- Source type: Analytical (context-based) or Comparative (analogue-based)
- Completeness indicators: checkmarks for Description, Date, URL, 3D

**3D Representation Section** (collapsible):

- If no 3D representation exists:
  - ``Import Image`` button to create an image plane

- If a quad (image plane) exists:
  - Object name with dimensions (width x height in meters)
  - If no camera: ``Create Camera`` button
  - If camera exists: camera name, editable focal length slider, ``Look Through`` button
  - ``Select Quad`` and ``Open File`` utility buttons

**Settings** (collapsible):

- ``Zoom to Selected``: auto-zoom when selecting items
- ``Default Focal Length``: default value for new cameras
- ``Default Alpha``: default transparency for image planes

Workflow
--------

**Syncing documents from the graph:**

1. Click ``Sync from Graph`` to populate the document list from the EM graph
2. Use the filter toggles to narrow the view to masters or documents with 3D representations

**Creating a 3D representation for a document:**

1. Select a document in the list
2. In the 3D Representation section, click ``Import Image`` to create an image plane
3. Position the image plane in the 3D viewport
4. Click ``Create Camera`` to add a camera aligned with the document
5. Adjust the focal length using the slider
6. Click ``Look Through`` to preview the camera view

**Navigating documents:**

- Click on the camera icon in the list row to instantly look through the camera associated with that document
- Use ``Select Quad`` to select the image plane for manual adjustments


.. _spatialized_documents:

Spatialized Documents (RMDoc)
-----------------------------

The RMDoc panel manages scene objects (mesh quads) linked to document nodes for spatial authoring. Each entry binds a Blender object to a document node from the graph, optionally with a dedicated camera aligned to the source image.

Use cases:

- Georeferencing historical photos or drawings onto a 3D survey
- Authoring orthographic documentation views
- Navigating between document-specific camera setups

**Robustness:** if a quad or its camera is deleted outside the RMDoc system, the panel detects the stale state and exposes a ``Repair`` button that resets the offending flag or removes the orphan item. A background handler keeps ``is_piloting_camera`` consistent with the actual scene state.


.. _rmdoc_camera:

RMDoc Camera
------------

Each RMDoc item can own a dedicated camera, created at the current viewport position. Two navigation actions are provided:

- **Pilot Camera**: locks the 3D viewport to the camera. Any viewport navigation now moves the camera (and its child quad) together. Click again to exit.
- **Look Through**: temporarily switches the viewport to the camera view and fits the render resolution to the image pixel size, so the camera frame exactly matches the document.

Perspective/Orthographic toggle, focal length and clip distances are editable from the detail panel. ``Autocrop Near`` / ``Autocrop Far`` set clip planes to tightly fit the quad.


.. _rmdoc_alpha:

RMDoc Alpha (Transparency)
--------------------------

The Alpha slider in the detail panel edits the ``Alpha`` input of the quad's Principled BSDF material. Lower values make the document image see-through, useful when overlaying historical imagery onto the current 3D survey.

Requires the quad to have a material with a Principled BSDF node wired to the base color image texture. Newly imported images are set up this way automatically.

