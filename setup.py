import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages
import sys, os

version = '0.13'

setup(name='ZopeSkel',
      version=version,
      description="A collection of skeletons for quickstarting Zope projects.",
      long_description="""
A collection of skeletons for quickstarting Zope projects.

This package adds to the list of available `PasteScript
<http://pythonpaste.org/script/>`_ templates a few that are useful for
quickly starting Zope projects that have a `setuptools
<http://peak.telecommunity.com/DevCenter/setuptools>`_-ready file
layout.

The latest version is available in a `Subversion repository
<http://svn.plone.org/svn/collective/ZopeSkel/trunk#egg=ZopeSkel-dev>`_.

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope projects.
""",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope command-line skeleton project',
      author='Daniel Nouri',
      author_email='daniel.nouri@gmail.com',
      url='',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "PasteScript>=0.9.1dev-r5487,==dev",
        "Cheetah",
      ],
      entry_points="""
      [paste.paster_create_template]
      basic_namespace = zopeskel:Namespace
      nested_namespace = zopeskel:NestedNamespace
      basic_zope = zopeskel:BasicZope
      plone = zopeskel:Plone
      plone_app = zopeskel:PloneApp
      plone2_theme = zopeskel:Plone2Theme
      plone2.5_theme = zopeskel:Plone25Theme
      plone3_theme = zopeskel:Plone3Theme
      plone2.5_buildout = zopeskel:Plone25Buildout
      plone3_buildout = zopeskel:Plone3Buildout
      """,
      )
