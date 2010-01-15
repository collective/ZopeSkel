# -*- coding: utf-8 -*-
import copy

from zopeskel.base import get_var
from zopeskel.base import var
from zopeskel import abstract_zope


class KssPlugin(abstract_zope.AbstractNestedZope):
    _template_dir = 'templates/kss_plugin'
    summary = "A project for a KSS plugin"
    ndots = 2
    help = """
This creates a project for a KSS plugins ('Kinetic Style Sheets', a 
Plone 3 framwork for JavaScript/AJAX).
"""
    category = "Plone Development"

    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(abstract_zope.AbstractNestedZope.vars)
    get_var(vars, 'namespace_package').default = 'kss'
    get_var(vars, 'namespace_package2').default = 'plugin'
    get_var(vars, 'keywords').default = 'kss plugin'
