# -*- coding: utf-8 -*-
"""
    tests.services.test_DummyRestService
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
import requests

from pip_services_runtime import ComponentSet
from pip_services_runtime.config import ComponentConfig
from pip_services_runtime.run import LifeCycleManager
from pip_services_runtime.portability import DynamicMap
from persistence.DummyMemoryPersistence import DummyMemoryPersistence
from logic.DummyController import DummyController
from .DummyRestService import DummyRestService

rest_config = ComponentConfig.from_tuples(
    'endpoint.host', 'localhost',
    'endpoint.port', 3000
)

DUMMY1 = { 'id': None, 'key': 'Key 1', 'content': 'Content 1' }
DUMMY2 = { 'id': None, 'key': 'Key 2', 'content': 'Content 2' }

@pytest.mark.skip(reason='Second execution of REST service (one is in REST client) hands')
class TestDummyRestService:

    db = None
    components = None

    def setup_class(cls):
        cls.db = DummyMemoryPersistence()
        cls.db.configure(ComponentConfig())
        
        cls.ctrl = DummyController()
        cls.ctrl.configure(ComponentConfig())
        
        cls.service = DummyRestService()
        cls.service.configure(rest_config)

        cls.components = ComponentSet.from_components(cls.db, cls.ctrl, cls.service)

        LifeCycleManager.link_and_open(DynamicMap(), cls.components)

    def teardown_class(cls):
        LifeCycleManager.close(cls.components)

    def setup_method(self, method):
        self.db.clear_test_data()
    
    def test_crud_operations(self):
        uri = rest_config.get_endpoint().get_uri()

        # Create one dummy
        r = requests.post(uri + '/dummies', json=DUMMY1)        
        dummy1 = r.json()

        assert dummy1 != None
        assert dummy1['id'] != None
        assert DUMMY1['key'] == dummy1['key']
        assert DUMMY1['content'] == dummy1['content']

        # Create another dummy
        r = requests.post(uri + '/dummies', json=DUMMY2)        
        dummy2 = r.json()

        assert dummy2 != None
        assert dummy2['id'] != None
        assert DUMMY2['key'] == dummy2['key']
        assert DUMMY2['content'] == dummy2['content']

        # Get all dummies
        r = requests.get(uri + '/dummies')        
        dummies = r.json()
        assert dummies != None
        assert 2 == len(dummies['data'])

        # Update the dummy
        r = requests.put(uri + '/dummies/' + dummy1['id'], json={ "content": "Updated Content 1" })
        dummy = r.json()

        assert dummy != None
        assert dummy1['id'] == dummy['id']
        assert dummy1['key'] == dummy['key']
        assert "Updated Content 1" == dummy['content']

        # Delete the dummy
        r = requests.delete(uri + '/dummies/' + dummy1['id'])

        # Try to get deleted dummy
        r = requests.get(uri + '/dummies/' + dummy1['id'])
        assert r.status_code == 404
