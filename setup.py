from setuptools import setup


version = '3.0a1'

setup(name='ZopeSkel',
      version=version,
      description="Templates and code generator for quickstarting Python, Zope and Plone projects.",
      long_description=open('README.txt').read() + "\n" +
                       open('HISTORY.txt').read(),
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.6",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
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
      url='http://svn.plone.org/svn/collective/ZopeSkel/trunk',
      packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "setuptools",
        "templer.core",
        "templer.buildout",
        "templer.zope",
        "templer.plone",
      ],
      entry_points="""
      [console_scripts]
      zopeskel = templer.core.zopeskel_script:run
      """,
      )
