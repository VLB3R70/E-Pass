REST
================

The REST package implements all the necessary modules to set up an API REST. The API REST have been developed with the
`Flask framework <https://flask.palletsprojects.com/en/2.1.x/>`_ and uses the `SQLAlchemy <https://flask-sqlalchemy.palletsprojects.com/en/2.x/>`_
ORM for the database operations, the `Flask login <https://flask-login.readthedocs.io/en/latest/>`_ package for login
operations and the `Flask WTF <https://flask-wtf.readthedocs.io>`_ package for the forms.

This package uses the database configured by the :doc:`core` package. It implements the necessary functions to `add`,
`modify` and `delete` password. For now, it will only access to the local database and the users stored there.

app
----------------

.. automodule:: REST.app
    :members:

models
----------------

.. automodule:: REST.models
    :members:

forms
-----------------

.. automodule:: REST.forms
    :members:

config
-----------------

.. automodule:: REST.config
    :members:

login
----------------

.. automodule:: REST.login
    :members:
