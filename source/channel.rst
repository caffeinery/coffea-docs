channel api
===========

.. class:: Channel(name, client, network)

           :param string name: The channel name
           :param object client: Client object.
           :param object network: Network object.

Create a new channel object.

.. function:: Channel.toString()

              :returns string hostmask: Hostmask of the channel.

.. function:: Channel.getName()

              :returns string Name: Name of the channel.

.. function:: Channel.getTopic()

              :returns string Topic: Topic of the channel.

.. function:: Channel.getNames()

              :returns object names: Nicks in the channel: ``{'nick': ['~']}``

.. function:: Channel.getNetwork()

              :returns string Network: Network of the channel.

.. function:: Channel.userHasMode(user, mode)

              :param object user: The user to check the mode of in the channel.
              :param string mode: The mode to check for.
              :returns boolean hasMode: ``true`` if specified user has specified mode.

.. function:: Channel.isUserInChannel(user)

              :param object user: The user to check.
              :returns boolean hasMode: ``true`` if specified user is in this channel.

.. function:: Channel.notice(msg)

              :param string msg: Notice message to send to the user.

.. function:: Channel.say(msg)

              :param string msg: Message to send to the user.

.. function:: Channel.reply(user, msg)

              :param object user: User to reply to.
              :param string msg: Message to send to the user.

.. function:: Channel.kick(user, reason)

              :param object user: User to kick from channel.
              :param string reason: Reason for the kick.

.. function:: Channel.ban(mask)

              :param string mask: Hostmask to ban.

.. function:: Channel.unban(mask)

              :param string mask: Hostmask to unban.

events
------

.. coffeaevent:: invite

The ``invite`` event, fired when someone gets invited by someone.

Event attributes:

* ``channel`` - Channel you got invited to.
* ``user`` - User who sent the invite.
* ``target`` - Invited user.

Example:

.. code-block:: javascript

		client.on('invite', function (err, event) {
		    console.log(event.target.getNick() + " got invited to "
                    + event.channel.getName() + " by " + event.user.getNick());
    });

.. coffeaevent:: topic

The ``topic`` event, fired when the topic gets changed. (or is originally sent)

Event attributes:

* ``topic`` - Current topic.
* ``user`` - User who changed the topic.
* ``time`` - Time of topic change.
* ``changed`` - ``true`` if topic was changed in this event.
* ``channel`` - Affected channel.
* ``network`` - Affected network.

Example:

.. code-block:: javascript

		client.on('topic', function (err, event) {
		    console.log(event.channel.getName() + ":", event.topic);
    });

.. coffeaevent:: join

The ``join`` event, fired when someone joins a channel.

Event attributes:

* ``user`` - User who joined.
* ``channel`` - Channel that was joined.

Example:

.. code-block:: javascript

		client.on('join', function (err, event) {
		    console.log(event.user.getNick() + " joined " + event.channel.getName());
    });

.. coffeaevent:: names

The ``names`` event, fired when getting users in the channel.

Event attributes:

* ``channel`` - Affected channel.
* ``names`` - List of users in the channel.

Example:

.. code-block:: javascript

		client.on('names', function (err, event) {
		    console.log(event.channel.getName() + ":", event.names);
    });

.. coffeaevent:: mode

The ``mode`` event, fired when a mode gets changed.

Event attributes:

* ``mode`` - Current mode.
* ``channel`` - Affected channel.
* ``by`` - User who changed the mode.
* ``argument`` - Mode argument.
* ``adding`` - boolean

Example:

.. code-block:: javascript

		client.on('mode', function (err, event) {
		    console.log(event.channel.getName() + ":", event.mode);
    });

.. coffeaevent:: kick

The ``kick`` event, fired when a user gets kicked.

Event attributes:

* ``channel`` - Affected channel.
* ``user`` - Affected user.
* ``by`` - User who changed the kick.
* ``reason`` - Reason for the kick.

Example:

.. code-block:: javascript

		client.on('kick', function (err, event) {
		    console.log(event.channel.getName() + ":", event.user.getNick(), "was kicked.");
    });

.. coffeaevent:: part

The ``part`` event, fired when a user parts a channel (channels).

Event attributes:

* ``user`` - Affected user.
* ``channels`` - Affected channels (channelList).
* ``message`` - Part message.

Example:

.. code-block:: javascript

		client.on('part', function (err, event) {
		    console.log(event.user.getNick(), "parted channels", event.channels);
    });


functions
---------

.. coffeafunction:: getChannelList(network)

              :param string network: The network to execute the command on.
              :return array channelList: List of channels.

Get a list of channels.

Example:

.. code-block:: javascript

    var channels = client.getChannelList(event.network); // usage in an event listener
    var channels = client.getChannelList("freenode"); // send to specific network
    var channels = client.getChannelList(); // get object of networks and channels


.. coffeafunction:: getChannel(name, network)

              :param string name: The name of the channel you want to get.
              :param string network: The network to execute the command on.

Gets a channel by name.

Example:

.. code-block:: javascript

    var channel = client.getChannel("#caffeinery", event.network); // usage in an event listener
    var channel = client.getChannel("#caffeinery", "freenode"); // send to specific network


.. coffeafunction:: isChannel(channel)

              :param object channel: The channel object you want to check.

Checks if the passed object is a valid channel object.

Example:

.. code-block:: javascript

    var channel = client.getChannel("#caffeinery", event.network); // usage in an event listener
    console.log(client.isChannel(channel)); // prints `true`


.. coffeafunction:: invite(name, channel, network, fn)

              :param string name: The name of the user you want to invite.
              :param string/object channel: The channel you want to invite him to.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Invites a user to a channel.

Example:

.. code-block:: javascript

    client.invite("omnidan", "#caffeinery", event.network); // usage in an event listener
    client.invite("omnidan", "#caffeinery", "freenode"); // send to specific network


.. coffeafunction:: topic(channel, topic, network, fn)

              :param string/object channel: The channel you want to set the topic in.
              :param string topic: The topic you want to set.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Sets the topic of a channel.

Example:

.. code-block:: javascript

    client.topic("#caffeinery", "welcome to caffeinery!", event.network); // usage in an event listener
    client.topic("#caffeinery", "welcome to caffeinery!", "freenode"); // send to specific network


.. coffeafunction:: join(channels, keys, network, fn)

              :param string/object/array channels: The channel(s) you want to join.
              :param string/array keys: The key(s) for the channel(s) you want to join.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Joins channels.

Example:

.. code-block:: javascript

    client.join("#caffeinery", event.network); // usage in an event listener
    client.join("#caffeinery", "freenode"); // send to specific network
    client.join(["#caffeinery", "#omnidan"], event.network); // join multiple channels

Example (Join password protected channels):

.. code-block:: javascript

    client.join("#caffeinery", event.network); // usage in an event listener
    client.join("#caffeinery", "freenode"); // send to specific network
    client.join(["#caffeinery", "#omnidan"], event.network); // join multiple channels


.. coffeafunction:: part(channels, msg, network, fn)

              :param string/object/array channels: The channels you want to kick from.
              :param string msg: The part message.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Parts channels.

Example:

.. code-block:: javascript

    client.part("#caffeinery", "byeee", event.network); // usage in an event listener
    client.part("#caffeinery", "byeee", "freenode"); // send to specific network
    client.part(["#caffeinery", "#omnidan"], "byeee", event.network); // part multiple channels


.. coffeafunction:: kick(channels, nicks, msg, network, fn)

              :param array/object/string channels: The channel(s) you want to kick from.
              :param array/string nicks: The nick(s) you want to kick.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Kick user from a channel.

Example:

.. code-block:: javascript

    client.kick("#caffeinery", "omnidan", "bye!", event.network); // kick user from specific channel
    client.kick(event.channel, "omnidan", "bye!", event.network); // kick user from current channel
    client.kick(["#caffeinery", "#omnidan"], "omnidan", "bye!", event.network); // kick user from multiple channels
    client.kick("#caffeinery", ["omnidan", "np_coffea"], "bye!", event.network); // kick multiple users from channel


.. coffeafunction:: names(channels, network, fn)

              :param string/object/array channels: The channel you want to get the nicknames from.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Gets users from a channel.

Example:

.. code-block:: javascript

    client.names("#caffeinery", event.network, function (names) {
      console.log(names);
    }); // usage in an event listener
    client.names("#caffeinery", "freenode, function (names) {
      console.log(names);
    }); // send to specific network
    client.names(["#caffeinery", "#omnidan"], event.network, function (names) {
      console.log(names);
    }); // get names from multiple channels


.. coffeafunction:: mode(target, flags, network, fn)

              :param string target: Target for the mode change, can be a user or channel.
              :param string flags: Flags of the mode change.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Sets modes.

.. note::

   You'll probably want to use the `umode` and `chanmode` functions instead of this function.

Example:

.. code-block:: javascript

    client.mode("omnidan", "+p", event.network); // set mode on specific user
    client.mode(client.me, "+p", event.network); // set mode on current client
    client.mode("#caffeinery", "+v omnidan", event.network); // voice a user in a specific channel
    client.mode(event.channel, "+v omnidan", event.network); // voice a user in the current channel


.. coffeafunction:: umode(flags, network, fn)

              :param string flags: Flags of the mode change.
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Sets modes on the current client.

Example:

.. code-block:: javascript

    client.umode("+p", event.network); // set mode on current client


.. coffeafunction:: chanmode(channel, mode, target, network, fn)

              :param string channel: Channel to change modes on.
              :param string mode: Consists of +/- and a mode character, e.g. `+v`, `-o`
              :param array/object/string target: Target for the mode change, can be (a) user(s) or channel(s).
              :param string network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Sets modes on a channel.

.. note::

   There are helper functions that work like `client.chanmode`, but without having to specify the `mode`: voice, devoice, op, deop, hop, dehop

Example:

.. code-block:: javascript

    client.chanmode("#caffeinery", "+v", "omnidan", event.network); // voice a user in a specific channel
    client.chanmode(event.channel, "+v", "omnidan", event.network); // voice a user in the current channel
    client.chanmode(event.channel, "+v", ["omnidan", "np_coffea"], event.network); // voice multiple users in the current channel

    // or using helper functions...
    client.voice("#caffeinery", "omnidan", event.network); // voice a user in a specific channel
    client.voice(event.channel, "omnidan", event.network); // voice a user in the current channel
    client.voice(event.channel, ["omnidan", "np_coffea"], event.network); // voice multiple users in the current channel

