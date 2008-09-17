from zopeskel.base import var
from zopeskel.base import BaseTemplate

class BasicNamespace(BaseTemplate):
    _template_dir = 'templates/basic_namespace'
    summary = "A project with a namespace package"
    required_templates = []
    use_cheetah = True

    vars = [
        var('namespace_package', 'Namespace package (like plone)', 
             default='plone'), 
        var('package', 'The package contained namespace package (like example)',
            default='example'),
        var('version', 'Version', default='1.0'),
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
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return super(BasicNamespace, self).check_vars(vars, command)

