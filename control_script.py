from templer.core.control_script import run as templer_run
from templer.core.control_script import usage as templer_usage
from templer.core.control_script import show_help as templer_show_help
from templer.core.control_script import show_version as templer_show_version

SCRIPT_NAME = "zopeskel"

VERSION_PACKAGES = ['ZopeSkel']


def show_version():
    import pdb; pdb.set_trace()
    templer_show_help()

def usage():
    templer_usage()

def show_help():
    templer_show_help()

def run():
    templer_run()