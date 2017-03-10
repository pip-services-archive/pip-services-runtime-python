# -*- coding: utf-8 -*-
"""
    tests.logs.test_LogCounters
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime import ComponentSet
from pip_services_runtime.config import ComponentConfig
from pip_services_runtime.logs import ConsoleLogger
from pip_services_runtime.counters import LogCounters
from pip_services_runtime.portability import DynamicMap
from .CountersFixture import CountersFixture

class TestLogCounters:

    counters = None
    fixture = None

    def setup_method(self, method):
        log = ConsoleLogger()

        self.counters = LogCounters()
        self.counters.configure(ComponentConfig())
        self.counters.link(DynamicMap(), ComponentSet.from_components(log))
        self.counters.open()

        self.fixture = CountersFixture(self.counters)

    def teardown_method(self, method):
        self.counters.close()

    def test_simple_counters(self):
        self.fixture.test_simple_counters()

    def test_measure_elapsed_time(self):
        self.fixture.test_measure_elapsed_time()
