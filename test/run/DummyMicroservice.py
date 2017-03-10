# -*- coding: utf-8 -*-
"""
    pip_services_runtime.run.DummyMicroservice
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy microservice container implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pip_services_runtime.run import Microservice
from build.DummyFactory import DummyFactory

class DummyMicroservice(Microservice):

    def __init__(self):
        super(DummyMicroservice, self).__init__("pip-services-dummies", DummyFactory.Instance)
