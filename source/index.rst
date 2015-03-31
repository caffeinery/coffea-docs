coffea documentation/api
========================

|NPM version (>=0.4)| |Build Status| |Dependencies| |Documentation
Status| |Code Climate|

.. |NPM version (>=0.4)| image:: https://img.shields.io/npm/v/coffea.svg?style=flat-square
   :target: https://browsenpm.org/package/coffea
.. |Build Status| image:: https://img.shields.io/travis/caffeinery/coffea/master.svg?style=flat-square
   :target: https://travis-ci.org/caffeinery/coffea
.. |Dependencies| image:: https://img.shields.io/david/caffeinery/coffea.svg?style=flat-square
   :target: https://david-dm.org/caffeinery/coffea
.. |Documentation Status| image:: https://readthedocs.org/projects/coffea/badge/?style=flat-square&version=latest
   :target: https://readthedocs.org/projects/coffea/?badge=latest
.. |Code Climate| image:: https://img.shields.io/codeclimate/github/caffeinery/coffea.svg?style=flat-square
   :target: https://codeclimate.com/github/caffeinery/coffea

`event based and extensible irc client library with multi-network support`

For support, report an issue on github or join our IRC channel at |##caffeinery @ chat.freenode.net|_

.. |##caffeinery @ chat.freenode.net| image:: https://img.shields.io/badge/IRC-irc.freenode.net%23%23caffeinery-00a8ff.svg?style=flat-square
.. _##caffeinery @ chat.freenode.net: https://webchat.freenode.net/?channels=%23%23caffeinery&uio=d4

If you want to support coffea, please consider donating: |gratipay.com/omnidan/|_

.. |gratipay.com/omnidan/| image:: https://img.shields.io/gratipay/omnidan.svg?style=flat-square
.. _gratipay.com/omnidan/: https://gratipay.com/omnidan/

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
   user
   channel
   message
   format
   motd
   welcome
   server
   cap
   away
   ping
   other
