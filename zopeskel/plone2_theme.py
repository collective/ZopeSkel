import copy

from zopeskel.base import BaseTemplate
from zopeskel.base import get_var
from zopeskel.base import var

theme_vars = [
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
              ]

class Plone2Theme(BaseTemplate):
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
    vars = theme_vars + vars[:3] + vars[4:6]

    def post(self, command, output_dir, vars):
        if str(vars['empty_styles']) == 'False':
            skinsdir = os.path.join(output_dir, 'skins')
            for dirpath, dirnames, filenames in os.walk(skinsdir):
                cleanupStylsheets(dirpath, filenames)



