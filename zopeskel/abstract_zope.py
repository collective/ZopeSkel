import copy
from zopeskel.basic_namespace import BasicNamespace
from zopeskel.nested_namespace import NestedNamespace
from zopeskel.vars import BooleanVar

VAR_ZOPE2 = BooleanVar(
        'zope2product',
        title='Zope2 Product?',
        description='Are you creating a product for Zope2/Plone or an Archetypes Product?',
        default=True,
        modes=(),
        help="""
Zope2 products will have a registration hook in their __init__.py,
used by the Zope2 machinery to handle any required processes during
server startup. Archetypes projects will require this, and all
projects for Zope2/Plone will benefit from it (even if not strictly
required, this allows the project to appear in places like the
Zope2 Control Panel list of products).

An appropriate time to choose False here would be if you are creating
a completely Zope3-only or non-Zope project.
"""
        )

class AbstractZope(BasicNamespace):
    """Abstract class for Zope-based packages in a namespace."""
    vars = copy.deepcopy(BasicNamespace.vars)
    vars.append(VAR_ZOPE2)
    category = "Zope Development"

class AbstractNestedZope(NestedNamespace):
    """Abstract class for Zope-based packages in a nested namespace."""
    vars = copy.deepcopy(NestedNamespace.vars)
    vars.append(VAR_ZOPE2)
    category = "Zope Development"


