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

    client.on('quit', function (err, event) {
      console.log(event.user.getNick() + " quit: " + event.message);
    });


functions
---------

.. coffeafunction:: quit(message, network)

			  :param string message: The reason you want to show to others about why you quit.
			  :param object network: The network to execute the command on.
			  :param function fn: The callback function to be called when the call has been finished.

.. coffeafunction:: getServerInfo(network)

              :param object network: The network to execute the command on.
              :returns object serverInfo: The server info about the network.
