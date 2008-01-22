import copy

from zopeskel.basic_namespace import BasicNamespace
from zopeskel.base import get_var
from zopeskel.base import var

class Plone(BasicNamespace):
    _template_dir = 'templates/plone'
    summary = "A Plone project"
    required_templates = ['basic_namespace']
    use_cheetah = True
    vars = copy.deepcopy(BasicNamespace.vars)
    get_var(vars, 'namespace_package').default = 'plone'
    get_var(vars, 'package').default = 'example'
    vars.insert(2, var('zope2product',
                       'Are you creating a Zope 2 Product?',
                       default=False))
    get_var(vars, 'author').default = 'Plone Foundation'
    get_var(vars, 'author_email').default = 'plone-developers@lists.sourceforge.net'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/plone/plone.example'


