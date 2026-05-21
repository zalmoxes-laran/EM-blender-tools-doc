Build the stratigraphic proxies in Blender
==========================================

.. _howto_build_proxies:

.. note::

   This how-to is adapted from *Exercise 3 — 3D modelling the stratigraphy*
   in the Reconstructive Archaeology handbook.

Once the stratigraphic reading of an object, an architecture or an
excavation has been formalised through an Extended Matrix
(`see how to draw one <https://docs.extendedmatrix.org/en/1.5/draw_the_matrix.html>`_),
it is time to represent that stratigraphy in 3D space. Each US in the matrix
gets its own **proxy** — a lightweight 3D placeholder that materialises the
unit and is bound to the corresponding node in the graph.

Prerequisites
-------------

* EM Tools installed in Blender — see :doc:`../installation`.
* A ``.graphml`` file produced in yEd —
  `see how to draw the matrix <https://docs.extendedmatrix.org/en/1.5/draw_the_matrix.html>`_.
* The reference data for modelling: a photogrammetric survey, an
  orthophoto, building plans and sections, drawings, written sources, or
  any combination of these.

Step 1: load the references and the graph
-----------------------------------------

If you have already prepared a ``.blend`` file in the ``SB`` subfolder
(source-based modelling space), open it. Otherwise, start a new Blender
file, delete the default cube, light and camera (``A`` ▸ ``X`` ▸ Enter)
and import the references you will model from.

Inside the EM Tools add-on (3D viewport ▸ N-panel ▸ *EM* tab) open the
**EM Data Tree** section, select the ``.graphml`` file, and load it.

For the full reference on this panel — supported file formats, GraphML ID
conventions, statistics, colour schemes and visualisation options — see
:doc:`../panels/em_setup`.

Once the graph is loaded, create a collection named ``Proxy`` in the
Outliner and make it the active collection — every proxy you create from
now on will land there.

Step 2: open the Stratigraphy Manager
-------------------------------------

The **Stratigraphy Manager** lists every stratigraphic unit present in
the matrix. Decide which US to model first, then begin with the standard
procedure for adding a mesh object (``SHIFT + A``).

For the full reference on filters, list rows, adding/editing US and the
proxy-association controls used below, see
:doc:`../panels/stratigraphy_manager`.

Step 3: model the proxy
-----------------------

Creating a proxy requires only minimal polygonal-modelling skill. The
process is summarised below.

1. Place the 3D cursor in the viewport with **SHIFT + LMB** (left mouse
   button click), ideally at one corner of the structure whose proxy you
   are about to create.
2. Add a base geometry with **SHIFT + A**. In the vast majority of cases
   a cube is the right choice.
3. Raise the cube one unit on the Z axis
   (**TAB, A, G, Z, 1, Enter, TAB**), then scale it down to a manageable
   size (**S, 0.02, Enter**) — a freshly added cube is 2×2×2 m.
4. In *Edit Faces* mode, select a face and extend it in the desired
   direction (**TAB, 2, select face, G, G, hold ALT and extend, Enter or
   LMB, TAB**).
5. Repeat the extension on the other directions required (typically the
   X axis next).

.. figure:: /_static/howto/build_proxies/proxy_modeling_process.png
   :alt: Sequence of steps for modelling a proxy in Blender.
   :width: 100%
   :align: center

   The proxy modelling process — five steps from base cube to fitted
   proxy.

Step 4: associate the proxy with its US
---------------------------------------

Once the proxy geometry is finished, select the corresponding US in the
:doc:`Stratigraphy Manager <../panels/stratigraphy_manager>` and use the
*associate* control to bind proxy and US.

After binding, the proxy colour will reflect the colour scheme currently
active in the EM Tools settings, and a closed-chain symbol will appear at
the beginning of the corresponding row in the Stratigraphy Manager — a
visual confirmation that proxy and US are successfully bound.

Colour schemes (EM vs. Periods, custom property-based mappings, saving and
loading ``.emc`` files) are documented in :doc:`../panels/visual_manager`.

Step 5: model the rest of the stratigraphy
------------------------------------------

Continue modelling every other US already prepared in the EM. The result
is a single Blender scene in which every proxy is bound to a
stratigraphic unit in the graph, classified by epoch, and ready to be
combined with the higher-detail representation models in the next stage
of the workflow.

For per-epoch selection, locking, visibility and *soloing* of the proxies
you have just produced, see the :doc:`../panels/epochs_manager` reference.

See also
--------

* `Draw the Extended Matrix <https://docs.extendedmatrix.org/en/1.5/draw_the_matrix.html>`_
  — drawing the ``.graphml`` that feeds this exercise.
* :doc:`20-em-2d-3d-linking` — the video-tied walkthrough of the same
  binding step.
* :doc:`../panels/em_setup` — full reference for the EM Data Tree panel
  used in step 1.
* :doc:`../panels/stratigraphy_manager` — full reference for the
  manager panel used in steps 2 and 4.
* :doc:`../panels/epochs_manager` — full reference for the Epochs Manager
  panel.
* :doc:`../panels/visual_manager` — colour schemes and visual settings
  applied to proxies.
