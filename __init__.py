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
        var('package', 'The package contained namespace package (like i18n)'),
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

class PloneCore(Namespace):
    _template_dir = 'templates/plone_core'
    summary = "A Plone Core project"
    required_templates = ['basic_namespace']
    use_cheetah = True

    vars = copy.deepcopy(Namespace.vars)
    get_var(vars, 'namespace_package').default = 'plone'
    get_var(vars, 'package').default = 'example'
    vars.insert(2,
                var(
        'zope2product', 'Are you creating a Zope 2 Product?',
        default=False))
    get_var(vars, 'author').default = 'plone-developers@lists.sourceforge.net'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/plone/plone.i18n'

class Plone2Theme(Namespace):
    _template_dir = 'templates/plone2_theme'
    summary = "A Theme for Plone 2.1 & Plone 2.5"
    required_templates = ['plone_core']
    use_cheetah = True
    
    vars = copy.deepcopy(PloneCore.vars)
    get_var(vars, 'namespace_package').default = 'plonetheme'
    get_var(vars, 'zope2product').default = True
    vars = vars[:2] + [
        var('skinname',
            "Name of the skin selection that will be added to 'portal_skins'",
            default="Example Plone Theme"),
        var('skinbase',
            'Name of the skin selection the new one will be copied from',
            default='Plone Default'),
        ] + vars[2:]
