.. EPass documentation master file, created by
   sphinx-quickstart on Tue May 10 11:42:16 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to EPass's documentation!
=================================
**Epass** is a simple yet powerful password manager developed in Python.

Documentation of the API
=================================

.. toctree::
   :maxdepth: 5
   :caption: Contents:

API
=========

This package contains three modules:

* `DAODatabase`
* `data`
* `Encryption`

This modules contains all the data to connect to the database and perform the necessary queries.
The `Encryption` module implements two classes to encrypt and decrypt the password before insert them in the database with
the data that provides the other two modules.

DAODatabase
-----------
.. automodule:: API.DAODatabase
   :members:

data
-----------
.. automodule:: API.data
   :members:

Encryption
-----------
.. automodule:: API.Encryption
   :members:

TUI
=========

UIManager
----------
.. automodule:: TUI.UIManager
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
