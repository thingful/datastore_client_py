from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='iotstore_client',
    version='0.0.1',
    maintainer='Sam Mulube',
    maintainer_email='sam@thingful.net',
    url='https://github.com/thingful/iotstore_client_py',
    description='Python client for the DECODE encrypted datastore',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'protobuf',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
