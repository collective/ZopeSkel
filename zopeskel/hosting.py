import errno
import os
import socket
import subprocess
import sys
import copy

from paste.script import templates
from zopeskel.base import BadCommand
from zopeskel.base import BaseTemplate, EASY, EXPERT
from zopeskel.vars import var, IntVar, BooleanVar, StringVar
from zopeskel import abstract_buildout

plone25s = {
        "2.5.5": "https://launchpad.net/plone/2.5/2.5.5/+download/Plone-2.5.5.tar.gz",
        "2.5.4": "https://launchpad.net/plone/2.5/2.5.4/+download/Plone-2.5.4-2.tar.gz",
        "2.5.3": "https://launchpad.net/plone/2.5/2.5.3/+download/Plone-2.5.3-final.tar.gz",
        "2.5.2": "http://plone.googlecode.com/files/Plone-2.5.2-1.tar.gz",
        "2.5.1": "http://heanet.dl.sourceforge.net/sourceforge/plone/Plone-2.5.1-final.tar.gz",
        "2.5"  : "http://heanet.dl.sourceforge.net/sourceforge/plone/Plone-2.5.tar.gz",
        }

class StandardHosting(abstract_buildout.AbstractBuildout):
    _template_dir = "templates/plone_hosting"
    use_cheetah = True
    summary = "Plone hosting: buildout with ZEO and Plone versions below 3.2"
    required_templates = []
    help = """
This template helps you to create an entire zope hosting setup, including
ZEO and a single Zope client instance.  If you desire, it can also install
and set up the Varnish Caching/Proxy Server.    

Please Note:
Due to changes in the packaging of Plone, this template is not suitable
for versions of Plone beyond 3.1.7.  If you are trying to use a later 
version of plone, you will need to edit the buildout resulting from this
template in order to have it work correctly.  Information related to these
issues may be found here:

http://plone.org/documentation/kb/repair-a-plone-3.1-buildout

and here:

http://plone.org/products/zopeskel/issues/25
"""

    vars = copy.deepcopy(abstract_buildout.AbstractBuildout.vars);
    vars = [

        abstract_buildout.VAR_ZOPE_USER,
        abstract_buildout.VAR_ZOPE_PASSWD, 

        IntVar(
            "base_port", 
            title="Base Port #",
            description="# to use as base for Zope/ZEO/proxy ports",
            modes=(EASY, EXPERT),
            page="Main",
            default=8000,
            help="""
For standardization, rather than selecting ports for Zope, ZEO, and
a proxy individually, these are tied together numerically.

ZEO port = Base + 0 | Proxy port = Base + 1 | HTTP port = Base + 10

If the ports specified by any of these numbers are already in use or
otherwise unavailable, this template will inform you of the problem and
exit with an error.  If this happens, please try another number for
'Base Port #'
""",
            ),
            
        BooleanVar(
            "proxy",
            title="Install proxy server?",
            description="Should a proxy server be installed?",
            default=False,
            help=""" 
If you ask for a proxy server to be installed, this template will include
the Varnish Caching/Proxy server.  If you wish to use a different proxy
server, please answer False and install your own.  
""",
            ),

        StringVar(
            "plone",
            title="Plone Version",
            description="Version to install (2.5, 2.5.1, 3.0, 3.0.1, etc)",
            default="3.1.7",
            help="""
You can use this template to install any version of Plone from 2.5 on. 
Versions of Plone more recent than 3.1.7 will require some editing of the
generated configuration files.  Please see the long description of this
template (run 'zopskel --list') for more details.  In general it is 
advisable to use the most recent version of Plone.  You can find a list of 
stable Plone releases at 

http://plone.org/products/plone/releases/

""",
            ),

        BooleanVar(
            "buildout",
            title="Run Buildout?",
            description="Should bin/buildout command be executed?",
            default=True,
            help="""
Would you like this template to automatically run the buildut command as soon
as it finishes creating the required files?  Please note that if you've chosen
to build a version of Plone more recent than 3.1.7 running buildout will fail
unless you make changes to the generated configuration files.  Please see the
long description of this package (run 'zopeskel --list') for more details.

If you intend on adding any specific third-party products or modifying the
buildout in any way, you should answer 'False'.  Then make your modifications
and run `python bootstrap.py` followed by `bin/buildout`.
""",
            ),

            ]

    def _buildout(self, output_dir):
        olddir=os.getcwd()
        try:
            os.chdir(output_dir)
            print "Bootstrapping the buildout"
            subprocess.call([sys.executable, "bootstrap.py"])
            print "Configuring the buildout"
            subprocess.call(["bin/buildout", "-n"])
        finally:
            os.chdir(olddir)

    def _checkPortAvailable(self, port):
        s=socket.socket()
        try:
            s.connect(("127.0.0.1", port))
        except socket.error, e:
            s.close()

            if e.args[0]==errno.ECONNREFUSED:
                return 

            raise BadCommand("Error checking port availability: %s" % e.args[1])

        s.close()
        raise BadCommand("Port %s is already in use" % port)


    def check_vars(self, vars, cmd):
        result=super(StandardHosting, self).check_vars(vars, cmd)

        base_port=result["base_port"]
        result["zeo_port"]=base_port
        result["proxy_port"]=base_port+1
        result["http_port"]=base_port+10

        self._checkPortAvailable(result["zeo_port"])
        self._checkPortAvailable(result["http_port"])
        if result["proxy"]:
            self._checkPortAvailable(result["proxy_port"])

        if vars["plone"] not in plone25s and not vars["plone"].startswith("3."):
            raise BadCommand("Unknown plone version: %s" % vars["plone"])

        return result

    def pre(self, command, output_dir, vars):
        vars["output_dir"]=os.path.abspath(output_dir)
        plone=vars["plone"]
        if plone.startswith("3."):
            vars["plone_recipe"]="plone.recipe.plone"
            vars["plone_recipe_version"]=plone
        else:
            vars["plone_recipe"]="plone.recipe.plone25install"
            vars["plone_url"]=plone25s[plone]
        super(StandardHosting, self).pre(command, output_dir, vars)

    def show_summary(self, vars):
        print
        print "Finished creation of standard hosting buildout."
        print
        print "Configuration summary:"
        print "  Plone     : %s" % vars["plone"]
        print
        print "  HTTP port : %s" % vars["http_port"]
        print "  ZEO port  : %s" % vars["zeo_port"]
        if vars["proxy"]:
            print "  Proxy port: %s" % vars["proxy_port"]
        else:
            print "  Proxy port: disabled"
        print
        print "  Zope admin user    :  %s" % vars["zope_user"]
        print "  Zope admin password:  %s" % vars["zope_password"]


    def post(self, command, output_dir, vars):
        output_dir=vars["output_dir"]
        if vars["buildout"]:
            self._buildout(output_dir)
        if not vars.get("hide_summary", False):
            self.show_summary(vars)
        super(StandardHosting, self).post(command, output_dir, vars)
