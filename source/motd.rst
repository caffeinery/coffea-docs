.. include:: ./globals.rst

motd plugin
===========

events
------

.. coffeaevent:: motd

The ``motd`` event, fired when the end of the MOTD (Message Of The Day) is received from the server.

Event attributes:

* ``motd``: The actual MOTD sent by the server.

Example:

.. code-block:: javascript

    client.on('motd', function (event) {
    	console.log("Connected to " + event.network + ". MOTD: " + event.motd);
    	client.join('##test'); // autojoins a channel when properly connected
    });
