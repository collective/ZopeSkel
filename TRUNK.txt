Running Trunk ZopeSkel
--------------------------

To execute ZopeSkel source code checkout ZopeSkel. In this folder run::

    PYTHONPATH=. python -c "from zopeskel import zopeskel_script ; zopeskel_script.run()" 

Test plone4_buildout 
---------------------

* Clears previous leftovers

* Runs clean plone4_buildout

* Run in ZopeSkel checkout folder

(hit enter to questions)::

    rm -rf plone4testfolder ; python -c "import sys ; sys.path.append('.') ; from zopeskel import zopeskel_script ; zopeskel_script.run()"  plone4_buildout plone4testfolder  ; cd plone4testfolder ; python bootstrap.py ; bin/buildout -vvv ; cd ..

.. note ::

    Since buildout command takes a long time it is recommend to set-up a user buildout cache folder.

