.. _vcs:

Version Control
===============

To summarize relevant take-aways from our :ref:`Website Primer <websites>`:

- ``Dynamic websites`` use a database system to modify the live website and then
  build each page at the time it is requested.
- ``Static websites`` generate a complete website with each change, with every
  single page a user might request already being generated prior to request.

Both options ultimately produce :ref:`a web page <webpage>` that a browser can
display. Content updates on dynamic websites tend to be much easier, but also
come at the cost of resources and security risk.

.. _editors:

Editors
-------

Content for static websites is typically stored in "plain text" file, using a
standardized format such as :ref:`Markdown (.md) <md>` or :ref:`RestructuredText
(.rst) <rst>`. These formats can be edited by :ref:`anyone <audience>` using
their favorite text editor.

Advanced editors include:

- `Vim <https://www.vim.org/about.php>`__
  is generally preferred by system developers and programmers
- `Emacs <https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html>`__
  is generally preferred by people that like many plugins and features
- `VScode <https://code.visualstudio.com/docs>`__
  is like a modern Emacs

Friendly editors include:

- `Notepad++ <https://notepad-plus-plus.org/>`__
  provides some helpful features for certain file types, like automatic spacing
- `Windows Notepad <https://apps.microsoft.com/detail/9msmlrh6lzf3>`__
  requires paying close attention to details like spacing, but it is probably
  already installed on your PC

.. warning::
   Although everything in this handbook /can/ be done from a phone, anyone
   deploying and maintaining a website is **highly** encouraged to use a regular
   computer--anything with a physical keyboard.

Version Control Systems
-----------------------

Using plain text to maintain website content means that ``Version Control
Systems (VCS)`` may be used to keep track of **all** changes made to the
website, essentially keeping track of every "version" of the website forever.

Rather than keeping an actual complete copy of every website, VCS keeps track of
the specific changes.

For example, in the following text file::

    Poem
    ----

    The quick brown fox
    jumps over the lazy dog

If a website editor changes ``fox`` to ``cow`` and ``lazy dog`` to ``moon``,
then the new file becomes::

    Poem
    ----

    The quick brown cow
    jumps over the moon

Rather than keeping track of this brand new file, version control systems will
keep track of only the words that were changed. This means that every change is
linked to the one that came before it.

After a website editor changes one (or more) files, VCS can compare existing
files against what was previously stored, and then save the difference into a
``commit``. These commits can be shared with others, ensuring that every other
copy can now have an exact copy of your new version.

.. _vcs-platform:

VCS Platforms
-------------

VCS platforms are "websites" that add extra functionality to VCS repositories.
They support collaboration with features like reporting/tracking issues and
reviewing proposed changes.

Many of these platforms also support automated website deployments using a
process known as ``Continuous Integration and Continuous Delivery (CI/CD)``.
These CI/CD processes follow "workflows" to automatically build the new website
version and then publish it to the internet after tests have succeeded.

.. note::
   This handbook (and project) use GitHub, and beginners are encouraged to stick
   with this, for now. Once familiar with the processes and terms, using an
   alternative like Gitlab will be exponentially easier.

Git
---

At a very basic level, a ``git repository`` (or ``repo``)  is a record of
changes. These records can then be "signed" by the author, and then uploaded to
a ``VCS platform``, that others can then download the change from. This allows
entire distributed teams to work collaboratively from the same ``repository``.

Each change that an author uploads is known as a ``commit``. When a change is
"committed" to the "git repository," that change becomes a permanent piece of
history, within that project.

.. _github-desktop:

GitHub Desktop
--------------


:ref:`Working with Git and GitHub <git-primer>` can be daunting for new
users, especially the first time a ``merge conflict`` is encountered--caused by
two people trying to make changes to the same word but not taking turns.

Applications like ``GitHub Desktop`` significantly reduce the learning curve by
guiding users through specific processes and providing additional information
when issues are encountered, often explaining how those issues can be resolved.

.. _vcs-tutorial:

Follow Along
------------

1. Download and install `GitHub Desktop <https://desktop.github.com/download/>`__
2. If you do not already have an account, choose ``Create your free account``
   and briefly skip to :ref:`Registering an Account <gh-register>` in the next
   section for help with this process.
3. Once you have a valid account, choose ``Sign in to GitHub.com``
4. Your browser will then open a web page in order to authorize the application
   to connect to your account.
5. Choose ``Continue`` and then ``Authorize desktop`` to effectively allow
   ``GitHub Desktop`` to make changes to any project you have access to.

.. _vcs-recap:

Chapter Recap
-------------

Version Control Systems allow teams of users to work on the same git repository.
