Format plugin
=============

Formatting
----------

The format plugin is a bit special. You can use various formattings by using the `client.format` object.

.. code-block:: javascript

    event.reply(client.format.red + 'Roses are red.' + client.format.blue + 'Violets are blue.' + client.format.reset + 'And ZWSP' + client.format.zwsp + ' is invisible.');

The following colors and formatting options are available: https://github.com/caffeinery/coffea/blob/master/lib/plugins/format.js#L2-L23


Emoji
-----

We expose ``require('node-emoji').emoji`` via ``client.emoji``. See the node-emoji documentation for more information: https://github.com/omnidan/node-emoji


Kaomoji
-------

We expose ``require('node-kaomoji').kaomoji`` via ``client.kaomoji``. See the node-kaomoji documentation for more information: https://github.com/omnidan/node-kaomoji


Commands
--------

.. function:: unhighlight(message)
              
              :param string message: The message to be unhighlighted.
              :returns string message: Unhighlighted message (does not highlight users)
                                         

Adds ZWSP to a ``message`` to make sure it doesn't highlight anyone.