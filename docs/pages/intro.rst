.. _intro:

Introduction
============

This library contains a minimal client library developed as part of the
`DECODE`_ project in order to provide a Python client for the encrypted
datastore component.

The purpose of this library is to enable a Python based client application to
easily read from and write to the encrypted datastore.

The datastore API is implemented using a simple RPC framework called `Twirp`_.
This framework uses protocol buffers as a transport layer, and provides a suite
of tools for generating server stubs as well as client bindings in a number of
programming languages and can be thought of as being akin to a simpler version
of `GRPC`_ but with fewer features and without the hard dependency on HTTP/2.

Because the client code is automatically generated from a set of protocol
buffer definitions, some aspects of the API might not be perfectly idiomatic
Python, but in general the affordances offered are fairly pythonic so should be
relatively straightforward to use.

.. _`DECODE`: https://decodeproject.eu/
.. _`Twirp`: https://github.com/twitchtv/twirp
.. _`GRPC`: https://grpc.io

License
-------

The library has currently been released under the `Apache 2.0 License`_. This
license is a permissive open source license that allows this code to be used
freely in either open source or proprietary, closed source software.

.. _`Apache 2.0 License`: https://www.apache.org/licenses/LICENSE-2.0

Install
-------

Some info on install
