"""
Local templates for the archetype zopeskel project
"""
import os
from zopeskel.base import var
from zopeskel.localcommands import ZopeSkelLocalTemplate

class ArchetypeSubTemplate(ZopeSkelLocalTemplate):
    use_cheetah = True
    parent_templates = ['archetype']


class Portlet(ArchetypeSubTemplate):
    """
    A plone 3 portlet skeleton
    """
    _template_dir = 'templates/archetype/portlet'
    summary = "A Plone 3 portlet"

    vars = [
      var('portlet_name', 'Portlet name (human readable)',  default="Example portlet"),
      var('portlet_type_name', 'Portlet type name (should not contain spaces)', default="ExamplePortlet"),
      var('description', 'Portlet description', default=""),
           ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['portlet_filename'] = vars['portlet_type_name'].lower()

        vars['dotted_name'] = "%s.portlets" % vars['package_dotted_name']


class View(ArchetypeSubTemplate):
    """
    A browser view skeleton
    """
    _template_dir = 'templates/archetype/view'
    summary = "A browser view skeleton"

    vars = [
      var('view_name', 'Browser view name',  default="Example"),
           ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['view_filename'] = vars['view_name'].lower()


class ZCMLMetaDirective(ArchetypeSubTemplate):
    """
    A zcml meta directive skeleton
    """
    _template_dir = 'templates/archetype/zcmlmeta'
    summary = "A ZCML meta directive skeleton"

    vars = [
      var('directive_name', 'The directive name',  default="mydirective"),
      var('directive_namespace', 'The directive namespace',  default="mynamespace"),
           ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['directive_class_name'] = vars['directive_name'].title()


class ContentType(ArchetypeSubTemplate):
    """
    A Content Type skeleton
    """

    _template_dir = 'templates/archetype/contenttype'
    summary = "A content type skeleton"

    vars = [
        var('contenttype_name', 'Content type name ', default='Example Type'),
        var('contenttype_description', 'Content type description ',
            default='Description of the Example Type'),
        var('folderish', 'True/False: Content type is Folderish ',
            default=False),
        var('global_allow', 'True/False: Globally addable ',
            default=True),
        var('allow_discussion', 'True/False: Allow discussion ',
            default=False),
        ]

    def pre(self, command, output_dir, vars):

        vars['contenttype_classname'] = vars['contenttype_name'].replace(" ", "")
        vars['schema_name'] = vars['contenttype_classname'] + "Schema"
        vars['content_class_filename'] = vars['contenttype_classname'].lower()
        vars['types_xml_filename'] = vars['contenttype_name'].replace(" ", "_")
        vars['interface_name'] = "I" + vars['contenttype_name'].replace(" ", "")
        vars['add_permission_name'] = vars['package_dotted_name'] + ': Add ' + vars['contenttype_name']
        
        
        
class ATSchemaField(ArchetypeSubTemplate):
    """
    A handy AT schema builder
    """

    _template_dir = 'templates/archetype/atschema'
    summary = "A handy AT schema builder"
    marker_name = "Your Archetypes field definitions here ..."

    vars = [
        var('welcome',
            '\n\nWelcome to the handy AT Schema maker, we hope you like it! Crtain things are implied: i.e. Field Type should be String, not StringField.  We do the work for you!',
            default='True'),
        var('content_class_filename',      
            '\n\nWhat is the module (file)name of your content class? (.py is implied)\n',           
            default='exampletype'),
        var('field_type',       
            '\n\nWhat kind of field should I make for you?\n', 
            default='String'),            
        var('field_name',       
            '\n\nWhat would you like to name this field?\n',     
            default='field'),
        var('widget_type',      
            '\n\nWhat kind of widget do you want to use?\n',   
            default='String'),
        var('field_label',      
            '\n\nWhat should be the label of this field (title)?\n',   
            default='New Field'),
        var('field_desc',       
            '\n\nWhat should be the description of this field (help text)?\n',   
            default='Field description'),
        var('i18n_domain',
            '\n\nWhat is the product name/i18n domain?\n',
            default='myProduct'),
        var('required',
            '\n\nIs this field required?\n',
            default='False'),
        var('default',
            "\n\nIf you'd like a default type it here, otherwise leave it blank\n",
            default=''),
        ]

    def pre(self, command, output_dir, vars):
        
        file = vars['content_class_filename']
        if file.endswith('.py'):
            file = os.path.splitext(file)[0]
        
        vars['content_class_filename'] = file

