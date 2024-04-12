.. _websites:

About Websites
==============

At a basic level, a website is just a very simple collection of text files with
special syntax and links to point to other files in the collection. The special
syntax tells web browsers how the file's content should be displayed.

For our purposes, a website is a place on the internet that lets you share
information about your group, but this definition does't explain anything about
how a website works or how/why anyone would be able to find it.

In order to understand what a website actually is, a few more foundational
concepts are required.

.. _ip:

Internet Protocol
-----------------

"The Internet" is a giant network of computers that are connected to each other.
This communication happens across "paths" that can be thought of as roads on a
map. These paths can be physical (network cable), wireless (wifi), or cellular
(cell).

"Internet Protocol" (IP) is the standard that defines how the computers on this
giant network talk to one another. IP provides a set of rules that define how a
computer gets an "IP address" on the network. This functions just like a
physical mailing address and allows one computer to address (talk to) another
computer on the network.

.. admonition:: Recap

   - Internet: Giant network of computers, like a road network.
   - IP: Addressing system that computers use to identify one another

For many years, internet traffic managed fine using the "IPv4" version of IP;
this version uses address that are like the street portion of a mailing address
(e.g. ``12 Main St``).

As the giant network grew, capacity was reached, and cracks started to form. In
2011, the pool of unallocated IPv4 addresses was officially depleated. To
resolve this, IPv6 was created.

From a very high level, IPv6 is very similar to IPv4, with a much longer address
format that includes extra features. This is very similar to using a full
mailing address, that includes street, zip, and country (e.g. ``Attn: Personal
Name, 12 Main Street, Cityville, Statestown, 12345, U.S.A.``)

.. admonition:: Check Point

   The following list contains (valid) IPv4 and IPv6 addresses; can you guess
   which addresses are IPv4 and which are IPv6?

   - 192.168.1.1
   - 2001:0bc4:9216:dead:beef:9a84:a158:34f7
   - 8.8.8.8
   - 210.133.240.120
   - 20:4:3::82
   - 2606:4700:3000::b44c
   - 127.47.30.4

   :sub:`Answer: Anything with a colon (:) is IPv6.`

Each version has their own features, but the knowledge that two versions exist
is sufficient for the remainder of this handbook.

.. _dns:

Domain Name System
------------------

Domain Name Systems (DNS) provide an address book of IP addresses. This allows
computers to find the IP address of a remote computer by telling it the "name"
of another computer that you are trying to find.

The proper term for the "name" of a computer is ``Fully Qualified Domain Name``
(FQDN). This is the "full name" of the computer, similar to a first and last
name.

.. admonition:: Recap

   Computers ask DNS for a FQDN and receive an IP address.

An FQDN can be looked at like a tree, with top level domains (TLDs) being the
trunk, domain names being the branches, and host names being the leaves.


**FQDN Examples:**

.. list-table::
   :header-rows: 1
   :widths: 40 20 30 10

   * - FQDN
     - Host Name
     - Domain Name
     - TLD

   * - www.google.com
     - www
     - google.com
     - com

   * - google.com
     - @
     - google.com
     - com

   * - drive.google.com
     - drive
     - google.com
     - com

   * - handbook.recoverysource.net
     - handbook
     - recoverysource.net
     - net

   * - aa0-1.sober.page
     - aa0-1
     - sober.page
     - page

   * - testbox1.devnet.example.com
     - testbox1
     - example.com
     - com

.. rst-class:: center

   :sub:`'@' is a common DNS symbol that indicates 'root domain name'`

Wikipedia provides `a good place <https://en.wikipedia.org/wiki/Fully_qualified_domain_name>`__
to dive deeper into this topic.

.. admonition:: Check Point

   DNS is an open directory; take some time and use `dig (online) <dig>`_ to
   query some names and observe the results.

   ::

       dig sober.page A
       dig google.com A
       dig www.google.com A
       dig google.com AAAA

.. _dig: https://toolbox.googleapps.com/apps/dig/

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
how to talk the web language, which happens to be HTTP (and HTTPS).

.. admonition:: Check Point

   What is the difference between an IP address and a port?

Web Servers
-----------

A web server is simply a computer on the internet that has a web specialist in
room #80, and maybe another in #443 if security is enabled. The job of a web
server is to receive requests for files and then return the content of those
files.

When a web browser is told to open a website, that computer will use the FQDN to
ask DNS for an IP address, and then send a request for a website file to Port 80
(or 443) at the address that was returned. The file returned uses special syntax
that a web browser can turn into a viewable page that a user can navigate.

In the early days, a web page was a single file with special syntax that told a
web browser how the page should be displayed and links pointing to other files
within the same domain, and sometimes linking to other websites. Each wep bage
is also able to link to other content, like pictures, which browsers will make
another follow-up request for.

.. admonition:: Recap

   User instructs their web browser to open a website
   Request is sent to DNS to ask for an IP address
   Address is returned from DNS
   Request is sent to web server at well-known port for a page
   Server returns the page requested
   Browser sees the page has an embedded image
   Browser sends another request for the image
   Server returns the image
   Browser displays the page

That's really all there is to website fundamentals! These are the building
blocks that will help you understand the remainder of this handook.
