# -*- coding: utf-8 -*-
"""
    tests.run.test_LifeCycleManager
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime import ComponentSet
from pip_services_runtime.config import ComponentConfig
from pip_services_runtime.logs import NullLogger
from pip_services_runtime.counters import NullCounters
from pip_services_runtime.run import LifeCycleManager
from pip_services_runtime.portability import DynamicMap

class TestLifeCycleManager:

    components = None
    context = DynamicMap()

    def setup_method(self, method):
        log = NullLogger()
        log.configure(ComponentConfig())

        counters = NullCounters()
        counters.configure(ComponentConfig())

        self.components = ComponentSet.from_components(log, counters)
    
    def test_link(self):
        LifeCycleManager.link(self.context, self.components)

    def test_init_and_open(self):
        LifeCycleManager.link_and_open(self.context, self.components)

    def test_open(self):
        LifeCycleManager.link(self.context, self.components)
        LifeCycleManager.open(self.components)

    def test_close(self):
        LifeCycleManager.link_and_open(self.context, self.components)
        LifeCycleManager.close(self.components)

    def test_force_close(self):
        LifeCycleManager.link_and_open(self.context, self.components)
        LifeCycleManager.force_close(self.components)
