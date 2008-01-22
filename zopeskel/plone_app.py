import copy

from zopeskel.nested_namespace import NestedNamespace
from zopeskel.base import get_vars
from zopeskel.base import var

class PloneApp(NestedNamespace):
    _template_dir = 'templates/plone_app'
    summary = "A Plone App project"
    required_templates = ['nested_namespace']
    use_cheetah = True

    vars = copy.deepcopy(NestedNamespace.vars)
    vars.insert(3, var('zope2product',
                       'Are you creating a Zope 2 Product?',
                       default=True))
    get_var(vars, 'author').default = 'Plone Foundation'
    get_var(vars, 'author_email').default = 'plone-developers@lists.sourceforge.net'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/plone/plone.app.example'

