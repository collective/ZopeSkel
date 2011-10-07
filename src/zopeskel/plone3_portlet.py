import copy

from zopeskel.plone_app import PloneApp
from zopeskel.base import get_var
from zopeskel.base import var, EASY, EXPERT
from zopeskel.vars import StringVar, DottedVar

class Plone3Portlet(PloneApp):
    _template_dir = 'templates/plone3_portlet'
    summary = "A Plone 3 portlet"
    help = """
This creates a Plone project for a portlet.
"""
    required_templates = ['nested_namespace']
    use_cheetah = True

    vars = copy.deepcopy(PloneApp.vars)
    get_var(vars, 'namespace_package').default = 'collective'
    get_var(vars, 'namespace_package2').default = 'portlet'
    vars.append(
        StringVar(
            'portlet_name',
            title='Portlet Name',
            description='Name of portlet (human readable)',
            modes=(EASY,EXPERT),
            default='Example Portlet',
            help="""
This becomes the human-readable title of the portlet.
It gets generated in the GenericSetup profile file for the portlet.
It appears in the Plone UI when managing portlets.
"""
        )
        )
    vars.append(
        DottedVar(
            'portlet_type_name',
            title='Portlet Type Name',
            description='Name of portlet type (actual name)',
            modes=(EASY, EXPERT),
            default='ExamplePortlet',
            help="""
This becomes the actual name of the portlet. It is not displayed
in the Plone UI, but is the name it is registered under, and is
used as the class name for the portlet, and is used in the
generated GenericSetup profile.
"""
        )
        )

    def pre(self, command, output_dir, vars):
        vars['zip_safe'] = False
        vars['portlet_filename'] = vars['portlet_type_name'].lower()
        vars['dotted_name'] = "%s.%s.%s" % (vars['namespace_package'],
                                            vars['namespace_package2'],
                                            vars['package'])

        super(Plone3Portlet, self).pre(command, output_dir, vars)


