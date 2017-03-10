# -*- coding: utf-8 -*-
"""
    tests.cache.test_MemoryCache
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime import ComponentSet
from pip_services_runtime.config import ComponentConfig
from pip_services_runtime.cache import MemoryCache
from pip_services_runtime.portability import DynamicMap
from .CacheFixture import CacheFixture

class TestMemoryCache:

    cache = None
    fixture = None

    def setup_method(self, method):
        config = ComponentConfig.from_tuples("options.timeout", 500)

        self.cache = MemoryCache()
        self.cache.configure(config)
        self.cache.link(DynamicMap(), ComponentSet())
        self.cache.open()

        self.fixture = CacheFixture(self.cache)

    def teardown_method(self, method):
        self.cache.close()

    def test_basic_operations(self):
        self.fixture.test_basic_operations()

    def test_read_after_timeout(self):
        self.fixture.test_read_after_timeout(1000)
