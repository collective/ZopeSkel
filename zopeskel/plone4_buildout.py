import copy

from zopeskel import abstract_buildout

class Plone4Buildout(abstract_buildout.AbstractBuildout):
    _template_dir = 'templates/plone4_buildout'
    summary = "A buildout for Plone 4 developer installation"
    help = """This template creates a Plone 4 buildout for development purposes.
It uses Zope in debug mode and sets a default password.
"""
    pre_run_msg = ""

    post_run_msg = """
Generation finished.

Now run bootstrap and buildout:

python bootstrap.by

bin/buildout

See ZopeSkel add-on page for more details:

http://plone.org/products/zopeskel 

"""

    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(abstract_buildout.AbstractBuildout.vars)
    
    vars = vars[1:]
    
    vars.extend(
           [ abstract_buildout.VAR_PLONEVER,           
        ]
    )
    
    # Set default Plone 4 version
    vars[0].default = "4.0.5"
    
    def pre(self, command, output_dir, vars):
        
        # For easy mode (don't ask stupid questions)
        vars['expert_mode'] = 'easy' 
        vars['eggifiedzope'] = True
        vars['zope2_install'] = True
        vars['zope2_version'] = "2.12.3"
        super(Plone4Buildout, self).pre(command, output_dir, vars)



