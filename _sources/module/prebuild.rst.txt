.. _aamod-prebuild:

Prebuild Generation
===================

The ``prebuild`` script builds content which hugo is not able to create.

Meeting Stubs
-------------

Hugo is `not able <https://github.com/gohugoio/hugo/issues/5074>`__ to generate
"new" pages from data sources. ``Prebuild`` can read :ref:`meeting data<meeting-format>`
from hugo's data source and generate stub files.

Printable PDF
-------------

This is a foldable PDF that is intended to be printed on two sides and then
folded twice, with Al-Anon meetings on one inner sheet and AA meetings on a full
inner sheet.

If there is enough interest, this can be broken into a separate repository and
turned into a more flexible design.

Live Example:

- `AAMod:meeting-schedule.pdf
  <https://aamod-demo.recoverysource.net/meeting-schedule.pdf>`__
- `SiouxFallsAA:meeting-schedule.pdf
  <https://siouxfallsaa.org/meeting-schedule.pdf>`__

----

Script Arguments
----------------

Arguments which define how ``prebuild`` is bootstrapped.

.. code-block:: text

    $ python3 ./prebuild.py -h
    usage: prebuild.py [-h] <optional arguments>

    options:
      -h, --help         show this help message and exit
      -c X, --config X   Configuration directory (default: ./prebuild.yaml)
      -r X, --runtime X  Runtime overrides for yaml configuration values (default: "{}")
      -v, --verbose      Use verbose logging

    basic example:
      python3 ../prebuild.py

    complicated example:
      prebuild.py -c ../prebuild.yaml --runtime '{"stub-path": "test/{shortcode}.md"}'

Configuration File
------------------

Configuration read from ``prebuild.yaml`` and merged with ``--runtime``.

**Default Values:**

.. code-block:: yaml

    # List of content to build
    builders: [stubs, pdf]

    # Location of meeting data (directory will be checked if .yaml is missing)
    meeting-data: data/meetings.yaml

    # Location of generated stubs
    # CAUTION: Any files matching this pattern will be purged before generation
    stub-path: content/meetings/{shortname}.md

    # Location of generated .pdf (and .tex)
    pdf-path: static/meeting-schedule.pdf

    # Number of columns used to display content
    pdf-cols:

      # Columns used on the second page (full sheet)
      aalist: 4

      # Columns used on the front (quarter sheet)
      anonlist: 2

    # Hide day-of-week header if there are no meetings within
    hide-empty:
      aalist: false
      anonlist: false

**Required Values:** (example provided)

The data below provides a functional example and was copied from `exampleSite
<https://aamod-demo.recoverysource.net/>`_. The ``pdf-blurbs`` section has `LaTeX
<https://typeset.io/resources/learn-latex-beginners-step-by-step-guide/>`_-formatted
data.

.. code-block:: yaml

    # Should be copied from hugo configuration (config.yaml)
    baseURL: https://aamod-demo.recoverysource.net/

    # Content that is dropped into the generated .tex file
    pdf-blurbs:

      # Image displayed in folded booklet
      image: themes/aamod/static/img/AAlogo.jpg

      # Helpline phone number
      helpline: 1-800-123-4567

      # Front cover of folded booklet
      front: |
        \vskip 2ex {\footnotesize If you have changes to this directory, please write to:}
        \vskip 1ex {\large Statestown Area Intergroup\\
        P.O. Box 1\\
        City, ST 42024}

      # Note above al-anon meetings (inside-right)
      alanon: |
        {\7pt Al-Anon members are people who are worried about someone with a drinking problem.}\\
        {\7pt\textbf{24-Hour Hotline:} (123) 456-7890}\\
        {\7pt\textbf{Al-Anon Information:} al-anon.org}

      # Links to additional resources on back of folded booklet
      resources: |
        {\7pt\textbf{Statestown Area:} aamod-demo.recoverysource.net/meeting-times}\\
        {\7pt\textbf{South Dakota State:} www.area63.org}

      # Informational box on bottom-right of back (second) page
      details: |
        \textbf{Statestown Area Intergroup}\\
        Meets at: Very Local AA\\
        {\6pt Every 2nd Sunday of the month at 4:30 PM}
