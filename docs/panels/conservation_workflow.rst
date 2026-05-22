Conservation Workflow (TSU)
===========================

.. seealso::

   In the Extended Matrix language manual:

   - :doc:`em-doc:stratigraphic_nodes` — formal definition of the
     :term:`em-doc:Transformation Stratigraphic Unit (TSU)` node type used
     throughout this workflow.

The **Conservation Workflow** is the EM Tools workflow for documenting
*states* and *transformations* of a built object — decay, restoration
phases, thematic surveys (e.g. material, surface treatment, damage
patterns) — over and above the strict stratigraphic sequence. It is
built around a dedicated stratigraphic unit type called **TSU**
(*Transformation Stratigraphic Unit*) introduced in EM 1.5.

When to use TSU
---------------

A **TSU** describes a *transformation that happened on an existing
unit* without creating a new physical body of matter. Typical cases:

- conservation surveys (mapping deterioration phenomena, biological
  colonisation, salt efflorescence, …);
- restoration interventions (consolidation, integration, cleaning);
- thematic readings of a surface that do not fit the standard
  US/USV/USD vocabulary (e.g. material change without removal,
  re-pointing campaigns, polychromy phases).

If the transformation produced a *new physical object* (for example,
a wall added on top of another) keep using the standard
``StratigraphicUnit`` types. If instead the surface is the same but
its *state* changes, TSU is the right type.

Creating TSU Units
------------------

The TSU authoring loop mirrors the standard US one but uses the TSU
type and a thematic proxy.

1. **Import the base model** that the TSU will be drawn on
   (typically a high-resolution mesh from a 3D survey, see
   :doc:`../tutorials/03-3dsc-lod-concept`).
2. **Create TSU nodes in the GraphML** in yEd by setting the node
   ``TYPE = TSU`` from the EM palette, or generate them in batch from
   ``em_data.xlsx``. Each TSU node should carry a unique name
   (``site_code.TSU_NN``) and be linked to the US it transforms via the
   appropriate connector.
3. **Assign a proxy to each TSU**. The proxy can be:

   - a **surface proxy** — a thin mesh draped on the model that marks
     the area affected by the transformation;
   - an **annotation proxy** — a point, polyline, or labelled shape
     when the transformation is localised.

   Use the :doc:`proxy_box_creator` (annotation mode) or the
   :doc:`surface_areale` panel to author surface proxies.
4. **Define the TSU properties**. The standard set is:

   .. list-table::
      :header-rows: 1
      :widths: 22 78

      * - Property
        - Meaning
      * - ``phenomenon``
        - The transformation observed (e.g. ``erosion``,
          ``biological_colonisation``, ``re_pointing``,
          ``polychromy_layer_2``).
      * - ``localisation``
        - Where on the host unit the transformation occurs
          (e.g. ``upper_face``, ``mortar_joints``,
          ``sw_corner``).
      * - ``material``
        - Material involved if relevant (e.g. ``lime_mortar``,
          ``patinated_surface``).
      * - ``date_of_survey``
        - ISO date the transformation was recorded.

   These properties are written into the graph as standard
   ``Property`` nodes connected to the TSU. Add further domain-specific
   properties as needed (severity, intervention urgency, …).

Managing TSU Visualization
--------------------------

TSU proxies are best rendered with **pattern-based materials** so that
different transformations are visually distinguishable on the model
without hiding the substrate.

1. **Download the TSU material library**
   (``EM_TSU_materials.blend``) from the
   `download page <https://www.extendedmatrix.org/download>`_ and
   *Append* the materials into your scene.
2. **Assign a material to each TSU proxy**. The library provides
   patterns for the most common phenomena (erosion, missing parts,
   biological growth, salt crusts, repointing, …); a
   ``TSU_generic`` material is the fallback.
3. **Apply pattern-based materials** by phenomenon. The
   :doc:`visual_manager` *Properties* mode can drive material
   assignment from the TSU's ``phenomenon`` property automatically.
4. **Tune readability** with the material parameters:

   - ``density`` — number of pattern repetitions per square metre.
   - ``thickness`` — line / dot width.
   - ``opacity`` — blend strength against the substrate.

   Density and thickness are exposed as material inputs; tweak them
   in the Shader Editor and save the result back to the library if
   you want the change to persist across projects.

Exporting TSU data
------------------

TSU information travels with the rest of the EM graph in any export
format:

- **Heriverse** — TSU proxies and their properties are included as
  standard stratigraphic units with ``type=TSU``; the consumer
  application can render them with their own materials.
- **CSV / xlsx** — TSU rows appear in the standard US tables with
  ``type`` set to ``TSU``; properties are columns.
- **GLTF** — TSU proxies are exported as separate meshes with the
  applied pattern material baked, when the ``Bake materials`` option
  is on in :doc:`export_manager`.

.. todo::
   Add screenshots — TSU node in yEd palette, surface proxy painted
   on a wall in Blender, *Visual Manager → Properties* mode driving
   TSU material assignment, and the resulting render.

.. seealso::

   - :doc:`stratigraphy_manager` — how the TSU rows fit alongside
     standard US/USV in the stratigraphy table.
   - :doc:`proxy_box_creator` — annotation-style TSU proxies.
   - :doc:`surface_areale` — surface-style TSU proxies.
   - :doc:`em-doc:stratigraphic_nodes` — formal definition of the
     :term:`em-doc:Transformation Stratigraphic Unit (TSU)` node.
