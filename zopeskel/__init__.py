import copy
import pkg_resources
from paste.script import templates

var = templates.var

def get_var(vars, name):
    for var in vars:
        if var.name == name:
            return var
    else:
        raise ValueError("No such var: %r" % name)


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


class Plone2Theme(Namespace):
    _template_dir = 'templates/plone2_theme'
    summary = "A Theme for Plone 2.1 & Plone 2.5"
    required_templates = ['plone']
    use_cheetah = True
    
    vars = copy.deepcopy(Plone.vars)
    get_var(vars, 'namespace_package').default = 'plonetheme'
    get_var(vars, 'zope2product').default = True
    get_var(vars, 'author').default = 'Plone Community Member'
    get_var(vars, 'author_email').default = 'product-developers@lists.plone.org'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/collective/plonetheme'
    vars = vars[:2] + [
        var('skinname',
            "Name of the skin selection that will be added to 'portal_skins'",
            default="Custom theme for Plone 2.1"),
        var('skinbase',
            'Name of the skin selection the new one will be copied from',
            default='Plone Default'),
        ] + vars[2:]

class Plone25Theme(Namespace):
    _template_dir = 'templates/plone2.5_theme'
    summary = "A Theme for Plone 2.5"
    required_templates = ['plone']
    use_cheetah = True
    
    vars = copy.deepcopy(Plone.vars)
    get_var(vars, 'namespace_package').default = 'plonetheme'
    get_var(vars, 'zope2product').default = True
    get_var(vars, 'author').default = 'Plone Community Member'
    get_var(vars, 'author_email').default = 'product-developers@lists.plone.org'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/collective/plonetheme'
    vars = vars[:2] + [
        var('skinname',
            "Name of the skin selection that will be added to 'portal_skins'",
            default="Custom theme for Plone 2.5"),
        var('skinbase',
            'Name of the skin selection the new one will be copied from',
            default='Plone Default'),
        ] + vars[2:]

class Plone3Theme(Namespace):
    _template_dir = 'templates/plone3_theme'
    summary = "A Theme for Plone 3.0"
    required_templates = ['basic_namespace']
    use_cheetah = True
    
    vars = copy.deepcopy(Namespace.vars)
    
    get_var(vars, 'namespace_package').default = 'plonetheme'
    get_var(vars, 'author').default = 'Plone Community Member'
    get_var(vars, 'author_email').default = 'product-developers@lists.plone.org'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/collective/plonetheme'
    vars = vars[:2] + [
        var('skinname',
            "Name of the skin selection that will be added to 'portal_skins'",
            default="Custom theme for Plone 3.0"),
        var('skinbase',
            'Name of the skin selection the new one will be copied from',
            default='Plone Default'),
        ] + vars[2:]
        

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
        
    
