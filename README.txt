.. contents ::

WARNING
=======

As of version 3.0, zopeskel is no longer a package of its own. All the
templates that make it work have been moved into packages in the templer
namespace. Some of the templates you may be expecting are no longer available.
If you require older templates, please be sure to install ZopeSkel<3.0

Introduction
============

ZopeSkel provides a collection of project templates for Plone and Zope
development projects.

ZopeSkel uses the `paster <http://pythonpaste.org/script/>`_ Python library
internally.

Installing ZopeSkel
===================

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

Creating a package using virtualenv ZopeSkel installation::

    source zopeskelenv/bin/activate
    zopeskel <template_name> <package_name>

The folder created (``<package_name>``) can be checked in to the versioning
system of your choice.

Local Commands
==============

Local commands are not currently fully implemented. They will return soon. If
you require templates with local commands, please install ZopeSkel<3.0 until
this package reaches a final release

Developing ZopeSkel
===================

If you wish to contribute to the zopeskel project we welcome your
contribution. Zopeskel is now distributed with its own built-in buildout, so
to begin, all you need to do is check out the source, bootstrap with your
desired version of python, and run bin/buildout.

Since all of the template that are provided by ZopeSkel are now in templer
namespace packages, the ZopeSkel package uses mr.developer to provide access
to all the templer packages required in the src directory of the buildout.
Development should take place in those packages. There should be no templates
in the ZopeSkel package at all.

Testing
-------

Since version 1.5, ZopeSkel has tests. It's required to run these before you
check in any changes you make. You should run the full test suite in both
Python 2.4 and Python 2.6, as both versions are in common use among Zope and
Plone developers. They can be run like so::

    bin/test -s templer

Please ensure that all tests pass in Python 2.4 and Python 2.6 before making
any checkins to any templer package used by zopeskel.

Fixing Bugs
-----------

There are a number of open issues in the queue at
http://plone.org/products/zopeskel/issues and your help is always welcome in
closing any you feel competent to take on. Please note that there is a
zopeskel mailing list, so if you have any questions about your approach to
fixing a bug, you should post to the list first.

Running trunk version
---------------------

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
