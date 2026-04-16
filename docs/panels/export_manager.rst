.. _export_manager:

.. _Export_Manager:

Export Manager
==============

.. _EM_Export_ManagerFIG:

.. figure:: ../img/EM_Export_Manager.png
   :width: 400
   :align: center

   Export Manager panel

This panel (:numref:`Fig. %s <EM_Export_ManagerFIG>`) is divided in two different sections: **Export** and **Heriverse Export**.
The first section allows to automatically export EM data in csv files.
By pressing one button user can export the entire EM (``EM (csv)`` button) or groups of nodes (``US/USV`` button, ``Sources`` button, ``Extractors`` button).

The second part of the panel allows to export geometries from Blender to Heriverse, that is the 3Dweb app, based on the Aton Framework, that allow to share online, within the same 3D scene, both 3D models (Proxies, Representation models and Source models) and the EM, with all its paradata.

To export correctly all the data, first it is necessary to control that every geometry (Representation Models and Source models) has been associated with the correct epoch/s.

Second, 3D objects have to be stored in the correct collection of Blender (Representation Models - **RM**; Reality Based - **RB**; **Proxy**).


Fourth, before exporting geometries, user must: locate the folder where the Heriverse project will be saved, set the name of the Project, and check/uncheck the desired options.

Finally, by pressing the ``Export Heriverse Project`` button, EMTools will export the project within a specific folder ready for the upload on Heriverse.
