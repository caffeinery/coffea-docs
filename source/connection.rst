Connection API
==============


.. class:: Client(info) 

           :param object info: details for IRC connection

Initialise a server connection using the ``info`` parameter. ``info`` can be a javascript object representing server details or an array of multiple server details.

Example:

.. code-block:: javascript

    var client = Client({
        'name': 'freenode', // Optional
        'host': 'chat.freenode.net', // Required
        'port': 6697, // Optional
        'ssl': true, // Optional
        'nick': 'nickname', // Required
        'username': 'test', // Optional
        'realname': 'Testing Robot' // Optional
    });

.. function:: add(info)
              
              :param object info: Details for new connection.
              :returns: The stream_id.

Add another network to an existing client, using the ``info`` parameter (as described at :js:class:`Client`), since the API supports multiple servers, more than one ``add`` calls can be specified throughout your program.

Multi-server example:

.. code-block:: javascript

    client.add([{ // existing `Client` object
        host: 'chat.freenode.net', // required
        name: 'freenode',  // optional, but aids in identification, when referenced later in the program.
        nick: 'test', // required
        ssl: true, // optional
        username: 'test', // optional
        'realname': 'Testing Robot' // optional
        },
        {
        host: 'chat.freenode.net',
        name: 'freenode',
        nick: 'test2',
        ssl: false,
        username: 'test',
        'realname': 'Testing Robot'
        }
    ]);

Single-server example:

.. code-block:: javascript

    client.add({ // existing `Client` object
      host: 'chat.freenode.net', // required
      name: 'freenode',  // optional, but aids in identification, when referenced later in the program.
      nick: 'test', // required
      ssl: true, // optional
      username: 'test', // optional
      'realname': 'Testing Robot' // optional'
      })


.. function:: write(str, network, fn)
              
              :param string str: The string to be written.
              :param object network: The network that the string shall be written to.
              :param function fn: The callback function to be called when the ``write`` call has been finished.
              :returns string stream_id: The stream ID from the call.
                                         

Writes raw data (``str``), to ``network``, when finished, calls ``fn``.
                                  



