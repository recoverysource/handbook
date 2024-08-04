.. _update-event:

Update Event Page
=================

- Reference basic page updates
- Reference Markdown syntax guide
- Show examples of links to documents
- Explain changing the link to an embedded resource
- Tutorial: Create a new event with an embedded "flyer" (pdf)

Create an Event
---------------

To create an event:

1. Navigate to your project:

   |repo_front|

2. Select ``content``, then ``events``:

   |repo_content|

3. The easiest way to proceed is to copy/paste an existing or example document:

   |repo_events|

4. Select the chosen source document and click the ``Display the source blob`` button:

   |repo_examplefile|

5. Highlight the document and "copy". If this is challenging, the ``Raw`` button
   will provide a "plain text" version that is easier to use.

   |repo_exampleraw|

6. Back in the ``events`` directory, choose ``Add file > Create new file``:

   |repo_newfile|

7. Paste the starting file contents into the large box and provide a filename
   above.

.. note:: This filename should NOT include spaces, keep it simple with numbers,
   lowercase letters, hyphens, and underscores. The filename *MUST* end with
   ``.md``.

   |repo_newfile|

8. Update the content as appropriate and provide a short explanation of the
   change that is being made:

   |repo_editfile|

9. After clicking the ``commit`` button, you can click ``Actions`` to observe
   the website update "build" process:

   |actions_home|

10. Once complete, green checkmarks will be displayed:

   |actions_succeess|

11. Your changes will now be available for the world to view:

   |site_event|

.. _yaml: https://www.redhat.com/en/topics/automation/what-is-yaml

..
  _images
.. |repo_front| image:: /static/images/updatesite/7_repo_front.png
.. |repo_content| image:: /static/images/updatesite/8_repo_content.png
.. |repo_events| image:: /static/images/updatesite/9_repo_events.png
.. |repo_examplefile| image:: /static/images/updatesite/10_repo_examplefile.png
.. |repo_exampleraw| image:: /static/images/updatesite/11_repo_exampleraw.png
.. |repo_newfile| image:: /static/images/updatesite/12_repo_newfile.png
.. |repo_newfilename| image:: /static/images/updatesite/13_repo_newfilename.png
.. |repo_editfile| image:: /static/images/updatesite/14_repo_editfile.png
.. |actions_home| image:: /static/images/updatesite/15_actions_home.png
.. |actions_succeess| image:: /static/images/updatesite/16_actions_succeess.png
.. |site_event| image:: /static/images/updatesite/17_site_event.png
