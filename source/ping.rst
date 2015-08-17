ping plugin
===========

events
------

.. coffeaevent:: pong

The ``pong`` event, fired when a ``PONG`` event was received from the server.

Event attributes:

* None.

Example:

.. code-block:: javascript

    client.on('pong', function (event) {
        console.log("PONG");
    });
