Event API
========


Events are applied using the following example (basically standard NodeJS EventEmitter syntax):

.. code-block:: javascript

		client.on('EVENT', // `EVENT` being any of the events listed in the documentation.
		  function(event) { // callback function, called when event is fired
		    console.log('Something happened!');
		  });


.. data:: message

The ``message`` event, fired when a standard IRC message is received.

Examples;

.. code-block:: javascript

		// From README
		client.on('message', function (event) {
		  console.log('[' + event.channel.getName() + '] ' + event.user.getNick() + ': ' + event.message);
		});


.. data:: motd

The ``motd`` event, fired when the end of the MOTD (Message Of The Day) is received from the server.

.. code-block:: javascript

		// From README
		client.on('message', function (event) {
		  client.join('##test'); // autojoins a channel when properly connected
		});
