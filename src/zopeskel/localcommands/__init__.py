"""
 ZopeSkel local command/template. Most of the code is a copy/paste from
 paste.script module
"""

import os
import subprocess
import ConfigParser
import pkg_resources
from paste.script import command, pluginlib
from paste.script import templates
from paste.script import copydir


class ZopeSkelLocalCommand(command.Command):
    """paster command to add content skeleton to plone project"""

    max_args = 2
    usage = "[template name]"
    summary = "Adds plone content types to your project"
    group_name = "ZopeSkel local commands"

    parser = command.Command.standard_parser(verbose=True)
    parser.add_option('-l', '--list',
                      action='store_true',
                      dest='listcontents',
                      help="List available templates for the current project")

    parser.add_option('-a', '--list-all',
                      action='store_true',
                      dest='listallcontents',
                      help="List all templates regardless of the current project")

    parser.add_option('-q', '--no-interactive',
                      action="count",
                      dest="no_interactive",
                      default=0)    

    template_vars = {}
    
    def command(self):
        """
        command method
        """
        self.interactive = 1
        options, args = self.options, self.args
        
        if options.listcontents:
            self._list_sub_templates()
            return

        if options.listallcontents:
            self._list_sub_templates(show_all=True)
            return

        if options.no_interactive:
            self.interactive = False

        if len(args) < 1:
            print "\n\tError: Need a template name\n"
            return

        (self.template_vars['namespace_package'],
         self.template_vars['namespace_package2'],
         self.template_vars['package']) = self.get_parent_namespace_packages()
        
        dest_dir = self.dest_dir()
        
        templates = []
        self._extend_templates(templates, args[0])

        templates = [tmpl for name, tmpl in templates]
        for tmpl in templates[::-1]:
            self.template_vars = tmpl.check_vars(self.template_vars, self)

        for tmpl in templates[::-1]:
            if self.verbose:
                print 'Creating template %s' % tmpl.name
            tmpl.run(self, dest_dir, self.template_vars)
        
    
    def dest_dir(self):
        dest_dir = os.path.join(
                   os.path.dirname(
                       pluginlib.find_egg_info_dir(os.getcwd())),
                                   self.template_vars['namespace_package'],
                                   self.template_vars['namespace_package2'],
                                   self.template_vars['package'])
        return dest_dir
    
    def get_parent_namespace_packages(self):
        """
        return the project namespaces and package name.
        This method can be a function
        """
        egg_info = pluginlib.find_egg_info_dir(os.getcwd())

        hfile = open(os.path.join(egg_info, 'namespace_packages.txt'))
        packages = [l.strip() for l in hfile.readlines()
                    if l.strip() and not l.strip().startswith('#')]
        hfile.close()

        packages.sort(lambda x, y: -cmp(len(x), len(y)))
        packages = packages[0].split('.')

        namespace_package = packages[0]
        namespace_package2 = ''
        if len(packages) == 2:
            namespace_package2 = packages[1]
        ( dirpath, dirnames, filenames) = os.walk(os.path.join(
                                            os.path.dirname(egg_info),
                                                    namespace_package,
                                                    namespace_package2)).next()
        # Get the package dir because we usually want to issue the 
        # localcommand in the package dir. 
        package = os.path.basename(os.path.abspath(os.path.curdir))

        # If the package dir is not in the list of inner_packages,
        # then:
        #    if there is only one package in the list, we take it
        #    else ask the user to pick a package from the list
        inner_packages = [d for d in dirnames if d != '.svn']
        if package not in inner_packages:
            package = inner_packages[0]
            if len(inner_packages) > 1:
                package = self.challenge('Please choose one package to inject content into %s' % inner_packages)

        return namespace_package, namespace_package2, package

    def _list_sub_templates(self, show_all=False):
        """
        lists available templates
        """
        templates = []
        parent_template = None

        egg_info_dir = pluginlib.find_egg_info_dir(os.getcwd())
        setup_cfg = os.path.join(os.path.dirname(egg_info_dir), 'setup.cfg')

        parent_template = None
        if os.path.exists(setup_cfg):
            parser = ConfigParser.ConfigParser()
            parser.read(setup_cfg)
            try:
                parent_template = parser.get('zopeskel', 'template') or None
            except:
                pass

        for entry in self._all_entry_points():
            try:
                entry_point = entry.load()
                t = entry_point(entry.name)
                if show_all or \
                   parent_template is None or \
                   parent_template in t.parent_templates:
                    templates.append(t)
            except Exception, e:
                # We will not be stopped!
                print 'Warning: could not load entry point %s (%s: %s)' % (
                    entry.name, e.__class__.__name__, e)

        print 'Available templates:'
        if not templates:
            print '  No template'
            return

        max_name = max([len(t.name) for t in templates])
        templates.sort(lambda a, b: cmp(a.name, b.name))
 
        for template in templates:
            _marker = " "
            if not template.parent_templates:
                _marker = '?'
            elif parent_template not in template.parent_templates:
                _marker = 'N'

            # @@: Wrap description
            print '  %s %s:%s  %s' % (
                _marker,
                template.name,
                ' '*(max_name-len(template.name)),
                template.summary)

    def _all_entry_points(self):
        """
        Return all entry points under zopeskel_sub_templates
        """
        if not hasattr(self, '_entry_points'):
            self._entry_points = list(pkg_resources.iter_entry_points(
            'zopeskel.zopeskel_sub_template'))
        return self._entry_points

    def _extend_templates(self, templates, tmpl_name):
        """
        Return ...
        """
        if '#' in tmpl_name:
            dist_name, tmpl_name = tmpl_name.split('#', 1)
        else:
            dist_name, tmpl_name = None, tmpl_name
        if dist_name is None:
            for entry in self._all_entry_points():
                if entry.name == tmpl_name:
                    tmpl = entry.load()(entry.name)
                    dist_name = entry.dist.project_name
                    break
            else:
                raise LookupError(
                    'Template by name %r not found' % tmpl_name)
        else:
            dist = pkg_resources.get_distribution(dist_name)
            entry = dist.get_entry_info(
                'paste.paster_create_template', tmpl_name)
            tmpl = entry.load()(entry.name)
        full_name = '%s#%s' % (dist_name, tmpl_name)
        for item_full_name, in templates:
            if item_full_name == full_name:
                # Already loaded
                return
        for req_name in tmpl.required_templates:
            self._extend_templates(templates, req_name)
        templates.append((full_name, tmpl))


class ZopeSkelLocalTemplate(templates.Template):
    """
    Base template class
    """

    marker_name = "extra stuff goes here"
    #list of templates this subtemplate is related to
    parent_templates = []

    def run(self, command, output_dir, vars):
        """
        the run method
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

        self.pre(command, output_dir, vars)
        self.write_files(command, output_dir, vars)
        self.post(command, output_dir, vars)

    def write_files(self, command, output_dir, vars):
        """
        method
        """
        self._command = command
        template_dir = self.template_dir()
        if not os.path.exists(output_dir):
            print "Creating directory %s" % output_dir
            if not command.simulate:
                # Don't let copydir create this top-level directory,
                # since copydir will svn add it sometimes:
                os.makedirs(output_dir)
        self.copy_dir(template_dir, output_dir,
                         vars,
                         verbosity=1,
                         simulate=0,
                         interactive=1,
                         overwrite=0,
                         indent=1,
                         use_cheetah=self.use_cheetah,
                         template_renderer=self.template_renderer)

    def copy_dir(self, source, dest, vars, verbosity, simulate, indent=0,
                 use_cheetah=False, sub_vars=True, interactive=False,
                 svn_add=True, overwrite=True, template_renderer=None):
        """
        This method is a modified copie of paste.script.copy_dir
        """
        # This allows you to use a leading +dot+ in filenames which would
        # otherwise be skipped because leading dots make the file hidden:
        vars.setdefault('dot', '.')
        vars.setdefault('plus', '+')
        names = os.listdir(source)
        names.sort()
        pad = ' '*(indent*2)
        if not os.path.exists(dest):
            if verbosity >= 1:
                print '%sCreating %s/' % (pad, dest)
            if not simulate:
                copydir.svn_makedirs(dest, svn_add=svn_add, verbosity=verbosity,
                             pad=pad)
        elif verbosity >= 2:
            print '%sDirectory %s exists' % (pad, dest)
        for name in names:
            full = os.path.join(source, name)
            reason = copydir.should_skip_file(name)
            if reason:
                if verbosity >= 2:
                    reason = pad + reason % {'filename': full}
                    print reason
                continue

            if sub_vars:
                dest_full = os.path.join(
                                  dest, copydir.substitute_filename(name, vars))
            sub_file = False
            if dest_full.endswith('_tmpl'):
                dest_full = dest_full[:-5]
                sub_file = sub_vars
            if os.path.isdir(full):
                if verbosity:
                    print '%sRecursing into %s' % (pad, os.path.basename(full))
                self.copy_dir(full, dest_full, vars, verbosity, simulate,
                         indent=indent+1, use_cheetah=use_cheetah,
                         sub_vars=sub_vars, interactive=interactive,
                         svn_add=svn_add, template_renderer=template_renderer)
                continue
            f = open(full, 'rb')
            content = f.read()
            f.close()
            try:
                content = copydir.substitute_content(
                                            content,
                                            vars, filename=full,
                                            use_cheetah=use_cheetah,
                                            template_renderer=template_renderer)
            except copydir.SkipTemplate:
                continue

            if dest_full.endswith('_insert'):
                dest_full = dest_full[:-7]

            already_exists = os.path.exists(dest_full)
            if already_exists:
                if sub_file and verbosity:
                    print "File '%s' already exists: skipped" % \
                           os.path.basename(dest_full)
                    continue
                f = open(dest_full, 'rb')
                old_content = f.read()
                f.close()
                if old_content == content:
                    if verbosity:
                        print '%s%s already exists (same content)' % \
                               (pad, dest_full)
                    continue

                if verbosity:
                    print "%sInserting from %s into %s" % \
                                (pad, os.path.basename(full), dest_full)

                if not content.endswith('\n'):
                    content += '\n'
                # remove lines starting with '#'
                content = '\n'.join([l for l in content.split('\n') \
                                     if not l.startswith('#')])
                self._command.insert_into_file(dest_full,
                                               self.marker_name,
                                               content)
                continue

            if verbosity:
                print '%sCopying %s to %s' % (pad,
                                              os.path.basename(full),
                                              dest_full)
            # remove '#' from the start of lines
            if not sub_file:
                content = content.replace('\n#','\n')
                if content[0] == '#': content = content[1:]

            if not simulate:
                f = open(dest_full, 'wb')
                f.write(content)
                f.close()
            if svn_add and not already_exists:
                if not os.path.exists(
                           os.path.join(
                               os.path.dirname(
                                   os.path.abspath(dest_full)), '.svn')):
                    if verbosity > 1:
                        print '%s.svn/ does not exist; cannot add file' % pad
                else:
                    cmd = ['svn', 'add', dest_full]
                    if verbosity > 1:
                        print '%sRunning: %s' % (pad, ' '.join(cmd))
                    if not simulate:
                        # @@: Should
                        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                        stdout, stderr = proc.communicate()
                        if verbosity > 1 and stdout:
                            print 'Script output:'
                            print stdout
            elif svn_add and already_exists and verbosity > 1:
                print '%sFile already exists (not doing svn add)' % pad
