=======================
Plone 4 buildout 
=======================

.. contents ::

Introduction
------------

Buildout is a tool which automatically downloads, installs and configures Python software.
Plone developers prefer uses buildout based installation method - it makes it easy to work with source code and developing your own Plone add-ons.

Prerequisitements
-----------------

What you need in order to use buildout with Plone 4

* Experience of using command line tools

* Experience of using text editor to work with configuration files (``buildout.cfg``)

* GCC compiler to build native Python extensions

* Python 2.6 (other versions are *not* ok)

* Python Imaging Library installed for your Python 2.6 interpreter (more below)

* Python `Distribute <http://pypi.python.org/pypi/distribute>`_ installation tool, provided by your operating system
  or installed by hand

Features
--------

This buildout provides

* Zope start up scripts (one instance)

* ``paster`` command for creating Plone add-ons (different from system-wide installation)

* ``test`` command for running unit tests

* ``i18ndude`` for translating Plone add-ons 

Creating Plone 4 buildout installation
------------------------------------------

Install ZopeSkel template package for your system-wide Python using Distribute::

 easy_install ZopeSkel
 
... or upgrade existing installation::

 easy_install -U ZopeSkel

You probably got here by running something like (replace *myplonefoldername* with the target folder where you want to Plone to be installed)::

 paster create -t plone4_buildout myplonefoldername

Now, you need to run (please see remarks regarding choosing Python interpreter below)::

 python bootstrap.py

This will create ``bin`` folder and ``bin/buildout`` script. If you any time want to change Python interpreter
associated with buildout, or you need to update ``buildout`` script itself to newer version please rerun ``bootsrap.py``.

Now you can run buildout script which will download all Python packages
(.egg files) and create ``parts/`` and ``var/`` folder structure ::

 bin/buildout

If this succesfully completes you can start buildout in foreground mode::

 bin/instance fg

Press *CTRL+C* to terminate the instance.

The default user is ``admin`` with password ``admin``. 
Please follow these instructions to change admin password.

Next steps
----------

Plone 4 buildout comes with ``bin/paster`` command for creating Plone add-ons.

.. note ::

	When working with Plone add-ons, use paster command from buildout bin folder, not the system wide paster command.

* `Instructions how to use Paster command to create your own add-ons <http://collective-docs.plone.org/tutorials/paste.html>`_ 

Installing Python 2.6
--------------------------------------

Please refer to your system instructions.

Installing Python Imaging Library
----------------------------------

Plone needs Python Imaging Library to be fully functional (image resizes). 
Please follow your system instructions to install PIL.

Alternatively, after configuring development versions 
of libjpeg, zlib and libpng for your system you can do::

	easy_install http://dist.repoze.org/PIL-1.1.6.tar.gz

System specific dependencies installations
-------------------------------------------

Ubuntu/Debian
==============

Tested for Ubuntu 10.10.

Install prerequisitements::

	sudo apt-get install python2.6 python-imaging wget build-essential python2.6-dev python-setuptools
	easy_install ZopeSkel

OSX
====

Install `OSX development tools (XCode) <http://developer.apple.com/>`_ from Apple.

Install `Macports <http://www.macports.org/>`_.

Then the following installs dependencies::

	sudo port install python26 py26-pil wget #make sure to install and use python26 from macports
	easy_install ZopeSkel


Windows
========

Microsoft Windows systems is problematic because
it does not provide to Microsoft Visual C compiler (commercial) which is
required to build native Python extensions.

Please read

* http://plone.org/documentation/kb/using-buildout-on-windows
