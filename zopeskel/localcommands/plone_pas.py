"""
Local templates for the plone PAS zopeskel project
"""
from zopeskel.localcommands import ZopeSkelLocalTemplate

class PlonePasSubTemplate(ZopeSkelLocalTemplate):
    use_cheetah = True
    marker_name = 'implemented plugins'
    parent_templates = ['plone_pas']


class ExtractionPlugin(PlonePasSubTemplate):
    """
    A plone pas extraction plugin
    """
    _template_dir = 'templates/plone_pas/extraction'
    summary = "A Plone PAS Extraction Plugin"


class AuthenticationPlugin(PlonePasSubTemplate):
    """
    A plone pas authentication plugin
    """
    _template_dir = 'templates/plone_pas/authentication'
    summary = "A Plone PAS Authentication Plugin"


class ChallengePlugin(PlonePasSubTemplate):
    """
    A plone pas challenge plugin
    """
    _template_dir = 'templates/plone_pas/challenge'
    summary = "A Plone PAS Challenge Plugin"


class CredentialsResetPlugin(PlonePasSubTemplate):
    """
    A plone pas CredentialsReset plugin
    """
    _template_dir = 'templates/plone_pas/credentials_reset'
    summary = "A Plone PAS CredentialsReset Plugin"


class UserAdderPlugin(PlonePasSubTemplate):
    """
    A plone pas UserAdder plugin
    """
    _template_dir = 'templates/plone_pas/user_adder'
    summary = "A Plone PAS UserAdder Plugin"


class RoleAssignerPlugin(PlonePasSubTemplate):
    """
    A plone pas RoleAssigner plugin
    """
    _template_dir = 'templates/plone_pas/role_assigner'
    summary = "A Plone PAS RoleAssigner Plugin"


class UserFactoryPlugin(PlonePasSubTemplate):
    """
    A plone pas UserFactory plugin
    """
    _template_dir = 'templates/plone_pas/user_factory'
    summary = "A Plone PAS UserFactory Plugin"


class AnonymousUserFactoryPlugin(PlonePasSubTemplate):
    """
    A plone pas AnonymousUserFactory plugin
    """
    _template_dir = 'templates/plone_pas/anonymous_user_factory'
    summary = "A Plone PAS AnonymousUserFactory Plugin"


class PropertiesPlugin(PlonePasSubTemplate):
    """
    A plone pas Properties plugin
    """
    _template_dir = 'templates/plone_pas/properties'
    summary = "A Plone PAS Properties Plugin"



class GroupsPlugin(PlonePasSubTemplate):
    """
    A plone pas Groups plugin
    """
    _template_dir = 'templates/plone_pas/groups'
    summary = "A Plone PAS Groups Plugin"


class RolesPlugin(PlonePasSubTemplate):
    """
    A plone pas Roles plugin
    """
    _template_dir = 'templates/plone_pas/roles'
    summary = "A Plone PAS Roles Plugin"


class UpdatePlugin(PlonePasSubTemplate):
    """
    A plone pas Update plugin
    """
    _template_dir = 'templates/plone_pas/update'
    summary = "A Plone PAS Update Plugin"


class ValidationPlugin(PlonePasSubTemplate):
    """
    A plone pas Validation plugin
    """
    _template_dir = 'templates/plone_pas/validation'
    summary = "A Plone PAS Validation Plugin"


class UserEnumerationPlugin(PlonePasSubTemplate):
    """
    A plone pas UserEnumeration plugin
    """
    _template_dir = 'templates/plone_pas/user_enumeration'
    summary = "A Plone PAS UserEnumeration Plugin"


class GroupEnumerationPlugin(PlonePasSubTemplate):
    """
    A plone pas GroupEnumeration plugin
    """
    _template_dir = 'templates/plone_pas/group_enumeration'
    summary = "A Plone PAS GroupEnumeration Plugin"


class RoleEnumerationPlugin(PlonePasSubTemplate):
    """
    A plone pas RoleEnumeration plugin
    """
    _template_dir = 'templates/plone_pas/role_enumeration'
    summary = "A Plone PAS RoleEnumeration Plugin"


