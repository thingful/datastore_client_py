from setuptools import setup

setup(
    name='iotstore_client',
    version='0.0.1',
    maintainer='Sam Mulube',
    maintainer_email='sam@thingful.net',
    url='https://github.com/thingful/iotstore_client_py',
    description='Python client for the DECODE encrypted datastore',
    packages=['iotstore_client'],
    install_requires=[
        'protobuf',
    ],
)
