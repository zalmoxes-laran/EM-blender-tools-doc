.. _graph_editor:

.. _Graph_Editor:

Graph Editor
============

The Graph Editor provides a node-based visualization of the Extended Matrix graph directly within Blender's Node Editor. It is composed of multiple sub-panels that control loading, filtering, appearance, and synchronization between the graph and the 3D viewport.

The Graph Editor is available in the **Node Editor** space under the **EM** category when **Experimental Features** are enabled.

.. note::
   A companion panel (``Graph Editor Sync``) also appears in the 3D Viewport under the EM tab, providing quick synchronization controls.

Main Panel
----------

The main panel provides quick-loading and navigation controls.

**Quick Load**:

- ``All Nodes`` button: loads the complete graph
- ``US - USV`` button: loads stratigraphic and site visit nodes only
- ``US Only`` button: loads stratigraphic nodes only
- ``Match Stratigraphy Manager`` button: loads nodes matching the current stratigraphy list filter

**Neighborhood View**:

Allows hierarchical exploration of node relationships. Select a node (in 3D, the UI list, or the graph), then choose a depth level:

- ``Lvl 1``, ``Lvl 2``, ``Lvl 3`` buttons: show only the selected node and its neighbors up to the chosen depth
- Keyboard shortcut: ``Shift+Alt+N``

**Node + Context View**:

Toggle switches for three context types that can be combined:

- **Stratigraphic**: shows stratigraphic relationships
- **Paradata**: shows documentation metadata connections
- **3D Models**: shows connections to representation models

Click ``Load Context View`` to apply the selected context combination.

**Synchronization**:

- ``Sync Selection`` button (shortcut: ``Shift+Alt+F``): synchronizes the selection between the 3D viewport and the graph

**Current Graph Info**:

- Displays the node count and edge count of the loaded graph

Edge Type Filters
-----------------

A collapsible sub-panel that controls which edge types are visible in the graph. Edges are organized into five categories:

- **Stratigraphic**: stratigraphic relationships between units
- **Temporal**: time-based connections (epochs, periods)
- **Paradata**: documentation and provenance edges
- **Model**: 3D model association edges
- **Other**: miscellaneous edge types

Controls:

- ``All`` / ``None`` quick buttons to toggle all edges at once
- Per-category checkbox to enable/disable an entire category
- Individual edge type checkboxes for fine-grained control
- ``Apply Edge Filter`` button to render the filtered graph

Appearance
----------

A collapsible sub-panel with four color scheme presets:

- ``Default``: neutral grays and blues
- ``Pastel``: soft, muted tones
- ``Vibrant``: high-saturation colors
- ``Gray``: grayscale for accessibility or printing

Click a scheme button to apply it to all nodes based on their type (US, USV, SF, etc.).

Node Info
---------

A collapsible sub-panel that appears when a node is selected in the graph. It displays:

- Node label, ID, and original name
- Input and output connection count
- ``Sync to 3D`` button: selects the corresponding object in the 3D viewport
- ``Show Neighborhood`` depth buttons (1, 2, 3)
- ``Show Full Context`` button

3D Viewport Sync Panel
-----------------------

A compact panel in the 3D Viewport (EM tab) that provides:

- ``Show EMGraph`` button: opens the graph in the Node Editor
- Active object display with human-readable name
- ``Sync`` button: centers the graph on the node corresponding to the selected 3D object
- Quick filter buttons: ``All`` and ``Strat`` (stratigraphic only)
- Neighborhood depth selector (1, 2, 3)

Workflow
--------

1. Enable Experimental Features in the :ref:`EMsetup` panel
2. Open the **Node Editor** and select the EM Graph node tree
3. Click ``All Nodes`` (or a filter preset) to load the graph
4. Choose a color scheme (e.g., ``Vibrant``) to colorize nodes by type
5. Select a node and use the neighborhood buttons to explore its relationships at different depths
6. Use the edge filters to focus on specific relationship types (e.g., only stratigraphic edges)
7. Click ``Sync Selection`` to jump between the 3D viewport and the graph
