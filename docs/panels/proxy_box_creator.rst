.. _Proxy_Box_Creator:

Proxy Box Creator
=================

.. seealso::

   In the Extended Matrix language manual:

   - `Paradata NodeGroup <https://docs.extendedmatrix.org/en/1.5/paradata_group.html#paradata-nodes-group>`_
     — DP-60 formal definition of the ``<US>_PD`` group written by this panel.
   - `Paradata nodes <https://docs.extendedmatrix.org/en/1.5/paradata_nodes.html>`_
     — Document, Extractor, Combiner and PropertyNode types in the chain.

The Proxy Box Creator builds a proxy mesh (a 7-point bounding volume) for a
Stratigraphic Unit and wires the full paradata chain behind it — Document
instance → Extractors → Combiner → PropertyNode ("Proxy Geometry") — all
wrapped in a per-US `ParadataNodeGroup
<https://docs.extendedmatrix.org/en/1.5/paradata_group.html#paradata-nodes-group>`_
(``<US>_PD``).

The panel lives under **EM Annotator → RM to Proxy Suite → Proxy Box Creator**
and is structured top-to-bottom as a two-step workflow:

1. **Step 1 — Anchor Document** (the source the extractors will cite).
2. **Step 2 — Measurement Points** (seven 3D positions defining the box).
3. **Parameters** (pivot, proxy collection, Active US, persistence).
4. **Chain Summary** (collapsible) + **Create / Clear** buttons.

The panel is gated behind ``scene.em_tools.experimental_features`` and
``mode_em_advanced``.

.. _proxy_box_step1:

Step 1 — Anchor Document
------------------------

Every paradata chain needs a :class:`DocumentNode` as its ultimate source.
You have three ways to set the anchor:

- **Pick from selected** (eyedropper icon): introspects the active mesh in the
  viewport. If the mesh is already linked to a DocumentNode through the RM
  Manager's :ref:`has_representation_model <rm_containers>` edge, the anchor
  is set immediately. If no link exists, a follow-up dialog opens that
  promotes the mesh to ``rm_list`` (when an active epoch is present),
  creates the :class:`RepresentationModelNode`, adds the
  ``has_representation_model`` edge, and records the anchor.
- **Search** (magnifying-glass icon): opens the shared
  ``draw_document_picker_with_create_button`` widget — search the existing
  document catalog or click **+ Add New Document...** to open the Master
  Document creation dialog. After the dialog closes, the newly-created
  document is the anchor.
- **Clear** (``X`` icon): drops the anchor without touching the scene.

A :guilabel:`Propagate to all 7 points` checkbox (default ON) controls whether
each measurement point automatically inherits the anchor document on Record
(and gets its extractor id auto-computed). Turn it off for rare multi-source
workflows where different points cite different documents.

.. _proxy_box_step2:

Step 2 — Measurement Points
---------------------------

Seven rows, one per semantic point:

.. list-table::
   :widths: 12 30 58
   :header-rows: 1

   * - #
     - Point
     - Purpose
   * - 1
     - Alignment Start
     - Beginning of the main axis
   * - 2
     - Alignment End
     - End of the main axis
   * - 3
     - Thickness
     - Perpendicular width
   * - 4
     - Quota Min
     - Minimum height
   * - 5
     - Quota Max
     - Maximum height
   * - 6
     - Length Start
     - Start of the axis extent
   * - 7
     - Length End
     - End of the axis extent

Each row displays: status icon (CHECKMARK when recorded), current position
``(x, y, z)`` or ``—``, and a :guilabel:`Record` button that captures the
3D cursor at click time. When **Propagate** is on and the anchor is set,
the Record button also fills the row's ``source_document`` and
``extractor_id`` (gap-aware, counts both graph-side extractors and ids
already staged on other points so no two extractors of the same Proxy
collide).

.. _proxy_box_parameters:

Parameters
----------

- :guilabel:`Pivot` — ``Bottom`` (default), ``Center`` or ``Top``; governs
  where the proxy mesh's origin sits.
- :guilabel:`Use Proxy Collection` — file the new mesh under the standard
  ``Proxy`` collection (default ON).
- :guilabel:`Save GraphML immediately after create` — default ON. Persists
  the new paradata chain to the active ``.graphml`` via
  ``export.graphml_update`` right after Create. The write-lock pre-flight
  handles yEd conflict detection; disable only if you want to batch-save
  later.
- :guilabel:`Active US` row — a ``prop_search`` on the Stratigraphy Manager
  list, bound to the ``target_us_name`` computed property. Picking here
  moves the Stratigraphy Manager's active US (and vice versa). The ``+``
  button (custom ``proxies_rows_add`` icon) opens the **Add Stratigraphic
  Unit** dialog; see :ref:`strat_manager_add_us`.

The proxy mesh will take the Active US's name on Create — there is no
separate "proxy name" field anymore.

.. _proxy_box_chain_summary:

Chain Summary
-------------

A collapsible box narrates the paradata chain that Create will write, with
the correct edge direction and type:

.. code-block:: text

   US10102  --has_property-->  Proxy Geometry
     --has_data_provenance-->  C.N (new)
     <--is_combined_in--       D.01.102, D.01.103, ..., D.01.108
     <--has_extractor--        D.01 (cloned instance)

The names shown are the ones currently resolved: Active US on the left,
the Step-1 anchor document on the right.

.. _proxy_box_create:

Create Proxy
------------

The Create button is enabled only when: (1) all 7 points are recorded, (2)
every point has a ``source_document`` + ``extractor_id`` (guaranteed when
Propagate is on), and (3) an Active US is resolved. If any prerequisite is
missing, the button's label spells out what's left (``Record all 7 points
first``, ``Set the anchor document (Step 1)``, ``Select the Active US
first``, …).

On Create the operator:

1. Runs a **write-lock pre-flight** on the active graphml.
2. **Clones** the Step-1 anchor Document into a fresh instance (same
   display name, new UUID, copied three-axis classification). Each run
   gets its own Document instance so the extractors never attach to a
   document already wrapped inside another PD group.
3. Writes seven :class:`ExtractorNode` s (one per point) with
   ``Extractor --extracted_from--> Document-instance`` edges (canonical,
   dashed).
4. Writes a :class:`CombinerNode` (``C.N``, gap-aware) with
   ``Combiner --combines--> Extractor`` edges, positioned at the
   extractor centroid in the Extractors collection.
5. Writes (or reuses) a :class:`PropertyNode` named ``Proxy Geometry``
   (canonical qualia from ``em_qualia_types_additions.json``) on the
   Active US with edge ``US --has_property--> PropertyNode``, and the
   provenance edge ``PropertyNode --has_data_provenance--> Combiner``.
6. **Wraps everything in a per-US ParadataNodeGroup** named ``<US>_PD``
   (``US --has_paradata_nodegroup--> PD_group``). Every paradata child
   gets an ``is_in_paradata_nodegroup`` edge pointing at the PD; the
   GraphMLPatcher nests the child's XML under the PD's ``<graph>`` at
   save time.
7. If the Active US has an ``is_in_activity`` edge (from the Add-US
   dialog's Activity picker), **mirrors** it onto the PD group so both
   sit inside the same :class:`ActivityNodeGroup` container in yEd.
8. Builds the proxy mesh (7-point box with the chosen pivot), prefixes
   the name with ``graph_code.`` per DP-46, and re-applies the active
   display mode (EM / Epochs / Horizons / Properties) so the new mesh
   picks up the correct material.
9. If :guilabel:`Save GraphML immediately` is on, invokes
   ``export.graphml_update``. The message reports ``[persisted]``.

What the result looks like in yEd: a group labelled ``US10102_PD`` sitting
in the same swimlane row as its US, containing the Document instance,
seven extractors (labelled ``D.01.102``…``D.01.108`` at Corner-NorthWest),
one combiner (``C.N``), and the ``Proxy Geometry`` property, all wired
with dashed paradata edges.

.. note::
   Inline US creation has been removed from this panel. Click the ``+``
   next to the Active US picker to launch the shared
   :ref:`Add-US dialog <strat_manager_add_us>` — the same form the
   Stratigraphy Manager and Surface Areas use.
