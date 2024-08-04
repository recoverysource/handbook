.. _hello-world:

Very Basic Site
===============

Although the ``index.html`` file from your :ref:`git repository <git-primer>`
is not valid HTML, browsers will render basic text as a text file. This means
that our existing ``git repo`` is already has everything needed to build a
website.

GitHub Pages
------------

To enabled ``GitHub Pages`` on this ``git repo``:

1. Navigate to your git project on GitHub
2. Click Settings (in the top menu)
3. Click Pages (in the side menu)
4. ``Source`` should already be set to ``Deploy from a branch``
5. Change ``Branch`` to ``main/master``
6. Click ``Save``
7. Periodically refresh the page, until ``Your site is live`` shows up:

.. image:: /static/images/basic/pages_setup.webp
   :align: center
   :width: 90%

8. Click ``View site`` to see how a web browser will render your ``index.html``:

.. image:: /static/images/basic/first_render.webp
   :align: center

Improving the Page
------------------

The page above is rendered from an ``index.html`` file that has only three lines
of text. We now want to replace this content with a proper :ref:`HTML page
<webpage>`.

Replace the content of ``index.html`` with the following::

    <!DOCTYPE html>
    <html>
    <head>
      <title>Home Page | DemoSite</title>
    </head>
    <body>
      <h1>Hello, World!</h1>
      <p>This <b>bold</b> exists within paragraph tags.</p>
    </body>
    </html>

Now create a high quality ``commit message`` and then ``push origin``. After a
few moments, your website will now be updated with these changes.

.. image:: /static/images/basic/second_render.webp
   :align: center

Second Page
-----------

With a valid ``index.html`` :ref:`HTML webpage <webpage>`, we can now create a
second file, named ``second.html``::

    <!DOCTYPE html>
    <html>
    <head>
      <title>Second Page | DemoSite</title>
    </head>
    <body>
      <h1>Page Number Two</h1>
      <p>This is a second page <a href="/">with a link</a> to the Home page.</p>
    </body>
    </html>

Add another set of paragraph tags to ``index.html`` with the following::

      <p>Check out <a href="/second.html">Page #2</a></p>

``GitHub Desktop`` should show the following ``diff``:

.. image:: /static/images/basic/second_diff.webp
   :align: center

Push these changes to GitHub and wait for your website to be updated.

Your website will now have two web pages with links back and forth!

.. image:: /static/images/basic/second_page.webp
   :align: center
   :width: 90%

.. _helloworld-recap:

Chapter Recap
-------------

At this point, you have now created a ``Static Website`` and put it onto the
:ref:`internet <internet>` using a :ref:`subdomain of github.io <fqdn>`
(``<subdomain>.github.io``). A second page was added and then both linked to
one another. You can even browse through each of these historical changes.

The complexity of maintaining these links grows exponentially as websites grow. 
Fortunately, :ref:`tools exist <jekyll>` to make this easier.
