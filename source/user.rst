user api
========

.. class:: User(nick, client, network)

           :param string nick: The users nickname
           :param object client: Client object.
           :param object network: Network object.

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
