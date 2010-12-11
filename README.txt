Introduction
============

ZopeSkel provides a collection of skeletons for quickstarting Plone 
and Zope development projects.

This package provides `paster <http://pythonpaste.org/script/>`_ based templates for some common development needs.

Available templates
===================

To see details of the available templates::

    zopeskel --list
    
... or more info about how zopekskel works::

	zopeskel --help
	    
Using templates
===============

For example,to create a theme (Plone 3 or higher) call::

    zopeskel plone3_theme src/plonetheme.yourcompanyid

Alternatively, you can call the underlying ``paster`` subsystem directly::

	paster -t plone3_theme src/plonetheme.yourcompanyid 

The comand will ask a few questions such as desired package name and a description
and output a complete package skeleton that you can immediately start using.
Interactive help is available by entering "?" as a response to any question.

Testing
=======

Since version 1.5, ZopeSkel has tests.  It's required to run these
before checking in; they can be run like::

    python setup.py test

More info
=========

Issue tracker

* http://plone.org/products/zopeskel/issues

Source code

* http://svn.plone.org/svn/collective/ZopeSkel/trunk

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope projects.