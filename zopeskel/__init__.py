import os
import copy
import pkg_resources
import datetime
from paste.script import templates

var = templates.var

def get_var(vars, name):
    for var in vars:
        if var.name == name:
            return var
    else:
        raise ValueError("No such var: %r" % name)

def remove_var(vars, name):
    idx = 0
    for var in vars:
        if var.name == name:
            del vars[idx]
            break
        idx += 1

def removeFile(dirpath, filename):
    print "Removing %s from %s%s" %(filename, dirpath, os.sep)
    os.remove(os.path.join(dirpath, filename))


class Namespace(templates.Template):
    _template_dir = 'templates/basic_namespace'
    summary = "A project with a namespace package"
    required_templates = []
    use_cheetah = True
    
    vars = [
        var('namespace_package', 'Namespace package (like plone)'),
        var('package', 'The package contained namespace package (like example)'),
        var('version', 'Version', default='0.1'),
        var('description', 'One-line description of the package'),
        var('long_description', 'Multi-line description (in reST)'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('keywords', 'Space-separated keywords/tags'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name', default='GPL'),
        var('zip_safe', 'True/False: if the package can be distributed '
            'as a .zip file', default=False),
        ]

    def check_vars(self, vars, command):
        if not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return super(Namespace, self).check_vars(vars, command)


class NestedNamespace(Namespace):
    _template_dir = 'templates/nested_namespace'
    summary = "A project with two nested namespaces."
    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(Namespace.vars)
    get_var(vars, 'namespace_package').default = 'plone'
    vars.insert(1,
                var(
        'namespace_package2', 'Nested namespace package (like app)',
        default='app'))
    get_var(vars, 'package').default = 'example'


class BasicZope(Namespace):
    _template_dir = 'templates/basic_zope'
    summary = "A Zope project"
    required_templates = ['basic_namespace']
    use_cheetah = True

    vars = copy.deepcopy(Namespace.vars)
    get_var(vars, 'namespace_package').default = 'myzopelib'
    get_var(vars, 'package').default = 'example'
    vars.insert(2,
                var(
        'zope2product', 'Are you creating a Zope 2 Product?',
        default=False))


class Plone(Namespace):
    _template_dir = 'templates/plone'
    summary = "A Plone project"
    required_templates = ['basic_namespace']
    use_cheetah = True

    vars = copy.deepcopy(Namespace.vars)
    get_var(vars, 'namespace_package').default = 'plone'
    get_var(vars, 'package').default = 'example'
    vars.insert(2,
                var(
        'zope2product', 'Are you creating a Zope 2 Product?',
        default=False))
    get_var(vars, 'author').default = 'Plone Foundation'
    get_var(vars, 'author_email').default = 'plone-developers@lists.sourceforge.net'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/plone/plone.example'


class PloneApp(NestedNamespace):
    _template_dir = 'templates/plone_app'
    summary = "A Plone App project"
    required_templates = ['nested_namespace']
    use_cheetah = True

    vars = copy.deepcopy(NestedNamespace.vars)
    vars.insert(3,
                var(
        'zope2product', 'Are you creating a Zope 2 Product?',
        default=True))
    get_var(vars, 'author').default = 'Plone Foundation'
    get_var(vars, 'author_email').default = 'plone-developers@lists.sourceforge.net'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/plone/plone.app.example'

def removeCSSOverrides(dirpath):
    filenames = os.listdir(dirpath)
    for prefix in ('base', 'generated', 'portlets', 'public'):
        filename = prefix + '.css.dtml'
        if filename in filenames:
            removeFile(dirpath, filename)

class Plone2Theme(templates.Template):
    _template_dir = 'templates/plone2_theme'
    summary = "A Theme Product for Plone 2.1 & Plone 2.5"
    use_cheetah = True
    
    vars = copy.deepcopy(templates.BasicPackage.vars)
    get_var(vars, 'version').default = '0.1'
    get_var(vars, 'description').default = 'An installable theme for Plone'
    get_var(vars, 'author').default = 'Plone Collective'
    get_var(vars, 'author_email').default = 'product-developers@lists.plone.org'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/collective/'
    get_var(vars, 'keywords').default = 'web zope plone theme'
    vars = [
        var('skinname',
            "The skin selection to be added to 'portal_skins' (like 'My Theme')"),
        var('skinbase',
            'Name of the skin selection from which the new one will be copied',
            default='Plone Default'),
        var('empty_styles',
            "Override default public stylesheets with empty ones?",
            default=True),
        var('include_doc',
            "Include in-line documentation in 'config.py'?",
            default=False),
        ] + vars[:3] + vars[4:6]

    def post(self, command, output_dir, vars):
        if vars['empty_styles'] is not True:
            spath = os.path.join(output_dir, 'skins')
            stylesdirname = '%(package)s_styles' %vars
            stylespath = os.path.join(spath, stylesdirname)
            removeCSSOverrides(stylespath)

class Plone25Theme(Plone):
    _template_dir = 'templates/plone2.5_theme'
    summary = "A Theme for Plone 2.5"
    required_templates = ['plone']
    use_cheetah = True
    
    vars = copy.deepcopy(Plone.vars)
    get_var(vars, 'namespace_package').description = 'Namespace package (like plonetheme or Products)'
    get_var(vars, 'namespace_package').default = 'Products'
    get_var(vars, 'zope2product').default = True
    get_var(vars, 'description').default = 'An installable theme for Plone 2.5'
    get_var(vars, 'author').default = 'Plone Collective'
    get_var(vars, 'author_email').default = 'product-developers@lists.plone.org'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/collective/'
    get_var(vars, 'keywords').default = 'web zope plone theme'
    vars = vars[:2] + [
        var('skinname',
            "The skin selection to be added to 'portal_skins' (like 'My Theme')"),
        var('skinbase',
            'Name of the skin selection from which the new one will be copied',
            default='Plone Default'),
        var('empty_styles',
            "Override default public stylesheets with empty ones?",
            default=True),
        var('include_doc',
            "Include in-line documentation in generated code?",
            default=False),
        ] + vars[2:]

    def post(self, command, output_dir, vars):
        if vars['include_doc'] is False:
            spath = os.path.join(output_dir, vars['namespace_package'], vars['package'], 'skins')
            for skindir in ('images', 'templates', 'styles'):
                custom = skindir in ('images', 'templates') and '_custom' or ''
                skindir = '%s%s_%s' % (vars['package'], custom, skindir)
                path = os.path.join(spath, skindir)
                removeFile(path, 'CONTENT.txt')
        if vars['empty_styles'] is not True:
            spath = os.path.join(output_dir, vars['namespace_package'], vars['package'], 'skins')
            stylesdirname = '%(package)s_custom_styles' %vars
            stylespath = os.path.join(spath, stylesdirname)
            removeCSSOverrides(stylespath)

class Plone3Theme(Plone):
    _template_dir = 'templates/plone3_theme'
    summary = "A Theme for Plone 3.0"
    required_templates = ['plone']
    use_cheetah = True
    
    vars = copy.deepcopy(Plone25Theme.vars)
    get_var(vars, 'namespace_package').default = 'plonetheme'
    get_var(vars, 'namespace_package').description = 'Namespace package (like plonetheme)'
    get_var(vars, 'description').default = 'An installable theme for Plone 3.0'

    def pre(self, command, output_dir, vars):
        vars['timestamp'] = datetime.date.today().strftime("%Y%m%d")

    def post(self, command, output_dir, vars):
        if vars['include_doc'] is False:
            namespace_package = vars['namespace_package']
            package = vars['package']
            ppath = os.path.join(output_dir, namespace_package, package)
            for resource_dir in ('images', 'stylesheets'):
                dirpath = os.path.join(ppath, 'browser', resource_dir)
                removeFile(dirpath, 'README.txt')
            spath = os.path.join(ppath, 'skins')
            for skindir in ('images', 'templates', 'styles'):
                custom = skindir in ('images', 'templates') and '_custom' or ''
                skindir = '%s_%s%s_%s' % (namespace_package, package,
                                          custom, skindir)
                path = os.path.join(spath, skindir)
                removeFile(path, 'CONTENT.txt')
        if vars['empty_styles'] is not True:
            spath = os.path.join(output_dir, vars['namespace_package'], vars['package'], 'skins')
            stylesdirname = '%(namespace_package)s_%(package)s_styles' %vars
            stylespath = os.path.join(spath, stylesdirname)
            removeCSSOverrides(stylespath)

class Plone3Buildout(templates.Template):
    _template_dir = 'templates/plone3_buildout'
    summary = "A buildout for Plone 3 projects"
    required_templates = []
    use_cheetah = True
    
    vars = [
        var('zope2_install', 'Path to Zope 2 installation; leave blank to fetch one', default=''),
        var('plone_products_install', 'Path to directory containing Plone products; leave blank to fetch one', default=''),
        var('zope_user', 'Zope root admin user', default='admin'),
        var('zope_password', 'Zope root admin password'),
        var('http_port', 'HTTP port', default=8080),
        var('debug_mode', 'Should debug mode be "on" or "off"?', default='off'),
        var('verbose_security', 'Should verbose security be "on" or "off"?', default='off'),
        ]
        
    def post(self, command, output_dir, vars):
        print "-----------------------------------------------------------"
        print "Generation finished"
        print "You probably want to run python bootstrap.py and then edit"
        print "buildout.cfg before running bin/buildout -v"
        print 
        print "See README.txt for details"
        print "-----------------------------------------------------------"

class Plone25Buildout(Plone3Buildout):
    _template_dir = 'templates/plone2.5_buildout'
    summary = "A buildout for Plone 2.5 projects"
    required_templates = ['plone3_buildout']
    
class Plone3Portlet(NestedNamespace):
    _template_dir = 'templates/plone3_portlet'
    summary = "A Plone 3 portlet"
    required_templates = ['nested_namespace']
    use_cheetah = True

    vars = copy.deepcopy(PloneApp.vars)
    get_var(vars, 'namespace_package').default = 'collective'
    get_var(vars, 'namespace_package2').default = 'portlet'
    get_var(vars, 'author').default = 'Plone Foundation'
    get_var(vars, 'author_email').default = 'plone-developers@lists.sourceforge.net'
    get_var(vars, 'url').default = 'http://plone.org'
    vars.append(var('portlet_name', 'Portlet name (human readable)', default="Example portlet"))
    vars.append(var('portlet_type_name', 'Portlet type name (should not contain spaces)', default="ExamplePortlet"))
    
    remove_var(vars, 'zope2product')
    remove_var(vars, 'zip_safe')
    
    def pre(self, command, output_dir, vars):
        vars['zip_safe'] = False
        vars['portlet_filename'] = vars['portlet_type_name'].lower()
        vars['dotted_name'] = "%s.%s.%s" % (vars['namespace_package'], vars['namespace_package2'], vars['package'])
    
class Archetype(Plone):
    _template_dir = 'templates/archetype'
    summary = 'A Plone project that uses Archetypes'
    required_templates = ['plone']
    use_cheetah = True
    
    vars = copy.deepcopy(Plone.vars)  
    
    vars.insert(0,
                var(
        'title', 'The title of the project',
        default='Plone Example'))      

