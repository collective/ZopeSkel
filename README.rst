.. contents ::

WARNING
=======

As of version 3.0, ZopeSkel is no longer a package of its own. All the
templates that make it work have been moved into packages in the templer
namespace. Some of the templates you may be expecting are no longer available.
If you require older templates, please be sure to install ZopeSkel<3.0

Introduction
============

ZopeSkel provides a collection of 
`scaffolds <http://docs.pylonsproject.org/projects/pyramid/en/latest/glossary.html#term-scaffold>`_
(software project templates) for Plone and Zope development projects.

ZopeSkel is an application built using the 
`Templer <http://templer-manual.readthedocs.org/en/latest/index.html>`_ 
code generation framework.  Internally, Templer is an extension of the 
`Paster <http://pythonpaste.org/script/>`_ Python library.

More information about Templer, and ZopeSkel as an example of a Templer application, can be found
in the `Templer Manual <http://templer-manual.readthedocs.org/en/latest/index.html>`_


Installing ZopeSkel
===================

ZopeSkel can be installed in one of two ways: with `buildout
<http://www.buildout.org/>`_ or in a `virtualenv <http://virtualenv.org/>`_.  When installing ZopeSkel, it is
very important that you start with a clean Python environment, one that does not already include ZopeSkel or any
other templer packages.  Package version conflicts can be the cause of many errors.  For this reason, it is 
recommended that you work either with a clean virtualenv or a buildout that has been bootstrapped by a Python 
installation that does not have ZopeSkel installed.

.. note ::

    Because of this, and despite any information to the contrary, it is strongly recommended never to
    install ZopeSkel in your system python.

Buildout installation
---------------------------

It is possible to add ZopeSkel to a buildout, providing you with the ability to develop new packages
directly in your project buildout environment.  Once you have added ZopeSkel, you can use it to add 
new packages in the ``src/`` folder within your buildout.

First, add the following to your ``buildout.cfg``::

    # Add zopeskel to the last line of the parts = section in the [buildout] part of buildout.cfg
    parts =
        ...
        zopeskel

    # Add zopeskel section generating zopeskel command and 
    # related scaffold packages
    [zopeskel]
    recipe = zc.recipe.egg
    unzip = true
    eggs =
        PasteScript
        ZopeSkel

After re-running buildout, you will have ``zopeskel`` and ``paster`` commands in the ``bin`` 
directory of your buildout.  You can use these commands as described below to begin creating new 
packages.

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
commands in the ``bin`` directory inside your virtualenv.  If your virtualenv is 'activated', then the 
commands will be available directly.  

Available Templates
===================

ZopeSkel internally consists of several ``templer.*`` packages which provide individual 
templates. When you install ZopeSkel you automatically get all the packages that are 
required to run ZopeSkel.

To see details of the available templates::

    zopeskel --list

More info about how zopeskel works::

    zopeskel --help


.. note ::

      If some templates are missing please see that you do not have old ZopeSkel versions
      or packages infering in your PYTHONPATH.

Using Templates
===============

Creating a package using virtualenv ZopeSkel installation::

    source zopeskelenv/bin/activate
    zopeskel <template_name> <package_name>

The folder created (``<package_name>``) can be checked in to the versioning
system of your choice.

Local Commands
==============

Local commands are available for the ``plone_basic`` and ``archetype``
package templates.  If you create a package using one of these templates you
will be provided with information about the presence of local commands.  

To run a local command and add further features to your package, you will
run the paster command ``add`` from within your package.  Your current working
directory must be at or inside the directory where you find your package's 
egg-info, so you can do the following::

    $ bin/templer plone_basic my.package
    ....
    $ cd my.package/src
    $ ../../bin/paster --help
    ...
    Templer local commands:
      add  Allows the addition of further templates to an existing package
    $ ../../bin/paster add --list
    browserlayer:  A Plone browserlayer
    browserview:   A browser view skeleton
    $ ../../bin/paster add browserlayer
    ...

.. note ::

    You need to be in src/ folder or below to make local commands available.

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

To get started, simply clone the zopeskel repository to your local machine,
bootstrap with your preferred python, and run the buildout::

    git clone git@github.com:collective/ZopeSkel.git zopeskel
    cd zopeskel
    python2.6 bootstrap.py
    ...
    bin/buildout

Testing
-------

Since version 1.5, ZopeSkel has tests. It's required to run these before you
check in any changes you make. You should run the full test suite in both
Python 2.4 and Python 2.6, as both versions are in common use among Zope and
Plone developers. They can be run like so::

    bin/test

Please ensure that all tests pass in Python 2.4 and Python 2.6 before making
any checkins to any templer package used by zopeskel.

Fixing Bugs
-----------

There are a number of open issues in the queue at
http://plone.org/products/zopeskel/issues and your help is always welcome in
closing any you feel competent to take on. Please note that there is a
zopeskel mailing list, so if you have any questions about your approach to
fixing a bug, you should post to the list first.

More info
=========

Issue tracker

* http://plone.org/products/zopeskel/issues

Source code

* https://github.com/collective/zopeskel

Mailing List

* https://lists.plone.org/mailman/listinfo/plone-zopeskel

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope and Plone projects.
