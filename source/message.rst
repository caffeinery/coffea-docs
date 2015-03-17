message plugins
===============

events
------

.. coffeaevent:: message

The ``message`` event, fired when a standard IRC message is received.

Event attributes:

* ``user`` - User who sent the message.
* ``channel`` - Channel this message was sent to.
* ``message`` - The actual message.
* ``isAction`` - ``true`` if this was an action (/me).

Example:

.. code-block:: javascript

		// From README
		client.on('message', function (err, event) {
		  console.log('[' + event.channel.getName() + '] ' + event.user.getNick() + ': ' + event.message);
			event.reply('I logged to the console!'); // Says to the relevent user "I logged to the console!", either in PM or the channel.
		});


.. coffeaevent:: privatemessage

The ``privatemessage`` event, fired when an IRC private message is received.
Like a ``message``, but more private.

Event attributes:

* ``user`` - User who sent the message.
* ``message`` - The actual private message.
* ``isAction`` - ``true`` if this was an action (/me).

Example:

.. code-block:: javascript

		// From README
		client.on('privatemessage', function (err, event) {
		  console.log('[PM] ' + event.user.getNick() + ': ' + event.message);
			event.reply(':)'); // Says to the relevent user ":)", in PM
		});


.. coffeaevent:: notice

The ``notice`` event, fired when an IRC notice is received.
Like a ``message``, but more private.

Event attributes:

* ``from`` - User who sent the notice.
* ``to`` - Where this notice was sent to.
* ``message`` - The actual notice message.

Example:

.. code-block:: javascript

		// From README
		client.on('notice', function (err, event) {
		  console.log('[' + event.to + '] ' + event.from.getNick() + ': ' + event.message);
    });



functions
---------

.. coffeafunction:: send(target, msg, network, fn)

              :param object target: The ``channel`` or ``user`` object to send this message to.
              :param string msg: The message you want to send.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Send an IRC message to a channel or a user.


.. coffeafunction:: action(target, msg, network, fn)

              :param object target: The ``channel`` or ``user`` object to send this action to.
              :param string msg: The action you want to send.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Send an IRC action to a channel or a user. (This is the /me command)


.. coffeafunction:: notice(target, msg, network, fn)

              :param object target: The ``channel`` or ``user`` object to send this notice to.
              :param string msg: The notice you want to send.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Send an IRC notice to a channel or a user.
