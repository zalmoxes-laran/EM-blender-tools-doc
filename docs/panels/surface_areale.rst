.. _Surface_Areale:

Surface Areale (RM2Proxy)
=========================

The **Representation Model to Proxy (RM2Proxy)** panel and its child
**Surface Areale** panel live in the ``EM Annotator`` sidebar tab and provide
tools for turning an existing Representation Model (RM) into a proxy geometry
via contour extraction.

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
2. Pick the stratigraphic unit (US/USV) the generated proxy will represent.
3. Configure the contour strategy in *Settings* (sampling density, smoothing,
   offset, extrusion direction).
4. Run the contour builder; the resulting proxy is placed in the working
   collection and linked to the stratigraphic unit.

The panel enforces a checklist before enabling the "Generate" action — each
prerequisite shows a ``CHECKMARK`` / ``X`` icon next to its description, so
you can immediately see what is missing (RM assigned, US selected, DosCo
linked, etc.).

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
