.. _RM_Manager:

Representation Models Manager
=============================


.. _RM_ManagerFIG:

.. figure:: ../img/RM_Manager.png
   :width: 400
   :align: center

   RM Manager panel


This panel (:numref:`Fig. %s <RM_ManagerFIG>`) allows to manage all the Representation models related to the reconstruciton project.
With the three buttons on the upper part of the panel (``Update from Scene``, ``Update from Graph``, and ``Select from Object``) it is possible to upadate the RM list and select the corresponding 3D model.

Other three actions can be made on the selected object by pressing the buttons ``Add Selected``, ``Remove Selected``, and ``Demote from RM``.
The first add the selected RM object to the active epoch, the second remove the active epoch fromm the selected RM object, and the third completely remove the selected RM from both the epochs and the graph.

The ``Add New Cesium Tileset`` allows to simply add an empty Cesium tileset object to the active epoch, this option will be useful for sharing data via the 3D viewer (online or local).

At the center of the panel the RM list shows all the selected Representation Models, on the right side of the list a set of buttons replicste actions already described (**add**, **select**, **publish**, and **remove**).
Under the RM list a box highlights the object currently selected and its the epoch.

When Experimental features are enabled (see :ref:`EMsetup` section), within the ``Settings (experimental)`` section new functions appears; these settings are still under development.
