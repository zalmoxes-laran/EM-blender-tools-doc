.. _Anastylosis_Manager:

Anastylosis Manager (RMSF)
==========================

The Anastylosis Manager panel manages the connection between 3D objects and SpecialFind (SF/VSF) nodes in the Extended Matrix graph. It creates and manages Representation Model Special Find (RMSF) nodes, supporting LOD switching and graph-based associations.

The panel is located in the **EM Annotator** tab.

.. _RMSFGIF:

.. figure:: ../img/gif/RMSF.gif
   :width: 600
   :align: center

   RMSF panel demonstration

Panel Layout
------------

**Selection Operations** (top area, visible when objects are selected):

- ``Sel: N obj(s)`` label showing the number of selected objects
- ``Select in List from Active Object`` button: highlights the active 3D object in the anastylosis list
- ``Add Selected Objects`` button: adds selected mesh objects to the anastylosis list
- ``Remove Selected from Anastylosis`` button: batch-removes all selected objects from the list and unlinks them from the graph

**Header**:

- Active graph code indicator
- ``Clean Missing Anastylosis Rows`` button: removes list entries whose objects no longer exist in the scene

**Main List**:

Each row in the list displays:

- **LOD indicator**: shows the current Level of Detail (0-4). Click to open a LOD selection menu, or ``X`` if no LOD variants are available
- **Object name**: with a checkmark icon if the object exists or an error icon if missing
- **Search SF button**: opens a search dialog to find and link a SpecialFind node
- **SF/VSF node label**: shows the connected SpecialFind node name or ``[Not Connected]``
- **Select button**: selects the corresponding object in the 3D viewport
- **Publish flag**: checkbox to mark the object for export
- **Remove button**: removes the item from the list and unlinks it from the graph

**Connection Info** (when an item is selected):

- Shows ``Connected to: {SF_node_name}`` with the appropriate icon (sphere for SF, empty for VSF)
- Or ``Not connected to any SpecialFind`` if no link has been established

**LOD Management** (when the selected item has LOD variants):

- ``Open Linked File`` button: opens the linked ``.blend`` file in a new Blender instance
- LOD level buttons (0 to 4): click to switch the selected item to a specific LOD level
- Batch LOD arrows: shift all items one LOD level up or down

**Settings** (collapsible):

- ``Zoom to Selected``: auto-zooms the viewport when clicking a list item

Workflow
--------

**Adding objects to the Anastylosis list:**

1. Select one or more mesh objects in the 3D viewport
2. Click ``Add Selected Objects``
3. The objects appear in the list with a ``[Not Connected]`` status

**Linking an object to a SpecialFind node:**

1. Select an item in the list
2. Click the search button (magnifying glass icon) next to the object name
3. A search dialog opens listing all available SF and VSF nodes from the graph
4. Type a search term to filter the results, then click the desired node
5. The connection is established: an RMSF node is created in the graph linking the 3D object to the SpecialFind unit

**LOD switching:**

1. Click a LOD number button (0-4) in the detail area or directly on the list row
2. For linked meshes, the mesh datablock is swapped from the linked library
3. For local objects, the current LOD variant is hidden and the new one is shown
4. Use the batch arrows to shift all items one LOD level at once

**Removing an object:**

- Click the trash button on the list row, or select the objects and click ``Remove Selected from Anastylosis``
- The RMSF node and its graph edges are also removed


.. _anastylosis_manager:

Anastylosis Manager Overview
----------------------------

The Anastylosis Manager coordinates reconstructions built from real fragments (Special Finds, SF) and virtual ones (VSF). Each entry pairs a 3D object in the scene with a node in the graph via a ``has_representation_model`` edge, exposing both graph and geometry actions from a single panel.

Typical workflow: promote selected meshes to the list, link them to the corresponding SF/VSF node, switch between LODs for preview vs. publication, then rely on the Export Manager to publish the linked scene together with the paradata.


.. _anastylosis_target:

Anastylosis Target (SF / VSF)
-----------------------------

The **target** of an anastylosis item is the SpecialFind (SF) or Virtual SpecialFind (VSF) node in the graph that the 3D object represents.

- **SF** — a real fragment found on site.
- **VSF** — a hypothetical fragment introduced during reconstruction.

The connection is materialized by a ``has_representation_model`` edge between the graph node and an RMSF node (the list entry). From the panel you can:

- Search the graph for a target node and link it (magnifying glass icon).
- Unlink an existing target (removing the RMSF and its edges).
- Jump to the target node in the Stratigraphy Manager for further inspection.


.. _anastylosis_fragments:

Anastylosis Fragments (LOD)
---------------------------

Each anastylosis object can have multiple LOD variants (LOD0 … LOD3). When LODs are detected, the panel shows a row of LOD buttons:

- Click a number to swap the active LOD for the selected item.
- Use the batch arrows to shift **all** items one LOD level up or down at once, keeping the reconstruction coherent.
- ``Open Linked File`` jumps to the source ``.blend`` file when the mesh is linked from a library.

LOD switching preserves transforms, materials and graph connections; only the mesh data-block is reassigned.
