====================================
Splitting ZopeSkel into Egg Packages
====================================

:Author: joel@joelburton.com
:Date: 5 Oct 2009

Background
==========

ZopeSkel is currently a single egg, "ZopeSkel". It contains templates
for:

- scripts/utilities that are not template specific

- basic nested Python packages, without any Zope/Plone bits

- Basic Zope product/buildout templates

- Plone product/buildout templates

- Silva buildout template

- Code for the "local commands" system

- Local commands for Plone products

Proposal
========

We propose to divide ZopeSkel into separate packages & eggs:

``zopeskel.base``
  Local commands system, scripts/utilities

``zopeskel.zope``   *(will depend on zopeskel.base)*
  basic_zope template and Zope-only buildouts

``zopeskel.plone``  *(will depend on zopeskel.zope)*
  all plone templates/buildouts and local commands for Plone

``zopeskel.silva``  *(will depend on zopeskel.zope)*
  Silva buildout


Backwards Compatibility
-----------------------

Since there is a great deal of documentation that tells users to
"easy_install ZopeSkel", we need to make sure there is still a package
called this that provides the assumed components.

Therefore, we will keep a ZopeSkel egg, but have this provide no
code/packages-- it will only exist so that it has setuptools requires to
pull in zopeskel.base, zopeskel.zope, zopeskel.plone, zopeskel.silva.
Therefore, people following this documentation will get the "full"
ZopeSkel.

Rationale
=========

Curently, ZopeSkel can be a bit of magnet for recipes that may not be
widely needed by all members--there are non-Plone users of it that don't
want to get all of the Plone recipes, for example. In the future, they
would be able to ::

  easy_install zopeskel.zope

to just get the Base/Zope parts.

With additional adoption of ZopeSkel, we anticipate other communities
(Repoze, etc) wishing to add templates, and would prefer to avoid an
overly- long list of packages. This is especially important as, at least in
the Plone world, ZopeSkel is increasingly used by
integrators/non-developers, and a long list of packages unrelated to their
needs is confusing.

In addition, this will subtly reinforce to people that there *can be* 3rd
party packages that add templates. Larger institutional users of
Python/Zope/Plone/Silva may find it beneficial to write their own,
customized templates (the author of this document already does, for
example); however, that this is possible is slightly obscured by the fact
that we ship only one monolithic system with all the recipes in it.

Tasks Needed
============

1) Change the imports and entry points inside of ZopeSkel to match
   these new package names; for example, changing "plone.py" to
   import the BasicZope class as
   "from zopeskel.zope.basic_zope import BasicZope". 

2) Adding imports to zopeskel/__init__.py to import everything into this
   namespace that was previously there. This will ensure that 3rd party
   templates that made assumptions like "from zopeskel import basic_zope"
   will still work.

3) Break packages into separate eggs and check into new repository.

4) Empty ZopeSkel package and add setuptools requires so that this egg
   now installs all the new eggs.

New Repository
--------------

Given that ZopeSkel has a wider audience than just Plone, we don't feel it
make sense to move it into the plone repository. However, it also doesn't
seem right to leave it in the collective--here, it has become a magnet for
individual, not-well-organized changes that run counter to the requirement
that it be a stable, best-practice product.

We recommend creating a new repository, "zopeskel", which would contain the
zopeskel packages. This would allow us to grant svn access to people
without sharing core plone access, and would discourage collective-style
drive-by improvements.





