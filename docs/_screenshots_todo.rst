:orphan:

Screenshots Backlog
===================

This page is the **maintainer-facing** inventory of screenshots and
screencasts the manual is missing. It is not linked from the main
toctree (so users do not see it) but is included in the build so the
``.. todo::`` directives appear in the global todo list.

The order below mirrors the priority Eleonora Scopinaro flagged in
the 3D-4CH Online Competence Centre review: the bigger the impact on
a first-time user, the higher the slot.

Tier 1 — first-contact moments
------------------------------

Screenshots a user lands on within their first ten minutes with the
addon. Must come first.

.. todo::
   *Installation flow* — six shots covering: Blender ``Edit →
   Preferences → Get Extensions``, the *Install from Disk* dialog,
   the EM Tools entry in the add-ons list before and after enabling,
   and the EM panels visible in the 3D Viewport sidebar after
   activation.
   See :doc:`installation`.

.. todo::
   *yEd palette import* — three shots: ``Edit → Manage Palette…``
   menu, the *Import Section* dialog with the EM palette file
   selected, the EM section visible in yEd's right-hand panel after
   import.
   See :doc:`installation`.

.. todo::
   *EM Setup quick start* — two shots: the EM Setup panel before any
   graph is loaded, and the same panel after loading the example
   ``.graphml`` with the DosCo path set.
   See :doc:`panels/em_setup`.

Tier 2 — panel reference
------------------------

Each panel reference page should carry at least one full-panel
screenshot (preferably with a small callout indicating the most
important controls).

.. todo::
   :doc:`panels/stratigraphy_manager` — full panel with a populated
   list, plus a close-up of the *+ Add US* dialog.

.. todo::
   :doc:`panels/visual_manager` — three shots, one per display mode
   (*EM*, *Epochs*, *Properties*); ideally on the same scene so the
   user can compare.

.. todo::
   :doc:`panels/epochs_manager` — one shot of the epoch table
   populated, one of the colour picker open.

.. todo::
   :doc:`panels/cronofilter` — one shot of the chronological horizons
   manager filtering a multi-graph scene.

.. todo::
   :doc:`panels/export_manager` — one shot of the Heriverse export
   form filled, one of the table-export section.

.. todo::
   :doc:`panels/proxy_box_creator` — the 7-point pick UI in action,
   plus the resulting proxy aligned to the mesh.

.. todo::
   :doc:`panels/document_manager_3d` — one shot of a 3D document
   placed in the scene with the camera and the image plane visible.

.. todo::
   :doc:`panels/conservation_workflow` — TSU node in yEd, surface
   proxy painted on a wall, *Visual Manager → Properties* mode
   driving the TSU material assignment, and the resulting render.

Tier 3 — workflow narrative
---------------------------

Short screencasts (60–90 s, no audio, captioned) embedded in the
workflow page so the reader can confirm they are doing the right
thing.

.. todo::
   :doc:`workflows` — one screencast per workflow, in this order of
   priority: workflow 1 (load a graph), workflow 4 (TSU — new in
   1.5), workflow 2 (author from a survey), workflow 3 (multi-temporal),
   workflow 5 (export).

Tier 4 — case study
-------------------

When the *Casa di Esempio* training dataset is published, every
session in the case study should ship with at least one anchor
screenshot.

.. todo::
   :doc:`tutorials/22-complete-case-study` — anchor screenshots for
   the three sessions, plus a final shot of the Heriverse package
   open in the web viewer.

How to use this list
--------------------

When you record a screenshot, replace the relevant ``.. todo::``
block with a proper ``.. figure::`` directive in the target file.
The todo will disappear from the global list automatically. Set
``todo_include_todos = False`` in :file:`conf.py` before tagging a
stable release so the warnings do not leak into the public build.
