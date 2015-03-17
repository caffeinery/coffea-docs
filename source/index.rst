coffea documentation/api
========================

quickstart
==========

This is all the code needed to get you started with coffea!

.. code-block:: javascript

    var client = require('coffea')(['chat.freenode.net', 'irc.oftc.net']); // or put just one network as a string

    client.on('motd', function (err, event) {
        client.join(['#foo', '#bar', '#baz'], event.network);
    });

    client.on('message', function (err, event) {
        console.log('[' + event.network + '][' + event.channel.getName() + '] ' + event.user.getNick() + ': ' + event.message);
        //[freenode][#foo] nick: message
        event.reply(event.message); // I'm a parrot
    });

For more information about events, click here: :ref:`event`


with ssl
--------

If you want to enable SSL for a connection, you have to use a network config object when connecting:

.. code-block:: javascript

    var client = require('coffea')({
        host: 'chat.freenode.net',
        ssl: true
    });


api
===

The best way to get started with coffea is playing around with it! You can use
the :ref:`genindex` to get a list of ``functions`` and ``events`` you can make use of.

**coffea function**: A function called with ``client.function()`` if coffea was
imported to ``client`` (see Quickstart)

.. code-block:: javascript

    client.function();

**coffea event**: You can listen to an event by defining an event listener like
this (make sure to replace ``event`` with the event name):

.. code-block:: javascript

    client.on('event', function (err, event) {
        if (err) throw err; // something bad happened!

        console.log(event); // do something with event here
    });

Go to `API reference`_ or browse the API by...

.. _API reference: genindex.html


plugins
-------

.. toctree::
   :maxdepth: 1

   connection
   event
   channel
   motd
   format
   cap
   away
   other
