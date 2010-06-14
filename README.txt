Introduction
============

ZopeSkel provides a collection of skeletons for quickstarting Zope
and Plone projects.

All skeletons are available as PasteScript_ templates and can be used
via the ''paster'' commandline tool. For example to create a package
for a Plone 3 theme you can do::

    paster create -t plone3_theme

this will ask a few questions such as desired package name and a description
and output a complete package skeleton that you can immediately start using.

INTERACTIVE HELP is available by entering "?" as a response to any
question.

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope projects.

.. _PasteScript: http://pythonpaste.org/script/

zopeskel script
===============

A script, ``zopeskel``, is available. This acts as a wrapper for
PasteScript's ``paster create``, hiding the newbie-error-prone syntax
of that command. ``zopeskel`` also provides some error-checking on
project names and additional help. It is recommended to use this
script, especially for new users, rather than using ``paster create``
directly. (The resulting packages produced, however, are the same).

For example, running the above command with the new script may be done like so::

    zopeskel plone3_theme

Doing so will allow you to validate the name you choose for your package as well as providing inline help for all of the questions you'll be asked.  For more information on this command, invoke the following::

    zopeskel --help

Available templates
===================

To see details of the available templates::

    zopeskel --list


Testing
=======

Since version 1.5, ZopeSkel has tests.  It's required to run these
before checking in; they can be run like::

    $ python setup.py test

