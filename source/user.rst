user api
========

.. class:: User(nick, client, network)

           :param string nick: The users nickname
           :param object client: Client object.
           :param string network: Network object.

Create a new user object.

.. function:: User.toString()

              :returns string hostmask: Hostmask of the user.

.. function:: User.getNick()

              :returns string Nick: Nick of the user.

.. function:: User.getNetwork()

              :returns string Network: Network of the user.

.. function:: User.getUsername()

              :returns string Username: Username of the user.

.. function:: User.getRealname()

              :returns string Realname: Realname of the user.

.. function:: User.getHostname()

              :returns string Hostname: Hostname of the user.

.. function:: User.getAccountName()

              :returns string AccountName: AccountName of the user.

.. function:: User.getChannels()

              :returns object Channels: Channels of the user. ``{'#channel': ['~']}``

.. function:: User.getServer()

              :returns string Server: Server the user is connected to.

.. function:: User.getServerInfo()

              :returns string ServerInfo: ServerInfo of the Server the user is connected to.

.. function:: User.getAway()

              :returns boolean Away: Away status of the user.

.. function:: User.getAccount()

              :returns string Account: Account of the user.

.. function:: User.isRegistered()

              :returns boolean registered: Registration status of the user.

.. function:: User.isUsingSecureConnection()

              :returns boolean secureConnection: SSL status of the user (on/off).

.. function:: User.getIdle()

              :returns int Idle: Idletime of the user.

.. function:: User.getSignonTime()

              :returns string SignonTime: SignonTime of the user.

.. function:: User.isOper()

              :returns boolean oper: Oper status of the user.

.. function:: User.notice(msg)

              :param string msg: Notice message to send to the user.

.. function:: User.say(msg)

              :param string msg: Message to send to the user.

.. function:: User.whois(fn)

              :param function fn: The callback function to be called when the call has been finished.


events
------

.. coffeaevent:: nick

The ``nick`` event, fired when someone changes nickname.

Event attributes:

* ``user`` - User who changed nick.
* ``oldNick`` - Their old nickname.

Example:

.. code-block:: javascript

    client.on('nick', function (event) {
        console.log(event.oldNick + " is now " + event.user.getNick());
    });


.. coffeaevent:: whois

The ``whois`` event, fired when the whois response is received from the server.

Event attributes:

* ``whoismap`` - ``{user: whois_data}``.

Example:

.. code-block:: javascript

    client.on('whois', function (err, event) {
        if (err) console.err("Couldn't whois:", err);
        console.log(event);
    });


functions
---------

.. coffeafunction:: getUser(nick, network)

              :param string nick: The user you want to get by nickname.
              :param string network: The network to execute the command on.

Get a user object by nickname.

Example:

.. code-block:: javascript

    var user = client.getUser("#caffeinery", event.network); // usage in an event listener
    var user = client.getUser("#caffeinery", "freenode"); // send to specific network


.. coffeafunction:: isUser(user)

              :param object user: The user object you want to check.

Checks if the passed object is a valid user object.

Example:

.. code-block:: javascript

    var user = client.getUser("#caffeinery", event.network); // usage in an event listener
    console.log(client.isUser(user)); // prints `true`


.. coffeafunction:: isMe(user)

              :param object user: The user object you want to check.

Checks if the passed object is the same user object as the client.

Example:

.. code-block:: javascript

    if (client.isMe(event.user)) {
        console.log("message was from me");
    } else {
        console.log("message was from somebody else");
    }


.. coffeafunction:: whois(target, network, fn)

              :param object target: The ``channel`` or ``user`` object to send this message to.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Send a whois request to the server.

Example:

.. code-block:: javascript

    client.whois("omnidan", event.network, function (event) {
        console.log(event.whois);
    }); // usage in an event listener

    client.whois("omnidan", "freenode", function (event) {
        console.log(event.whois);
    }); // send to specific network


.. coffeafunction:: identify(username, password, network, fn)

              :param string username: The username to identify with.
              :param string password: The password to identify with.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Identifies the user with nickserv.

Example:

.. code-block:: javascript

    client.on('motd', function (event) {
        client.identify("omnidan", "p@$$w0rd", event.network); // log in with nickserv
    });

You can specify this data in the config too like this:

.. code-block:: javascript

    {
      nickserv: {
        username: 'test',
        password: 'l33tp455w0rD'
      }
    }


.. coffeafunction:: nick(nick, network, fn)

              :param string nick: The nickname you want to use now.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Change your nickname to the specified nick.

Example:

.. code-block:: javascript

    client.on('motd', function (event) {
        client.nick("omnidan", event.network); // log in with nickserv
    });

You can specify this data in the config too like this:

.. code-block:: javascript

    {
      nick: 'omnidan'
    }

