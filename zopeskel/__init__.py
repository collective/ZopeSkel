import pkg_resources
from paste.script import templates

var = templates.var

class BasicZope(templates.Template):
    _template_dir = 'templates/basic_zope'
    summary = "A Zope project"
    required_templates = ['basic_package']

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
