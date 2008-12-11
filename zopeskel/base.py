import os
import ConfigParser
from paste.script import pluginlib
from paste.script import templates
from paste.script.command import BadCommand
from paste.script.templates import BasicPackage

var = templates.var

LICENSE_CATEGORIES = {
    'DFSG' : 'License :: DFSG approved',
    'EFS' : 'License :: Eiffel Forum License (EFL)',
    'NPL' : 'License :: Netscape Public License (NPL)',
    'ASL' : 'License :: OSI Approved :: Apache Software License',
    'BSD' : 'License :: OSI Approved :: BSD License',
    'FDL' : 'License :: OSI Approved :: GNU Free Documentation License (FDL)',
    'GPL' : 'License :: OSI Approved :: GNU General Public License (GPL)',
    'LGPL' : 'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'MIT' : 'License :: OSI Approved :: MIT License',
    'MPL' : 'License :: OSI Approved :: Mozilla Public License 1.0 (MPL)',
    'MPL11' : 'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
    'QPL' : 'License :: OSI Approved :: Qt Public License (QPL)',
    'ZPL' : 'License :: OSI Approved :: Zope Public License',
    }

def get_var(vars, name):
    for var in vars:
        if var.name == name:
            return var
    else:
        raise ValueError("No such var: %r" % name)


def update_setup_cfg(path, section, option, value):
    
    parser = ConfigParser.ConfigParser()
    if os.path.exists(path):
        parser.read(path)

    if not parser.has_section(section):
        parser.add_section(section)
        parser.set(section, option, value)
        parser.write(open(path, 'w'))


class BaseTemplate(templates.Template):
    """Base template for all ZopeSkel templates"""

    #a zopeskel template has to set this to True if it wants to use 
    #localcommand
    use_local_commands = False

    #this is just to be able to add ZopeSkel to the list of paster_plugins if
    #the use_local_commands is set to true and to write a zopeskel section in 
    #setup.cfg file containing the name of the parent template. 
    #it will be used by addcontent command to list the apropriate subtemplates 
    #for the generated project. the post method is not a candidate because 
    #many templates override it
    def run(self, command, output_dir, vars):
        
        if self.use_local_commands and 'ZopeSkel' not in self.egg_plugins:
            self.egg_plugins.append('ZopeSkel')

        templates.Template.run(self, command, output_dir, vars)

        setup_cfg = os.path.join(output_dir, 'setup.cfg')
        if self.use_local_commands:
            update_setup_cfg(setup_cfg, 'zopeskel', 'template', self.name)

    def print_subtemplate_notice(self, output_dir=None):
            """Print a notice about local commands begin availabe (if this is
            indeed the case).
    
    
            Unfortunately for us, at this stage in the process, the
            egg_info directory has not yet been created (and won't be
            within the scope of this template running [see
            paste.script.create_distro.py]), so we're cannot show which
            subtemplates are available.
            """
            plugins = pluginlib.resolve_plugins(['ZopeSkel'])
            commands = pluginlib.load_commands_from_plugins(plugins)
            if not commands:
                return
            commands = commands.items()
            commands.sort()
            longest = max([len(n) for n, c in commands])
            print_commands = []
            for name, command in commands:
                name = name + ' ' * (longest - len(name))
                print_commands.append('  %s  %s' % (name,
                                                    command.load().summary))
            print_commands = '\n'.join(print_commands)
            print '-' * 78
            print """\
The project you just created has local commands. These can be used from within
the product.

usage: paster COMMAND

Commands:
%s

For more information: paster help COMMAND""" % print_commands
            print '-' * 78

    def post(self, *args, **kargs):
        if self.use_local_commands:
            self.print_subtemplate_notice()
        templates.Template.post(self, *args, **kargs)

    def _map_boolean(self, responses):
        for var in self.vars:
            if var.name in responses and var.default in [True, False]:
                value = responses[var.name]

                #Get rid of bonus whitespace
                if type(value)==str:
                    value = value.strip()

                #Map special cases to correct values.
                if value in ['t','T','y','Y']: 
                    value = True
                elif value in ['f','F','n','N']:
                    value = False

                responses[var.name]=value
        return responses

    def check_vars(self, vars, cmd):
        responses = super(BaseTemplate, self).check_vars(vars, cmd)

        return self._map_boolean(responses)
