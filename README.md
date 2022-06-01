# E-Pass

**E-Pass** is a simple password manger which uses a local [SQLite3](https://sqlite.org/index.html) database to store the passwords. The project
is developed purely in [Python](https://www.python.org/) and the documentation is built with [Sphinx](https://www.sphinx-doc.org/en/master/).

This project offers three types of applications: a TUI *Terminal User Interface*, a GUI *Graphical User Interface*
and a Web developed with the [Flask](https://flask.palletsprojects.com/en/2.1.x/) framework.

The user can decide which of these packages can use. The three packages uses the same database which is stored 
locally and uses the [cryptography](https://pypi.org/project/cryptography/) module to encrypt and decrypt the passwords.

- The `TUI` uses the [rich](https://pypi.org/project/rich/) module to render a prettier and clean prompt.
- For the `GUI` I have used the [Tkinter]() module which is built-in in Python.
- For the Web application I used the Flask framework and the app is deployed in an AWS server using Nginx.

To access to the Web application you only have to click in this link [https://epass.duckdns.org/](https://epass.duckdns.org/); if you 
want to see more documentation about the project you can check it out [here](https://e-pass.readthedocs.io/en/latest/).

