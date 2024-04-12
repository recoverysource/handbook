.. _meeting-format:

Meeting Data Format
-------------------

.. warning::
   Use of correct space and syntax in yaml files is CRITICAL!
   If unsure, syntax can be validated with: https://yaml-online-parser.appspot.com/

- Use two spaces to indent elements.
- Required Fields: [``name``, ``time``, ``type``]
- Valid ``type`` codes come from https://github.com/code4recovery/spec#meeting-types)

  Partial List: ``EN:English``, ``B:BigBook``, ``C:Closed``, ``O:Open``,
  ``12x12:TwelveByTwelve``, ``D:Discussion``, ``SP:Speaker``, ``ST:StepStudy``,
  ``TR:TraditionStudy``, ``X:WheelchairAccess``, ``BA:Babysitting``

- Default ``timezone`` is provided by the :ref:`Meeting Guide<aamod-meetingguide>` shortcode
- Each "meeting" can be placed into a file named ``data/meetings/<shortname>.yaml``:

  + The filename replaces ``<shortname>:`` in the format and this should be removed;
    the leading two spaces must also be removed in this structure
  + The <shortname> tag is arbitrary, but used as the slug portion of the URL
  + It can be helpful to prepend a district tag to each meeting filename
  + Live example: https://github.com/area63aa/area63aa.org/tree/master/data/meetings

- For online-only meetings, ``place`` can be ``Zoom-Only`` (or similar)
- Meeting Guide expects US-formatted "``address``" => ``<street_address>, <city>, <state>, <zip>``

  + AAMod will split on comma (``,``) and trim spaces
  + If no ``address`` is provided, ``,,,Online`` is used as a
    :ref:`aamod-meetingguide`-compatible default
  + If no ``country`` is provided, ``US`` is used as a valid default
