Usage Examples (text under review)
==============

This section provides practical examples of using EM Tools in various workflows.

Basic Workflow
--------------

Loading an Extended Matrix Graph
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open Blender with EM Tools installed
2. In the 3D Viewport, press ``N`` to open the sidebar
3. Navigate to the ``EM Data Tree`` panel
4. Click on the file path field and select your ``.graphml`` file
5. Click ``Reload`` to establish the connection
6. The summary table will show the loaded data

Connecting to DosCo Folder
^^^^^^^^^^^^^^^^^^^^^^^^^^

If your project uses a DosCo (Documentation Source Collection) folder:

1. In the ``EM Data Tree`` panel, locate the DosCo path field
2. Browse to your DosCo folder location
3. The system will automatically link documents to their corresponding nodes

Archaeological Workflow
-----------------------

Creating Stratigraphic Units
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Import your archaeological model
2. Use the ``Stratigraphy Manager`` to explore stratigraphic units
3. Assign proxies to each unit
4. Define temporal relationships in the ``Epochs Manager``

Managing Epochs
^^^^^^^^^^^^^^^

1. Open the ``Epochs Manager``
2. Define your chronological periods
3. Assign colors to each period for visual distinction
4. Use the visibility and selection toggles to isolate specific time periods

Reconstruction Workflow
-----------------------

Setting Up Reconstruction Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Import your base archaeological data
2. Create reconstruction models (RM) in separate collections
3. Use the ``RM Manager`` to assign models to epochs
4. Toggle reconstruction visibility with epoch controls

Creating Multiple Hypotheses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Duplicate your reconstruction collection
2. Modify the alternative hypothesis
3. Assign to the same epoch with different properties
4. Use property nodes to document reasoning

Data Export
-----------

Exporting to Heriverse
^^^^^^^^^^^^^^^^^^^^^^

1. Ensure all models are properly assigned to epochs
2. Navigate to ``Export Manager``
3. Fill in the Heriverse export settings:

   - Project name
   - Output folder path
   - Desired export options

4. Choose export format (GLTF recommended)
5. Set texture compression settings
6. Click ``Export Heriverse Project``

Exporting Tables
^^^^^^^^^^^^^^^^

To export data as CSV files:

1. Go to ``Export Manager``
2. In the Tables Export section, choose:

   - ``EM (csv)`` for complete export
   - ``US/USV`` for stratigraphic units only
   - ``Sources`` for documentation export

3. Select output directory
4. Click the export button

Visualization Techniques
------------------------

Using Display Modes
^^^^^^^^^^^^^^^^^^^

1. Open ``Visual Manager``
2. Choose display mode:

   - ``EM`` - Shows nodes by type with monochromatic materials
   - ``Epochs`` - Colors proxies by chronological period
   - ``Properties`` - Colors proxies by property values with customizable color ramps

3. Adjust alpha transparency for better visibility
4. Use wireframe or solid modes for selected objects

Creating Labels
^^^^^^^^^^^^^^^

1. Add a camera to the CAMS collection in your scene
2. Orient it towards the objects to label
3. Select the proxies you want to label
4. In ``Visual Manager``, expand the Label Tools section
5. Click ``Create Labels for Selected``
6. Labels will be created in camera view (press ``Numpad 0`` to see them)

Statistical Analysis
--------------------

Volume Calculations
^^^^^^^^^^^^^^^^^^^

1. Select the objects to analyze
2. Use the ``Export Statistics`` panel to calculate:

   - Total volume
   - Volume by period
   - Volume by reconstruction certainty

3. Click ``Export data in CSV`` to save the results

Advanced Features
-----------------

Paradata Streaming
^^^^^^^^^^^^^^^^^^

1. Enable ``Filter Paradata`` in the ``Paradata Manager``
2. Select a stratigraphic unit
3. The connected properties, extractors, and documents will filter automatically
4. Navigate through the information hierarchy

Graph Visualization
^^^^^^^^^^^^^^^^^^^

1. Enable Experimental Features in the ``EM Data Tree`` panel
2. Open the Node Editor and select the EM Graph node tree
3. Use the ``Graph Editor`` to visualize:

   - Stratigraphic relationships
   - Temporal sequences
   - Source connections

4. Use neighborhood view to explore node relationships at different depths

Tips and Best Practices
-----------------------

Organization
^^^^^^^^^^^^

- Use consistent naming conventions for proxies
- Organize models in collections by type
- Keep reconstruction models separate from evidence models
- Document uncertainties using property nodes

Performance
^^^^^^^^^^^

- Use proxy models for working, high-resolution for export
- Enable GPU instancing for repeated elements
- Optimize textures before final export
- Use LOD (Level of Detail) for large sites

Documentation
^^^^^^^^^^^^^

- Link all sources to their corresponding nodes
- Use extractors to document interpretation processes
- Create combiner nodes for synthesized information
- Export regular backups of your EM graph
