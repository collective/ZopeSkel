import copy

from zopeskel import abstract_zope
from zopeskel.base import get_var

class PlonePas(abstract_zope.AbstractNestedZope):
    _template_dir = 'templates/plone_pas'
    summary = "A project for a Plone PAS plugin"
    help = """
This create a project for developing a PAS ('pluggable authentication
system') plugin.
"""
    category = "Plone Development"
    required_templates = ['nested_namespace']
    use_cheetah = True
    use_local_commands = True

    vars = copy.deepcopy(abstract_zope.AbstractNestedZope.vars)
    get_var(vars, 'namespace_package2').default = 'pas'

    def pre(self, command, output_dir, vars):
      vars['multiplugin_name'] = vars['package'].title()
      super(PlonePas, self).pre(command, output_dir, vars)

