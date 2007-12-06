import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

version = '1.3.1'

setup(name='ZopeSkel',
      version=version,
      description="A collection of skeletons for quickstarting Zope projects.",
      long_description=open('README.txt').read() + open('HISTORY.txt').read(),
      classifiers=[
        "Development Status :: 5 - Production/Stable",
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
        "PasteScript",
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
      archetype = zopeskel:Archetype
      plone3_portlet = zopeskel:Plone3Portlet
      plone_hosting = zopeskel.hosting:StandardHosting
      recipe = zopeskel:Recipe
      """,
      )
