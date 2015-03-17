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

.. coffeafunction:: getServerInfo(network)

              :param object network: The network to execute the command on.
              :returns object serverInfo: The server info about the network.
