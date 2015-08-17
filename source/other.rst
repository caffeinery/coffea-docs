.. include:: ./globals.rst

other plugins
=============

events
------

.. coffeaevent:: error

The ``error`` event, fired when any error happens.

Make sure to listen to ``error`` events to see possible errors/warnings:

.. code-block:: javascript

    client.on('error', function (err, event) {
        console.log(event.name, err.stack);
    });

You can also add the ``err`` parameter to any event listener (change from ``function (event)`` to ``function (err, event)``:

.. code-block:: javascript

    client.on('whois', function (err, event) {
        if (err) console.log("WHOIS ERROR:", err.stack);
        console.log("whois:", event);
    });


.. coffeaevent:: errors

The ``errors`` event, fired when IRC errors are received. List of possible errors: https://github.com/williamwicks/irc-replies/blob/master/replies.json#L113-L170

Event attributes:

* None

Example:

.. code-block:: javascript

    client.on('errors', function (err, event) {
        console.error('IRC Error:', err);
    });


functions
---------

.. coffeafunction:: pass(pass, network, fn)

              :param string pass: The password
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.


Sends an IRC PASS command to the network with the specified password (``pass``)

Example:

.. code-block:: javascript

    client.on('motd', function (event) {
        client.pass('pa$$w0rd', event.network);
    });


.. coffeafunction:: user(username, realname, network, fn)

              :param string username: The username
              :param string realname: The realname
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.


Sends an IRC USER command to the network with the specified username (``username``) and realname (``realname``).

Example:

.. code-block:: javascript

    client.on('motd', function (event) {
        client.user('username', 'Real Name', event.network);
    });


.. coffeafunction:: oper(name, password, network, fn)

              :param string name: The oper name
              :param string password: The oper password
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.


Sends an IRC OPER command and tries to oper to the network with the specified name (``name``) and password (``password``).

Example:

.. code-block:: javascript

    client.on('motd', function (event) {
        client.oper('opername', 'pa$$w0rd', event.network);
    });
