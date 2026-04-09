.. _Stratigraphy_Manager:

Stratigraphy Manager
====================

This tool allows to explore and filter all the EM graph nodes. The panel is divided into a header with filter status, an expandable filter section, and a scrollable list of stratigraphic units.

.. _EM_Strat_ManagerFIG:

.. figure:: ../img/stratigraphy_manager/strat_manager_overview.png
   :width: 400
   :align: center

   Stratigraphy Manager panel overview

Header
------

The header displays the total or filtered row count. When any filter is active, a ``FILTER`` icon appears along with:

- An ``X`` button to reset all filters and restore the full list
- A visibility toggle to show/hide all proxies when resetting

List Rows
---------

Each row in the stratigraphy list displays:

- A **link icon** on the left: indicates whether the node has a corresponding proxy in the 3D scene. A linked chain means the proxy exists; a broken chain indicates a mismatch between the EM graph and the 3D scene (**NB**: a common cause is a mismatch between the node name in the EM and the proxy name in Blender)
- The **node name**
- **Special icons** next to the name (see below)
- The **node description**

Clicking the link icon selects the corresponding 3D proxy. Use Blender's ``Frame Selected`` command to navigate to it.

.. _filter_system:

Filter System
-------------

Expand the ``Available filters`` section to access all filtering options.

.. _EM_Strat_FiltersFIG:

.. figure:: ../img/stratigraphy_manager/strat_filters.png
   :width: 400
   :align: center

   Available filter options

**Epoch and Activity Filters**

- ``By Epoch``: toggle to show only units belonging to the selected epoch. Use the dropdown menu to change the active epoch
- ``By Activity``: toggle to show only units belonging to the selected activity group

These two filters can be combined. When epoch filtering is active, additional options appear:

- ``Surviving Units``: include units that survive from earlier epochs into the current one
- ``Reconstructive Units``: include virtual stratigraphic units (USV)

**3D Sync**: When epoch/activity filters are active, a ``Sync 3D scene with filter results`` section appears with options to synchronise the visibility of **Proxies** and **RM Models** in the 3D viewport.

.. _containment_filter:

Containment Filter
------------------

.. _EM_Strat_ContainmentFIG:

.. figure:: ../img/stratigraphy_manager/strat_containment.png
   :width: 400
   :align: center

   Containment icons: group icon on the container row, back-arrow on contained elements

When a stratigraphic unit acts as a **container** (a US, USD, or VSF containing SF or VSF elements via ``is_part_of`` edges), special icons appear next to the node name:

- **Group icon** on the container row: click to filter the list to show only the container and its contained elements
- **Back-arrow icon** on contained elements: click to navigate back to (select) the parent container row in the current list

The containment relationship is mereological (part--whole): for example, a wall (US) containing a reused capital (SF), or a reconstructed roof (VSF) composed of tile fragments (SF).

.. seealso::
   The `Extended Matrix documentation on containment <https://extendedmatrix.readthedocs.io/en/latest/connectors.html#is-part-of-is-part-of>`_ for the formal specification.

.. _instance_chain_filter:

Instance Chain Filter
---------------------

.. _EM_Strat_ChainFIG:

.. figure:: ../img/stratigraphy_manager/strat_instance_chain.png
   :width: 400
   :align: center

   Instance chain icon (three dots) on rows connected by dotted connectors

When nodes are connected by **dotted connectors** (``changed_from`` edges), representing the same conceptual object across different epochs, a **three dots** icon appears next to each chain member.

Clicking the three dots icon filters the list to show **all instances in the chain**, sorted chronologically (most recent epoch first).

For example: a capital that exists today on the ground (SF5000-C), existed in a previous epoch as a collapsed element (USD5000-B), and in the Roman era was in its original position (USM5000-A). All three are connected by dotted edges and form a single instance chain.

.. seealso::
   The `Extended Matrix documentation on instance chains <https://extendedmatrix.readthedocs.io/en/latest/connectors.html#instance-chains>`_ for the formal specification and naming conventions.

Filter Interactions
-------------------

Filters are **mutually exclusive by category**:

- Activating the **containment filter** automatically resets epoch, activity, and instance chain filters
- Activating the **instance chain filter** automatically resets epoch, activity, and containment filters
- Activating **epoch or activity filters** resets containment and instance chain filters
- **Selecting a 3D proxy** in the viewport automatically resets containment and instance chain filters to ensure the selected element can be found in the full list

The ``X`` button in the header resets all filters at once.

Selected Item Details
---------------------

When an item is selected in the list, a details box appears below showing:

- The node **name** (editable) and **type**
- A **link** button to associate a 3D proxy with this node
- A **select** button to select the corresponding proxy in the 3D scene
- The node **description**

Associated Documents
--------------------

An expandable ``Associated Documents`` section shows thumbnails of documents linked to the selected stratigraphic unit. Two view modes are available:

- ``List``: shows documents as rows with thumbnail, name, and action buttons (open file, open folder)
- ``Gallery``: shows documents as a grid of thumbnails using Blender's native icon view

.. note::
   Thumbnails must be generated first from the EM Data Tree panel (see the :ref:`EMsetup` section).
