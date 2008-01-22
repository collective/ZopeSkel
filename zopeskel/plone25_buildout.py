from zopeskel.plone3_buildout import Plone3Buildout

class Plone25Buildout(Plone3Buildout):
    _template_dir = 'templates/plone2.5_buildout'
    summary = "A buildout for Plone 2.5 projects"
    required_templates = ['plone3_buildout']


