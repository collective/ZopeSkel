import copy
import datetime

from zopeskel.plone25_theme import Plone25Theme
from zopeskel.base import get_var, EXPERT

class Plone3Theme(Plone25Theme):
    _template_dir = 'templates/plone3_theme'
    summary = "A theme for Plone 3"
    help = """
This creates a project for a theme for Plone 3.
"""
    required_templates = ['plone']
    use_cheetah = True

    vars = copy.deepcopy(Plone25Theme.vars)
    get_var(vars, 'namespace_package').default = 'plonetheme'
    get_var(vars, 'description').default = 'An installable theme for Plone 3'
    #add_profile should always default to True for theme packages
    get_var(vars, 'add_profile').default = True
    #add_profile need not appear as a question for theme packages
    get_var(vars, 'add_profile').modes = ()
