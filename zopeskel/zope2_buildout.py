import copy

from zopeskel import abstract_buildout
from zopeskel.base import var, EASY, EXPERT
from zopeskel.vars import StringVar


class Zope2Buildout(abstract_buildout.AbstractBuildout):
    _template_dir = 'templates/zope2_buildout'
    summary = "A buildout for a blank (non-Silva, non-Plone) Zope 2 instance"
    help = """
This template creates a buildout that does not contain Plone or Silva
information. It is intended for people using Zope 2 directly. If you
would like to use Plone or Silva, you should use the appropriate buildouts.
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
        StringVar(
            'zope2_version',
            title='Zope 2 Version',
            description='Version of Zope 2 to fetch, if needed',
            modes=(EASY, EXPERT),
            page='Main',
            default='2.11.1',
            help="""
If a version of Zope needs to be pulled down, this option lets you
specify the version.
"""
            ),
        abstract_buildout.VAR_ZOPE_USER,
        abstract_buildout.VAR_ZOPE_PASSWD,
        abstract_buildout.VAR_HTTP,
        abstract_buildout.VAR_DEBUG_MODE,
        abstract_buildout.VAR_VERBOSE_SEC,
        ]
    )



