.. _aamod-newsite:

Start New Site
==============

- Full explanation of what needs to happen
- How to update configuration
- Heavy linking to previous resources in order to fully explain each step
- Tutorial: Deploy a hugo template


**New Website:**

It is important to understand that deploying a website, maintaining the website
itself, and maintaining the content on the website are three fundamentally
different challenges.

The instructions on this page cover the initial setup and require a level of
technical competency which may not be readily available; this should not stop
you! Please, reach out on `discord`_ if you need help.

Continued maintenance is primarily limited to content updates.

Prerequisite: DNS
-----------------

Domain Name Systems (DNS) are like a phone book for the internet. They tell your
computer/phone where to find a website. The number looks much different than a
phone number, but works exactly the same.

There are two primary options available for your domain name:

1. Use a subdomain of https://sober.page/:

   - Share your fork (if any) on `discord`_ and ask for help!
   - **OR** Create a `Pull Request <https://github.com/recoverysource/sober.page/tree/master/data/domains>`__
     with a new CNAME
   - **OR** Open an `Issue <https://github.com/recoverysource/sober.page/issues>`__
     with a link to your website project

2. Register your own domain using a "DNS Registrar":

   - The best options out there have shut down
   - This project transitioned from Porkbun (better interface) to Epik (better support/features)
   - A good rule of thumb is to avoid any service that offers to build your website (i.e. BlueHost)

   You will need these addresses if hosting on GitHub::

       A     @     185.199.108.153
                   185.199.109.153
                   185.199.110.153
                   185.199.111.153
       AAAA  @     2606:50c0:8000::153
                   2606:50c0:8001::153
                   2606:50c0:8002::153
                   2606:50c0:8003::153
       CNAME www   <username|project>.github.io.

Initial Setup
-------------

This assumes you have a Domain Name (DNS) picked out and need to go from looking
at a confusing repository to having a website published on the internet.

1. Create an account and log in to GitHub

   - You can (optionally) create a "github organization," which is functionally
     equivalent to a "team". This is not required to share your fork and can be
     set up later.

2. Make a copy of `hugo-website`_, giving it a meaningful name and description

   |github_start|

   - Choose ``Fork`` if you would like us to watch ``aamod`` for you (easier).
   - Choose ``Use this template`` to create a copy without the link (safer).

     E.g. |github_create|

3. Note: Actions are enabled by default, but these will fail until a valid
   configuration is created.

4. Copy any example content (without ``example-``) and update as appropriate:

   - ``example-config.yaml`` (live `sample config`_)

     + Focus on baseURL, title, descrition, phone, copyright, and aasites.

   - ``example-prebuild.yaml`` (live `sample prebuild`_)

     + Remove "example-" from the "meeting-data" and copy baseURL
     + Tweak "pdf-blurbs" to your liking

   - ``content/example-contact.md``

     + Remove line: ``draft: true``
     + Replace example content with your own

5. Update ``static/CNAME`` with the domain name (DNS) that was chosen earlier.
6. Create local meeting information in ``data/meetings.yaml``

   - This can optionally be broken into one meeting per file (see `Area 63 Meetings`_)

7. After making chanegs, wait for a successful build and deploy of your website
8. Open the ``Settings`` page of your repository then go to ``Pages`` and set ``Source`` to ``Branch[gh-pages]``
9. Verify DNS check in ``Settings>Pages`` passes before checking ``Enforce HTTPS``

.. _apikey:

Interactive Maps
----------------

If you do not want display Google Maps on your site, then you can put a ``#`` in
front of "mapapikey" (in your ``config.yaml``), similar to the comment above it.

The cost of this service is cumulative (across all sites), so we cannot provide
a generice key. However, anyone can register for an account and create an
`API Key <https://developers.google.com/maps/documentation/embed/get-api-key>`__.

GitHub will warn administrators about an API key being discovered in a
repository. This key cannot be kept secret and instead needs to be kept secure
using the following settings:

- Application restrictions: ``*<your-domain>/*`` (e.g. ``area63aa.org/*``)
- API restrictions: ``Maps Embed API``, ``Maps JavaScript API``, ``Places API``

.. _meeting-guide:

Meeting Guide App
-----------------

AAMod produces a JSON file that can be used by the `Meeting Guide`_ phone application.

This file will be available at: https://yourdomain.tld/meeting-times.json

Connecting your meeting information to this application requires filling out a
`connection form`_. Where it asks for ``Site Sharing Key``, the web address of
``meeting-times.json`` should be provided.

Security Updates
----------------

Most website vulnerabilities involve user authentication and authorization.
They attempt to find ways to act like an admin or bypass an admin check or
convince someone to share their password. Truly static websites do not suffer
these problems because there is no dynamic component to be exploited. You cannot
exploit that which is not present! (user authentication, file uploads, page
edits, etc.)

In other words ... there is nothing for you to be concerned about. A security
update for this project is currently inconceivable.

..
   _links:
.. _discord: https://discord.gg/hjTJSA7Ynu
.. _hugo-website: https://github.com/recoverysource/hugo-website
.. _sample config: https://github.com/area63aa/area63aa.org/blob/master/config.yaml
.. _sample prebuild: https://github.com/area63aa/area63aa.org/blob/master/prebuild.yaml
.. _Area 63 Meetings: https://github.com/area63aa/area63aa.org/tree/master/data/meetings
.. _Meeting Guide: https://www.aa.org/meeting-guide-app
.. _connection form: https://meetingguide.helpdocs.io/article/jsydw3bxw8-connection-form

..
   _images:
.. |github_start| image:: /static/images/newsite/2_github_start.png
.. |github_create| image:: /static/images/newsite/2_github_create.png
   :scale: 60%
