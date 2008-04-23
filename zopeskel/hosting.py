import errno
import os
import socket
import subprocess
import sys

from zopeskel.base import templates
from zopeskel.base import BaseTemplate
from zopeskel.base import BadCommand
from zopeskel.base import var

plone25s = {
        "2.5.5": "https://launchpad.net/plone/2.5/2.5.5/+download/Plone-2.5.5.tar.gz",
        "2.5.4": "https://launchpad.net/plone/2.5/2.5.4/+download/Plone-2.5.4-2.tar.gz",
        "2.5.3": "https://launchpad.net/plone/2.5/2.5.3/+download/Plone-2.5.3-final.tar.gz",
        "2.5.2": "http://plone.googlecode.com/files/Plone-2.5.2-1.tar.gz",
        "2.5.1": "http://heanet.dl.sourceforge.net/sourceforge/plone/Plone-2.5.1-final.tar.gz",
        "2.5"  : "http://heanet.dl.sourceforge.net/sourceforge/plone/Plone-2.5.tar.gz",
        }

class StandardHosting(BaseTemplate):
    _template_dir = "templates/plone_hosting"
    use_cheetah = True
    summary = "Plone hosting: buildout with ZEO and any Plone version"
    required_templates = []

    vars = [
            var("zope_password", "Initial Zope admin password", default="admin"),
            var("base_port", "Base port number", default=8000),
            var("proxy", "Install a proxy server", default="no"),
            var("plone", "Plone version (2.5, 2.5.1, 3.0, 3.0.1, etc.)",
                default="3.1"),
            var("buildout", "Run buildout", default="yes"),
            ]

    def _buildout(self, output_dir):
        os.chdir(output_dir)
        print "Bootstrapping the buildout"
        subprocess.call([sys.executable, "bootstrap.py"])
        print "Configuring the buildout"
        subprocess.call(["bin/buildout", "-n"])


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
        result=templates.Template.check_vars(self, vars, cmd)

        try:
            base_port=int(vars["base_port"])
        except ValueError:
            raise BadCommand("Illegal base port number: %s" % vars["base_port"])

        result["zeo_port"]=base_port
        result["proxy_port"]=base_port+1
        result["http_port"]=base_port+2
        result["proxy"]=vars["proxy"].lower() in [ "yes", "true", "on" ]
        result["buildout"]=vars["buildout"].lower() in [ "yes", "true", "on" ]

        self._checkPortAvailable(result["zeo_port"])
        self._checkPortAvailable(result["http_port"])
        if result["proxy"]:
            self._checkPortAvailable(result["proxy_port"])

        if vars["plone"] not in plone25s and not vars["plone"].startswith("3."):
            raise BadCommand("Unknown plone version: %s" % vars["plone"])

        return result

    def pre(self, command, output_dir, vars):
        plone=vars["plone"]
        if plone.startswith("3."):
            vars["plone_recipe"]="plone.recipe.plone"
            vars["plone_recipe_version"]=plone
        else:
            vars["plone_recipe"]="plone.recipe.plone25install"
            vars["plone_url"]=plone25s[plone]

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
        print "  Zope admin user    :  admin"
        print "  Zope admin password:  %s" % vars["zope_password"]


    def post(self, command, output_dir, vars):
        output_dir=os.path.abspath(output_dir)
        os.chmod(os.path.join(output_dir, "bin", "control"), 0755)
        if vars["buildout"]:
            self._buildout(output_dir)
        self.show_summary(vars)

