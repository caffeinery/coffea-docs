Event API
========


Events are applied using the following example (basically standard NodeJS EventEmitter syntax):

.. code-block:: javascript

		client.on('EVENT', // `EVENT` being any of the events listed in the documentation.
		  function(event) { // callback function, called when event is fired
		    console.log('Something happened!');
		  });


Events
======

A list of the different events.


.. data:: message


The ``message`` event, fired when a standard IRC message is received.

Example:

.. code-block:: javascript

		// From README
		client.on('message', function (event) {
		  console.log('[' + event.channel.getName() + '] ' + event.user.getNick() + ': ' + event.message);
			event.reply('I logged to the console!'); // Says to the relevent user "I logged to the console!", either in PM or the channel.
		});

.. data:: cap_list
.. data:: cap_ack
.. data:: cap_nack

Fired when ``CAP`` is received from the server. (More information available at https://github.com/ircv3/ircv3-specifications/blob/master/specification/capability-negotiation-3.1)

Event attributes:

* ``capabilities``: The list of capabilities

.. data:: motd

The ``motd`` event, fired when the end of the MOTD (Message Of The Day) is received from the server.

Event attributes:

* ``motd``: The actual MOTD sent by the server.


.. code-block:: javascript

		// From README
		client.on('message', function (event) {
		  client.join('##test'); // autojoins a channel when properly connected
		});

.. data:: away

The ``away`` event, fired when a user is AWAY.

Event attributes:

* ``user``: A User object of the user that changed away status.
* ``message``: The message of the AWAY user's AWAY status.
