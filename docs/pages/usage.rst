.. _usage:

Usage
=====

The client may be used to either read data from the encrypted datastore, or to
write data via the two API methods the datastore exposes.

Initializing Client
-------------------

A client instance can be initialized as follows::

    from datetime import datetime, timedelta

    from datastore_client.datastore_pb2_twirp import DatastoreClient

    # create our API client
    datastore_address = 'http://datastore:8080'

    # initialize a client instance for the given datastore address
    client = DatastoreClient(datastore_address)

.. important:: Currently the client does not require any authentication information
   to be be added when making requests, but this may change if the DECODE system
   requires this.

Reading Data
------------

Here's a code snippet showing how the library may be used in order to read data
from the encrypted datastore::

    from datetime import datetime, timedelta

    from datastore_client.datastore_pb2 import ReadRequest

    # we create a start_time of 1 hour ago
    start_time = datetime.utcnow() - timedelta(hours=1)

    # obtain the public key we are requesting data for
    public_key = 'BGBgTKU7ZJHRBl...'

    # construct our read request
    read_request = ReadRequest()

    # set the public key we are requesting data for
    read_request.public_key = public_key

    # set the start time from our datetime object
    read_request.start_time.FromDatetime(start_time)

    # set the page size we want to work with (max 1000)
    read_request.page_size = 100

    # now make the first request
    response = client.read_data(read_request)

    while True:
        for event in response.events:
            print(event.data) # encoded data requiring decryption
            print(event.event_time.ToJsonString())

        if response.next_page_cursor == "":
            break

        read_request.page_cursor = response.next_page_cursor
        response = client.read_data(read_request)


Note in the above code example we continue consuming data from the server until
it returns an empty value for ``next_page_cursor``. In a real application we
would need to decode the retrieved data for each ``event``.

Writing Data
------------

Here's a code example showing how the client library may be used to write
data::

    from datetime import datetime, timedelta

    from datastore_client.datastore_pb2 import WriteRequest

    # obtain the public key we are writing data for
    public_key = 'BGBgTKU7ZJHRBl...'

    write_request = WriteRequest()
    write_request.public_key = public_key
    write_request.data = b'encrypted bytes'
    write_request.device_token = 'abc123'

    client.write_data(write_request)
