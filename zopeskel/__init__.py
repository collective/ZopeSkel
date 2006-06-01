import pkg_resources
from paste.script import templates

var = templates.var

class BasicZope(templates.Template):
    _template_dir = 'templates/basic_zope'
    summary = "A Zope project"
    required_templates = ['basic_package']

class BasicPloneCore(templates.Template):
    _template_dir = 'templates/basic_plonecore'
    summary = "A Plone Core project"
    required_templates = []
    vars = [
        var('namespace_package', 'Namespace package', default='plone'),
        var('package', 'The package contained namespace package (like i18n)'),
        var('version', 'Version', default='0.1'),
        var('description', 'One-line description of the package'),
        var('long_description', 'Multi-line description (in reST)'),
        var('author', 'Author name', default='Plone Foundation'),
        var('author_email', 'Author email',
            default='plone-developers@lists.sourceforge.net'),
        var('keywords', 'Space-separated keywords/tags'),
        var('url', 'URL of homepage',
            default='http://svn.plone.org/svn/plone/plone.i18n'),
        var('license_name', 'License name', default='GPL'),
        var('zip_safe', 'True/False: if the package can be distributed '
            'as a .zip file', default=False),
        ]

    def run(self, command, output_dirs, vars):
        del vars['package']
        super(BasicPloneCore, self).run(command, output_dirs, vars)

class BasicNamespaced(templates.Template):
    # XXX: This needs to be pushed down into paster, because we're
    # repeating lots of code here (including the whole template of
    # basic_package).
    _template_dir = 'templates/basic_namespacepackage'
    summary = "A basic setuptools-enabled package with a namespace"
    required_templates = []
    vars = [
        var('namespace_package', 'Namespace package (like zope)'),
        var('package', 'The package contained namespace package '
            '(like formlib)'),
        var('version', 'Version (like 0.1)'),
        var('description', 'One-line description of the package'),
        var('long_description', 'Multi-line description (in reST)'),
        var('keywords', 'Space-separated keywords/tags'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name'),
        var('zip_safe', 'True/False: if the package can be distributed as a .zip file', default=False),
        ]

    def run(self, command, output_dirs, vars):
        del vars['package']
        super(BasicNamespaced, self).run(command, output_dirs, vars)
