format plugin
=============

formatting
----------

The format plugin is a bit special. You can use various formattings by using the `client.format.get()` function.

.. code-block:: javascript

    event.reply(client.format.get('red') + 'Roses are red.' + client.format.get('blue') + 'Violets are blue.' + client.format.get('reset') + 'And ZWSP' + client.format.get('zwsp') + ' is invisible.');

The following colors and formatting options are available: https://github.com/caffeinery/coffea/blob/master/lib/plugins/format.js#L2-L26


emoji
-----

We expose ``require('node-emoji').emoji`` via ``client.emoji``. See the node-emoji documentation for more information: https://github.com/omnidan/node-emoji


kaomoji
-------

We expose ``require('node-kaomoji').kaomoji`` via ``client.kaomoji``. See the node-kaomoji documentation for more information: https://github.com/omnidan/node-kaomoji


functions
---------

.. coffeafunction:: get(formatting)

              :param string formatting: The formatting to be inserted.
              :returns string formatting: Format characters that format the message.

The following colors and formatting options are available: https://github.com/caffeinery/coffea/blob/master/lib/plugins/format.js#L2-L26

Example:

.. code-block:: javascript

    client.on('message', function (event) {
    	event.reply(client.format.get('green') + '>' + event.message); // convert message to greentext
    });


.. coffeafunction:: unhighlight(message)

              :param string message: The message to be unhighlighted.
              :returns string message: Unhighlighted message (does not highlight users)

Adds ZWSP to a ``message`` to make sure it doesn't highlight anyone.
