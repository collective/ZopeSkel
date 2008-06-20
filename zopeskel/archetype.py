import copy

from zopeskel.plone import Plone
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



