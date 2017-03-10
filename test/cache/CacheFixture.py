# -*- coding: utf-8 -*-
"""
    tests.cache.CacheFixture
    ~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import time

class CacheFixture:
    
    _cache = None

    def __init__(self, cache):
        self._cache = cache

    def test_basic_operations(self):
        # Set the first value
        value = self._cache.store("test", 123)
        assert 123 == value
        
        value = self._cache.retrieve("test")
        assert 123 == value

        # Set null value
        value = self._cache.store("test", None)
        assert value == None

        value = self._cache.retrieve("test")
        assert value == None
        
        # Set the second value
        value = self._cache.store("test", "ABC")
        assert "ABC" == value
        
        value = self._cache.retrieve("test")
        assert "ABC" == value

        # Unset value
        self._cache.remove("test")

        value = self._cache.retrieve("test")
        assert value == None

    def test_read_after_timeout(self, timeout):
        # Set value
        value = self._cache.store("test", 123)
        assert 123 == value
        
        # Read the value
        value = self._cache.retrieve("test")
        assert 123 == value
        
        # Wait
        time.sleep(timeout / 1000)
        
        # Read the value again
        value = self._cache.retrieve("test")
        assert value == None
