"""
Local templates
"""

from zopeskel import get_var, removeFile, var
from zopeskel.localcommands import ZopeSkelLocalTemplate


class Portlet(ZopeSkelLocalTemplate):
    """
    A plone 3 portlet skeleton
    """
    _template_dir = 'templates/portlet'
    summary = "A Plone 3 portlet"
    use_cheetah = True

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


class View(ZopeSkelLocalTemplate):
    """
    A browser view skeleton
    """
    _template_dir = 'templates/view'
    summary = "A browser view skeleton"
    use_cheetah = True

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


class ZCMLMetaDirective(ZopeSkelLocalTemplate):
    """
    A zcml meta directive skeleton
    """
    _template_dir = 'templates/zcmlmeta'
    summary = "A ZCML meta directive skeleton"
    use_cheetah = True

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


class ContentType(ZopeSkelLocalTemplate):
    """
    A Content Type skeleton
    """

    _template_dir = 'templates/contenttype'
    summary = "A content type skeleton"
    use_cheetah = True

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
