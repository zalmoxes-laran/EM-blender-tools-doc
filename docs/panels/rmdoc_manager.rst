.. _rmdoc_manager:

.. _spatialized_documents:

RMDoc — Representation Model Document
=====================================

.. seealso::

   In the Extended Matrix language manual:

   - `Document node <https://docs.extendedmatrix.org/en/1.5/paradata_nodes.html#documentnode>`_
     — the formal node type each RMDoc row materialises in 3D space.

The **RMDoc** panel manages scene objects (mesh quads) linked to document nodes for spatial authoring. Each RMDoc item binds a Blender object to a document node from the graph, optionally with a dedicated camera aligned to the source image.

It is the object-centric counterpart of the :ref:`document_manager`: while the Document Manager catalogs documents at graph level, RMDoc manages their materialisation in the 3D scene.

The panel is located in the **EM Annotator** tab and is available in Advanced EM mode.

Typical use cases
-----------------

- Georeferencing historical photos or drawings onto a 3D survey so they line up with the reconstruction.
- Authoring orthographic documentation views from a fixed vantage point.
- Navigating between document-specific camera setups for paradata review.

Panel layout
------------

**Summary bar**

The top row shows the total number of RMDoc items and how many have a dedicated camera.

**Add actions**

- When one or more mesh objects are selected in the viewport, an ``Add Selected`` button appears. Each selected mesh becomes an RMDoc item.
- When a document is selected in the Document Manager, a ``Create from 'doc_name'`` button appears to generate an RMDoc pre-linked to that document.

**UIList**

Each row displays:

- an icon indicating whether the quad object still exists in the scene (error icon if missing — see :ref:`rmdoc_robustness`);
- the quad object name;
- a magnifying-glass button to search and link a document node;
- the linked document name (or ``[Not Connected]``);
- select and delete buttons.

**Detail panel**

Selecting an item opens a detail box with :ref:`rmdoc_alpha`, :ref:`rmdoc_camera`, select/open/delete actions and — when applicable — repair controls.

.. _rmdoc_alpha:

Quad Transparency (Alpha)
-------------------------

The Alpha slider edits the ``Alpha`` input of the quad's Principled BSDF material. Lower values make the document image see-through, useful when overlaying historical imagery onto the current 3D survey.

Requires the quad to have a material with a Principled BSDF node wired to the base color image texture. Newly imported images are set up this way automatically; if the material is edited manually to remove the BSDF, the Alpha slider is hidden and a notice is shown instead.

.. _rmdoc_camera:

Dedicated Camera
----------------

Each RMDoc item can own a dedicated camera, created at the current viewport position with ``Create Camera``. When a camera exists, the detail panel shows:

- **Focal length / Ortho scale** — edits the camera data directly.
- **Perspective / Orthographic toggle** — switches the camera between the two projection modes.
- **Near / Far clip distances** plus ``Autocrop Near`` / ``Autocrop Far`` buttons that set the clip planes tightly around the quad.

Two navigation actions are available:

- **Pilot Camera** — locks the 3D viewport to the camera. Any viewport navigation now moves the camera (and its child quad) together. Click again to exit.
- **Look Through** — temporarily switches the viewport to the camera view and fits the render resolution to the image pixel size, so the camera frame exactly matches the document.

A ``Fly`` button enters Blender's fly-navigation mode for free camera placement.

.. _rmdoc_robustness:

Robustness and recovery
-----------------------

RMDoc state survives the deletion of scene objects without corrupting the panel.

- If a user deletes the **quad** (the mesh object) from the Outliner, the RMDoc item is flagged as orphan. The detail panel shows a warning and a ``Remove orphan item`` button.
- If the **camera** is deleted but the quad still exists, the flag ``has_camera`` is automatically reset; the detail panel shows ``Camera missing`` with a ``Reset camera flag`` button, after which ``Create Camera`` can be used again.
- If the user was piloting a camera that is then deleted, a background handler clears the ``is_piloting_camera`` flag and unlocks the viewport. A manual ``Force Exit Pilot`` button is also exposed whenever the flag is still active.

A single ``em.rmdoc_repair`` operator backs these actions. It can also be invoked with ``mode='FULL_SWEEP'`` from the Python console to clean up the whole ``rmdoc_list`` in one pass.

Workflow
--------

**From a selected mesh**

1. Select one or more mesh objects that represent document supports (printed photo plane, ortho image plane, etc.).
2. Click ``Add Selected`` in the RMDoc panel. Each mesh becomes an RMDoc item.
3. Use the magnifying glass on the row to link each item to the correct document node from the graph.
4. Optionally click ``Create Camera`` in the detail panel to snapshot the current viewport as the document's dedicated view.

**From an active document**

1. In the Document Manager, select a document.
2. In the RMDoc panel, click ``Create from 'doc_name'`` — a new RMDoc is created already linked to that document.
3. Position the quad, then ``Create Camera`` and ``Look Through`` to align the camera to the image.
