.. include:: ./globals.rst

connection api
==============


.. class:: Client(info)

           :param object info: details for IRC connection

Initialise a server connection using the ``info`` parameter. ``info`` can be a javascript object representing server details or an array of multiple server details.

Example:

.. code-block:: javascript

    var client = Client({
        name: 'freenode', // Optional
        host: 'chat.freenode.net', // Required
        port: 6697, // Optional
        ssl: true, // Optional
        nick: 'nickname', // Optional, but will autogenerate nick if not specified
        username: 'test', // Optional
        realname: 'Testing Robot' // Optional
    });

.. coffeafunction:: add(info)

              :param object info: Details for new connection.
              :returns: The stream_id.

Add another network to an existing client, using the ``info`` parameter (as described at :js:class:`Client`), since the API supports multiple servers, more than one ``add`` calls can be specified throughout your program.

Multi-server example:

.. code-block:: javascript

    client.add([
        { // existing `Client` object
            host: 'chat.freenode.net', // required
            name: 'freenode',  // optional, but aids in identification, when referenced later in the program.
            nick: 'test', // optional, but will autogenerate nick if not specified
            ssl: true, // optional
            username: 'test', // optional
            realname: 'Testing Robot' // optional
        },
        {
            host: 'irc.oftc.net',
            name: 'oftc',
            nick: 'test2',
            ssl: false,
            username: 'test',
            realname: 'Testing Robot'
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
        realname': 'Testing Robot' // optional'
    });


.. coffeafunction:: write(str, network, fn)

              :param string str: The string to be written.
              :param string network: The network that the string shall be written to.
              :param function fn: The callback function to be called when the ``write`` call has been finished.
              :returns string stream_id: The stream ID from the call.


Writes raw data (``str``), to ``network``, when finished, calls ``fn``.


full config
-----------

For multiple networks, use a JavaScript array with multiple config objects inside.

.. code-block:: javascript

   var client = require('coffea')({
       host: 'chat.freenode.net',
       port: 6667, // default value: 6667
       ssl: false, // set to true if you want to use ssl
       ssl_allow_invalid: false, // set to true if the server has a custom ssl certificate
       prefix: '!', // used to parse commands and emit on('command') events, default: !
       channels: ['#foo', '#bar'], // autojoin channels, default: []
       nick: 'test', // default value: 'coffea' with random number
       username: 'test', // default value: username = nick
       realname: 'test', // default value: realname = nick
       pass: 'sup3rS3cur3P4ssw0rd', // by default no password will be sent
       nickserv: {
           username: 'test',
           password: 'l33tp455w0rD'
       },
       throttling: 250 // default value: 250ms, 1 message every 250ms, disable by setting to false
   });
