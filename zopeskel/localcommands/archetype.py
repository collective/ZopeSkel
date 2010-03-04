"""
Local templates for the archetype zopeskel project
"""
import os
from zopeskel.base import var
from zopeskel.localcommands import ZopeSkelLocalTemplate

from Cheetah.Template import Template as cheetah_template


class ArchetypeSubTemplate(ZopeSkelLocalTemplate):
    use_cheetah = True
    parent_templates = ['archetype']


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

    # mapping of ATSchema types to zope.schema types
    typemap = {'boolean': 'Bool',
               'computed': 'TextLine',
               'cmfobject': 'TextLine',
               'datetime': 'Date',
               'file': 'Bytes',
               'fixedpoint': 'Float',
               'float': 'Float',
               'image': 'Bytes',
               'integer': 'Int',
               'lines': 'List',
               'reference': 'Object',
               'string': 'TextLine',
               'text': 'Text',
               'unknown': 'TextLine'}

    # fieldtypes-map to (widget, validator)
    fieldtypes = {
        'boolean': ('boolean', None),
        'computed': ('computed', None),
        'cmfobject': ('file', None),
        'datetime': ('calendar', 'isValidDate'),
        'file': ('file', 'isNonEmptyFile'),
        'fixedpoint': ('decimal', 'isDecimal'),
        'float': ('decimal', 'isDecimal'),
        'image': ('image', 'isNonEmptyFile'),
        'integer': ('integer', 'isInt'),
        'lines': ('lines', None),
        'reference': ('reference', None),
        'string': ('string', None),
        'text': ('textarea', None),
    }

    vars = [
        var('content_class_filename',      
            'What is the module (file)name of your content class?',           
            default='exampletype'),
        var('field_name',
            'What would you like to name this field?',
            default='newfield'),
        var('field_type',       
            'What kind of field should I make for you?\nSome examples: ['+','.join(fieldtypes.keys())+']\n', 
            default='string'),            
        var('widget_type',      
            'What kind of widget do you want to use (example: Password)?',   
            default='default'),
        var('field_label',
            'What should be the label of this field (title)?',
            default='New Field'),
        var('field_desc',
            'What should be the description of this field (help text)?',
            default='Field description'),
        var('required',
            'Is this field required?',
            default='False'),
        var('default',
            "If you'd like a default type it here, otherwise leave it blank",
            default=''),
        var('validator',
            "Enter a validator (isEmail), or None, or get a default validator for your specified field type.",
            default='use default validator'),
        ]

    def check_vars(self, *args, **kwargs):
        """
        Overloading check_vars to print welcome message
        """

        print "Welcome to the ATSchema Builder. Field names/widgets can be specified in lowercase or upper case."
        print "NOTE: No need to add 'widget' or 'field' to the names. atschema does the work for you!"
        print "See "
        print "    http://plone.org/documentation/manual/archetypes-developer-manual/fields/fields-reference/"
        print "and "
        print "    http://plone.org/documentation/manual/archetypes-developer-manual/fields/widgets-reference"
        print "for field and widget details"

        return super(ATSchemaField, self).check_vars(*args, **kwargs)

    def run(self, command, output_dir, vars):
        """
        By-passing the base run so I can do multiple inserts
        with different marker names
        """

        (vars['namespace_package'],
         vars['namespace_package2'],
         vars['package']) = command.get_parent_namespace_packages()

        if vars['namespace_package2']:
            vars['package_dotted_name'] = "%s.%s.%s" % \
                (vars['namespace_package'],
                vars['namespace_package2'],
                vars['package'])
        else:
            vars['package_dotted_name'] = "%s.%s" % \
                (vars['namespace_package'],
                 vars['package'])
        
        vars['a_validator'] = ''
        if vars['validator'] == 'use default validator':
            ## take default Validator...
            val = ATSchemaField.fieldtypes[vars['field_type'].lower()][1]
            if val is not None:
                vars['a_validator'] = """'%s'""" % val
        elif vars['validator'] != 'None':    ## user providing 'aValidator'
            vars['a_validator'] = """'%s'""" % vars['validator']

        self.pre(command, output_dir, vars)

        interface_insert_template = open(os.path.join(self.template_dir(), 'interfaces/+interface_name+.py_insert')).read()
        atschema_insert_template = open(os.path.join(self.template_dir(),'content/+content_class_filename+.py_insert')).read()
        bridges_insert_template = open(os.path.join(self.template_dir(),'content/schema_field_bridge.txt_insert')).read()
        content_messagefactory_insert_template = open(os.path.join(self.template_dir(), 'content/messagefactory_insert.txt_insert')).read()
        interface_additional_imports_template = open(os.path.join(self.template_dir(), 'interfaces/additional_imports.txt_insert')).read()

        # insert_into_file really wants the inserted text to end with a newline
        interface_insert = str(cheetah_template(interface_insert_template, vars))+"\n"
        atschema_insert = str(cheetah_template(atschema_insert_template, vars))+"\n"
        bridges_insert = str(cheetah_template(bridges_insert_template, vars))+"\n"
        content_messagefactory_insert = str(cheetah_template(content_messagefactory_insert_template, vars))+"\n"
        interface_additional_imports = str(cheetah_template(interface_additional_imports_template, vars))+"\n"

        # self.write_files(command, output_dir, vars)
        command.insert_into_file(os.path.join(command.dest_dir(), 'content', '%s.py' % (vars['content_class_filename'])), self.marker_name, atschema_insert)
        command.insert_into_file(os.path.join(command.dest_dir(), 'interfaces', '%s.py' % (vars['content_class_filename'])), 'schema definition goes here', interface_insert)
        command.insert_into_file(os.path.join(command.dest_dir(), 'content', '%s.py' % (vars['content_class_filename'])), 'Your ATSchema to Python Property Bridges Here ...', bridges_insert)
        command.insert_into_file(os.path.join(command.dest_dir(), 'content', '%s.py' % (vars['content_class_filename'])), 'Message Factory Imported Here', content_messagefactory_insert)
        command.insert_into_file(os.path.join(command.dest_dir(), 'interfaces', '%s.py' % (vars['content_class_filename'])), 'Additional Imports Here', interface_additional_imports)

        self.post(command, output_dir, vars)


    def pre(self, command, output_dir, vars):

        file = vars['content_class_filename']
        if file.endswith('.py'):
            file = os.path.splitext(file)[0]

        vars['field_type'] = vars['field_type'].capitalize()

        if vars['widget_type'].lower() == 'default':
            vars['widget_type'] = self.fieldtypes[vars['field_type'].lower()][0]
        
        vars['widget_type'] = vars['widget_type'].capitalize()

        # camelcase multiword names
        if vars['field_type'].lower() == 'fixedpoint':
            vars['field_type'] = 'FixedPoint'

        if vars['field_type'].lower() == 'datetime':
            vars['field_type'] = 'DateTime'

        if vars['field_type'].lower() == 'date':
            vars['field_type'] = 'DateTime'

        if vars['widget_type'].lower() == 'inandout':
            vars['widget_type'] = 'InAndOut'

        if vars['widget_type'].lower() == 'multiselection':
            vars['widget_type'] = 'MultiSelection'

        if vars['widget_type'].lower() == 'picklist':
            vars['widget_type'] = 'PickList'

        if vars['widget_type'].lower() == 'referencebrowser':
            vars['widget_type'] = 'ReferenceBrowser'

        if vars['widget_type'].lower() == 'textarea':
            vars['widget_type'] = 'TextArea'

        # try to get the zope.schema type, but default to TextLine if no dice
        try:
            vars['zopeschema_type'] = self.typemap[vars['field_type'].lower()]
        except:
            vars['zopeschema_type'] = self.typemap['unknown']

        # if the widget is the RichWidget, set the type to 'SourceText'
        if vars['widget_type'].lower() == 'rich':
            vars['zopeschema_type'] = 'SourceText'

        # if not vars['i18n_domain']:
        #     vars['i18n_domain'] = vars['package_dotted_name']

        vars['content_class_filename'] = file
