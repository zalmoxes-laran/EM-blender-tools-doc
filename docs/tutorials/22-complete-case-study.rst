.. badge:: Intermediate
   :color: orange
.. badge:: Case study
   :color: purple

End-to-End: A Complete Site Workflow
====================================

The previous intermediate tutorials each focused on one slice of
the EM workflow. This one stitches them together on a real (small)
site so you can see the whole life-cycle: from the field report and
the photogrammetric survey to the published reconstruction with
auditable paradata.

It is the longest tutorial in the manual and is meant to be taken
in **three sessions** of 60–90 minutes each.

Learning objectives
-------------------

By the end you will have:

- a complete EM graph for a real (training) site, with units,
  relations, sources, paradata and TSU;
- a Blender scene where every proxy is bound to its graph node and
  every selection cross-walks both ways;
- a multi-temporal reconstruction with at least two epochs and one
  alternative hypothesis;
- a Heriverse export that opens in the web viewer;
- a small report (auto-generated CSV + your commentary) summarising
  the project's quantitative side.

Prerequisites
-------------

All four intermediate tutorials:

- :doc:`19-manual-em-construction`
- :doc:`20-em-2d-3d-linking`
- :doc:`21-sources-metadata`
- familiarity with at least one of the advanced tutorials
  (:doc:`14-multitemporal-visualization` is the most relevant).

Dataset
-------

The case study uses the *Casa di Esempio* training dataset, which
includes:

- 18 stratigraphic units (US, USV, USD, SF) covering one room across
  three phases;
- one TSU campaign (decay survey) on the south wall;
- 12 source PDFs (excavation report, drawings, archival photographs,
  one material analysis);
- a photogrammetric mesh (~250k tris) and an orthophoto of the
  floor;
- two reference reconstructions (one published, one alternative).

.. todo::
   The training dataset is being assembled and will be downloadable
   from the Extended Matrix website. Until then, follow the
   sessions below using your own equivalent material — every step
   is dataset-agnostic.

Session 1 — Authoring (~90 min)
-------------------------------

Goal: get the graph and the proxies in place.

1. Apply :doc:`19-manual-em-construction` to the 18 units of the
   case study. Save the GraphML.
2. Apply :doc:`20-em-2d-3d-linking`: bring in the orthophoto, the
   section drawing and the photogrammetric mesh; create proxies for
   every US that has a physical body.
3. Save the project.

**Acceptance check.** Selecting any US in the
:doc:`../panels/stratigraphy_manager` reveals at least one source
and (for physical units) flies the camera to the proxy.

Session 2 — Reasoning (~90 min)
-------------------------------

Goal: turn the units into *justified* claims.

1. Apply :doc:`21-sources-metadata` to the five units whose
   interpretation depends on more than one source.
2. Define the three epochs of the case study in
   :doc:`../panels/epochs_manager`; assign every US to its
   ``has_first_epoch`` (and ``has_last_epoch`` where it differs).
3. Build the alternative reconstruction hypothesis for the southern
   wall: duplicate the RM, mark the divergence with a Property node
   pointing to the supporting Document.
4. Add the TSU campaign on the south wall using
   :doc:`../panels/conservation_workflow`.

**Acceptance check.** The :doc:`../panels/paradata_manager` filter
view shows full chains for the five interpreted units; the
Cronofilter steps cleanly through the three epochs; the TSU
materials are visible on the south-wall proxy.

Session 3 — Publication (~60 min)
---------------------------------

Goal: produce the deliverables.

1. Run a full Heriverse export
   (:doc:`../panels/export_manager`); open the result in the web
   viewer, verify epoch switching and source pop-ups work.
2. Run the table exports (``EM (csv)``, ``US/USV``, ``Sources``);
   check that every row carries the right epoch, type and source
   reference.
3. Run :doc:`../panels/export_statistics` — volumes by epoch and
   by certainty.
4. Write a 1-page commentary describing what the numbers mean
   (this is the part that no exporter can do for you).

**Acceptance check.** A colleague who has *never* seen the project
can open the Heriverse package and reach, for any selected unit,
the supporting source within two clicks.

What to take away
-----------------

- A site that looks small (18 units) generates a non-trivial graph
  (~50 nodes including paradata). EM rewards discipline.
- The interesting part of the workflow is *not* the panels. It is
  the moments where you decide *which type a unit is*, *what an
  extractor extracted*, *whether a divergence is a real
  hypothesis or a stylistic preference*. The panels make those
  decisions traceable.
- The deliverables you produce here (Heriverse package + CSVs +
  commentary) are a complete archival unit on their own — they
  can be deposited in a repository alongside the field
  documentation.

Where to go next
----------------

- :doc:`../export_guide` — deeper export options for archive
  deposit, Zenodo, etc.
- :doc:`../panels/cronofilter` — fine-grained chronological
  horizons across multiple sites.
- The advanced tutorials (14–18) — each picks one of the patterns
  you used here and explores it in depth.

.. seealso::

   The published case-study report (when available) will live on
   the `Extended Matrix showcase <https://www.extendedmatrix.org/showcase>`_.
