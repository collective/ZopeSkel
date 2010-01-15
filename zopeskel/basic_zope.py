import copy 
from zopeskel.base import get_var
from zopeskel.vars import var, BooleanVar
from zopeskel import abstract_zope


class BasicZope(abstract_zope.AbstractZope):
    _template_dir = 'templates/basic_zope'
    summary = "A Zope project"
    help = """
This creates a Zope project without any specific Plone features.
"""
    required_templates = ['basic_namespace']
    use_cheetah = True

    vars = copy.deepcopy(abstract_zope.AbstractZope.vars)
    get_var(vars, 'namespace_package').default = 'myzopelib'
    get_var(vars, 'package').default = 'example'


