.. _Surface_Areas:

Surface Areas
=============

.. seealso::

   In the Extended Matrix language manual:

   - `Special Find (SF) nodes <https://docs.extendedmatrix.org/en/1.5/stratigraphic_nodes.html#sf-special-find-specialfindnode>`_
     — the stratigraphic node type usually targeted by Surface Areas annotations.
   - `Paradata nodes <https://docs.extendedmatrix.org/en/1.5/paradata_nodes.html>`_
     — Property / Extractor / Document chain wired behind a surface annotation.

The **Surface Areas** panel lives in the ``EM Annotator`` sidebar tab and
provides a four-step checklist for linking a drawn area on a
Representation Model (RM) to the extended matrix.

Unlike :ref:`Proxy_Box_Creator`, which builds a proxy from measurement
points, Surface Areas attaches a sketched contour to an existing RM and
wires the full paradata chain (US → Property → Extractor → Document →
RM) in the graph.

The panel is **production-ready** as of EM 1.6 — it is no longer gated
behind ``Enable Experimental Features``. Advanced EM mode is still
required so the tab itself shows up.

.. _surface-areas:

Workflow
--------

The panel renders a compact checklist; the *Draw* button at the bottom
unlocks only when every step is met.

**1. Mesh** — single-line row that walks the chain *mesh → RM → Document*:

- Pick the target mesh in the object slot.
- An ``RM_on`` / ``RM_off`` badge tells you whether the mesh is
  registered as an RM via :ref:`rm_manager`.
- A document badge shows the linked document code (e.g. ``D.06``) when
  the chain resolves, or ``no D.`` otherwise.
- The help icon at the end of the row opens this manual page.

If the mesh isn't an RM yet, a hint row appears with a **Promote** button
that registers the mesh in the currently-active RM container — no
need to switch panels. If the RM has no Document linked, the row expands
into a document picker (search existing or create a new master via the
shared :ref:`Add Master Document <document_manager>` dialog).

**2. Extractor** — single row with the extractor method picker.

**3. Property** — single row with the property name field.

**4. SU** — single row with a Stratigraphic Unit picker. The ``+`` button
opens the shared :ref:`Add-US dialog <strat_manager_add_us>` when a
fresh unit is needed.

**Chain Summary** — a collapsible section under the four steps shows the
graph statements that will be committed when *Draw* runs, so you can
sanity-check node names and arrow directions without leaving the panel.

**Draw** — modal grease-pencil operator. Sketch the contour on the RM
surface; ``[B]`` toggles a whisker handle, ``[Enter]`` confirms,
``[Esc]`` cancels. On confirm the area is registered as a SurfaceAreale
proxy, parented to the RM, and the paradata chain is materialised in the
graph.

Relationship to other panels
----------------------------

- **Input**: requires a valid Representation Model and an active GraphML —
  see :ref:`rm_manager` and :ref:`EMsetup`.
- **Output**: the generated proxy is a standard scene object, visible and
  editable in :ref:`Stratigraphy_Manager` and :ref:`visual_manager`.
- **Alternatives**: :ref:`Proxy_Box_Creator` for measurement-driven
  proxies.

Implementation notes
--------------------

:file: ``surface_areale/ui.py``, ``surface_areale/operators.py``,
       ``surface_areale/postprocess.py``, ``surface_areale/strategies.py``

Settings live on the ``SurfaceArealeSettings`` PropertyGroup, exposed via
``scene.em_tools.surface_areale``. The mesh→RM→Document detection is
shared with :ref:`Proxy_Box_Creator` via ``find_rm_document`` in
``surface_areale.postprocess``.
