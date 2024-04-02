.. _project:

Recovery Source
===============

**Recovery Source** provides a collection of tools that are meant to demystify
website maintenance, leaving :ref:`anyone <def-anyone>` with the skills required
to support :ref:`12-Step <def-12step>` groups.

:ref:`Our goal <principles>` is to help 12-Step groups reach out to those who
are still suffering.

.. _services:

**What We Provide:**

:ref:`Recovery Source Handbook <project>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`Get Started <start>`

*This* handbook is designed to take our :ref:`target audience <audience>` from
absolute beginner to a competent website administrator who is able to support a
website for their 12-Step group.

The documentation provided here covers the breadth of our projects and provides
the foundational knowledge required to understand how websites work and how all
of the pieces fit together.

:ref:`Sober Page <domain>`
~~~~~~~~~~~~~~~~~~~~~~~~~~

The primary purpose of ``Sober Page`` is to offer a free :ref:`domain name
<def-domain>` to 12-Step ``Sober Support Groups``, allowing them to easily
create a website and place it onto the internet using a standardized URL format
(ex. https\://**aa0**-**1**.sober.page for Area **0**, District **1** of **A.A.**).

This :ref:`domain solution <domain>` allows us to easily absorb the overhead
required to provide a :ref:`basic set of services <soberpage>`, which grants us
a tremendous amount of flexibility to resolve a wide variety of "common" issues.

With https://sober.page/, groups can avoid the cost and hassle of purchasing and
naming their own domain, or they can mix-and-match whatever works best in their
current situation.

:ref:`Website Template <template>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Live Demo <https://template-demo.recoverysource.net>`__

Our website template provides a "turn-key" website solution that enables you to
focus on little more than meeting accuracy. This removes many stumbling blocks
commonly seen on new websites, and allows us to ensure the accuracy of this
handbook.

Unlike website builders (wix, shopify, squarespace, etc.) or content management
systems (wordpress, drupal, etc.), our solution is based on a :ref:`Static Site
Generator (SSG) <def-ssg>`, which means the website can be hosted anywhere and
you can easily keep your own working copy as a functional backup of the live.

If any of this explanation sounds confusing but you still want what we have,
then please :ref:`Get Started <start>` with our handbook and :ref:`Ask Us
<support>` if something is not properly explained.

:ref:`AAMod Plugin <aamod>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Our Features <https://aamod-demo.recoverysource.net>`__
- `Mainroad Features <https://mainroad-demo.netlify.app>`__

The real heavy lifter behind our template is ``AAMod``, which improves
accessibility and adds website features built to serve the needs of 12-Step
groups.

Many of these features are written in a way that should enable them to be easily
re-used in other projects with very few modifications.

.. note::
   - Hugo is a :ref:`Static Site Generator (SSG) <def-ssg>`.
   - Mainroad is a clean and lightweight "theme" for Hugo.
   - AAMod is designed as a "sub-theme" of Mainroad.
   - AAMod functions as both a Hugo theme, and as a set of helper scripts.

.. _support:

Support
-------

If you struggle to follow this handbook, we encourage you to first take a break,
go for a walk, and then return to :ref:`Getting Started <start>`. Our goal is
to teach you everything, so if there's something we missed, please let us know
using this `Discord Link`_.

Not all things can be answered in documentation, especially if you would like us
to help with maintenance tasks; our `Discord Link`_ is open to all who wish to
support 12-Step sober support group websites.

.. _Discord Link: https://discord.gg/hjTJSA7Ynu>

..
   _menu:

.. toctree::
   :hidden:
   :includehidden:
   :caption: Our Project

   self
   project/internals
   project/getting-started
   project/glossary

.. toctree::
   :hidden:
   :includehidden:
   :caption: Essentials

   essentials/websites
   essentials/domains
   essentials/version_control
   essentials/github
   essentials/markdown
   essentials/yaml
   essentials/commits

.. toctree::
   :hidden:
   :includehidden:
   :caption: Our Domain Solution

   domain/about
   domain/services
   domain/address
   domain/email

.. toctree::
   :hidden:
   :includehidden:
   :caption: Your First Website

   basic/website
   basic/jekyll

.. toctree::
   :hidden:
   :includehidden:
   :caption: Our Website Template

   template/about
   template/new
   template/setup
   template/meeting
   template/page
   template/event
   template/menu
   template/update

.. toctree::
   :hidden:
   :includehidden:
   :caption: Our Template Plugin

   module/about
   module/features
   module/format
   module/prebuild

.. toctree::
   :hidden:
   :includehidden:
   :caption: Helping Others

   helping/issues
   helping/pulls

.. toctree::
   :hidden:
   :includehidden:
   :caption: Developer Corner

   guide/principles
   guide/hugo-themes
   guide/html
   guide/css
   guide/actions
