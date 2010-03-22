import copy

from zopeskel.basic_zope import BasicZope
from zopeskel.base import get_var
from zopeskel.base import var, EASY, EXPERT
from zopeskel.vars import BooleanVar

class Plone(BasicZope):
    _template_dir = 'templates/plone'
    summary = "A project for Plone products"
    help = """
This creates a Plone project (to create a Plone *site*, you probably
want to use the one of the templates for a buildout).

To create a Plone project with a name like 'plone.app.myproject' 
(2 dots, a 'nested namespace'), use the 'plone_app' template.
"""
    category = "Plone Development"
    required_templates = ['basic_namespace']
    use_local_commands = True
    use_cheetah = True
    vars = copy.deepcopy(BasicZope.vars)
    vars.insert(5, BooleanVar(
        'add_profile',
        title='Register Profile',
        description='Should this package register a GS Profile',
        modes=(EASY, EXPERT),
        default=False,
        help="""
If your package has need of a Generic Setup profile, set this value to 'True'.  

Having a Generic Setup profile registered makes your package 'installable'
using the ZMI portal_quickinstaller or Plone's 'Add/Remove Products' control
panel.  This allows any portions of your package that require Generic
Setup--such as portlets, content types, actions and so on--to be
properly installed.
"""
    ))
    get_var(vars, 'namespace_package').default = 'plone'
    get_var(vars, 'package').default = 'example'


