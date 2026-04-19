.. _Server_Panel:

Server Panel (Experimental)
===========================

The Server Panel provides TCP connectivity for remote control of EMtools. It allows external applications to send commands to Blender via a TCP socket connection.

The panel is located in the **EM Bridge** tab and is available in Advanced EM mode.

Panel Layout
------------

**Status Display**:

- Shows the current server status: ``Status: ON`` or ``Status: OFF`` with a color-coded icon

**Configuration**:

- ``Host`` text field (default: ``localhost``)
- ``Port`` integer field (default: ``9001``)

**Control Buttons**:

- ``Start`` button: starts the TCP server on the configured host and port
- ``Stop`` button: stops the running server

Workflow
--------

1. Set the host address and port number
2. Click ``Start`` to begin listening for incoming connections
3. External applications can connect to the specified host:port and send UTF-8 encoded JSON commands
4. Click ``Stop`` to terminate the server

.. note::
   The server listens for connections on the configured port and accepts UTF-8 encoded commands (up to 1024 bytes per message). The command protocol is extensible for custom integrations.
