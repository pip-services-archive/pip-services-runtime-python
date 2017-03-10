# -*- coding: utf-8 -*-
"""
    pip_services_runtime.run.DummyProcessRunner
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy process runner implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import traceback

from pip_services_runtime.run import ProcessRunner
from run.DummyMicroservice import DummyMicroservice

class DummyProcessRunner(ProcessRunner):

    def __init__(self):
        super(DummyProcessRunner, self).__init__(DummyMicroservice())

if __name__ == '__main__':
    runner = DummyProcessRunner()
    try:
        runner.run_with_default_config_file("./config/config.yaml")
    except Exception as e:
        print(traceback.format_exc())
        #sys.stderr.write(str(e) + '\n')
