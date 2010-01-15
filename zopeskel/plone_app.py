import copy

from zopeskel.base import get_var
from zopeskel.base import var
from zopeskel import abstract_zope

class PloneApp(abstract_zope.AbstractNestedZope):
    _template_dir = 'templates/plone_app'
    summary = "A project for Plone products with a nested namespace (2 dots in name)"
    help = """
This creates a Plone project (to create a Plone *site*, you probably
want to use the one of the templates for a buildout).

To create a Plone project with a name like 'mycompany.myproject' (1 dot,
a 'basic namespace'), use the 'plone' template instead.
"""
    required_templates = ['nested_namespace']
    use_cheetah = True
    category = "Plone Development"

    vars = copy.deepcopy(abstract_zope.AbstractNestedZope.vars)

