import copy

from zopeskel import abstract_buildout
from zopeskel.base import var, EASY, EXPERT
from zopeskel.vars import StringVar, StringChoiceVar


class SilvaBuildout(abstract_buildout.AbstractBuildout):
    _template_dir = 'templates/silva_buildout'
    summary = "A buildout for Silva projects"
    help = """
This template creates an installation of Silva 
(http://www.infrae.com/products/silva).
"""
    post_run_msg = """
Generation finished.

You probably want to run python bootstrap.py and then edit
buildout.cfg before running bin/buildout -v".

See README.txt for details.
"""
    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(abstract_buildout.AbstractBuildout.vars)
    vars.extend([
        abstract_buildout.VAR_Z2_INSTALL,
        StringChoiceVar(
            'silva_distribution',
            title='Silva Distribution',
            description='Version of Silva to install, "stable" or "development"',
            default="stable",
            modes=(EASY, EXPERT),
            page='Main',
            choices=('stable','development'),
            ),
        abstract_buildout.VAR_ZOPE_USER,
        abstract_buildout.VAR_ZOPE_PASSWD,
        abstract_buildout.VAR_HTTP,
        abstract_buildout.VAR_DEBUG_MODE,
        abstract_buildout.VAR_VERBOSE_SEC,
        ]
    )
