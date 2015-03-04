MOTD Plugin
===========

Events
------

.. data:: motd

The ``motd`` event, fired when the end of the MOTD (Message Of The Day) is received from the server.

Event attributes:

* ``motd``: The actual MOTD sent by the server.


.. code-block:: javascript

    client.on('message', function (event) {
      console.log("Connected to " + event.network + ". MOTD: " + event.motd);
      client.join('##test'); // autojoins a channel when properly connected
    });