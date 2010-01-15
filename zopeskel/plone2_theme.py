import os
import copy

from zopeskel.base import BaseTemplate
from zopeskel.base import get_var
from zopeskel.base import var, EASY, EXPERT
from zopeskel.base import BasicPackage
from zopeskel.vars import StringVar, BooleanVar

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
    StringVar(
        'skinname',
        title='Skin Name',
        description='Name of the theme (human facing, added to portal_skins)',
        modes=(EASY, EXPERT),
        page='Main',
        help="""
This becomes the theme name (eg "My Theme").

It appears as the skin name choice in portal_skins, and is generated into
the GenericSetup profile.
"""
        ),

    StringVar(
        'skinbase',
        title='Skin Base',
        description='Name of the theme from which this is copied',
        modes=(EXPERT,),
        page='Main',
        default='Plone Default',
        help="""
Themes can descend from other themes--by choosing a base theme here,
your new theme will use the same skinpath ordering as this theme, except
your theme-specific folders will appear at the top (right below 'custom').

Typically, this will be 'Plone Default', the standard Plone theme.
Unless you are certain what you are doing, keep this choice.
"""
        ),

    BooleanVar('empty_styles',
        title='Empty Styles?',
        description='Override default public stylesheets with empty ones?',
        modes=(EASY, EXPERT),
        page='Main',
        default=False,
        help="""
If this is not selected, your new theme will have the same CSS as the
theme you are descending from (your skin base, answered above).

If this is selected, your theme will have empty CSS files for several
common 'public' areas--thereby starting you off with a theme that has
less of the skin base's look and feel.

Typically, if you are descending from Plone Default, this effectively
hides some of the 'plone look and feel' from your theme; you'd then
have to write CSS to provide more of your own look and feel.

You can always refine the choice made here--to hide more of the base
theme, create additional empty CSS files in your new theme to override
other standard CSS files. To gain back some of the lost base look,
you can just delete these overriding CSS files from your theme
and the originals will now shine through.
"""
            ),

    BooleanVar('include_doc',
        title='Include Documentation?',
        description="Include in-line documentation in generated code?",
        modes=(EASY, EXPERT),
        page="Main",
        default=True,
        help="""
If selected, this adds verbose, helpful comments to the generated files.
It does not change the appearance or functionality of the theme.
These comments can always later be deleted.

It is recommend you leave this on.
"""
        ),
              ]

class Plone2Theme(BaseTemplate):

    # This does not descend from AbstractZope, since it's not
    # a egg package, but just a raw Zope Product (unlike other
    # templates)

    _template_dir = 'templates/plone2_theme'
    summary = "A theme for Plone 2.1"
    ndots = 0
    help = """
This creates a project for a theme for Plone 2.1.

This is not an egg, but a classic Product, and therefore is usable in
Plone 2.1. This product should also work, without changes, in Plone
2.5, though you may prefer to use the 'plone25_theme' template for
this, as this will build an eggified Plone 2 theme.

This template expects a name that is just the name of a classic
product--a legal Python identifer without any dots in the name.
"""
    category = "Plone Development"

    use_cheetah = True

    vars = copy.deepcopy(BasicPackage.vars)
    get_var(vars, 'description').default = 'An installable theme for Plone'
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
