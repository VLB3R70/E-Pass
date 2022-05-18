TUI
===========

The TUI package implements the necessary functions to display a simple version of the app in the user terminal. This
package uses the `rich <https://pypi.org/project/rich/>`_ package to print a more prettier prompt than the one you can
make manually.

This package access to the database configured in the :doc:`core` package. This package also offers a simple login and
a menu with different options to perform like add a new password, list all the passwords of the user or modify one of them.

This package is installed as command-line entry on the user terminal- you can check more information in :doc:`installation` -
when installed, the user only has to enter ``epass`` and the login will prompt. It also adds another command named
``epass-help`` which will prompt a help of how to use the ``epass`` command. ``epass-help`` prompts the help text like if it was
a `Markdown <https://www.markdownguide.org/>`_ file! To exit the app the user just simply needs to enter ``Ctrl+C``

Example of the login prompt:

.. code-block::

    ________         ________
    |   ____|        |   __  |
    |   |__    ___   |  |__| |  __ _      ____   ____
    |   ___|  |___|  |  _____| / _` |    / __/  / __/
    |   |___         |  |      |(_| |  __\ \  __\ \
    |_______|        |__|      \__,_| |____/ |____/

    Welcome to a fast and smart password manager for the linux terminal lovers.




    1. Login.
    2. Create a new user
    3. Remember password [1/2/3]:


UIManager
----------
.. automodule:: TUI.UIManager
   :members:

TUIHelp
----------
.. automodule:: TUI.TUIHelp
   :members:
