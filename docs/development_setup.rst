Development Setup
=================

.. admonition:: Documentation in progress

   This section will describe how to set up a development environment for EM Tools.

See also the :doc:`installation` section for basic setup instructions.

When the s3Dgraphy datamodel changes
------------------------------------

EM Tools keeps no copy of the datamodel JSON files. It reads them from the
**s3dgraphy wheel it bundles**, which ``blender_manifest.toml`` lists under
``wheels/``:

- the graph editor's edge filter asks the library:
  ``graph_editor/utils.py`` ``get_connection_rules()`` calls
  ``s3dgraphy.edges.get_connections_datamodel()``, and ``with_spellings()`` asks
  it for the older spellings of each relation;
- ``graph_editor/socket_generator.py`` ``load_datamodels()`` opens the node and
  connections datamodels inside the installed package.

So a datamodel change reaches EM Tools only when the wheel is rebuilt. From the
EM-blender-tools repository, with the s3Dgraphy checkout beside it:

.. code-block:: bash

   ./em.sh rebundle            # rebuild the wheel from ../s3Dgraphy and verify it
   ./em.sh rebundle --check    # verify only

``rebundle`` verifies the wheel by content with ``python -m
s3dgraphy.tools.wheel_drift --check``, which fails when the bundled code is not the
code of the checkout, even when both declare the same version. If the wheel's file
name changed, regenerate the manifest too, with ``./em.sh manifest 3.11`` or
``./em.sh manifest 3.13``.

One part of the filter is still written by hand: the categories it groups edges
into (``STRATIGRAPHIC_RELATIONS`` in ``graph_editor/utils.py`` and the lists in
``graph_editor/properties.py``). A new edge type appears in the filter, but under
the "other" category until those lists name it. ``tests/test_graph_editor_spellings.py``
checks that the edge types come from the live datamodel.

The whole chain, from the datamodel JSON to every tool, is documented once in the
s3Dgraphy manual: `Datamodel propagation
<https://docs.extendedmatrix.org/projects/s3dgraphy/en/v1.6/DATAMODEL_PROPAGATION.html>`__.
