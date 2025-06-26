.. _project-internals:

Project Internals
=================

This page provides detailed internal information about our project. If you are
new to our documentation, this may not be the best place to :ref:`Get Started
<start>`.

Project Background
------------------

``Recovery Source`` was created to support groups who are struggling to reach
those who still suffer. The services we offer will remain free for all 12-Step
programs that wish to participate.

Our original goal was to provide a website solution that **anyone** can easily
deploy/maintain, without having to worry about cost, security updates, or
predatory services, allowing "website maintenance" to become a matter of
accurate record keeping.

.. _principles:

Core Principles
~~~~~~~~~~~~~~~

Our primary purpose is to support 12-Step Groups who are struggling to reach
those who still suffer. Above all else, we are lead by the 12th Step.

.. admonition:: The 12th Step of Alcoholics Anonymous

   Having had a spiritual awakening as the result of these steps, we tried to
   carry this message to alcoholics, and to practice these principles in all
   our affairs."

Financial Transparency
----------------------

The website solution developed to meet our original goal requires no financial
overhead and only requires that you provide a :ref:`domain name <def-dns>`.

Unfortunately, we found that predatory DNS (and over-priced services) are
extremely common, with multiple known instances of groups paying over $500/yr
on services which were not even utilized.

By accepting a certain amount of overhead, we are able to **fully** absorb
operational expenses related to owning a domain. This allows us a great amount
of flexibility to provide specialized support, but does require that we pay
for that overhead.

The financial disclosures presented in this section are meant to provide
assurance that 1) we can meet our operational expenses, 2) because we are are
effective stewards of financial resources.

.. _tradition-7:

7th Tradition
~~~~~~~~~~~~~

.. admonition:: The 7th Tradition of Alcoholics Anonymous

   Every A.A. group ought to be fully self-supporting, declining outside
   [financial] contributions.

In the same way that newcomers are encouraged to focus on their sobriety first
and foremost, we too wish for the groups we serve to focus on their outreach.

**We do not accept donations** from the groups we serve and encourage new group
members to contribute time and effort, rather than financial resources.

By following the 7th Tradition, we are able to prioritize reaching out to those
who still suffer. For more information, refer to our :ref:`Core Principles <principles>`.

.. _expensens:

Recurring Expenses
~~~~~~~~~~~~~~~~~~

Recovery Source strives for solutions with the lowest total cost of ownership,
focusing on both predictable billing and a high quality end-user experience.

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Cost
     - Item
     - Purpose

   * - $13/yr
     - Register recoverysource.net
     - Documentation, Demonstrations, Tests, Etc.

   * - $32/yr
     - Register sober.page
     - Top-level address for support group sites

   * - $20/yr
     - Register sobersupport.group
     - Non-premium URL, reserved as a backup for sober.page

   * - $51/yr
     - VPS
     - DNS forwarding service

   * - $0/yr
     - CloudFlare
     - Basic CDN and DDoS protection

Total: ``$100/yr``

.. _prudent-reserve:

Prudent Reserve
~~~~~~~~~~~~~~~

Registrar pricing is not entirely predictable, especially for premium domains,
making it wise to secure favorable prices for as long as possible, which ICANN
limits to ten years.

In order to maintain ``project balance of $0.00``, our prudent reserve is
limited to these non-refundable domain costs.

This table lists maximum contributions that can currently be accepted (from
project members):

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - Cost
     - Item

   * - $128
     - 4 yr Registration for https://sober.page/

.. _
   * - $0
     - 0 yr Registration for https://recoverysource.net/

   * - $0
     - 0 yr Registration for https://sobersupport.group/

   * - $0
     - Consider reimbursement or yearly memo

Last Updated: ``26 Jun 2025``

Service Level Agreement
-----------------------

It is important to note that this team is made up of volunteers who provide
their best effort and in good faith believe that their contribution meet the
standards of our :ref:`Core Principles <principles>`. We do not establish any
contractual agreements or provide any guaranteed level of service (or outcome).

If our service is deemed to be unsatisfactory, then the best recourse is verify
we do not have access to your website repository and verify `our index
<https://sober.page/>`__ redirects to your :ref:`domain <def-domain>`.

.. _conduct:

Code of Conduct
---------------

.. note::
   This Code is not exhaustive or complete. It is not a rulebook; it serves to
   distil our common understanding of a collaborative, shared environment and
   goals. We expect it to be followed in spirit as much as in the letter.

- Version: 1.0 [`view history <https://github.com/recoverysource/recoverysource.github.io/commits/master/code-of-conduct.rst>`_]

Recovery is about reaching those who are still suffering.

We want a productive, happy and agile community that can welcome new ideas in a
complex field, improve every process every year, and foster collaboration between
groups with very different needs, interests and skills.

We gain strength from diversity, and actively seek participation from those who
enhance it--we are people who normally would not mix. This code of conduct exists
to ensure that diverse groups collaborate to mutual advantage and enjoyment. We
will challenge prejudice that could jeopardise the participation of any person
in the project.

The Code of Conduct governs how we behave in public or in private whenever the
project will be judged by our actions. We expect it to be honoured by everyone 
who represents the project officially or informally, claims affiliation with
the project, or participates directly.

We strive to:

- **Be considerate**: Our work will be used by other people, and we in turn will
  depend on the work of others. The support provided by 12-Step Programes has
  helped many alcoholics avoid a low bottom and prevented many alcohol-related
  deaths. Any decision we take will affect users and colleagues, and we should
  consider them (future editors, newcomers, curious, etc.) when making decisions.
  Users may wish to remain anonymous for any number of reasons; it is not our
  place to decide what another person is comfortable sharing publicly or
  privately.

- **Be respectful**: Disagreement is no excuse for poor manners. We work together
  to resolve conflict, assume good intentions and do our best to act in an empathic
  fashion. We don’t allow frustration to turn into a personal attack. A community
  where people feel uncomfortable or threatened is not a productive one.

- **Take responsibility for our words and our actions**: We can all make mistakes;
  we understand that we can make mistakes just as easily as anyone else. We
  continue to take personal inventory and when we are wrong, promptly admit it.
  If someone has been harmed or offended, we listen carefully and respectfully,
  and work to right the wrong. We take only our own personal inventory.

- **Be collaborative**: What we produce is a complex whole made of many parts,
  it is the sum of many dreams. Collaboration between teams that each have their
  own goal and vision is essential; for the whole to be more than the sum of its
  parts, each part must make an effort to understand the whole.Collaboration
  reduces redundancy and improves the quality of our work. Internally and
  externally, we celebrate good collaboration. Wherever possible, we work closely
  with upstream projects and others in the free software community to coordinate
  our efforts. We prefer to work transparently and involve interested parties as
  early as possible--typically when a reasonable demonstration is available.

- **Value decisiveness, clarity and consensus**: Disagreements, social and
  technical, are normal, but we do not allow them to persist and fester leaving
  others uncertain of the agreed direction. We expect participants in the project
  to resolve disagreements constructively. When they cannot, we may seek
  guidance from structures with designated leaders to arbitrate and provide
  clarity and direction.

- **Ask for help when unsure**: Nobody is expected to be perfect in this
  community. Asking questions early avoids many problems later, so questions
  are encouraged, though they may be directed to the appropriate forum. Those
  who are asked should be responsive and helpful; those directed toward
  "beginner documentation" should not assume they are above reviewing it.

- **Step down considerately**: When somebody leaves or disengages from the
  project, we ask that they do so in a way that minimises disruption to the
  project. They should tell people they are leaving and take the proper steps
  to ensure that others can pick up where they left off. When possible,
  ownership/control should be shared across multiple roles/contributors.

- **Lead responsibly**: We all lead by example, in debate and in action. We
  encourage new participants to feel empowered to lead, to take action, and to
  experiment when they feel innovation could improve the project. Leadership
  can be exercised by anyone simply by taking action, there is no need to wait
  for recognition when the opportunity to lead presents itself.

- **Value discussion, data and decisiveness**: We gather opinions, data and
  commitments from concerned parties before making a decision. We expect leaders
  to help teams come to a decision in a reasonable time, to seek guidance or be
  willing to make the decision themselves when consensus is lacking, and to take
  responsibility for implementation.

  The poorest decision of all is no decision: clarity of direction has value in
  itself. Sometimes all the data is not available, or consensus is elusive. A
  decision must still be made. There is no guarantee of a perfect decision every
  time--we prefer to err, learn, and err less in future than to postpone action
  indefinitely. We remember the importance of taking responsibility for our word
  and actions.

- **Be an open meritocracy**: We invite anybody, from any walk of life, to
  participate in any aspect of the project. Our community is open, and any
  responsibility can be carried by any contributor who demonstrates the required
  capacity and competency.

- **Avoid drive from self-will**: We recognize that our own will is often flawed
  and littered with fear and selfish motivations. We take time to seek the
  advice from others whom we can go to for critical feedback. At times, we may
  need to dig in and do the work and hope that it was "the right thing," while
  understanding that the work may have "missed the mark." We recognize these as
  learning opportunities that pave the way for further growth. We do not forget
  that the ultimate goal is to reach the newcomer.

  A good leader does not seek the limelight, but celebrates team members for the
  work they do. Leaders may be more visible than members of the team, good ones
  use that visibility to highlight the great work of others.

  When in doubt, ask for a second opinion.

.. note::
   This Code of Conduct (CoC) is based on `Ubuntu Code of Conduct v2.0
   <https://ubuntu.com/community/ethos/code-of-conduct>`_ with various
   modifications intended to follow the spirit of `12-Step Programs
   <https://en.wikipedia.org/wiki/Twelve-step_program>`_.

   The Recovery Source Code of Conduct is licensed under the `Creative Commons
   Attribution-Share Alike 3.0 <https://creativecommons.org/licenses/by-sa/3.0/>`_
   license. You may re-use it for your own project, and modify it as you wish,
   just allow others to use your modifications and give credit to the Ubuntu and
   Recovery Source projects.
