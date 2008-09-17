# -*- coding: utf-8 -*-
import copy

from zopeskel.base import get_var
from zopeskel.base import var
from zopeskel.basic_namespace import BasicNamespace


class KssPlugin(BasicNamespace):
    _template_dir = 'templates/kss_plugin'
    summary = "A KSS plugin template"
    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(BasicNamespace.vars)
    get_var(vars, 'namespace_package').default = 'kss'
    vars.insert(1, var('namespace_package2',
                        'Nested namespace package (like app)',
                        default='plugin'))
    get_var(vars, 'keywords').default = 'kss plugin'
