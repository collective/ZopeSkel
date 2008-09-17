import os
import copy

from zopeskel.base import BaseTemplate
from zopeskel.base import get_var
from zopeskel.base import var
from zopeskel.base import BasicPackage

TARGET_STYLESHEETS = (
    'base.css.dtml',
    'generated.css.dtml',
    'portlets.css.dtml',
    'public.css.dtml'
    )

def cleanupStylsheets(skinsdir, targets=TARGET_STYLESHEETS):
    for dirpath, dirnames, filenames in os.walk(skinsdir):
        for target in [t for t in targets if t in filenames]:
            print "Removing %s from %s%s" %(target, dirpath, os.sep)
            os.remove(os.path.join(dirpath, target))


theme_vars = [
    var('skinname',
        "The skin selection to be added to 'portal_skins' (like 'My Theme')"),
    var('skinbase',
        'Name of the skin selection from which the new one will be copied',
        default='Plone Default'),
    var('empty_styles',
        "Override default public stylesheets with empty ones?",
        default=True),
    var('include_doc',
        "Include in-line documentation in generated code?",
        default=False),
              ]

class Plone2Theme(BaseTemplate):
    _template_dir = 'templates/plone2_theme'
    summary = "A Theme Product for Plone 2.1 & Plone 2.5"
    use_cheetah = True

    vars = copy.deepcopy(BasicPackage.vars)
    get_var(vars, 'version').default = '1.0'
    get_var(vars, 'description').default = 'An installable theme for Plone'
    get_var(vars, 'author').default = 'Plone Collective'
    get_var(vars, 'author_email').default = 'product-developers@lists.plone.org'
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/collective/'
    get_var(vars, 'keywords').default = 'web zope plone theme'
    vars = theme_vars + vars[:3] + vars[4:6]

    def pre(self, command, output_dir, vars):
        if vars['skinname'] == '':
            # It is always good to have a name for the skin.
            vars['skinname'] = 'Custom Skin'
        super(Plone2Theme, self).pre(command, output_dir, vars)

    def post(self, command, output_dir, vars):
        if str(vars['empty_styles']) == 'False':
            cleanupStylsheets(os.path.join(output_dir, 'skins'))
        super(Plone2Theme, self).post(command, output_dir, vars)
