Recovery Source Handbook
========================

This repository holds the data used by sphinx-do to build
https://handbook.recoverysource.net/.

Repository Structure:

- ``README.rst``: This file.
- ``conf.py``: Configuration file for sphinx-doc (python3-sphinx)
- ``index.rst``: Front page of website and main menu (structure)
- ``_templates/``: Overrides to the furo theme
- [``Makefile``, ``CNAME``, ``.github``]: Magic stuff used by GitHub (ignore it)
- ``*``: Everything else is typically content for the website.

  Example: ``basic/website.rst`` -> https://handbook.recoverysource.net/essentials/websites.html
