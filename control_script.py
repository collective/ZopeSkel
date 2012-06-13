import sys

from templer.core.control_script import Runner
from templer.core.control_script import run as templer_run


class ZopeSkelRunner(Runner):
    """subclass templer runner to override show_version
    """

    def show_version(self):
        """show installed version of packages listed in self.versions

        method must exit by raising error or calling sys.exit
        """
        version_info = self._get_version_info()
        print self._format_version_info(version_info)
        sys.exit(0)


zopeskel_runner = ZopeSkelRunner(name='zopeskel', versions=['ZopeSkel', ])


def run():
    templer_run(zopeskel_runner)
