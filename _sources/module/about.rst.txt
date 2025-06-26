.. _aamod:

About Hugo
==========

- Recap SSG
- Summarize Hugo and modules/themes

About AAMod
-----------

`AAMod`_ (``aamod``) is a website solution for Alcoholics Anonymous (A.A.)-related
website, with a focus on sharing meeting information in a fast and secure manner.

AAMod is a Subtheme for `Hugo`_ with some extra documentation, scripts, etc.
Hugo is a website framework that builds statically-generated websites. These
static websites are immune to the vast majority of new vulnerabilities, meaning
your website will only ever have to change/update for content or design.

This added documentation walks a user through deploying this website and hosting
it using `GitHub Pages`_. If you have decided you want what we  have
and want to avoid major hurdles to get there, then you are ready to take
:ref:`certain steps<aamod-newsite>`.

Website Bootstrap
-----------------

The `Hugo Template`_ repository holds a copy of ``exampleSite/``
with customization done to help bootstrap a brand :ref:`aamod-newsite`
This lets you skip a lot of requisite knowledge and get straight maintenance.

AAMod is a subtheme of `Mainroad`_. It can be used like any other theme with
the exception of requiring the Mainroad subtheme be loaded first. This parent
theme provides some great documentation which is not replicated here.

Features
--------

The primary feature of ``aamod`` is turning easily maintained meeting data
into content suitable for hugo to turn into a website.

- Build a json file suitable for use with `Meeting Guide`_
- Build pages for each meeting
- Build meeting schedule list (by time and by zip)
- Build meeting schedule pdf (printable)
- Maintains internationalization (i18n) support
- Config-customized sidebar menus
- Report list function embed a list of uploaded files, such as treasury reports

.. _Hugo: https://gohugo.io/
.. _Hugo Template: https://github.com/recoverysource/hugo-template
.. _GitHub Pages: https://pages.github.com/
.. _Area 63: https://area63aa.org/
.. _Mainroad: https://themes.gohugo.io/themes/mainroad/
.. _Meeting Guide: https://www.aa.org/meeting-guide-app
