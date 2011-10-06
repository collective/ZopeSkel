.. contents ::

Introduction
============

ZopeSkel provides a collection of project templates for Plone and Zope
development projects.

ZopeSkel uses the `paster <http://pythonpaste.org/script/>`_ Python library
internally.

The ABCs of typical Plone development
=====================================

For the typical developer working on a plone project, the following path is
recommended:

* Install ZopeSkel package to virtualenv, or otherwise
  isolated from system Python installation, on your local computer.

* Create a new Plone 4 development installation using the
  ``plone4_buildout`` template.

* Create a new logic package for the content types, forms and logic of the
  site. This can be done using the
  `Dexterity ZopeSkel template <http://collective-docs.plone.org/content/dexterity.html>`_
  (included in ``plone4_buildout``).

* Create a new theme package for the site. This can be done using the
  `XDV template <http://collective-docs.plone.org/templates_css_and_javascripts/xdv.html>`_
  (included in ``plone4_buildout``).

* Test and develop on your local computer until everything is perfect.

* Put created packages under source code sversion control (Subversion, Git).

* Create a Plone installation on the production server. For this step the
  Plone Unified installer is the preferred method of building a distribution.

* Install your site customization packages on the production server.

Installing ZopeSkel
====================

ZopeSkel can be installed in one of two ways: with `buildout
<http://www.buildout.org/>`_ or with `virtualenv <http://virtualenv.org/>`_.

.. note ::

    Despite existing documentation to the contrary, it is not recommended to
    install ZopeSkel in your system python.

Buildout installation
---------------------------

Here are instructions how to include ZopeSkel as a part of your
local ``buildout.cfg``.

* You can use zopeskel to add new projects to your buildout ``src/`` folder.

* You can use code skeleton local commands to add more content to your
  package.

.. note ::

    The ``plone4_buildout`` template has ZopeSkel and paster support out of
    the box and this is not needed if you used ``plone4_buildout`` to create
    your ``buildout.cfg``.

Add to your ``buildout.cfg``::

    parts =
       ...
       zopeskel

    [zopeskel]
    # installs paster and Zopeskel
    recipe = zc.recipe.egg
    eggs =
       PasteScript
       ZopeSkel

After re-running buildout, you will have ``zopeskel`` and ``paster``
commands in the ``bin`` directory of your buildout.

Virtualenv installation
-----------------------

First, install virtualenv into your system::

    easy_install virtualenv

Next, create a virtual environment with the new ``virtualenv`` command::

    virtualenv --no-site-packages --distribute zopeskelenv

Once virtualenv is finished, you can install zopeskel to your new virtual
environment::

    zopeskelenv/bin/easy_install zopeskel

Once this is complete, you will be left with ``zopeskel`` and ``paster``
commands in the ``bin`` directory inside your virtualenv.

Available Templates
===================

To see details of the available templates::

    zopeskel --list

More info about how zopeskel works::

    zopeskel --help

Using Templates
===============

Creating a Plone 4 buildout using virtualenv ZopeSkel installation::

    source zopeskelenv/bin/activate
    zopeskel plone4_buildout yourfoldername

The folder created (``yourfoldername``) can be checked in to the versioning
system of your choice.  It is now a portable, self-contained, ready-to-build
Plone site.  You can build the system at any time using the following::

    cd yourfoldername
    python bootstrap.py
    bin/buildout

The ``plone4_buildout`` recipe results in a self-contained version of ZopeSkel
installed via the buildout method described above. It thus provides the
``zopeskel`` and ``paster`` commands inside its ``bin`` folder. You can use these
commands inside the buildout to create packages for your new Plone site::

    bin/zopeskel plone3_theme src/plonetheme.yourcompanyid

The command will ask a few questions such as the desired package name and
description, and output a complete package you can immediately start using.
Interactive help is available by entering "?" as a response to any question.

.. note ::

    Because ZopeSkel is built on paster you can do anything we describe here
    using the ``paster`` command directly.  If you do so, you can gain access to
    certain features of ``paster`` that have been disabled for ``zopeskel``, but
    you also will lose access to many of the nicer features of ``zopeskel``,
    including validation and in-line help.

Local Commands
==============

In addition to project templates, the ZopeSkel system provides local commands.
Local commands are context aware commands that help you to add more
functionality to an existing ZopeSkel generated project.

.. note ::

    Local commands require using the ``paster`` command directly - the
    ``zopeskel`` command does not support them yet.

.. note ::

    Not all ZopeSkel templates provide local commands.  In general, if local
    commands are available, you will be informed of the fact as your new
    package is generated.

Using local commands to create a content type package
-----------------------------------------------------

To use local commands you need to first include the paster command in your ``buildout.cfg``
as instructed above.

Starting inside your Plone buildout, first create a new archetypes add-on::

    cd src
    ../bin/zopeskel archetype mycompanyid.mycustomcontenttypes

Next, change directories into your new package and invoke ``paster`` to add a
content type::

    cd mycompanyid.mycustomcontenttypes
    ../../bin/paster

    Usage: ../../bin/paster COMMAND
    usage: paster [paster_options] COMMAND [command_options]

    ...

    Commands:
    ...

    ... local commands:
        addcontent   Adds plone content types to your project


As you can see from the ``paster`` command output, your new package supports a
local command called ``addcontent``. You can use the ``addcontent`` command
to add new code to your package. As with both ``zopeskel`` and ``paster``,
you can use the ``--list`` option to see what local commands are available
in the context of the package you've created::

    ../../bin/paster addcontent --list

    Available templates:
        atschema:      A handy AT schema builder
        browserlayer:  A Plone browserlayer
        contenttype:   A content type skeleton
        form:          A form skeleton
        formfield:     Schema field for a form
        i18nlocale:    An i18n locale directory structure
        portlet:       A Plone 3 portlet
        view:          A browser view skeleton
        zcmlmeta:      A ZCML meta directive skeleton

You can add an archetypes content type for managing lectures::

        ../../bin/paster addcontent -t contenttype LectureInfo

Then you can add schema fields to that content type::

        ../../bin/paster addcontent -t atschema

Local commands can be run as many times as needed to create your package.
You can iteratively develop your content type, other content types, and
more.

.. note ::

    When changing your package code, local commands will often change
    GenericSetup XML files (found in the in ``profiles/default`` folder of your
    package). These changes will not appear in Plone/Zope simply by restarting your
    instance. You will usually need to re-install your package in your development
    Plone site if you run any local commands in a package you've already installed.

More info

* http://collective-docs.plone.org/tutorials/paste.html

Developing ZopeSkel
===================

If you wish to contribute to the zopeskel project we welcome your
contribution. Zopeskel is now distributed with its own built-in buildout, so
to begin, all you need to do is check out the source, bootstrap with your
desired version of python, and run bin/buildout. A couple of things to keep in
mind while you work:

Testing
-------

Since version 1.5, ZopeSkel has tests. It's required to run these before you
check in any changes you make. You should run the full test suite in both
Python 2.4 and Python 2.6, as both versions are in common use among Zope and
Plone developers. They can be run like so::

    bin/test -s zopeskel

Please ensure that all tests pass in Python 2.4 and Python 2.6 before making
any checkins to the trunk of zopeskel.

Fixing Bugs
-----------

There are a number of open issues in the queue at
http://plone.org/products/zopeskel/issues and your help is always welcome in
closing any you feel competent to take on. Please note that there is a
zopeskel mailing list, so if you have any questions about your approach to
fixing a bug, you should post to the list first.

Running trunk version
----------------------

The easiest way to run the trunk of zopeskel is to check out the code,
bootstrap the buildout with your favored version of Python, and run
bin/buildout::

    svn co http://svn.plone.org/svn/collective/ZopeSkel/trunk zopeskel
    cd zopeskel
    python2.6 bootstrap.py
    ...
    bin/buildout

More info
=========

Issue tracker

* http://plone.org/products/zopeskel/issues

Plone and ZopeSkel related documentation

* http://collective-docs.plone.org/tutorials/paste.html

Source code

* http://svn.plone.org/svn/collective/ZopeSkel/trunk

Mailing List

* https://lists.plone.org/mailman/listinfo/zopeskel

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope projects.
