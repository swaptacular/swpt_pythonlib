"""
Flask-SignalBus
---------------

Adds to Flask-SQLAlchemy the capability to *atomically* send messages
(signals) over a message bus.

The processing of each message involves three steps:

  1. The message is recorded in the SQL database as a row in a table.

  2. The message is sent over the message bus (RabbitMQ for example).

  3. Message's corresponding table row is deleted.

Normally, the sending of the recorded messages (steps 2 and 3) is done
automatically after each transaction commit, but when needed, it can
also be triggered explicitly with a method call, or through the Flask
CLI.
"""

from setuptools import setup

setup(
    name='Swpt-Pythonlib',
    version='0.10.6',
    url='https://github.com/swaptacular/swpt_pythonlib',
    license='MIT',
    author='Evgeni Pandurski',
    author_email='epandurski@gmail.com',
    description='A Python library used by many Swaptacular micro-services',
    long_description=__doc__,
    packages=[
        'swpt_pythonlib',
        'swpt_pythonlib.rabbitmq',
        'swpt_pythonlib.flask_signalbus',
    ],
    zip_safe=True,
    platforms='any',
    install_requires=[
        'Flask>=2.2.5,<4',
        'SQLAlchemy>=1.4.18,<3',
        'Flask-SQLAlchemy>=3.0.5,<4',
        'marshmallow>=3.10,<4',
        'pika>=1.3,<2',
    ],
    tests_require=[
        'pytest~=6.2',
        'pytest-cov~=2.7',
        'mock~=2.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
