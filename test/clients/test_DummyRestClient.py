# -*- coding: utf-8 -*-
"""
    tests.clients.test_DummyRestClient
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest

from pip_services_runtime import ComponentSet
from pip_services_runtime.config import ComponentConfig
from pip_services_runtime.run import LifeCycleManager
from pip_services_runtime.portability import DynamicMap
from persistence.DummyMemoryPersistence import DummyMemoryPersistence
from logic.DummyController import DummyController
from services.DummyRestService import DummyRestService
from .DummyRestClient import DummyRestClient
from .DummyClientFixture import DummyClientFixture

rest_config = ComponentConfig.from_tuples(
    'endpoint.host', 'localhost',
    'endpoint.port', 3000
)

class TestDummyRestClient:

    db = None
    components = None
    fixture = None

    def setup_class(cls):
        cls.db = DummyMemoryPersistence()
        cls.db.configure(ComponentConfig())
        
        cls.ctrl = DummyController()
        cls.ctrl.configure(ComponentConfig())
        
        cls.service = DummyRestService()
        cls.service.configure(rest_config)

        cls.client = DummyRestClient()
        cls.client.configure(rest_config)

        cls.components = ComponentSet.from_components(cls.db, cls.ctrl, cls.service, cls.client)
        
        cls.fixture = DummyClientFixture(cls.client)

        LifeCycleManager.link_and_open(DynamicMap(), cls.components)

    def teardown_class(cls):
        LifeCycleManager.close(cls.components)

    def setup_method(self, method):
        self.db.clear_test_data()
    
    def test_crud_operations(self):
        self.fixture.test_crud_operations()

