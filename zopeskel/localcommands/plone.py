"""
Local templates that are generically useful for every plone related project.
"""
from zopeskel.base import var
from zopeskel.localcommands import ZopeSkelLocalTemplate

class PloneSubTemplate(ZopeSkelLocalTemplate):
    use_cheetah = True
    parent_templates = ['plone', 'archetype']


class Portlet(PloneSubTemplate):
    """
    A plone 3 portlet skeleton
    """
    _template_dir = 'templates/plone/portlet'
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


class View(PloneSubTemplate):
    """
    A browser view skeleton
    """
    _template_dir = 'templates/plone/view'
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
        vars['view_filename'] = vars['view_name'].lower().replace(' ', '')
        vars['view_classname'] = vars['view_name'].replace(' ', '')


class ZCMLMetaDirective(PloneSubTemplate):
    """
    A zcml meta directive skeleton
    """
    _template_dir = 'templates/plone/zcmlmeta'
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


class I18nLocale(PloneSubTemplate):
    """
    A skeleton for an i18n language
    """
    _template_dir = 'templates/plone/i18nlocales'
    summary = "An i18n locale directory structure"

    vars = [
      var('language_code', 'The iso-code of the language'),
           ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        # There is no default for language_code, because that makes no sense
        # To accomodate testing, we introduce a default here.

        language_iso_code = vars['language_code'].lower().strip()
        vars['language_iso_code'] = language_iso_code and language_iso_code or 'nl'

class Form(PloneSubTemplate):
    """
    A form skeleton
    """
    _template_dir = 'templates/plone/form'
    summary = "A form skeleton"

    vars = [
      var('form_name', 'Form name',  default="Example"),
           ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['form_filename'] = vars['form_name'].lower()
        
        
class Z3cForm(PloneSubTemplate):
    """
    A zc3 form skeleton
    """
    _template_dir = 'templates/archetype/form'
    summary = "A form skeleton"

    vars = [
      var('form_name', 'Form name',  default="Example"),
           ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['form_filename'] = vars['form_name'].lower()

class FormFields(PloneSubTemplate):
    """
    A template to add form fields
    """
    _template_dir = 'templates/archetype/formfields'
    summary = "Schema fields for a form"

    vars = [
      var('form_filename', "Name of the form file (in /browser)", default="example"),
      var('form_fields_str', 'Enter the form fields. To enter multiple fields at a time please enter a \
      comma-separated list of "name:type" pairs. Possible types are: text,textline,int',  default="examplefield:text"),
           ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['form_fields'] = [[y.strip() for y in x.strip().split(":")] 
                               for x in vars['form_fields_str'].split(",")]

