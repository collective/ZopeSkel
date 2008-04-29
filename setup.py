from setuptools import setup, find_packages

version = '1.11'

setup(name='ZopeSkel',
      version=version,
      description="A collection of skeletons for quickstarting Zope projects.",
      long_description=open('README.txt').read() + "\n" + 
                       open('HISTORY.txt').read(),
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
      tests_require=['zope.testing', 'zc.buildout', 'Cheetah', 'PasteScript'],
      test_suite='zopeskel.tests.test_zopeskeldocs.test_suite',
      entry_points="""
      [paste.paster_create_template]
      basic_namespace = zopeskel:BasicNamespace
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
      silva_buildout = zopeskel:SilvaBuildout

      [paste.paster_command]
      addcontent = zopeskel.localcommands:ZopeSkelLocalCommand

      
      [zopeskel.zopeskel_sub_template]
      portlet = zopeskel.localcommands.templates:Portlet
      view = zopeskel.localcommands.templates:View
      zcmlmeta = zopeskel.localcommands.templates:ZCMLMetaDirective
      contenttype = zopeskel.localcommands.templates:ContentType
      atschema = zopeskel.localcommands.templates:ATSchemaField
      """,
      )
