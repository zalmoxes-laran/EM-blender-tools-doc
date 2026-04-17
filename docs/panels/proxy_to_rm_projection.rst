:orphan:

.. _Proxy_To_RM_Projection:

RM Coloring / Proxy to RM Projection (Experimental)
===================================================

.. warning::
   This panel is experimental. Behavior, operator IDs and property names may
   change between releases. The page is built but kept out of the main
   navigation until the feature stabilizes.

   To make this panel visible in Blender, enable
   ``scene.em_tools.experimental_features`` and ensure RM temporal sync
   is active.

Overview
--------

*RM Coloring* renders Representation Model surfaces using the colors of the
proxies that intersect them, so that a viewer can visually assess which
stratigraphic unit occupies which portion of the RM.

The feature has two UI surfaces, both gated behind experimental features:

- A **collapsible section inside Visual Manager** labelled
  ``RM Coloring (Experimental)``, drawn inline by
  ``visual_manager.ui.VisualManager.draw_rm_coloring``. This is the
  recommended entry point for users.
- A **standalone sub-panel** ``VIEW3D_PT_proxy_projection_panel`` labelled
  ``Proxy to RM Projection (Experimental)``, registered as a child of Visual
  Manager, kept mainly for deep links and scripting.

Methods
-------

Two projection methods are provided via the
``scene.proxy_projection_settings.method`` enum:

- **Vertex Paint** — bakes proxy colors into the RM's vertex color layer.
  Fast, non-destructive; the RM's material is not modified.
- **Material Override** — inserts a mix shader node network into the RM's
  material (named ``RMColoring_Multi_*``) blending proxy color with the
  original texture. See ``proxy_to_rm_projection/material_override.py``.

Controls
--------

When inactive, the section shows an ``Apply RM Coloring`` button (guarded by
prerequisite checks). When active:

- ``Clear Coloring`` — remove the coloring artefacts.
- ``Update`` — recompute intersections / shader setup.
- ``Toggle`` — temporarily hide/show the coloring without removing it.
- ``Auto Update`` — rebuild on depsgraph changes.
- ``Blend Strength`` — mix weight between proxy color and the original material.
- ``Hide Non-Intersected Areas`` — mask parts of the RM that no proxy touches.

Operators
---------

All live in ``proxy_to_rm_projection/operators.py``:

- ``proxy_projection.apply``
- ``proxy_projection.clear``
- ``proxy_projection.update``
- ``proxy_projection.toggle``
- ``proxy_projection.update_strength``
- ``proxy_projection.update_visibility``
- ``proxy_projection.update_colors``
- ``proxy_projection.diagnose`` — emits a diagnostic report to the console.

Files
-----

:file: ``proxy_to_rm_projection/ui.py`` — standalone sub-panel and helpers
       (the visible UI section is drawn inline in ``visual_manager/ui.py``)
:file: ``proxy_to_rm_projection/data.py`` — ``proxy_projection_settings`` PropertyGroup
:file: ``proxy_to_rm_projection/operators.py`` — operators listed above
:file: ``proxy_to_rm_projection/utils.py`` — vertex paint + intersection helpers
:file: ``proxy_to_rm_projection/material_override.py`` — shader-node multi-proxy blending
