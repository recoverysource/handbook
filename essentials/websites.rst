.. _websites:

Website Primer
==============

At a basic level, a website is just a very simple collection of text files with
special syntax and links to point to other files in the collection. The special
syntax tells :ref:`web browsers <def-browser>` how a file (or "web page") should
be displayed.

For our purposes, a website is a place on the internet that lets you share
information about your group, but this definition does't explain anything about
how a website works or how/why anyone would be able to find it.

Some foundational knowledge is required in order to understand these basics, and
to troubleshoot issues that may be encountered. These foundations are similar to
understanding that vehicles need galosine for propulsion.

This chapter demystifies how websites and the Internet operate and lays the
groundwork for the remainder of this handbook.

.. _ip:

Internet Protocol
-----------------

"The Internet" is a giant network of computers that are connected to each other.
This communication happens across "paths" that can be thought of as roads on a
map. These paths can be physical (network cable), wireless (wifi), or cellular
(cell).

"Internet Protocol" (IP) is the standard that defines how the computers on this
giant network identify one another. IP provides a set of rules that define how a
computer gets an "IP address" on the network. This functions just like a
physical mailing address and allows one computer to address (talk to) another
computer on the network.

.. admonition:: Recap

   - Internet: Giant network of computers, like a road network.
   - IP: Addressing system that computers use to identify one another

For many years, internet traffic managed fine using version 4 of IP (IPv4);
this version uses address that are like the street portion of a mailing address
(e.g. ``12 Main St``).

As the giant network grew, capacity was reached, and cracks started to form. In
2011, the pool of unallocated IPv4 addresses was officially depleated. To
resolve this, IPv6 was released.

From a very high level, IPv6 is very similar to IPv4, with a much longer address
format that includes extra features. This is very similar to using a full
mailing address, that includes street, zip, and country (e.g. ``Attn: Personal
Name, 12 Main Street, Cityville, Statestown, 12345, U.S.A.``)

.. admonition:: Check Point

   The following list contains (valid) IPv4 and IPv6 addresses; can you guess
   which addresses are IPv4 and which are IPv6?

   - 112.18.1.1
   - 2001:0bc4:9216:dead:beef:9a84:a158:34f7
   - 8.8.8.8
   - 210.133.240.120
   - 20:4:3::82
   - 2606:4700:3000::b44c
   - 147.47.30.4

   :sub:`Answer: Anything with a colon (:) is IPv6.`

Each version has their own features, but the knowledge that two versions exist
is sufficient for the remainder of this handbook.

**Internet Superhighway:**

.. image:: /static/images/essentials/ip_highway.webp
   :alt: IP addresses plotted on a map

.. admonition:: Nerd Note

   The "rules of the road" that Internet traffic must follow to reach its
   destination are known as `TCP (stateful) and UDP (stateless)
   <https://www.cloudflare.com/learning/network-layer/internet-protocol/>`__.

.. _dns:

Domain Name System
------------------

Domain Name Systems (DNS) provide an address book that links computer "names" to
IP addresses. This is like a phone book that allows one computer to find out the
address of another computer using a human-friendly name.

The proper term for the "name" of a computer is ``Fully Qualified Domain Name``
(:ref:`FQDN <fqdn>`). This is the "full name" of the computer, similar to a first
and last name.

.. admonition:: Recap

   Computers ask DNS for a FQDN and receive an IP address.

Wikipedia provides `a good place <https://en.wikipedia.org/wiki/Fully_qualified_domain_name>`__
to dive deeper into this topic.

.. _port:

Ports and Services
------------------

When "internet traffic" reaches the computer at the IP address, that it found
from DNS, this "destination computer" needs to double check the address and then
determine how to repond.

Each computer on the internet is similar to an apartment building, with just a
very basic path to each individual apartment; most individual apartments are
empty, but a few have specialists that can respond to a specific type of
request.

Computers that have a specialist capable of responding to requests are known as
"servers," and the individual apartment they are located in is known as a "port."

.. admonition:: Recap

   Port numbers identify the specialist being requested from a given IP address.

In the same way standardized abbreviations exist to describe specific
specialties, standardized port numbers exist to describe specific services that
may be run by a server.

**Specialty Examples**:

.. list-table::
   :header-rows: 1

   * - Port
     - Abbreviation
     - Specialty
   * - \-
     - MD
     - Medical Doctor
   * - \-
     - PI
     - Private Investigator
   * - 53
     - DNS
     - Domain Name Services
   * - 80
     - HTTP
     - HyperText Transfer Protocol
   * - 443
     - HTTPS
     - HyperText Transfer Protocol (Secured)
   * - 25
     - SMTP
     - Simple Mail Transfer Protocol

When one computer makes a request to another computer, it will specify the
specialist that it needs to communicate with. If a specialist is available, then
they will send a response back.

The specialist that is responding to requests is known as a "service." Likewise,
a "web server" is simply a computer that runs a specialized service which knows
how to talk the web language, which is officially HTTP/S.

.. admonition:: Stop and Think

   What is the difference between an :ref:`IP address <ip>`
   and a :ref:`port <port>`?

.. _internet:

The Internet
------------

The Internet is vast, and website traffic is just one type of traffic. There are
many rules (standards) that govern how these services are expected to behave,
which enables all the different types of traffic to coexist in harmony. This is
similar to the rules (laws) that govern how people are expected to drive on a
road network.

This workflow covers the standards that will be used throughout this handbook:

0. Users will try to open a website using a computer
1. Computers use DNS to find the IP address of a website
2. DNS uses port 53 to query a global directory
    Such as Google DNS at 8.8.8.8 (for IPv4) or 2001:4860:4860::8888 (for IPv6)

    Or Cloudflare at 1.1.1.1 (for IPv4) or 2606:4700:4700::1111 (for IPv6)
3. Computers will use HTTP (or HTTPS) to contact the IP address that was returned
4. Web Servers at the other end of the connection will send back the website

.. admonition:: Stop and Think

   If (step 0) becomes a user opening an email client, how will steps 3 and 4
   also change?

.. _url:

Uniform Resource Locator
------------------------

In order to reach a specific page on a specific website on the vast internet, a
standardized format exist to identify how a specific resource should be
requested. This format is known as a Uniform Resource Locator (URL) and is
packed with lots of information.

The format for a URL is::

    scheme "://" [fqdn] path ["?" query] ["#" fragment]
    Note: Anything in square brackets is optional.

For example, the following URL points to **this** exact section of text:
  https://handbook.recoverysource.net/essentials/websites.html#url

- **scheme:** We want to talk to the ``https`` :ref:`"specialist" (or service) <port>`,
- **fqdn:** who resides at ``handbook.recoverysource.net``;
- **path:** we would like them to share a copy of ``/essentials/websites.html``,
- **fragment:** and we will jump to the ``url`` section.

.. admonition:: Stop and Think

   What is the full sequence of events a browser will take to resolve this fqdn
   and request the page (path) from the named service (scheme)?

.. _webpage:

Web Page
--------

In the earlier days of the Internet, HyperText Markup Language (HTML) was adopted
as the standard format that files use to describe how a web browser should display
each page (or :ref:`resource <url>`). This "markup" adds support for tags like
``<b>`` for bold or ``<ul>`` for unordered lists.

.. admonition:: Further Reading

   The `'History of HTML' chapter of 'Raggett on HTML 4' <web_history>`_
   provides a great place to start learning about this fascinating history.

Visit this `demonstration.html`_ page to see how the following HTML is displayed:

.. literalinclude:: ../static/demos/html/demonstration.html
   :language: html

.. admonition:: Recall

    At a basic level, a website is just a [collection of web pages] with
    syntax and links to point to other files in the collection. The special syntax
    tells web browsers how a file (or “web page”) should be displayed.

.. _css-intro:

Cascading Style Sheets (CSS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTML pages can also include CSS to change the "style" of various elements, such
as making all text in list items (``<li>``) use larger text, or adding a
background image to a page.

These CSS "style sheets" are often maintained in separate files, in order to
separate presentation from content.

For example, `demonstration_with_css.html`_ is exactly like `demonstration.html`_,
with the addition of ``<link rel="stylesheet" href="demonstration.css">``.

.. _js-intro:

JavaScript (JS)
~~~~~~~~~~~~~~~

HTML pages can also include JavaScript, which can be used to add dynamic
content 

such as making
interactive elements respond to user input or updating page content in real-time.

These files can also be be maintained in separate files. 
These JavaScript "scripts" are often maintained in separate files, in order to
separate syntax from content.

This `demonstration_with_js.html`_ example is exactly like `demonstration.html`_,
with the addition of ``<script>alert("Hello visitor!");</script>``.

.. admonition:: Recap

   A web page is a text file with HTML markup (tags) that tell a web browser how
   the file should be displayed to the user. These files often include other
   elements like CSS and JS to improve appearance and functionality of the
   website.

.. _dynamic-site:

Dynamic Websites
----------------

Maintaining a collection of HTML files by hand is tedious, time consuming, and
error-prone. Dynamic website solutions, like Wordpress, offer an alternative to
maintaining individual files.

This is additional software that runs on a web server and connects to a
database, which stores configuration for how every page should be displayed and
what the content of each page should be. These solutions also allow website
administrators to manage user accounts which can log in and make changes to the
website through the website itself.

Instead of a web service returning files exactly as they are stored, requests are
forwarded to a dynamic website solution that looks into a database to build the
requested page if the data exists. Most of these dynamic website applications
support user accounts, which can log into the website in order to add, remove, or
update website content.

While this approach introduces a tremendous amount of flexibility, it naturally
creates brand new classes of security vulnerabilities. Users can now be tricked
into exposing their credentials to a malicious website clone, or they can
unintentionally upload malicious content. The sheer volume of features means
that these projects also have a never-ending supply of currently-undiscovered
security flaws, many which do not require any user account to exploit.

.. admonition:: Recap

   Dynamic Websites use software that builds (or generates) each page at the time
   it is requested. This software often includes support for user accounts that
   can log in and create/edit/delete content on the website, through the website
   itself.

In order to prevent (often hidden) vandalism, it is critical that administrators
of dynamic websites apply updates as soon as they have been tested and review
logs to monitor for suspicious modifications. If a website is the victim of a
targeted attack, regular updates are unlikely to be sufficient and there will be
times when restoring from a backup is the only option, so it is also critical to
verify that the backup works and is not accessible to the compromised website.

.. _static-site:

Static Website
--------------

Static Site Generators (SSG) are a middleground between :ref:`Dynamic Websites
<dynamic-site>` and maintaining every :ref:`Web Page <webpage>` by hand. These
generators use text files, written in an easier-to-read markup language, and
then create all pages on a website, using template files to ensure everything
looks the same.

In other words, SSGs turn simple source material into the many :ref:` HTML pages
<webpage>` that make up :ref:`a complete website <websites>`.

For example, our earlier `demonstration.html`_ page could have been created from
this Markdown document:

.. literalinclude:: ../static/demos/html/demonstration.md
   :language: md

This approach ultimately generates :ref:`every page <webpage>` that a user may
want to visit and keeps the role of a :ref:`web service <port>` very simple.

.. admonition:: Recap

   Static Websites use Static Site Generators (SSG) to turn reader-friendly text
   files into computer-friendly HTML files using templates to ensure every page
   looks similar.

The lack of :ref:`dynamic web software <dynamic-site>` negates nearly all common
security risks and provides an inherently lightweight website, which many
platforms (such as `GitHub Pages`_, `Gitlab Pages`_, `Cloudflare Pages`_, etc.)
are happy to host for free, as an incentive to use their service.

Web Software
------------

There are **MANY** website generation options available, and each has their own
pros and cons. Generally, the more dynamic a product is, the more regular
security updates need to be a top priority.

`Dynamic and Static Website Security by S. Ranby <sranby>`_ provides a more
detailed comparison between static and dynamic website solutions.


.. list-table::
   :header-rows: 1

   * - Comparison
     - Static Website
     - Dynamic Website (self-hosted)
     - Hosted Wordpress
   * - Requires a :ref:`web service <port>` to return content
     - X
     - X
     - X
   * - Requires :ref:`additional software <dynamic-site>` to generate requested pages
     - 
     - X
     - X
   * - Typical cost for budget-friendly hosting
     - $0/yr
     - `$60/yr <https://www.linode.com/pricing/#compute-shared>`__
     - $300+/yr
   * - Initial learning curve
     - High
     - Medium
     - Low
   * - Maintainance difficulty/burden
     - Low
     - High
     - Medium
   * - Typical frequency of critical (security) issues
     - `Almost Never
       <https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=hugo>`__
     - `Never Ending
       <https://blog.cloudflare.com/application-security-report-q2-2023>`__
     - `Always Growing <https://wpscan.com/statistics/>`__
   * - Backups
     - :ref:`Part of version control <vcs>`
     - `Takes research & time
       <https://developer.wordpress.org/advanced-administration/security/backup/>`__
     - `GoDaddy charges $36/yr
       <https://www.godaddy.com/web-security/website-backup>`__

.. note::

   This handbook is primarily intended for users who wish to deploy our
   :ref:`Website Template <template>` which uses Hugo to build a static
   website. Remaining chapters will focus on this goal.

.. _website-tutorial:

Follow Along
------------

We are going to investigate https://example.com/:

1. Open `dig (online) <dig>`_ in a web browser
2. Type the domain (``example.com``) and locate the ``A`` record
3. This is the ``IP address`` our computer will use to talk to that website
4. Now open https://example.com/
5. Right-click on the empty background and choose ``View page source``
6. This is the actual :ref:`HTML webpage <webpage>` that the server returned to
   your browser
7. By the end of this handbook, you will understand how to read this file.

.. _website-recap:

Chapter Recap
-------------

A web server is another computer on the internet that has a :ref:`web specialist
<port>` in room #80, and maybe another in #443 if security is enabled. The job
of a web server is to receive :ref:`requests for files <url>` and then return
the content of those :ref:`HTML files <webpage>`.

Web browsers will use the :ref:`Uniform Resource Locator <url>`, found in the
"address bar," to look up an :ref:`IP address <ip>` and request a specific path
from the web service.

Some websites are :ref:`dynamic <dynamic-site>` and generate each page as it is
requested, while others are :ref:`static <static-site>` and generate all pages
any visitor may want to view while being published.

**The entire process from the perspective of a web browser:**

.. admonition:: Workflow of a Web Request

   1. User instructs their web browser to open a website
   2. :ref:`Browser normalizes the request <url>`
   3. :ref:`Computer asks DNS for an IP address <dns>`
   4. :ref:`IP address is returned from DNS <ip>`
   5. :ref:`Computer asks web service to return a web page <port>`
   6. :ref:`Web service returns the page requested <webpage>`
   7. Browser begins to construct the page
   8. Steps 3 through 7 are repeated for any extra content,
      such as :ref:`CSS <css-intro>`, :ref:`Javascript <js-intro>` or images
   9. The constructed page is delivered to the user

  .. image:: /static/images/essentials/web_request.webp
     :alt: Logical workflow of a web request

That's really all there is to website fundamentals! Having a basic understanding
of these building blocks will enable you to understand what is being done, why
it is done that way, how to adapt it to your needs, and how to troubleshoot
potential issues. This fundamental knowledge will also enable you to clearly
communicate issues when you run into problems that you cannot solve yourself.

..
   _links:
.. _dig: https://toolbox.googleapps.com/apps/dig/
.. _web_history: https://www.w3.org/People/Raggett/book4/ch02.html
.. _demonstration.html: https://handbook.recoverysource.net/_static/demos/html/demonstration.html
.. _demonstration_with_css.html: https://handbook.recoverysource.net/_static/demos/html/demonstration_with_css.html
.. _demonstration_with_js.html: https://handbook.recoverysource.net/_static/demos/html/demonstration_with_js.html
.. _XSS: https://www.cloudflare.com/learning/security/threats/cross-site-scripting
.. _srandby: https://srandby.org/digital-writing/index.html
.. _GitHub Pages: https://pages.github.com/
.. _Gitlab Pages: https://docs.gitlab.com/ee/user/project/pages/
.. _Cloudflare Pages: https://pages.cloudflare.com/
