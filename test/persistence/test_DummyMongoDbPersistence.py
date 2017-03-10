# -*- coding: utf-8 -*-
"""
    tests.persistence.test_DummyMongoDbPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime import ComponentSet
from pip_services_runtime.config import Category
from pip_services_runtime.config import ConfigReader
from pip_services_runtime.config import MicroserviceConfig
from pip_services_runtime.config import ComponentConfig
from pip_services_runtime.portability import DynamicMap
from .DummyMongoDbPersistence import DummyMongoDbPersistence
from .DummyPersistenceFixture import DummyPersistenceFixture

config = ConfigReader.read('./config/config.yaml')
db_config = config.get_section(Category.Persistence)

# Skip test if mongodb is not configured
db_config = db_config[0] if len(db_config) == 1 else None
test_enabled = db_config != None and db_config.get_descriptor().get_type() == 'mongodb'

@pytest.mark.skipif(not test_enabled, reason='MongoDB persistence is not configured')
class TestDummyMongoDbPersistence:

    db = None
    fixture = None

    @classmethod
    def setup_class(cls):
        cls.db = DummyMongoDbPersistence()
        cls.fixture = DummyPersistenceFixture(cls.db)

        cls.db.configure(db_config)
        cls.db.link(DynamicMap(), ComponentSet())
        cls.db.open()

    @classmethod
    def teardown_class(cls):
        cls.db.close()

    def setup_method(self, method):
        self.db.clear_test_data()
    
    def test_crud_operations(self):
        self.fixture.test_crud_operations()
