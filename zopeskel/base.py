import os
from paste.script import templates
from paste.script.command import BadCommand
from paste.script.templates import BasicPackage

var = templates.var

LICENSE_CATEGORIES = {
    'DFSG' : 'License :: DFSG approved',
    'EFS' : 'License :: Eiffel Forum License (EFL)',
    'NPL' : 'License :: Netscape Public License (NPL)',
    'ASL' : 'License :: OSI Approved :: Apache Software License',
    'BSD' : 'License :: OSI Approved :: BSD License',
    'FDL' : 'License :: OSI Approved :: GNU Free Documentation License (FDL)',
    'GPL' : 'License :: OSI Approved :: GNU General Public License (GPL)',
    'LGPL' : 'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'MIT' : 'License :: OSI Approved :: MIT License',
    'MPL' : 'License :: OSI Approved :: Mozilla Public License 1.0 (MPL)',
    'MPL11' : 'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
    'QPL' : 'License :: OSI Approved :: Qt Public License (QPL)',
    'ZPL' : 'License :: OSI Approved :: Zope Public License',
    }

def get_var(vars, name):
    for var in vars:
        if var.name == name:
            return var
    else:
        raise ValueError("No such var: %r" % name)

class BaseTemplate(templates.Template):
    """Base template for all ZopeSkel templates"""

    #make all ZopeSkel templates localcommand ready
    egg_plugins = ['ZopeSkel']

    #this is just to be able to write a zopeskel.txt file containing
    #the name of the parent template. it will be used by addcontent command
    #to list the apropriate subtemplates for the generated project.
    #the post method is not a candidate because many templates override it
    def run(self, command, output_dir, vars):
        templates.Template.run(self, command, output_dir, vars)
        open(os.path.join(output_dir, 'zopeskel.txt'),
             'w').write(self.name)
