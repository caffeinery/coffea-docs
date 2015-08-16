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

`event based and extensible nodejs irc client library with multi-network support`

For support, report an issue on github or join our IRC channel at |#caffeinery @ chat.freenode.net|_

.. |#caffeinery @ chat.freenode.net| image:: https://img.shields.io/badge/IRC-irc.freenode.net%23caffeinery-00a8ff.svg?style=flat-square
.. _#caffeinery @ chat.freenode.net: https://webchat.freenode.net/?channels=%23caffeinery&uio=d4

If you want to support coffea, please consider donating (it helps me keeping the project active and alive!): |gratipay.com/omnidan/|_

.. |gratipay.com/omnidan/| image:: https://img.shields.io/gratipay/omnidan.svg?style=flat-square
.. _gratipay.com/omnidan/: https://gratipay.com/omnidan/

quickstart
==========

This is all the code needed to get you started with coffea!

.. code-block:: javascript

    var client = require('coffea')(['chat.freenode.net', 'irc.oftc.net']); // or put just one network as a string

    client.on('motd', function (event) {
        client.join(['#foo', '#bar', '#baz'], event.network);
    });

    client.on('message', function (event) {
        console.log('[' + event.network + '][' + event.channel.getName() + '] ' + event.user.getNick() + ': ' + event.message);
        //[freenode][#foo] nick: message
        event.reply(event.message); // I'm a parrot
    });
   
   client.on('command', function (event) {
       if (event.cmd === 'ping') { // respond to `!ping SOMETHING` with `SOMETHING`, or `pong`, if SOMETHING is not specified
           event.reply(event.args.length > 0 ? event.args.join(' ') : 'pong');
       }
   });


with ssl
--------

If you want to enable SSL for a connection, you have to use a network config object when connecting:

.. code-block:: javascript

    var client = require('coffea')({
        host: 'chat.freenode.net',
        ssl: true,
        // ssl_allow_invalid: true // uncomment this if the server has a self signed certificate, make sure to listen on('ssl-error') to catch bad certificates
    });


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

    client.on('event', function (event) {
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
