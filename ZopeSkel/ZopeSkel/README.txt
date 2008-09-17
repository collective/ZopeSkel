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

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope projects.

.. _PasteScript: http://pythonpaste.org/script/
.. _Subversion repository: http://svn.plone.org/svn/collective/ZopeSkel/trunk#egg=ZopeSkel-dev


Available templates
===================

Development templates
---------------------
plone
  This is a small template which creates a bare bones package with a
  single namespace. This can be used to create plone.* packages
  for example.
  
plone_app
  This is a small template which creates a bare bones package with a
  nested namespace. This can be used to create plone.app.* packages
  for example.

plone3_portlet
  Creates a package with a new portlet. This includes everything needed
  to register the portlet in Plone and tests which check if the portlet can
  be added, edited and rendered properly.

plone2_theme
  A template to create a new Zope 2 products for a Plone 2.1 or Plone 2.5
  site. If you are targetting Plone 3 please use the plone3_theme template
  instead.

plone2.5_theme
  A template to create a new Zope 2 products for Plone 2.5
  site. If you are targetting Plone 3 please use the plone3_theme template
  instead.

plone3_theme
  This template creates a theme package for Plone 3.0. This is the succesor
  to the popular DIYPloneStyle_ product.

recipe
  This template creates a recipe skeleton for zc.buildout.


.. _DIYPloneStyle: http://plone.org/products/diyplonestyle


Hosting / deployment templates
------------------------------

plone2.5_buildout
  A basic buildout_ based instance for Plone 2.5 projects. If you also need
  ZEO or caching take a look at the plone_hosting template.

plone3_buildout
  A basic buildout_ based instance for Plone 3.0.x projects. If you also need
  ZEO or caching take a look at the plone_hosting template.

plone_hosting
  This template creates a buildout_-based Plone deployment. It supports
  all Plone 2.5 and 3.0 versions: it will ask you for the desired Plone
  version.

  If you configure a proxy port a varnish_ cache server will be installed
  and configured as well.

  supervisord_ is used to manage the ZEO server, Zope instance and, if chosen,
  Varnish server.

silva_buildout
  A basic buildout Silva instance.


.. _buildout: http://plone.org/documentation/tutorial/buildout
.. _varnish: http://varnish.projects.linpro.no
.. _supervisord: http://www.supervisord.org


Testing
-------

Since version 1.5, ZopeSkel has tests.  It's required to run these
before checking in; they can be run like::

    $ python setup.py test

