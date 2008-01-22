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
    pass

def cleanupStylsheets(dirpath, filenames):
    for prefix in ('base', 'generated', 'portlets', 'public'):
        filename = prefix + '.css.dtml'
        if filename in filenames:
            print "Removing %s from %s%s" %(filename, dirpath, os.sep)
            os.remove(os.path.join(dirpath, filename))


