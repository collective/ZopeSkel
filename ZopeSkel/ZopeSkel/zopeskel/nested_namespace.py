import copy

from zopeskel.base import get_var
from zopeskel.base import var
from zopeskel.basic_namespace import BasicNamespace

class NestedNamespace(BasicNamespace):
    _template_dir = 'templates/nested_namespace'
    summary = "A project with two nested namespaces."
    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(BasicNamespace.vars)
    get_var(vars, 'namespace_package').default = 'plone'
    vars.insert(1, var('namespace_package2',
                        'Nested namespace package (like app)',
                        default='app'))
    get_var(vars, 'package').default = 'example'


