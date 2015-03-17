welcome plugin
==============

events
------

.. coffeaevent:: welcome

The ``welcome`` event, fired when the ``RPL_WELCOME`` command is received from
the server. When this is fired ``client.me.nick`` gets set correctly and
``client.welcomed`` gets set to ``true``.

Event attributes:

* ``nick``: Your nick in the welcome message received from the server.
* ``message``: The rest of the welcome message.


.. code-block:: javascript

    client.on('welcome', function (err, event) {
      console.log("Welcome " + event.nick + ": " + event.message);
    });
