.. _Surface_Areale:

Surface Areale (Experimental)
=============================

.. warning::
   This panel is experimental and shipping as a preview in **EM 1.6**.
   Behavior, operator IDs and property names may change between releases.
   The page is built but kept out of the main navigation until the feature
   stabilizes.

   To make the panel visible in Blender, enable
   ``scene.em_tools.experimental_features`` in the EM Data Tree panel.

The **Representation Model to Proxy (Experimental)** panel and its child
**Surface Areale (Experimental)** panel live in the ``EM Annotator`` sidebar
tab and provide tools for turning an existing Representation Model (RM) into a
proxy geometry via contour extraction.

Unlike :ref:`Proxy_Box_Creator`, which builds a proxy from measurement points,
this tool generates the proxy by sampling a horizontal contour on an RM surface
and extruding it to match a set of archaeological boundaries.

Panel structure
---------------

The toolbox is composed of three stacked panels:

- **Representation Model to Proxy (RM2Proxy)** — parent panel. Shown only
  when a GraphML is loaded.
- **Surface Areale** — child of RM2Proxy; step-by-step workflow with a
  requirement checklist (target RM, stratigraphic layer, working collection,
  etc.). Driven by ``scene.em_tools.surface_areale`` settings.
- **Settings** — child of Surface Areale; advanced parameters
  (``DEFAULT_CLOSED``).

Workflow
--------

1. Select a Representation Model in the scene.
2. Pick the Document (existing or create a new one via the shared
   **+ Add New Document...** widget; see :ref:`document_manager`).
3. Pick the target Stratigraphic Unit — the row has a ``+`` button
   (custom ``proxies_rows_add`` icon) that launches the shared
   :ref:`Add-US dialog <strat_manager_add_us>` when you need a fresh
   one. After the dialog closes the new unit is already active, so
   the picker immediately reflects it.
4. Configure the contour strategy in *Settings* (sampling density,
   smoothing, offset, extrusion direction).
5. Run the contour builder; the resulting proxy is placed in the
   working collection and linked to the stratigraphic unit via the
   full paradata chain (experimental mode) or just parented to the
   RM (1.5 baseline).

The panel enforces a checklist before enabling the "Generate" action — each
prerequisite shows a ``CHECKMARK`` / ``X`` icon next to its description, so
you can immediately see what is missing (RM assigned, Document picked,
US picked, etc.).

.. note::
   Inline US creation has been removed from this panel. The previous
   ``Create New US`` toggle (with its own type / name / epoch / activity /
   stratigraphic-link fields) is replaced by the ``+`` next to the US
   picker, which opens the shared :ref:`Add-US dialog <strat_manager_add_us>`.
   Same form the Stratigraphy Manager and Proxy Box Creator use — one
   changepoint for every US creation rule.

Relationship to other panels
----------------------------

- **Input**: requires a valid Representation Model and an active GraphML —
  see :ref:`rm_manager` and :ref:`EMsetup`.
- **Output**: the generated proxy is a standard scene object, visible and
  editable in :ref:`Stratigraphy_Manager` and :ref:`visual_manager`.
- **Alternatives**: :ref:`Proxy_Box_Creator` for measurement-driven proxies.

Implementation notes
--------------------

:file: ``surface_areale/ui.py``, ``surface_areale/operators.py``,
       ``surface_areale/strategies.py``, ``surface_areale/contour_builder.py``

Settings live on the ``SurfaceArealeSettings`` PropertyGroup, exposed via
``scene.em_tools.surface_areale``.
