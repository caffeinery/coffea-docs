Welcome to coffea's documentation!
==================================

.. warning:: This documentation is a work in progress.

Contents
========

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

Quickstart
==========

This is all the code needed to get you started with coffea!

.. code-block:: javascript

    var client = require('coffea')(['chat.freenode.net', 'irc.oftc.net']); // or put just one network as a string
    
    client.on('motd', function (motd, network) {
        client.join(['#foo', '#bar', '#baz'], network);
    });
    
    client.on('message', function (event) {
        console.log('[' + event.network + '][' + event.channel.getName() + '] ' + event.user.getNick() + ': ' + event.message);
        //[freenode][#foo] nick: message
        event.reply(event.message); // I'm a parrot
    });

For more information about events, click here: :ref:`event`

With SSL
========

If you want to enable SSL for a connection, you have to use a network config object when connecting:

.. code-block:: javascript

    var client = require('coffea')({
        host: 'chat.freenode.net',
        ssl: true
    });

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
