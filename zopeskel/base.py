from paste.script import templates
from paste.script.command import BadCommand
from paste.script.templates import BasicPackage

var = templates.var

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


