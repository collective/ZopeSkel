import copy

from zopeskel.nested_namespace import NestedNamespace
from zopeskel.base import get_var

class Recipe(NestedNamespace):
    """A template for buildout recipes"""
    _template_dir = 'templates/recipe'
    summary = "A recipe project for zc.buildout"
    help = """
This creates a skeleton for a buildout recipe.
"""
    category = "Buildout"
    required_templates = []
    use_cheetah = True
    vars = copy.deepcopy(NestedNamespace.vars)
    get_var(vars, 'namespace_package2').default = 'recipe'
    get_var(vars, 'license_name').default = 'ZPL'

