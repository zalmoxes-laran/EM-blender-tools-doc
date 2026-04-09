.. _Document_Manager_3D:

3D Document Manager
===================

The 3D Document Manager panel handles spatial-temporal documents within the EM project. It allows linking documents to 3D representations (image planes and cameras), managing their certainty classification, and navigating between documents and their spatial context.

The panel is located in the **EM Annotator** tab and is available in Advanced EM mode.

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
