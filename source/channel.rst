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

.. coffeafunction:: getChannelList()

              :return array channelList: List of channels.

Get a list of channels.

.. coffeafunction:: getChannel(name, network)

              :param object name: The name of the channel you want to get.
              :param object network: The network to execute the command on.

Gets a channel by name.

.. coffeafunction:: isChannel(channel)

              :param object channel: The channel object you want to check.

Checks if the passed object is a valid channel object.

.. coffeafunction:: invite(name, channel, network, fn)

              :param string name: The name of the user you want to invite.
              :param object channel: The channel you want to invite him to.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Invites a user to a channel.

.. coffeafunction:: topic(channel, topic, network, fn)

              :param object channel: The channel you want to set the topic in.
              :param string topic: The topic you want to set.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Sets the topic of a channel.

.. coffeafunction:: join(channels, keys, network, fn)

              :param array channels: The channels you want to join.
              :param array keys: The keys for the channels you want to join.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Joins channels.

.. coffeafunction:: ircNames(channel, network, fn)

              :param array channels: The channel you want to get the nicknames from.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Gets users from a channel.

.. coffeafunction:: ircMode(target, flags, network, fn)

              :param string target: Target for the mode change, can be a user or channel.
              :param string flags: Flags of the mode change.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Sets modes.

.. coffeafunction:: ircKick(channels, nicks, msg, network, fn)

              :param array channels: The channels you want to kick from.
              :param array nicks: The nicks you want to kick.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Kick user from a channel.

.. coffeafunction:: ircPart(channels, msg, network, fn)

              :param array channels: The channels you want to kick from.
              :param string msg: The part message.
              :param object network: The network to execute the command on.
              :param function fn: The callback function to be called when the call has been finished.

Parts channels.
