import copy

from zopeskel.nested_namespace import NestedNamespace
from zopeskel.plone_app import PloneApp
from zopeskel.base import get_var

class Plone3Portlet(NestedNamespace):
    _template_dir = 'templates/plone3_portlet'
    summary = "A Plone 3 portlet"
    required_templates = ['nested_namespace']
    use_cheetah = True

    vars = copy.deepcopy(PloneApp.vars)
    get_var(vars, 'namespace_package').default = 'collective'
    get_var(vars, 'namespace_package2').default = 'portlet'
    get_var(vars, 'author').default = 'Plone Foundation'
    get_var(vars, 'author_email').default = 'plone-developers@lists.sourceforge.net'
    get_var(vars, 'url').default = 'http://plone.org'
    vars.append(var('portlet_name',
                    'Portlet name (human readable)',
                    default="Example portlet"))
    vars.append(var('portlet_type_name',
                    'Portlet type name (should not contain spaces)',
                    default="ExamplePortlet"))

    def pre(self, command, output_dir, vars):
        vars['zip_safe'] = False
        vars['portlet_filename'] = vars['portlet_type_name'].lower()
        vars['dotted_name'] = "%s.%s.%s" % (vars['namespace_package'],
                                            vars['namespace_package2'],
                                            vars['package'])



