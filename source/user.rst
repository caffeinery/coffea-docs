user api
========

.. class:: User(nick, client, network)

           :param string nick: The users nickname
           :param object client: Client object.
           :param object network: Network object.

Create a new user on a network.

.. function:: toString()

              :returns string hostmask: Hostmask of the user.

.. function:: getNick()

              :returns string Nick: Nick of the user.

.. function:: getNetwork()

              :returns string Network: Network of the user.

.. function:: getUsername()

              :returns string Username: Username of the user.

.. function:: getRealname()

              :returns string Realname: Realname of the user.

.. function:: getHostname()

              :returns string Hostname: Hostname of the user.

.. function:: getAccountName()

              :returns string AccountName: AccountName of the user.

.. function:: getChannels()

              :returns object Channels: Channels of the user. ``{'#channel': ['~']}``

.. function:: getServer()

              :returns string Server: Server the user is connected to.

.. function:: getServerInfo()

              :returns string ServerInfo: ServerInfo of the Server the user is connected to.

.. function:: getAway()

              :returns boolean Away: Away status of the user.

.. function:: getAccount()

              :returns string Account: Account of the user.

.. function:: isRegistered()

              :returns boolean registered: Registration status of the user.

.. function:: isUsingSecureConnection()

              :returns boolean secureConnection: SSL status of the user (on/off).

.. function:: getIdle()

              :returns int Idle: Idletime of the user.

.. function:: getSignonTime()

              :returns string SignonTime: SignonTime of the user.

.. function:: isOper()

              :returns boolean oper: Oper status of the user.

.. function:: notice(msg)

              :param string msg: Notice message to send to the user.

.. function:: say(msg)

              :param string msg: Message to send to the user.

.. function:: whois(fn)

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

		client.on('nick', function (err, event) {
		    console.log(oldNick + " is now " + event.user.getNick());
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
              :param object network: The network to execute the command on.

Get a user object by nickname.

.. coffeafunction:: isUser(user)

              :param object user: The user object you want to check.

Checks if the passed object is a valid user object.

.. coffeafunction:: whois(target, network, fn)

              :param object target: The ``channel`` or ``user`` object to send this message to.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Send a whois request to the server.

.. coffeafunction:: identify(username, password, network, fn)

              :param string username: The username to identify with.
              :param string password: The password to identify with.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Identifies the user with nickserv.

.. coffeafunction:: nick(nick, network, fn)

              :param string nick: The nickname you want to use now.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Change your nickname to the specified nick.
