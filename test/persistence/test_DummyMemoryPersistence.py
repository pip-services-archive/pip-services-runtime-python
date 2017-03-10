# -*- coding: utf-8 -*-
"""
    tests.persistence.test_DummyFilePersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime import ComponentSet
from pip_services_runtime.config import ComponentConfig
from pip_services_runtime.portability import DynamicMap
from .DummyMemoryPersistence import DummyMemoryPersistence
from .DummyPersistenceFixture import DummyPersistenceFixture

class TestDummyMemoryPersistence:

    config = ComponentConfig.from_tuples(
        "type", "memory",
    )

    db = None
    fixture = None

    @classmethod
    def setup_class(cls):
        cls.db = DummyMemoryPersistence()
        cls.fixture = DummyPersistenceFixture(cls.db)

        cls.db.configure(cls.config)
        cls.db.link(DynamicMap(), ComponentSet())
        cls.db.open()

    @classmethod
    def teardown_class(cls):
        cls.db.close()

    def setup_method(self, method):
        self.db.clear_test_data()
    
    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_load_data(self):
        self.db.load()
