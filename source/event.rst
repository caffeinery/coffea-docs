event api
=========


Events are applied using the following example (basically standard NodeJS EventEmitter syntax):

.. code-block:: javascript

		client.on('EVENT', // `EVENT` being any of the events listed in the documentation.
		  function(err, event) { // callback function, called when event is fired
		  	if (err) console.error('Event error:', err);
		    console.log('Something happened!');
		  });

event object
------------

You may have noticed that we are passing an event argument to the event binding function. This is actually not just data but an object with an API to help you deal with events without hassle. Not all events are the same, so please check the various plugin documentations to see what events are available. The following functions and attributes are always available:

.. data:: network

The network this event was triggered in.

.. note:: The reply functions are only going to succeed when the ``channel`` or ``user`` attribute is available.

.. data:: reply(message)

Answer to a message (same channel/query as the event came from).

.. data:: replyAction(message)

Answer to a message with an action (``/me``).

.. data:: replyNotice(message)

Answer to a message with a notice.


core events
-----------

.. coffeaevent:: ssl-error

The ``ssl-error`` event, fired when there was an error establishing an SSL connection. If you're running with ``ssl_allow_invalid`` this event will still fire, but coffea will continue connecting to the server afterwards.

Event attributes:

* None

Example:

.. code-block:: javascript

		client.on('ssl-error', function (err, event) {
			console.error('SSL Error:', err);
		});


.. coffeaevent:: disconnect

The ``disconnect`` event, fired when the client was disconnected from a network.

Event attributes:

* None

Example:

.. code-block:: javascript

		client.on('disconnect', function (err, event) {
			console.log("We disconnected!");
		});
