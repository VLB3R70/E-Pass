.. EPass documentation master file, created by
   sphinx-quickstart on Tue May 10 11:42:16 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to EPass's documentation!
=================================
**Epass** is a simple yet powerful password manager developed in Python.

Nowadays everyone uses web applications or desktop applications that needs a login to access it.
By this logic is pretty normal to have a plenty list of passwords to remember and most of them we don't remember it.
Even so, many people still use the same password for all their accesses. We all know the danger that this entails
and more and more people use password managers, either in a web portal or in a desktop application, to keep their
passwords safe.

That's the reason of why I decided to develop this application. But, why in Python?
Well, I recently started studying this amazing programming language and I was surprised by its simple syntax,
the large number of libraries it has either official or created by the community and the possible integrations
with other applications or frameworks such as Django or Flask - the last one is the one I used to create
the REST API.
The first programming language I studied was Java so finding such a simple language was very relieving for me.

Project planning and monitoring
-------------------------------

Technologies used
------------------

The principal technology used is ``Python``. I used three packages to add more functionalities to the project.

The `cryptography <https://pypi.org/project/cryptography/>`_ package is used for the encryption of character
strings with a generated `GPG` key; this package is very powerful and the encryption is pretty good,
in addition, it's implementation is very simple and the encryption of any password only uses a couple of code lines.

Example:

.. code-block::

   >>> from cryptography.fernet import Fernet
   >>> password = 'ThisIsATestPassword'
   >>> key = Fernet.generate_key()
   >>> f = Fernet(key)
   >>> encrypted_password = f.encrypt(password.encode('utf-8'))
   >>> print(encrypted_password)
   b'gAAAAABif-y7z_7cJ3pr2RhIeN45-jm7zIHdIW3CfjhFmcPU1UCAPdE8jQLcjZCYVc5z3-1qTTkuOr_igE0o_PxbRCElfgOiFm7hXJ1QB5gP-ZQKe5Y-kWE='
   >>>

Pretty difficult to guess the password! 😉



The `rich <https://pypi.org/project/rich/>`_ package is used to prompt a prettier Terminal User Interface.

Example:

.. code-block::

   ┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
   ┃ Selection number ┃ Description       ┃
   ┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
   │ 0                │ Show menu         │
   ├──────────────────┼───────────────────┤
   │ 1.               │ List user data    │
   ├──────────────────┼───────────────────┤
   │ 2                │ Select a password │
   ├──────────────────┼───────────────────┤
   │ 3                │ Add new entry     │
   ├──────────────────┼───────────────────┤
   │ 4                │ Update password   │
   ├──────────────────┼───────────────────┤
   │ 5                │ Update username   │
   ├──────────────────┼───────────────────┤
   │ 6                │ Delete an entry   │
   ├──────────────────┼───────────────────┤
   │ exit             │ Exit              │
   └──────────────────┴───────────────────┘
   Enter one of the options given:

With this package configure a TUI prompt is much easier! It also accepts `Markdown <https://www.markdownguide.org/>`_ files to prompt
them in the terminal.

The `pyperclip <https://pypi.org/project/pyperclip/>`_ package is simply used to copy the selected password by the user
in the clipboard.

Useful links
------------

* `Python <https://www.python.org/>`_

   * `cryptography <https://pypi.org/project/cryptography/>`_
   * `rich <https://pypi.org/project/rich/>`_
   * `pyperclip <https://pypi.org/project/pyperclip/>`_

* `Flask <https://flask.palletsprojects.com/en/2.1.x/>`_

   * `SQLAlchemy <https://flask-sqlalchemy.palletsprojects.com/en/2.x/>`_
   * `Flask WTF <https://flask-wtf.readthedocs.io/en/1.0.x/>`_
   * `Flask Login <https://flask-login.readthedocs.io/en/latest/>`_

* `SQLite3 <https://sqlite.org/index.html>`_

The IDE I used it's `Pycharm <https://www.jetbrains.com/pycharm/>`_ and I have developed everything on `GNU/Linux Ubuntu <https://ubuntu.com/>`_


Project structure
=================




Technical documentation
=======================

.. toctree::

   api
   tui
   gui
   rest

Check out the :doc:`api` section for more information about the API

