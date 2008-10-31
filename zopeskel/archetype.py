import os
import copy

from zopeskel.plone import Plone
from zopeskel.base import get_var
from zopeskel.base import var

class Archetype(Plone):
    _template_dir = 'templates/archetype'
    summary = 'A Plone project that uses Archetypes'
    required_templates = ['plone']
    use_cheetah = True
    use_local_commands = True

    vars = copy.deepcopy(Plone.vars)
    vars.insert(0, var('title',
                       'The title of the project',
                       default='Plone Example'))

    #zope2product should always defaults to True
    get_var(vars, 'zope2product').default = True

    def post(self, command, output_dir, vars):
        # Remove tests.py -- we already have a tests/ package
        path = os.path.join(output_dir,
                            vars['namespace_package'],
                            vars['package'])
        os.remove(os.path.join(path, 'tests.py'))

        super(Archetype, self).post(command, output_dir, vars)
