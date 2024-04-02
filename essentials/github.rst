.. _github:

Working With Github
===================

Finding Repositories:

- How to find a repository
  Note link at the bottom of our web template points to their repository
- How to browse a repository and look at the contents of a file
- How to review the history of a file
- How to review history for the whole repository and review individual commits

Working With Git:

- Using a web interface to make changes
- Using Github Desktop to make a local copy
- Tutorial: Create README.md in (previous tutorial) an empty repository
  Note how this name is special and the contents saved show up like a repo front page


Register an Account
-------------------

In order to be granted access to make any changes, you must create an account.

1. Open https://github.com and click ``Sign up``:

   |github_homepage|

2. Provide basic account information:

   |github_create|

3. Check email and provide the temporary token:

   |github_token|

4. Either provide demographic information or click ``Skip personalization``:

   |github_demographics|

At this point, your account has been created and is ready for use.

You can now contact anyone in charge of the website you would like to help with
and provide your account name with a request for access.

Pull Requests
-------------

If you have not been provided access to a project and attempt to make changes on
a website, Github will automatically create a `Fork`_. This simply means your
account now owns a copy of the project, which means you are free to make any
changes to your copy.

After making changes to this copy, you can create a `Pull Request`_, which just
means you would like the main project to "absorb" your changes. Github provides
a web interface for this which is documented on their website.

Responsibility
--------------

After a project (website) administrator has given you access to their ``Team``,
you will likely be able to make changes directly to the website repository.

**NOTICE:** Most websites will automatically "build and deploy" (or "publish
the changes") with all file changes. Various safeguards exist to prevent
impacting a live/production website--the best safeguard is small/trivial updates
that can be easily explained (in the commit title/description).

**REMEMBER:** We may make mistakes, but we will promptly admit when we become
aware of mistakes we have made. We will recognize the earnest effort of others
and guide them through mistakes. Open communication will enable us to reach the
newcomer.

The :ref:`Code of Conduct <conduct>` used by this project is offered as a basic
template that aims to embody A.A. principles, including respect for others and
anonymity.

To accept this responsibility ...

1. Open https://github.com, select your user icon, and select ``Your Organizations``:

   |github_menu_org|

2. Select ``Join`` next to the organization/team you have been invited to:

   |github_org_list|

3. Read through the disclaimer and choose the appropriate option.

..
   _links:
.. _Fork: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks
.. _Pull Request: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with⇲-pull-requests/about-pull-requests

..
   _images:
.. |github_homepage| image:: /static/images/updatesite/1_github_homepage.png
.. |github_create| image:: /static/images/updatesite/2_github_create.png
.. |github_token| image:: /static/images/updatesite/3_github_token.png
.. |github_demographics| image:: /static/images/updatesite/4_github_demographics.png
.. |github_menu_org| image:: /static/images/updatesite/5_github_menu_org.png
.. |github_org_list| image:: /static/images/updatesite/6_github_org_list.png
