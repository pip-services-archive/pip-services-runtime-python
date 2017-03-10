# -*- coding: utf-8 -*-
"""
    tests.logs.test_NullCounters
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime import ComponentSet
from pip_services_runtime.config import ComponentConfig
from pip_services_runtime.logs import ConsoleLogger
from pip_services_runtime.counters import NullCounters
from pip_services_runtime.portability import DynamicMap

class TestNullCounters:

    counters = None

    def setup_method(self, method):
        log = ConsoleLogger()

        self.counters = NullCounters()
        self.counters.configure(ComponentConfig())
        self.counters.link(DynamicMap(), ComponentSet.from_components(log))
        self.counters.open()

    def teardown_method(self, method):
        self.counters.close()

    def test_simple_counters(self):
        self.counters.last("Test.LastValue", 123)
        self.counters.increment("Test.Increment", 3)
        self.counters.stats("Test.Statistics", 123)

    def test_measure_elapsed_time(self):
        timer = self.counters.begin_timing("Test.Elapsed")
        timer.end_timing()
