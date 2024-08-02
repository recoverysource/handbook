.. _formats:

Document Formats
================

.. _html:

HTML
----

HyperText Markup Language is the standard language of the internet.

For example:

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>My First Webpage</title>
    </head>
    <body>
        <h1>Welcome to My Webpage</h1>
        <p>This is my <b>first</b> paragraph of text. I'm learning HTML!</p>
    </body>
    </html>

In this example, "first" is wrapped in "bold" tags and so a web browser will
display that text as bold:

.. code-block:: markdown

    This is my **first** paragraph of text. I'm learning HTML!

This format is not particularly friendly to newcomers, but it is what we must
work with. In order to make this easier, :ref:`static website generators
<static-site>` will read files that were written with a different format and
then produce :ref:`HTML files <webpage>` that web browsers can download and
understand.

.. _md:

Markdown
--------

Markdown (.md) is one of the most widely supported document formats that is
designed to become :ref:`HTML content <webpage>`.

Example Markdown:

.. code-block:: markdown

    **Best** Food:

    - Lettuce
    - Turnip
    - Pea

This becomes the following HTML:

.. code-block:: html

    <p><b>Best</b> Food:</p>
    <ul>
        <li>Lettuce</li>
        <li>Turnip</li>
        <li>Pea</li>
    <ul>

and will display as:

    **Best** Food:

    - Lettuce
    - Turnip
    - Pea

`Markdown Guide <https://www.markdownguide.org/basic-syntax/>`__ provides a
complete list of syntax that can be used and `Dillinger
<https://dillinger.io/>`__ provides an interactive website to watch how
changes impact the rendered page.

.. _rst:

RestructuredText
----------------

RestructuredText (.rst) serves the same general purpose as Markdown but uses a
different syntax to produce :ref:`HTML content <webpage>`.

Many basic formatting features are the same between Markdown and RST, and our
Markdown example from above is valid RST as well.

`The RST Spec <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`__
provides a complete list of syntax and FEAT provides an `online RST editor
<https://feat.dlup.link/rsted>`__ that can be used to see the result of changes.

.. _yml:

YAML
----

YAML (.yml) is designed to store information (data) in a way that is easy to
read and write.

For example, we could have file named ``recipes.yml`` with the content:

.. code-block:: yaml

   Peanut Butter Toast:
     ingredients:
       - item: bread
         quantity: 1 slice
       - item: peanut butter
         quantity: 1 Tbsp
     process:
       - Insert sliced bread into toaster
       - Toast to desired level and remove from toaster
       - Apply peanut butter to toast and smear

   Yogurt Parfait:
     ingredients:
       - item: yogurt
         quantity: 1 cup
       - item: granola
         quantity: 1/2 cup
       - item: mixed berries
         quantity: 1/2 cup
     process:
       - Combine ingredients into container
       - Mix until combines

Ansible provides `an explanation of YAML syntax
<https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html>`__.
For the purposes of this handbook, it is sufficient to understand that this
syntax requires paying close attention to details. Something as trivial as an
extra space, or using tabs, or a forgotten hyhpen/colon can break a document.

Use `Online YAML Parser <https://yaml-online-parser.appspot.com/>`__ to copy/paste
this example and experiment with making changes, like removing a leading spaces.

.. _formats-tutorial:

Follow Along
------------

Pull out ``GitHub Desktop`` and open the ``git repository`` from the :ref:`Git
Primer <git-primer>`, and remember to ``fetch`` any recent changes.

Update ``README.md`` so that it contains the following text:

.. code-block:: yaml

    My Demo
    =======

    This is a git playground for my personal experiments.

    Scratch Pad
    -----------

    The area below is a great place to play around with Markdown syntax.

    You can:

    - Make a list
    - Make **bold** text
    - Make *italic* text
    - Make **bold *and italic*** text

Commit any changes and push them to your git repository. Then open your
repository on https://github.com to see how these changes to ``README.md`` are
displayed.

.. image:: /static/images/essentials/markdown_demo.webp

.. _formats-recap:

Chapter Recap
-------------

There are many :ref:`document formats <formats>` that are built from ``plain
text`` files. Each have their own strengths, weaknesses, and use cases.
