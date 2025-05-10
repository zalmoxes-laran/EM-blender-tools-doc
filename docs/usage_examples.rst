Usage Examples
==============

This section provides practical examples of using EM Tools in various workflows.

Basic Workflow
--------------

Loading an Extended Matrix Graph
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open Blender with EM Tools installed
2. In the 3D Viewport, press ``N`` to open the sidebar
3. Navigate to the ``EM Setup`` panel
4. Click on the file path field and select your ``.graphml`` file
5. Click ``Reload`` to establish the connection
6. The summary table will show the loaded data

Connecting to DosCo Folder
^^^^^^^^^^^^^^^^^^^^^^^^^^

If your project uses a DosCo (Documentation Source Collection) folder:

1. In the ``EM Setup`` panel, locate the DosCo path field
2. Browse to your DosCo folder location
3. The system will automatically link documents to their corresponding nodes

Archaeological Workflow
-----------------------

Creating Stratigraphic Units
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Import your archaeological model
2. Use the ``US/USV Manager`` to create stratigraphic units
3. Assign proxies to each unit
4. Define temporal relationships in the ``Periods Manager``

Managing Epochs
^^^^^^^^^^^^^^^

1. Open the ``Periods Manager``
2. Define your chronological periods
3. Assign colors to each period for visual distinction
4. Use the soloing feature to isolate specific time periods

Reconstruction Workflow
-----------------------

Setting Up Reconstruction Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Import your base archaeological data
2. Create reconstruction models (RM) in separate collections
3. Use the ``RM`` section in ``Periods Manager`` to assign models to epochs
4. Toggle reconstruction visibility with epoch controls

Creating Multiple Hypotheses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Duplicate your reconstruction collection
2. Modify the alternative hypothesis
3. Assign to the same epoch with different properties
4. Use property nodes to document reasoning

Data Export
-----------

Exporting to EMviq
^^^^^^^^^^^^^^^^^^

1. Ensure all models are properly assigned to epochs
2. Navigate to ``Export Manager``
3. Fill in the EMviq export settings:
   
   - Project name
   - ATON path
   - User credentials
   
4. Choose export format (GLTF recommended)
5. Set texture compression settings
6. Click ``Generate full EMviq Project``

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
   - ``Periods`` - Colors proxies by chronological period
   
3. Adjust alpha transparency for better visibility
4. Use wireframe or solid modes for selected objects

Creating Labels
^^^^^^^^^^^^^^^

1. Add a camera to your scene
2. Orient it towards the objects to label
3. Select the proxies you want to label
4. In ``Visual Manager``, click the ``Ab`` button
5. Labels will be created in camera view
6. Use ``Collection`` button to organize labels

Statistical Analysis
--------------------

Volume Calculations
^^^^^^^^^^^^^^^^^^^

1. Select the objects to analyze
2. Use the Statistics panel to calculate:
   
   - Total volume
   - Volume by period
   - Volume by reconstruction certainty

Source Analysis
^^^^^^^^^^^^^^^

1. Navigate to the Statistics panel
2. Generate reports on:
   
   - Types of sources used
   - Source distribution by period
   - Property density analysis

Advanced Features
-----------------

Paradata Streaming
^^^^^^^^^^^^^^^^^^

1. Enable ``Paradata Streaming`` in the manager
2. Select a stratigraphic unit
3. The connected properties, extractors, and documents will filter automatically
4. Navigate through the information hierarchy

Graph Visualization
^^^^^^^^^^^^^^^^^^^

1. Use the Graph2Geometry feature to visualize:
   
   - Stratigraphic relationships
   - Temporal sequences
   - Source connections
   
2. Export graph visualizations for documentation

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