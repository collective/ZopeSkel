import copy
from zopeskel.plone3_buildout import Plone3Buildout
from zopeskel.base import get_var

class Plone25Buildout(Plone3Buildout):
    _template_dir = 'templates/plone2.5_buildout'
    summary = "A buildout for Plone 2.5 projects"
    help = """
This template creates a buildout for Plone 2.5, appropriate for
development. If you also need ZEO or caching, you may wish to look
at the plone_hosting template.
"""
    required_templates = ['plone3_buildout']

    vars = copy.deepcopy(Plone3Buildout.vars)
    get_var(vars, 'plone_version').default = "2.5.5"

    # The Plone3Buildout has an appropriate "use-the-installer"
    # message, but this wouldn't be right here, so let's
    # override it.
    pre_run_msg = "" 
