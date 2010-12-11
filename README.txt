.. contents :: 

Introduction
============

ZopeSkel provides a collection of skeletons for quickstarting Plone 
and Zope development projects.

This package provides `paster <http://pythonpaste.org/script/>`_ based templates for some common development needs.

Installing ZopeSkel
====================	

If you are working with Plone add-on projects, install ZopeSkel using buildout method.
Otherwise you might run into problems with local commands.
Only when you need to boostrap new Plone installation use system-wide installation method.

System-wide installation 
-------------------------

For Plone buildout project templates::

	easy_install -U ZopeSkel
	
Buildout based installations 
-----------------------------

For Plone project templates.

Add to your ``buildout.cfg``::

        
        parts =
            ...
            zopeskel
            
        
        [zopeskel]
        recipe = zc.recipe.egg
        eggs = 
                ZopeSkel 
                ${instance:eggs}

This will generate ``bin/paster`` and ``bin/zopeskel`` commands for your buildout.

Available templates
===================

To see details of the available templates::

    zopeskel --list
    
... or more info about how zopekskel works::

	zopeskel --help
		    
Using templates
===============

Creating Plone 4 buildout (system-wide installation)::

	zopeskel plone4_buildout yourfoldername

For example,to create a theme (Plone 3 or higher) call (buildout based installation)::

    bin/zopeskel plone3_theme src/plonetheme.yourcompanyid

Alternatively, you can call the underlying ``paster`` subsystem directly (this method is more error prone)::

	bin/paster -t plone3_theme src/plonetheme.yourcompanyid 

The command will ask a few questions such as desired package name and a description
and output a complete package skeleton that you can immediately start using.
Interactive help is available by entering "?" as a response to any question.

Local commands
=================

Besides project templates, ZopeSkel package provides local commands.
Local commands are context aware commands to add more functionality to an existing ZopeSkel generated
project.

.. note ::

	To use local commands you need to use paster command directly - zopeskel does not support them yet.


How-to create content type and add fields into it using local commands
-----------------------------------------------------------------------

In this example we create Archetypes based content types add-on product.
We will first create the project skeleton, then enter the project
and add more content types there using local commands.

Example or creating a content type::

		# First create an add-on skeleton if one does not exist
        cd src
        ../bin/zopeskel archetype mycompanyid.mycustomcontenttypes
                
        # Now new paster commands are available and listed when paster is run in this folder
        cd mycompanyid.mycustomcontenttypes
        ../../bin/paster
        
	        Usage: ../../bin/paster COMMAND
	        usage: paster [paster_options] COMMAND [command_options]
	        
	        ...
	                
	        Commands:
	          ...
	                  
	        ZopeSkel local commands:
	          addcontent   Adds plone content types to your project
                
As you can see from help output above, the project contains local command called ``addcontent``.
Tou can use ``addcontent`` command to add more functionality to the existing projects.

Example how to create special contenet type for managing lecture (this applies for ``archetype`` template only)::

        ../../bin/paster addcontent -t contenttype LectureInfo # 

Then you can add new fields to that content type::

        ../../bin/paster addcontent -t atschema

.. note ::

	When changing the add-on code the changes usually touch GenericSetup XML files (ones
	in profiles/default folder). This changes are not reflected to Plone/Zope application
	server when it is restarted, because they are site database specific changes which apply to one
	site only (Zope application server can host multiple Plone sites). 
	You need to rerun add-on product installer on Plone site  
	if you want to make these changes effective.      

More info

* http://collective-docs.plone.org/tutorials/paste.html

Testing
=======

Since version 1.5, ZopeSkel has tests.  It's required to run these
before checking in; they can be run like::

    python setup.py test

To execute ZopeSkel source code checkout in ZopeSkel trunk folder::

	PYTHONPATH=. python -c "from zopeskel import zopeskel_script ; zopeskel_script.run()" 

To test plone4_buildout (hit enter to questions)::

	rm -rf plone4testfolder ; PYTHONPATH=. python -c "from zopeskel import zopeskel_script ; zopeskel_script.run()"  plone4_buildout plone4testfolder  ; cd plone4testfolder ; python bootstrap.py ; bin/buildout -vvv ; cd ..

More info
=========

Issue tracker

* http://plone.org/products/zopeskel/issues

Source code

* http://svn.plone.org/svn/collective/ZopeSkel/trunk

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope projects.