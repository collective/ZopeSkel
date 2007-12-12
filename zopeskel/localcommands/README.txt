.. contents::

ZopeSkel with local commands
============================

ZopeSkel is a great tool for generating plone projects structure from paste 
templates. You can install it with::

  $ easy_install \
  http://svn.plone.org/svn/collective/ZopeSkel/trunk#egg=ZopeSkel-dev

You can list the available templates::

  $ paster create --list-templates
  Available templates:
    archetype:          A Plone project that uses Archetypes
    asic_namespace:    A project with a namespace package
    basic_package:      A basic setuptools-enabled package
    basic_zope:         A Zope project
    nested_namespace:   A project with two nested namespaces.
    paste_deploy:       A web application deployed through paste.deploy
    plone:              A Plone project
    plone2.5_buildout:  A buildout for Plone 2.5 projects
    plone2.5_theme:     A Theme for Plone 2.5
    plone2_theme:       A Theme Product for Plone 2.1 &amp; Plone 2.5
    plone3_buildout:    A buildout for Plone 3 projects
    plone3_portlet:     A Plone 3 portlet
    plone3_theme:       A Theme for Plone 3.0
    plone_app:          A Plone App project

You can start a new project::

  $ paster create -t archetype myproject

You have to answer many questions and in the end you will get an archetype 
based skeleton to start your project.

Now what will you do to add a new plone content type, Zope 3 utility, ...etc ?
You have to create the new files by hand and copy/paste code from other 
projects. This is not the best approach to the problem. Martin Aspeli comes 
with the idea of implementing a paster local commands/templates so one can 
just add plone content types by running paster local commands inside 
the project directory.

zopeskel.localcommands is one implementation of such idea.

How to use zopeskel.localcommands
=================================

List the available paster commands::

  $ paster --help
  ...
  Commands:
    create       Create the file layout for a Python distribution
    help         Display help
    make-config  Install a package and create a fresh config file/directory
    points       Show information about entry points
    serve        Serve the described application
    setup-app    Setup an application, given a config file

Now create an archetype project as described above, cd to the project folder 
and check the available commands::

  $ cd myproject
  myproject$ paster --help
  ...
  Commands:
    create       Create the file layout for a Python distribution
    grep         Search project for symbol
    help         Display help
    make-config  Install a package and create a fresh config file/directory
    points       Show information about entry points
    serve        Serve the described application
    setup-app    Setup an application, given a config file
  
  ZopeSkel local commands:
    addcontent   Add plone content types to your project

You get a new section called ``ZopeSkel local commands`` with one command 
called ``addcontent``. This new section is only available if paster detects 
that your project is ``addcontent`` aware (more about this later) . 
To see the list of available templates from this command::

  myproject$ paster addcontent --list
  Available templates:
    contenttype:  A content type skeleton
    portlet:      A Plone 3 portlet
    view:         A browser view skeleton
    zcmlmeta:     A ZCML meta directive skeleton

To add a portlet to your project, run the following command from anywhere 
inside your project (you don't need to be in the project's root folder)::

  myproject$ paster addcontent portlet
  Enter portlet_name (Portlet name (human readable)) ['Example portlet']: My Portlet
  Enter portlet_type_name (Portlet type name (should not contain spaces)) ['ExamplePortlet']: MyPortlet
  Enter description (Portlet description) )['']: My Portlet
    Recursing into portlets
      Copying +portlet_filename+.pt_tmpl to /home/mustapha/Projects/pylonsenv/test/plone/example/portlets/myportlet.pt
      Copying +portlet_filename+.py_tmpl to /home/mustapha/Projects/pylonsenv/test/plone/example/portlets/myportlet.py
    Recursing into profiles
      Recursing into default
    Recursing into tests
      Copying +portlet_filename+_base.py_tmpl to /home/mustapha/Projects/pylonsenv/test/plone/example/tests/myportlet_base.py
      Copying test_+portlet_filename+.py_tmpl to /home/mustapha/Projects/pylonsenv/test/plone/example/tests/test_myportlet.py

You get new files and if you check the ``configure.zcml`` in the portlets 
folder and the ``portlet.xml`` in the profiles/default folder, you will see 
that they are updated too.

How to add new templates ?
==========================

The python part is very similar to what you know from ZopeSkel. The only 
difference is that your template class must inherit from 
``ZopeSkelLocalTemplate``.

The template structure on the file system is the same as what you know from 
ZopeSkel with one difference: if your project has a file with the same name 
as a template file or the template filename ends with ``_insert``, 
the ``addcontent`` command will operate in insert-mode.

To make things easy, let's take Martin's plone 3 portlet template and 
transform it to ``zopeskel.localcommands`` template so you can add as many 
portlets as you want to your project. Here is the files and the structure 
we use::

  portlets/
           +portlet_filename+.pt_tmpl
           +portlet_filename+.py_tmpl
           configure.zcml_insert
  profiles/
          default/
                  portlets.xml_insert
  tests/
        base_+portlet_filename+.py_tmpl
        test_+portlet_filename+portlet.py_tmpl

The files that end with ``_tmpl`` will be handled as normal ZopeSkel templates.
But the new thing here is the files that end with ``_insert``. 
The content of these files will be inserted in the correspondent files of 
the destination project. As example here is the content of the file 
``portlet.xml_insert``::

    #<?xml version="1.0"?>
    #  <!-- This file is used to register new types of portlets. It can also
    #       be used to register completely new column types. See CMFPlone's 
    #       version of this file for more information.
    #  -->
    #  <portlets>
    #    <!-- -*- extra stuff goes here -*- -->      

    <portlet
      addview="${dotted_name}.${portlet_type_name}"
      title="${portlet_name}"
      description="${description}"
    />
    
    #</portlets>

Here, some notes are needed:

1. If your project contains a file named ``profile/default/portlets.xml``, 
    only the lines not starting with ``#`` will be inserted
  
2. If your project doesn't contain the file ``profile/default/portlets.xml``,
   the ``#``'s in the beginning of lines will be removed and a 
   ``profile/default/portlets.xml`` file will be created with the hole 
   content. 
   So it is a good idea when creating a new local template to think 
   about how the file will look like if it has to be created from scratch.
   Look at the zcmlmeta template as example.

Now, if you are asking how ``zopeskel.localcommands`` knows where (in the 
destination file) to insert the content of the source file, keep reading.

NOTE:
-----

The '_insert' in the end of the name of the template file is required for .py 
files and optional for other kind of files. For zopeskel.localcommands there is 
no difference between `configure.zcml_insert` and `configure.zcml`. Both will be
treated in insert-mode. In the case of .py files if you don't add '_insert' in 
the end of their name, setuptools will fail with 'SyntaxError' when installing
ZopeSkel. That's normal because of the template variables in the file.
For readability I recommand using the '_insert' syntax in all cases.

Now, take a look to the python part. Here is the Portlet class::

  from zopeskel import var
  from zopeskel.localcommands import ZopeSkelLocalTemplate
  
  class Portlet(ZopeSkelLocalTemplate):
      """
      A plone 3 portlet skeleton
      """
      _template_dir = 'templates/portlet'
      summary = "A Plone 3 portlet"
      use_cheetah = True
  
      vars = []
      vars.append(var('portlet_name', 
                      'Portlet name (human readable)', 
                      default="Example portlet"))
                    
      vars.append(var('portlet_type_name', 
                      'Portlet type name (should not contain spaces)', 
                      default="ExamplePortlet"))

      vars.append(var('description', 
                      'Portlet description', 
                      default=""))

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them 
        for free in the vars argument
        """
        vars['portlet_filename'] = vars['portlet_type_name'].lower()
        
        vars['dotted_name'] = "%s.portlets" % vars['package_dotted_name'] 

Three things to say here:

1. Your template class has to inherit from ``ZopeSkelLocalTemplate``

2. You get the package_namespace, package_namespace2, package and
   package_dotted_name of the parent package for free in the vars argument
   of the "pre" method.

3. The ZopeSkelLocalTemplate class defines an attribute named ``marker_name`` 
   like this::

     marker_name = "extra stuff goes here"

   Your can override it in your template class if you want. The purpose of this 
   marker_name is to tell ``addcontent`` command where to insert the content if 
   it has to insert something in a file. The correspondent file must include 
   a line containing ``-*- marker_name -*-`` in our case::

     -*- extra stuff goes here -*-

   if you look in portlet.xml of your project you will find a line containing::

     <!-- -*- extra stuff goes here -*- -->     

   If you want to know more about marker_name look at insert_into_file method 
   of paste.script.command.Command.

OK, now we have the file system structure and the template class. We need just
one more thing: add an egg entry point for our template class to make it 
available for the ``addcontent`` command. As I said before it is very similar 
to how you add a normal ZopeSkel template. The difference is that for normal 
ZopeSkel templates the entry point is added under 
``[paste.paste_create_template]`` section, but ``zopeskel.localcommands`` 
adds a new kind of entry points named ``[zopeskel.zopeskel_sub_template]`` 
and our templates have to be added under that section. If you look in the 
setup.py file of ZopeSkel to the entry_points argument, you will find::

    [zopeskel.zopeskel_sub_template]
    portlet = zopeskel.localcommands.templates:Portlet

Enable ``addcontent`` in other ZopeSkel templates
-------------------------------------------------

To enable ``addcontent`` command in your current project add a line with 
``ZopeSkel`` to your ``paster_plugins.txt`` file of your egg-info folder.


For the moment the ``addcontent`` command is only enabled for ZopeSkel's 
archetype template. You can enable ``addcontent`` command for other ZopeSkel 
templates by addinng an ``egg_plugins`` attribute to the template class 
like this::

    egg_plugins = ['ZopeSkel']
    
    

/Mustapha
url: http://www.mustap.com
email: mustap_at_gamail_com

