.. _Tapestry_Integration:

Tapestry Integration (Experimental)
===================================

The Tapestry Integration panel provides AI-powered photorealistic reconstruction capabilities. It connects to an external Tapestry server to submit rendering jobs that transform proxy-based scenes into photorealistic visualizations.

.. warning::
   This is an **experimental feature**. It requires Experimental Features enabled in the :ref:`EMsetup` panel.

The panel is located in the **EM Bridge** tab.

Panel Layout
------------

**Network Configuration** (collapsible):

- ``Server`` text field: Tapestry server address (IP or hostname)
- ``Port`` integer field: server port
- Connection status indicator: ``Connected`` or ``Disconnected``
- ``Test Connection`` button: validates server connectivity
- ``Open Tapestry Web UI`` button: opens the Tapestry dashboard in the browser

**Render Settings**:

- ``Camera`` dropdown: select the active camera for rendering
- ``Job Name`` text field with ``Generate`` button for auto-naming
- ``Epoch`` dropdown (Advanced EM mode only): select the temporal context
- ``Width`` and ``Height`` integer fields for render resolution
- ``Use Only Visible Proxies`` toggle: limits the render to currently visible geometry
- Epoch filter controls (Advanced EM mode only): enable/disable epoch-based filtering with status display

**Preview & Queue Management**:

- ``Visible Proxies: N objects`` counter
- ``Analyze Camera View`` button: scans the viewport and lists visible proxies with their visibility percentages (shows the first 5 objects)
- ``Render for Tapestry`` button (large): renders the scene and prepares the export
- ``Auto-submit to Server`` toggle: automatically sends the render to the Tapestry server after rendering
- Last export path display with ``Open Export Folder`` button

**Advanced Settings** (collapsible):

- Render engine info: ``Cycles (required)``
- ``Samples`` value: Cycles render samples
- ``Export Normals`` toggle: include surface normal data
- ``Keep Intermediate Files`` toggle: preserve temporary files for debugging

AI Generation Parameters:

- ``Model`` dropdown: AI model selection
- ``Steps`` value: number of denoising iterations
- ``CFG Scale`` value: classifier-free guidance strength
- ``Denoise Strength`` value: noise reduction intensity

Workflow
--------

1. Configure the network connection (server address and port) and test it
2. Select a camera and set the render resolution
3. Optionally select an epoch and enable epoch filtering (Advanced EM mode)
4. Click ``Analyze Camera View`` to verify which proxies are visible
5. Adjust the AI generation parameters if needed (model, steps, CFG scale, denoise strength)
6. Click ``Render for Tapestry`` to render the scene
7. If ``Auto-submit`` is enabled, the render is automatically sent to the server for AI processing
8. Access results via the Tapestry Web UI
