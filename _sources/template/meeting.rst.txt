.. _update-meeting:

Update Meeting Data
===================

- Reference YAML in Fundamentals
- Thoroughly explain the structure of our meeting data
- Tutorial: Play around with example data

Update a Meeting
----------------

It is recommended to first read :ref:`meeting-format`.

The process to update meetings is very similar to the process required to
``Create an Event``. Meeting information is stored in the ``data`` folder, which
can either have a single ``meetings.yaml`` file, or a directory named
``meetings/`` with any number of ``____.yaml`` files within, each one
representing a meeting.

**Spaces:** These `yaml`_ files are a special format that functions very similar
to a database. Spaces (**NOT TABS**) and colons are very important.

.. _yaml: https://www.redhat.com/en/topics/automation/what-is-yaml
