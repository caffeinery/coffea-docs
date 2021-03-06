.. include:: ./globals.rst

away plugin
===========

events
------

.. coffeaevent:: away

The ``away`` event, fired when an IRC AWAY event is received.

Event attributes:

* ``user`` - A User object of the user that changed away status.
* ``message`` - The message of the AWAY user's AWAY status (away message).

Example:

.. code-block:: javascript

    client.on('away', function (event) {
    	console.log(event.user.getNick() + ' is now away: ' + event.message);
    });


functions
---------

.. coffeafunction:: away(reason, network, fn)

              :param string reason: The reason to be away (away message).
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Sets the client as away on ``network`` with an away message (``reason``).

Example:

.. code-block:: javascript

    client.away("busy", event.network); // usage in an event listener
    client.away("busy", "freenode"); // send to specific network
    client.away("busy"); // send to all networks