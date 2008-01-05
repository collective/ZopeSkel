==============
Using buildout
==============

Working with buildout.cfg
-------------------------

You can change any option in buildout.cfg and re-run bin/buildout to reflect
the changes. This may delete things inside the 'parts' directory, but should
keep your Data.fs and source files intact.

To save time, you can run buildout in "offline" (-o) and non-updating (-N)
mode, which will prevent it from downloading things and checking for new
versions online:

 $ bin/buildout -Nov

Adding eggs to your buildout
----------------------------

New packages you are working on (but which are not yet released as eggs and
uploaded to the Python Package Index, aka PYPI) should be placed in src. You can do:

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
package name to the list of eggs in the "[instance]" section, or under the
main "[buildout]" section:

 [instance]
 ...
 eggs =
    ${buildout:eggs}
    ${plone:eggs}
    my.package

Leave the ${buildout:eggs} part in place - it tells the instance to use the
eggs that buildout will have downloaded from the Python Package Index previously.

If you also require a ZCML slug for your package, buildout can create one
automatically. Just add the package to the 'zcml' option:

 [instance]
 ...
 zcml =
    my.package

When you are finished, re-run buildout. Offline, non-updating mode should
suffice:

 $ bin/buildout -Nov

Depending on a new egg
----------------------

If you want to use a new egg that is in the Python Package Index, all you need
to do is to add it to the "eggs" option under the main "[buildout]" section:

 [buildout]
 ...
 eggs =
    my.package

If it's listed somewhere else than the Python Package Index, you can add a link
telling buildout where to find it in the 'find-links' option:

 [buildout]
 ...
 find-links =
    http://dist.plone.org
    http://download.zope.org/distribution/
    http://effbot.org/downloads
    http://some.host.com/packages

If you want to use a package that is not registered with the package index
you can add it to the src/ directory. You need to tell buildout about your
package by editing buildout.cfg and adding your source directory to
the 'develop' line:

 [buildout]
 ...
 develop =
    src/my.package

You can list multiple packages here, separated by whitespace or indented
newlines.

You probably also want the Zope instance to know about the package. Add its
package name to the list of eggs in the "[instance]" section, or under the
main "[buildout]" section:

 [instance]
 ...
 eggs =
    ${buildout:eggs}
    ${plone:eggs}
    my.package

Leave the ${buildout:eggs} part in place - it tells the instance to use the
eggs that buildout will have downloaded from the Python Package Index
previously.

If you also require a ZCML slug for your package, buildout can create one
automatically. Just add the package to the 'zcml' option:

 [instance]
 ...
 zcml =
    my.package

When you are finished, re-run buildout. Offline, non-updating mode should
suffice:

 $ bin/buildout -Nov


Adding Zope products
--------------------

If you are using an old-style (non-egg) product, you can either add it as an
automatically downloaded archive or put it in the top-level "products" folder.

To use a product archive add this to buildout.cfg:
buildout.cfg more easily:

 [productdistros]
 recipe = plone.recipe.distros
 urls =
    http://plone.org/products/someproduct/releases/1.3/someproduct-1.3.tar.gz

If someproduct-1.3.tar.gz extracts into several products inside a top-level
directory, e.g. SomeProduct-1.3/PartOne and SomeProduct-1.3/PartTwo, then
add it as a "nested package":

 [productdistros]
 recipe = plone.recipe.distros
 urls =
    http://plone.org/products/someproduct/releases/1.3/someproduct-1.3.tar.gz
 nested-packages =
    someproduct-1.3.tar.gz

Alternatively, if it extracts to a directory which contains the version
number, add it as a "version suffix package":

 [productdistros]
 recipe = plone.recipe.distros
 urls =
    http://plone.org/products/someproduct/releases/1.3/someproduct-1.3.tar.gz
 version-suffix-packages =
    someproduct-1.3.tar.gz

You can also track products by adding a new bundle checkout part. It
doesn't strictly have to be an svn bundle at all, any svn location will do,
and cvs is also supported:

 [buildout]
 ...
 parts =
    plone
    zope2
    productdistros
    myproduct
    instance
    zopepy

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
