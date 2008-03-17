from zopeskel.base import BaseTemplate
from zopeskel.base import BadCommand
from zopeskel.base import var
from zopeskel.base import templates


class SilvaBuildout(BaseTemplate):
    _template_dir = 'templates/silva_buildout'
    summary = "A buildout for Silva projects"
    required_templates = []
    use_cheetah = True

    vars = [
        var('zope2_install',
            'Path to Zope 2 installation; leave blank to fetch one',
            default=''),
        var('silva_distribution',
            'Silva version to install, "stable" or "development"',
            default="stable"),
        var('zope_user',
            'Zope root admin user',
            default='admin'),
        var('zope_password',
            'Zope root admin password'),
        var('http_port',
            'HTTP port',
            default=8080),
        var('debug_mode',
            'Should debug mode be "on" or "off"?',
            default='off'),
        var('verbose_security',
            'Should verbose security be "on" or "off"?',
            default='off'),
        var('silva_layout',
            'Include the new Silva Layout (filesystem based layout), "yes" or "no"?',
            default='yes'),
        ]

    def check_vars(self, vars, cmd):
        result = templates.Template.check_vars(self, vars, cmd)
        if not (vars['silva_distribution'] in ['stable', 'development']):
            raise BadCommand("Unknown silva distribution %s" % vars['silva_distribution'])
        return result

    def post(self, command, output_dir, vars):
        print "-----------------------------------------------------------"
        print "Generation finished"
        print "You probably want to run python bootstrap.py and then edit"
        print "buildout.cfg before running bin/buildout -v"
        print
        print "See README.txt for details"
        print "-----------------------------------------------------------"



