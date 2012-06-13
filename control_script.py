from templer.core.control_script import Runner
from templer.core.control_script import run as templer_run


zopeskel_runner = Runner(name='zopeskel', versions=['ZopeSkel', ])


def run():
    templer_run(zopeskel_runner)
