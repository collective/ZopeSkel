from setuptools import setup, find_packages
import sys, os

version = '0.1'

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

Please contribute by submitting patches to what we consider 'best of
breed' file layouts for starting Zope projects.
""",
      classifiers=[
        "Development Status :: 3 - Alpha",
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
      install_requires=["PasteScript>=0.5.2dev-r5180,==dev"],
      entry_points="""
      [paste.paster_create_template]
      basic_zope = zopeskel:BasicZope
      basic_namespacepackage = zopeskel:BasicNamespaced
      """,
      )
