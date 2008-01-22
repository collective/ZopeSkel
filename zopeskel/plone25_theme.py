import copy

from zopeskel.plone import Plone
from zopeskel.plone2_theme import theme_vars
from zopeskel.base import get_var

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
    vars = vars[:2] + theme_vars + vars[2:]

    def post(self, command, output_dir, vars):
        np, p = vars['namespace_package'], vars['package']
        sdir = os.path.join(output_dir, np, p, 'skins')

