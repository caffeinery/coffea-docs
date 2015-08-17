.. include:: ./globals.rst

cap plugins
===========

.. warning:: This part of the documentation is a work in progress and might be incomplete.

events
------

.. coffeaevent:: cap_list
.. coffeaevent:: cap_ack
.. coffeaevent:: cap_nck

Fired when ``CAP`` is received from the server. (More information available at https://github.com/ircv3/ircv3-specifications/blob/master/specification/capability-negotiation-3.1)

Event attributes:

* ``capabilities``: The list of capabilities


.. coffeaevent:: extended-join

The ``extended-join`` event, fired when the client has the ``extended-join`` capability, and a user has joined a channel.

Event attributes:

* ``channel``: The channel the user joined.
* ``user``: The nick of the user.
* ``account``: The host of the user.
* ``realname``: The realname of the user.
