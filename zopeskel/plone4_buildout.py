import copy

from zopeskel import abstract_buildout

class Plone4Buildout(abstract_buildout.AbstractBuildout):
    _template_dir = 'templates/plone4_buildout'
    summary = "A buildout for Plone 4 developer installation"
    help = """

This template creates a Plone 4 buildout (for most users, a preferred
way to get an installation of Plone is to use the appropriate installer,
as these are all buildout-based since Plone 3.1)
"""
    pre_run_msg = """
*** NOTE: You probably don't want to use this template!

Since Plone 3.1, the preferred way to get a buildout-based setup for
Plone is to use the standard installer for your operating system (the
Windows installer, the Mac installer, or the Unified Installer for
Linux/Unix/BSD). These give you a best-practice, widely-used
setup with an isolated Python and a well-documented buildout.
This template is here for older versions of Plone and for experts
who explicitly want a raw, non-installer-based installation.

(This message is particularly aimed at people following out-of-date
books/documentation that suggest this is the right way to get
a Plone-based buildout. This is no longer the case.)
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
    vars.extend(
           [ abstract_buildout.VAR_PLONEVER,           
             abstract_buildout.VAR_Z2_INSTALL,
             abstract_buildout.VAR_PLONE_PRODUCTS,
        ]
    )

    def pre(self, command, output_dir, vars):
        vars['eggifiedzope'] = True
        vars['zope2_install'] = True
        vars['zope2_version'] = "2.12.3"
        super(Plone4Buildout, self).pre(command, output_dir, vars)



