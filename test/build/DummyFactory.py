# -*- coding: utf-8 -*-
"""
    pip_services_runtime.build.DummyFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy component factory implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pip_services_runtime.build import ComponentFactory
from pip_services_runtime.build import DefaultFactory
from persistence.DummyFilePersistence import DummyFilePersistence
from persistence.DummyMemoryPersistence import DummyMemoryPersistence
from persistence.DummyMongoDbPersistence import DummyMongoDbPersistence
from logic.DummyController import DummyController
from clients.DummyDirectClient import DummyDirectClient
from clients.DummyRestClient import DummyRestClient
from services.DummyRestService import DummyRestService

class DummyFactory(ComponentFactory):
    
    def __init__(self):
        super(DummyFactory, self).__init__(DefaultFactory.Instance)

        self.register(DummyFilePersistence.Descriptor, DummyFilePersistence)
        self.register(DummyMemoryPersistence.Descriptor, DummyMemoryPersistence)
        self.register(DummyMongoDbPersistence.Descriptor, DummyMongoDbPersistence)
        self.register(DummyController.Descriptor, DummyController)
        self.register(DummyDirectClient.Descriptor, DummyDirectClient)
        self.register(DummyRestClient.Descriptor, DummyRestClient)
        self.register(DummyRestService.Descriptor, DummyRestService)
        
DummyFactory.Instance = DummyFactory()
