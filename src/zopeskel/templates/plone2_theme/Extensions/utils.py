import os, string
from Globals import package_home
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.utils import getToolByName


def getSkinsFolderNames(globals, skins_dir='skins'):
    # Get the content of the skins folder
    skins_path = os.path.join(package_home(globals), skins_dir)
    return [ filename for filename in os.listdir(skins_path)
        if (not filename.startswith('.') or filename in ('CVS', '{arch}'))
        and os.path.isdir(os.path.join(skins_path, filename)) ]

def setupSkin(self, out, globals, skin_selection, make_default,
                         allow_any, cookie_persistence, skins_dir='skins'):
    skins_tool = getToolByName(self, 'portal_skins')
    skin_name, base_skin = skin_selection['name'], skin_selection['base']

    # Only add the skin selection if it doesn't already exist
    if skin_name not in skins_tool.getSkinSelections():

        # Get the skin layers of the base skin and convert to an array
        layers = skins_tool.getSkinPath(base_skin)
        layers = map(string.strip, string.split(layers, ','))

        # Add the skin folders to the layers, under 'custom'
        filenames = skin_selection.get('layers',
                                     getSkinsFolderNames(globals, skins_dir))
        for filename in filenames:
            if filename not in layers:
                try:
                    layers.insert(layers.index('custom')+1, filename)
                except ValueError:
                    layers.insert(0, filename)

        # Add our skin selection
        layers = ', '.join(layers)
        skins_tool.addSkinSelection(skin_name, layers)
        print >> out, "Added skin selection to portal_skins."

        # Activate the skin selection
        if make_default:
            skins_tool.default_skin = skin_name

        # Setup other tool properties
        skins_tool.allow_any = allow_any
        skins_tool.cookie_persistence = cookie_persistence

    else:
        print >> out, "Skin selection already exists, leaving it alone."

def setupSkins(self, out, globals, skin_selections, select_skin, default_skin,
                          allow_any, cookie_persistence, skins_dir='skins'):
    skins_tool = getToolByName(self, 'portal_skins')

    # Add directory views
    addDirectoryViews(skins_tool, skins_dir, globals)
    print >> out, "Added directory views to portal_skins."

    # Install skin selections
    for skin in skin_selections:
        make_default = False
        if select_skin and skin['name'] == default_skin:
            make_default = True
        setupSkin(self, out, globals, skin, make_default,
                                   allow_any, cookie_persistence, skins_dir)

def registerResources(self, out, toolname, resources):
    tool = getToolByName(self, toolname)
    existing = tool.getResourceIds()
    cook = False
    for resource in resources:
        if not resource['id'] in existing:
            # register additional resource in the specified registry...
            if toolname == "portal_css":
                tool.registerStylesheet(**resource)
            if toolname == "portal_javascripts":
                tool.registerScript(**resource)
            print >> out, "Added %s to %s." % (resource['id'], tool)
        else:
            # ...or update existing one
            parameters = tool.getResource(resource['id'])._data
            for key in [k for k in resource.keys() if k != 'id']:
                originalkey = 'original_'+key
                original = parameters.get(originalkey)
                if not original:
                    parameters[originalkey] = parameters[key]
                parameters[key] = resource[key]
                print >> out, "Updated %s in %s." % (resource['id'], tool)
                cook = True
    if cook:
        tool.cookResources()
    print >> out, "Successfuly Installed/Updated resources in %s." % tool

def removeSkins(self, out, skin_selections=(),
                           default=None, resetskintool=True):
    skins_tool = getToolByName(self, 'portal_skins')

    # Remove skin selections from portal_skins
    for skin in skin_selections:
        skin_name = skin['name']
        if skin_name in skins_tool.getSkinSelections():
            skins_tool.manage_skinLayers(del_skin=1, chosen=(skin_name,))
            print >> out, \
                "Removed skin selection '%s' from portal skins." %skin_name

    # Set Skins Tool parameters back to defaults
    if resetskintool:
        # Restore Plone defaults
        skins_tool.allow_any = 0
        skins_tool.cookie_persistence = 0
        selection = 'Plone Default'
        print >> out, "Restored Plone defaults in portal_skins"
    else:
        # Select the base of the default skin selection in the skins tool
        if skin_selections:
            if default:
                selection = [ s for s in skin_selections
                              if s['name'] == default ]
                if selection:
                    selection = selection[0]['base']
            else:
                selection = skin_selections[0]['base']
    skins_tool.default_skin = selection
    print >> out, "Setup '%s' as default skin in portal_skins" % selection

def resetResources(self, out, toolname, resources):
    # Revert resource customizations
    tool = getToolByName(self, toolname)
    for resource in [tool.getResource(r['id']) for r in resources]:
        if resource is None:
            continue
        for key in resource._data.keys():
            originalkey = 'original_'+key
            if resource._data.has_key(originalkey):
                try: # <- BBB
                    resource._data[key] = resource._data[originalkey]['value']
                except TypeError:
                    resource._data[key] = resource._data[originalkey]
                del resource._data[originalkey]

__all__ = (
    "setupSkins",
    "registerResources",
    "removeSkins",
    "resetResources",
        )
