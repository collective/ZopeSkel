import copy 
from zopeskel.basic_namespace import BasicNamespace
from zopeskel.base import get_var
from zopeskel.base import var

class BasicZope(BasicNamespace):
    _template_dir = 'templates/basic_zope'
    summary = "A Zope project"
    required_templates = ['basic_namespace']
    use_cheetah = True

    vars = copy.deepcopy(BasicNamespace.vars)
    get_var(vars, 'namespace_package').default = 'myzopelib'
    get_var(vars, 'package').default = 'example'
    vars.insert(2, var('zope2product',
                       'Are you creating a Zope 2 Product?',
                       default=False))


