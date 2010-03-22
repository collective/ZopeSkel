from setuptools import setup, find_packages

version = '2.16'

setup(name='ZopeSkel',
      version=version,
      description="A collection of skeletons for quickstarting Zope projects.",
      long_description=open('README.txt').read() + "\n" +
                       open('HISTORY.txt').read(),
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        ],
      license='MIT',
      keywords='web zope command-line skeleton project',
      author='Daniel Nouri',
      author_email='daniel.nouri@gmail.com',
      maintainer='Cris Ewing',
      maintainer_email="cewing@uw.edu",
      url='http://svn.plone.org/svn/collective/ZopeSkel/trunk',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "PasteScript",
        "Cheetah>1.0,<=2.2.1",
      ],
      tests_require=['zope.testing', 'zc.buildout', 'Cheetah', 'PasteScript'],
      test_suite='zopeskel.tests.test_all.test_suite',
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
      plone_pas = zopeskel:PlonePas
      kss_plugin = zopeskel:KssPlugin

      [paste.paster_command]
      addcontent = zopeskel.localcommands:ZopeSkelLocalCommand

      [zopeskel.zopeskel_sub_template]
      portlet = zopeskel.localcommands.plone:Portlet
      view = zopeskel.localcommands.plone:View
      zcmlmeta = zopeskel.localcommands.plone:ZCMLMetaDirective
      i18nlocale = zopeskel.localcommands.plone:I18nLocale

      contenttype = zopeskel.localcommands.archetype:ContentType
      atschema = zopeskel.localcommands.archetype:ATSchemaField
      form = zopeskel.localcommands.plone:Form
      formfield = zopeskel.localcommands.plone:FormField

      extraction_plugin = zopeskel.localcommands.plone_pas:ExtractionPlugin
      authentication_plugin = zopeskel.localcommands.plone_pas:AuthenticationPlugin
      challenge_plugin = zopeskel.localcommands.plone_pas:ChallengePlugin
      credentials_reset_plugin = zopeskel.localcommands.plone_pas:CredentialsResetPlugin
      user_adder_plugin = zopeskel.localcommands.plone_pas:UserAdderPlugin
      role_assigner_plugin = zopeskel.localcommands.plone_pas:RoleAssignerPlugin
      user_factory_plugin = zopeskel.localcommands.plone_pas:UserFactoryPlugin
      anonymous_user_factory_plugin = zopeskel.localcommands.plone_pas:AnonymousUserFactoryPlugin
      properties_plugin = zopeskel.localcommands.plone_pas:PropertiesPlugin
      groups_plugin = zopeskel.localcommands.plone_pas:GroupsPlugin
      roles_plugin = zopeskel.localcommands.plone_pas:RolesPlugin
      update_plugin = zopeskel.localcommands.plone_pas:UpdatePlugin
      validation_plugin = zopeskel.localcommands.plone_pas:ValidationPlugin
      user_enumeration_plugin = zopeskel.localcommands.plone_pas:UserEnumerationPlugin
      group_enumeration_plugin = zopeskel.localcommands.plone_pas:GroupEnumerationPlugin
      role_enumeration_plugin = zopeskel.localcommands.plone_pas:RoleEnumerationPlugin

      [console_scripts]
      zopeskel = zopeskel.zopeskel_script:run
      """,
      )
