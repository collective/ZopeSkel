from Products.Five.formlib import formbase

from zope import interface, schema
from zope.formlib import form
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


def failing_constraint(value):
    return 1 == 2


def successfull_constraint(value):
    return 1 == 1


class IObjectSchema(interface.Interface):
    test_field = schema.Text(
        title=u'Test field',
        description=u'field description',
        required=True,
        readonly=False,
        default=u'default',
        missing_value=u'missing value')

class IExampleSchema(interface.Interface):
    """
    Field types:
        Datetime - Field containing a DateTime
        Date - Field containing a date
        Timedelta - Field containing a timedelta
        Password - Field containing a unicode string without newlines that is a
            password
        Object - Field containing an Object value
        URI - A field containing an absolute URI
        ASCII - Field containing a 7-bit ASCII string. No characters > DEL
            (chr(127)) are allowed
        ASCIILine - Field containing a 7-bit ASCII string without newlines
        Bytes - Field containing a byte string (like the python str)
        BytesLine - Field containing a byte string without newlines
        Tuple - Field containing a value that implements the API of a
            conventional Python tuple
        List - Field containing a value that implements the API of a
            conventional Python list
        Set - Field containing a value that implements the API of a
            conventional Python standard library sets
        FrozenSet - Field containing a value that implements the API of a
            conventional Python 2.4+ frozenset
        Dict - Field containing a conventional dict
        SourceText - Field for source text of object
        Id - A field containing a unique identifier
            A unique identifier is either an absolute URI or a dotted name.
            If it's a dotted name, it should have a module/package name as a
            prefix
        DottedName - Dotted name field
        InterfaceField - Fields with a value that is an interface (implementing
            zope.interface.Interface)

    Field types arguments:
        title - A short summary or label
        description - A description of the field (to be displayed as a hint)
        required - Tells whether a field requires its value to exist
        readonly - If true, the field's value cannot be changed
        default - The field default value may be None or a legal field value
        missing_value - If a field has no assigned value, set it to this value
        constraint - function checking a constraint on the field
    """

    # Text - Field containing a unicode string
    text_field = schema.Text(
        title=u'Text field',
        description=u'field description',
        required=True,
        readonly=False,
        default=u'default value',
        missing_value=u'missing value'
        )

    # TextLine - Field containing a unicode string without newlines
    textline_field = schema.TextLine(
        title=u'Textline field',
        description=u'field description',
        required=True,
        readonly=False,
        default=u'default value',
        missing_value=u'missing value',
        constraint=successfull_constraint
        )

    # Int - Field containing an Integer Value
    int_field = schema.Int(
        title=u'Integer field',
        description=u'field description',
        required=True,
        readonly=False,
        default=0,
        missing_value=1,
        min=0,
        max=10
        )

    # Bool - Boolean Field
    bool_field = schema.Bool(
        title=u'Boolean field',
        description=u'field description',
        required=True,
        readonly=False,
#        default=True,
#        missing_value=True
        )

    # Float - Field containing a Float
    float_field = schema.Float(
        title=u'Float field',
        description=u'field description',
        required=True,
        readonly=False,
#        default=0.0,
#        missing_value=0.0
        )

    # Choice - Field whose value is contained in a predefined set
    # Only one, values or vocabulary, may be specified for a given choice
    choice_field = schema.Choice(
        title=u'Choice field',
        description=u'field description',
        required=True,
        readonly=False,
#        default='Title 2',
#        missing_value='Option 2',
#        Only one of the arguments: vocabulary, source or values may be used
        vocabulary=SimpleVocabulary((
            SimpleTerm(value=1, token='Option 1', title='Title 1'),
            SimpleTerm(value=2, token='Option 2', title='Title 2')
            ))
#        source=VocabularyExample
#        values=['Option 1', 'Option 2'],
        )

#    object_field = schema.Object(
#        title=u'Object field',
#        description=u'field description',
#        required=True,
#        readonly=False,
#        default=None,
#        missing_value=None,
#        schema=IObjectSchema
#        )


class ExampleForm(formbase.PageForm):
    form_fields = form.FormFields(IExampleSchema)
    # Put here the label to be displayed as form title
    label = u'Form label'
    # Put here the form description to be displayed under the form title
    description = u'Form short description'

    # Instead of 'Submit button' put here the label of the form submit button
    @form.action('Submit button', failure='handle_failure')
    def handle_success(self, action, data):
        """
        Called when the action was submitted and there are NO validation
        errors.

        This form is generated with ZopeSkel. Please make sure you fill in
        the implementation of the form processing.

        """
        # Put here the feedback to show in case the form submission succeeded
        self.status = 'The handle_success method of the %s form is not \
            implemented.' % (self.__class__.__name__)

        # Put here the code for processing the form


    def handle_failure(self, action, data, errors):
        """
        Called when the action was submitted and there are validation errors.

        """
        # Put here the feedback message to show in case the validation failed
        self.status = 'Errors occured while submitting the form'



