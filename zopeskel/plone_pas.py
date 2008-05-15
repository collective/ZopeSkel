import copy

from zopeskel.nested_namespace import NestedNamespace
from zopeskel.base import get_var
from zopeskel.base import var

class PlonePas(NestedNamespace):
    _template_dir = 'templates/plone_pas'
    summary = "A Plone PAS project"
    required_templates = ['nested_namespace']
    use_cheetah = True

    vars = copy.deepcopy(NestedNamespace.vars)
    get_var(vars, 'namespace_package2').default = 'pas'
    get_var(vars, 'author').default = 'Plone Foundation'
    get_var(vars, 'author_email').default = 'plone-developers@lists.sourceforge.net'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/plone/plone.app.example'

    def pre(self, command, output_dir, vars):
      vars['multiplugin_name'] = vars['package'].title()

