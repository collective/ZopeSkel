==============
Using buildout
==============

You probably got here by running something like:

 $ paster create -t plone3_buildout
 
Now, you need to run:

 $ python bootstrap.py
 
This will install zc.buildout for you. 

To create an instance immediately, run:

 $ bin/buildout -v
 
This will download Plone's eggs and products for you, as well as other 
dependencies, create a new Zope 2 installation (unless you specified
an existing one when you ran "paster create"), and create a new Zope instance
configured with these products.

You can start your Zope instance by running:

 $ bin/instance start
 
or, to run in foreground mode:

 $ bin/instance fg
 
To run unit tests, you can use:

 $ bin/instance test -s my.package
 
Changing buildout.cfg
----------------------

You can change any option in buildout.cfg and re-run bin/buildout to reflect
the changes. This may delete things inside the 'parts' directory, but should
keep your Data.fs and source files intact. 

To save time, you can run buildout in "offline" mode, which will prevent it 
from downloading things and checking for new versions online:

 $ bin/buildout -ov
 
Creating new eggs
-----------------

New packages you are working on (but which are not yet released as eggs and
uploaded to the Cheese Shop aka pypi) should be placed in src. You can do:

 $ cd src/
 $ paster create -t plone my.package
 
Use "paster create --list-templates" to see all available templates. Answer
the questions and you will get a new egg. Then tell buildout about your egg
by editing buildout.cfg and adding your source directory to 'develop':

 [buildout]
 ...
 develop =
    src/my.package
    
You can list multiple packages here, separated by whitespace or indented
newlines.

You probably also want the Zope instance to know about the package. Add its
package name to the list of eggs in the "[instance]" section:

 [instance]
 ...
 eggs =
    ${buildout:eggs}
    my.package
    
Leave the ${buildout:eggs} part in place - it tells the instance to use the
eggs that buildout will have downloaded from the cheeseshop previously.

If you also require a ZCML slug for your package, buildout can create one
automatically. Just add the package to the 'zcml' option:

 [instance]
 ...
 zcml =
    my.package
    
When you are finished, re-run buildout. Offline mode should suffice:

 $ bin/buildout -ov
 
Developing old-style products
-----------------------------

If you are developing old-style Zope 2 products (not eggs) then you can do so
by placing the product code in the top-level 'products' directory. This is
analogous to the 'Products/' directory inside a normal Zope 2 instance and is
scanned on start-up for new products.

Depending on a new egg
----------------------

If you want to use a new egg that is in the cheese shop, all you need to do
is to add it to the "eggs" option under the main "[buildout]" section:

 [buildout]
 ...
 eggs =
    elementtree
    python-yadis
    python-openid
    python-urljr
    my.package
    
If it's listed somewhere else than the cheeseshop, you can add a link telling
buildout where to find it in the 'find-links' option:

 [buildout]
 ...
 find-links =
    http://download.zope.org/distribution/
    http://effbot.org/downloads
    http://some.host.com/packages
    
Using existing old-style products
---------------------------------
    
If you are using an old-style (non-egg) product, you can either add it as an 
automatically downloaded archive or put it in the top-level "products" folder.
The former is probably better, because it means you can redistribute your
buildout.cfg more easily:

 [productdistros]
 ...
 urls =
    http://www.dieter.handshake.de/pyprojects/zope/AdvancedQuery.tgz
    http://antiloop.plone.org/download/ZopeVersionControl-0.3.3.tar.gz
    http://plone.org/products/external-editor/releases/0.9.3/ExternalEditor-0.9.3-src.tgz
    http://plone.org/products/i18ntestcase/releases/1.1/i18ntestcase-1.1.tar.gz
    http://plone.org/products/someproduct/releases/1.3/someproduct-1.3.tar.gz
    
You can also track products from by adding a new bundle checkout part. It 
doesn't strictly have to be an svn bundle at all, any svn location will do,
and cvs is also supported:

 [buildout]
 ...
 parts =
    zope2
    productdistros
    plonebundle
    myproduct
    instance

Note that "myproduct" comes before the "instance" part. You then
need to add a new section to buildout.cfg:

 [myproduct]
 recipe = plone.recipe.bundlecheckout
 url = http://svn.plone.org/svn/collective/myproduct/trunk
 
Finally, you need to tell Zope to find this new checkout and add it to its
list of directories that are scanned for products:

 [instance]
 ...
 products =
    ${buildout:directory}/products
    ${productdistros:location}
    ${plonebundle:location}
    ${myproduct:location}
    
Without this last step, the "myproduct" part is simply managing an svn 
checkout and could potentially be used for something else instead.