.. _Proxy_Inflate_Manager:

Proxy Inflate Manager
=====================

The Proxy Inflate Manager adds thickness to proxy models using Blender's Solidify modifier. This is useful for giving volume to flat proxy geometry, both for visualization and for export workflows.

.. warning::
   This is an **experimental feature**. It must be enabled via the ``Enable Experimental Features`` button in the :ref:`EMsetup` panel.

The controls are integrated into the :ref:`Visual_Manager` panel as a collapsible section labeled ``Proxy Inflate Manager (Experimental)``.

Controls
--------

**Inflation Settings**:

- ``Thickness`` value: controls the Solidify modifier thickness
- ``Offset`` value: controls the modifier offset (even offset is applied)

**Selection Modification**:

- ``Add`` button: adds a Solidify modifier to each selected mesh object
- ``Activate`` button: enables the inflate modifier on the selected objects
- ``Deactivate`` button: disables the inflate modifier without removing it
- ``Remove`` button: deletes the inflate modifier from the selected objects

**Global Operations**:

- ``Inflate All Proxies`` button: applies Solidify modifiers to all proxy objects in the Proxy collection (or the EM list as fallback)
- ``Auto-inflate on export`` checkbox (if available): automatically adds temporary inflate modifiers during export operations; modifiers are removed after export

**Status Counter**:

- Displays the number of proxies that currently have an inflate modifier applied

Workflow
--------

1. Enable Experimental Features in the :ref:`EMsetup` panel
2. Open the :ref:`Visual_Manager` panel and expand the ``Proxy Inflate Manager`` section
3. Set the desired ``Thickness`` and ``Offset`` values
4. Select the proxy objects to inflate and click ``Add``
5. Use ``Activate`` / ``Deactivate`` to toggle the modifiers without removing them
6. Use ``Inflate All Proxies`` for bulk operations on the entire Proxy collection
