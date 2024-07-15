.. _register-domain:

Domain Setup
============

In the :ref:`Website Primer <websites>` section, and for most of this handbook,
:ref:`DNS <dns>` is treated like one giant global directory listing of all
websites on the :ref:`Internet <internet>`. However, this is an extreme
simplification that focuses on how :ref:`end users <def-enduser>` interact with
this type of service.

As ":ref:`the website person <audience>`" for your 12-Step group, you will most
likely be responsible for maintaining your groups :ref:`domain <dns>` in this
global index.

.. _registrars:

Registrars
----------

A ``DNS registrar`` is a company that facilitates the registration and management
of :ref:`domain names <domain>` on behalf of individuals and organizations,
allowing them to manage :ref:`DNS information <dns>` on the :ref:`Internet
<internet>`.

Registrars handle the administrative tasks of domain registration, ensuring that
each domain is unique and properly configured in the :ref:`DNS system <dns>`.

.. admonition:: Further Reading

    Cloudflare provides a great explanation of how the `registrar/registry/tld
    <https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/>`__
    relationship works.

Reputable DNS registrars also provide a web interface that allows
:ref:`administrators <audience>` to manage :ref:`DNS Records <dns-records>`
within this global index. Most also provide the option to update Name Server
(NS) records, allowing a company other than the registrar to be responsible for
:ref:`DNS Records <dns-records>` that are presented to :ref:`end users
<def-enduser>`.

.. admonition:: Recap

   DNS is a distributed system, spread across thousands of organizations.
   Registrars allow consumers to register and maintain domain names within this
   global index.

.. _bad-registrars:

Predatory Registrars
~~~~~~~~~~~~~~~~~~~~

Unfortunately, **most** registrars engage in predatory practices, attempting to
upsell unnecessary services or charging inflated prices for renewals.

Common tactics to watch out for include:

- **Privacy Protection Fees**: Charging for "enhanced" privacy protection,
  despite `ICANN mandating privacy by default
  <https://www.icann.org/resources/pages/gtld-registration-data-specs-en/#temp-spec>`__,
- **Surprise Services**: Automatically enrolling customers in additional services
  like web hosting or backups without clear consent, often through pre-checked
  boxes during checkout.
- **Domain Fronting and Squatting**: Registering domains that users search for
  or similar variants, then selling them at inflated prices.
- **Domain Sniping**: Monitoring for domains that will expire soon in hopes the
  original owner will pay to get it back.
- **Renewal Price Hikes**: Increasing renewal fees significantly higher than
  initial registration costs.
- **Complicated Transfers**: Creating obstacles for transferring domains away
  from their service, making it seem "not woth the effort"--it is.

These registrars have been reported to engage in various predatory practices:

- **GoDaddy**: Aggressive and misleading marketing tactics for over-priced
  services with frequent price changes; known for domain sniping and fronting.
- **1&1**: Known for confusing pricing structures and non-responsive support.
- **Network Solutions**: Infamous for domain fronting and high renewal prices.
- **BlueHost**: Known for surprise services/fees and complicated transfers.
- **Hostinger**: Uses domain fronting/squatting and renewal price hikes.
- **Squarespace**: Aggressive upselling and complicated transfers.
- **Register**: Known for surprise services and hidden transfer fees.

As a general rule of thumb, any registrar that offers Wordpress websites as an
add-on service is likely worth avoiding.

.. _okay-registrars:

Reputable Services
~~~~~~~~~~~~~~~~~~

Nearly all registrars participate in some level of predatory behavior, making it
difficult to find reputable services. Although a "safe list" cannot be provided,
the subjective lists below aim to provide some critical review to begin your own
research.

**Registrars**:

- **Dynadot**: Provides a clean interface with transparent pricing and clearly
  labeled up-charges.
- **CloudFlare**: Offers DNS registration and renewal at registry cost, offering
  their registrar service for free, in exchange for using only their name
  servers.
- **Porkbun**: Offers transparent pricing with a simple and clean user
  interface, although customer service is terrible and renewal rates can be
  high.

**Turn-Key Websites** (also registrars, but with very limited DNS support):

- **inMotion Hosting**: Provides fully-managed Wordpress websites that include
  many optimally-configured caching features.
- **Pantheon**: Provides optimized websites using Drupal, rather than Wordpress.

.. admonition:: Recap

   It is important to research various forums for recent reviews to determine
   which registrar to do business with.

.. _fqdn:

Fully Qualified Domain Name
---------------------------

A Fully Qualified Domain Name (FQDN) consists of a series of labels separated by
dots. These are structured similar to a mailing address, with the Top-Level
Domain (TLD) on the far right, and then the Second-Level Domain (SLD) directly
to the left, followed by optional Subdomains.

Web browsers use this FQDN in the :ref:`URL <url>` they use to request a web
resource.

**FQDN Examples:**

.. list-table::
   :header-rows: 1
   :widths: 40 20 30 10

   * - FQDN
     - Subdomain (Hostname)
     - :ref:`Domain Name <dns>`
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

   * - site.dev.handbook.recoverysource.net
     - site.dev.handbook
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

   :sub:`'@' is a common DNS term (symbol) that indicates 'root (or naked) domain name'`


:ref:`Administrators <audience>` are generally free to manage their :ref:`DNS
records <dns-records>` as they see fit, creating whatever subdomains may be
needed.

.. note:: This is what enables Sober Page to offer :ref:`free "3rd-level"
   domains <domain>`, via sober.page (and sobersupport.group).

.. _dns-records:

Record Types
------------

Every :ref:`FQDN <fqdn>` placed into DNS is known as a "DNS Record." These
records have specific types that identify the exact type of information the
record contains.

These are the most common types of DNS records:

.. list-table::
   :header-rows: 1
   :widths: 10 20 70

   * - Type
     - Description
     - Purpose

   * - A
     - Address
     - Maps a domain name to an :ref:`IPv4 <ip>` address
   * -
     -
     - e.g. ``www.example.com`` points to ``192.0.2.1`` and ``93.184.215.14``

   * - AAAA
     - Quad-A
     - Maps a domain name to an :ref:`IPv6 <ip>` address
   * -
     -
     - e.g. ``www.example.com`` points to ``2001:0db8:85a3::8a2e:0370:7334``

   * - CNAME
     - Canonical Name
     - Maps an alias or alternative name for a domain to the actual domain
   * -
     -
     - e.g. ``example.com`` points to ``www.example.com``

   * - MX
     - Mail Exchanger
     - Specifies the mail server responsible for receiving email for a domain
   * -
     -
     - e.g. mail for ``example.com`` is handled by ``mx1.example.net``

   * - NS
     - Name Server
     - Specifies the computer name responsible for a domain
   * -
     -
     - e.g. ``example.com`` in managed by ``a.iana-servers.net.``

   * - TXT
     - Text
     - Stores text information about a domain, such as public keys
   * -
     -
     - e.g. ``_dmarc.example.com`` returns a string of public key data

Each FQDN can be represented by multiple DNS records. Both DNS records will be
returned to the computer making the request, which enables (round-robin) redundancy.

Follow Along
------------

For the following exercise, you can either use our domain and :ref:`DNS records
<dns-records>`, or you can lease a :ref:`domain <dns>` from a :ref:`registrar
<okay-registrars>` and configure your own :ref:`DNS records <dns-records>` to
look like ours.

Our **dnsdemo** DNS records:

.. image:: /static/images/essentials/dnsdemo_records.webp
   :alt: DNS records for dnsdemo.sober.page

In order to query DNS and validate records have been updated, we need either the
`dig command line utility`_, or an online option such as `google dig`_ or `dig
webUI`_.

.. _dig command line utility: https://linux.die.net/man/1/dig
.. _google dig: https://toolbox.googleapps.com/apps/dig/
.. _dig webUI: https://digwebinterface.com/

**Try these DNS queries for yourself!**

`dnsdemo.sober.page - TXT
<https://digwebinterface.com/?hostnames=dnsdemo.sober.page&type=TXT&ns=resolver&useresolver=1.1.1.1>`__::

    $ dig +short dnsdemo.sober.page TXT
    "Hello World!"
    "This is demonstration text for a TXT record. :)"

`dnsdemo.sober.page - A
<https://digwebinterface.com/?hostnames=dnsdemo.sober.page&type=A&ns=resolver&useresolver=1.1.1.1>`__::

    $ dig +short dnsdemo.sober.page A
    1.1.1.2

Chapter Recap
-------------

:ref:`DNS registrars <registrars>` allow :ref:`website administrators
<audience>` to manage :ref:`DNS records <dns-records>` on the
:ref:`Internet <internet>`. These records form the :ref:`FQDN <fqdn>` portion of
the :ref:`URL <url>` that users type into their web browser in order to view
your :ref:`website <websites>`.
