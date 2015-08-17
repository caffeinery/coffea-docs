other plugins
=============

events
------

.. coffeaevent:: errors

The ``errors`` event, fired when IRC errors are received. List of possible errors: https://github.com/williamwicks/irc-replies/blob/master/replies.json#L113-L170

Event attributes:

* None

Example:

.. code-block:: javascript

    client.on('errors', function (event) {
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
