from setuptools import setup, find_packages


version = '3.0b3'

setup(name='ZopeSkel',
      version=version,
      description="Templates and code generator for quickstarting Python, Zope and Plone projects.",
      long_description=open('README.rst').read() + "\n" +
                       open('HISTORY.txt').read(),
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Framework :: Plone :: 3.2",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        ],
      license='MIT',
      keywords='web zope command-line skeleton project',
      author='Daniel Nouri',
      author_email='daniel.nouri@gmail.com',
      maintainer='Cris Ewing',
      maintainer_email="cris@crisewing.com",
      url='https://github.com/collective/zopeskel',
      packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "setuptools",
        "templer.core",
        "templer.buildout",
        "templer.zope",
        "templer.plone[localcommands]",
      ],
      entry_points="""
      [console_scripts]
      zopeskel = control_script:run
      """,
      )
