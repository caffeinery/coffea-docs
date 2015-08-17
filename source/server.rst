.. include:: ./globals.rst

server plugins
==============

events
------

.. coffeaevent:: quit

The ``quit`` event, fired when the ``QUIT`` command is received from
the server. When this is fired someone has quit from the irc network.

Event attributes:

* ``user``: The affected user.
* ``message``: The quit message.


.. code-block:: javascript

    client.on('quit', function (event) {
        console.log(event.user.getNick() + " quit: " + event.message);
    });


functions
---------

.. coffeafunction:: quit(message, network)

			  :param string message: The reason you want to show to others about why you quit.
			  :param string network: The network to execute the command on.
			  :param function fn: The callback function to be called when the call has been finished.

Quit from the server.

Example:

.. code-block:: javascript

    client.quit("bye", event.network); // usage in an event listener
    client.quit("bye", "freenode"); // send to specific network
    client.quit("bye"); // send to all networks


.. coffeafunction:: getServerInfo(network)

              :param string network: The network to execute the command on.
              :returns object serverInfo: The server info about the network.

Get info about a network.

Example:

.. code-block:: javascript

    var info = client.getServerInfo(event.network); // usage in an event listener
    var info = client.getServerInfo("freenode"); // send to specific network
