Workflows
=========

This page is the **operational map** of EM Tools. Every workflow below
follows the same four-column rhythm so you can locate yourself in the
addon at any time:

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - what you start with
     - where you act
     - what you do
     - what you take away

If you are looking for a step-by-step tutorial instead of a map,
see :doc:`tutorials/index`. If you are looking for the panel
references, see :doc:`panels/index`.

.. contents::
   :local:
   :depth: 1


1. From an existing GraphML to a navigable 3D scene
---------------------------------------------------

The most common entry path: somebody else (or yourself in yEd) has
already authored an EM graph, and you bring it into Blender to
explore it spatially.

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - ``site.graphml`` from yEd; DosCo folder
     - :doc:`panels/em_setup`
     - Set the ``.graphml`` path, set the DosCo path, click *Reload*.
     - Loaded summary; sources auto-linked to nodes.
   * - the loaded graph
     - :doc:`panels/stratigraphy_manager`
     - Browse units, filter by epoch / activity / containment.
     - Working selection of stratigraphic units.
   * - selected units + 3D model
     - :doc:`panels/visual_manager`
     - Choose display mode (*EM*, *Epochs*, *Properties*).
     - Coloured 3D scene reflecting the graph.

.. tip::
   Want a worked example?
   See :doc:`tutorials/13-first-matrix-creation` for the full setup,
   then :doc:`tutorials/14-multitemporal-visualization` for the epoch
   side.


2. Authoring an EM graph from a 3D survey
-----------------------------------------

You start from a 3D survey (mesh + textures) and you build the
stratigraphic graph *while* you annotate the model.

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - high-resolution mesh; (optional) skeleton GraphML
     - :doc:`panels/em_setup`
     - Load the empty / skeleton graph; set DosCo.
     - Empty stratigraphic table ready to be populated.
   * - the mesh, the active US
     - :doc:`panels/proxy_box_creator`
     - Pick 7 points on the mesh; create the proxy and the US in one shot.
     - New US node + proxy aligned to the mesh; paradata stub.
   * - the new US, the active epoch
     - :doc:`panels/stratigraphy_manager`
     - Add description, link sources from DosCo, set ``has_first_epoch``.
     - US fully described in the graph.
   * - the populated graph
     - :doc:`panels/em_setup`
     - *Save GraphML*.
     - ``site.graphml`` updated on disk and ready to share.

.. seealso::
   :doc:`creating_em` — the unified ``em_data.xlsx`` flow if you
   prefer to author the graph in a spreadsheet rather than directly
   in Blender.


3. Multi-temporal reconstruction (epochs and hypotheses)
--------------------------------------------------------

You have a documented stratigraphy; you now want to make the
*reconstruction* explicit, with epochs and alternative hypotheses.

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - the loaded graph
     - :doc:`panels/epochs_manager`
     - Define epochs, their time bounds, and their colours.
     - Epoch table; colour scheme available to the Visual Manager.
   * - 3D base + reference imagery
     - :doc:`panels/rm_manager`
     - Build / import reconstruction models; assign each to its epoch.
     - RM collection, one per epoch, linked to the relevant units.
   * - the same epoch, an alternate idea
     - :doc:`panels/rm_manager`
     - Duplicate the RM, mark the new branch with a property explaining the divergence.
     - Two coexisting hypotheses sharing the same epoch.
   * - everything above
     - :doc:`panels/visual_manager` + :doc:`panels/cronofilter`
     - Step through epochs / chronological horizons; review consistency.
     - Visual proof the reconstruction is coherent across time.


4. Conservation survey (TSU)
----------------------------

You have a built object and you want to document its *state* —
decay, restoration phases, thematic readings — without touching the
stratigraphic sequence.

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - high-resolution mesh of the object
     - :doc:`panels/em_setup`
     - Load the existing graph (or start a new one).
     - Working scene.
   * - the host US already in the graph
     - :doc:`panels/conservation_workflow` (TSU section)
     - Add ``TSU`` nodes (manually or via xlsx); link to the host US.
     - TSU nodes attached to the substrate.
   * - the active TSU
     - :doc:`panels/proxy_box_creator` / :doc:`panels/surface_areale`
     - Author a surface or annotation proxy on the mesh.
     - TSU proxy aligned to the affected area.
   * - the TSU + library materials
     - :doc:`panels/visual_manager` (*Properties* mode)
     - Drive pattern-based material assignment from the ``phenomenon`` property.
     - Visual conservation map of the object.

The full reference for this workflow is in
:doc:`panels/conservation_workflow`.


5. Export and publication
-------------------------

When the graph is complete and the 3D scene is annotated, you produce
a deliverable.

.. list-table::
   :header-rows: 1
   :widths: 24 24 28 24

   * - Data
     - Panel
     - Action
     - Output
   * - the entire scene + graph
     - :doc:`panels/export_manager`
     - Pick *Heriverse export*; set project name and output folder.
     - Heriverse-ready package (GLTF + JSON + assets) for the web viewer.
   * - the same scene
     - :doc:`panels/export_manager`
     - Pick *Tables export* → ``EM (csv)`` / ``US/USV`` / ``Sources``.
     - CSV files for QGIS, spreadsheets, archive deposit.
   * - the same scene
     - :doc:`panels/export_statistics`
     - Compute volumes by epoch / by certainty.
     - CSV report for the project's quantitative section.

.. seealso::
   :doc:`export_guide` for the full export reference.


.. todo::
   Add a short screencast next to each workflow once filmed
   (suggested length: 60–90 seconds, no audio, captioned). The
   priority order is: workflow 1, workflow 4 (TSU is new),
   workflow 2.
