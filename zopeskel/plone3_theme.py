import copy

from zopeskel.plone2_theme import Plone25Theme
from zopeskel.base import get_var

class Plone3Theme(Plone25Theme):
    _template_dir = 'templates/plone3_theme'
    summary = "A Theme for Plone 3.0"
    required_templates = ['plone']
    use_cheetah = True

    vars = copy.deepcopy(Plone25Theme.vars)
    get_var(vars, 'namespace_package').default = 'plonetheme'
    get_var(vars, 'namespace_package').description = 'Namespace package (like plonetheme)'
    get_var(vars, 'description').default = 'An installable theme for Plone 3.0'

    def pre(self, command, output_dir, vars):
        vars['timestamp'] = datetime.date.today().strftime("%Y%m%d")
        super(Plone3Theme, self).pre(command, output_dir, vars)


