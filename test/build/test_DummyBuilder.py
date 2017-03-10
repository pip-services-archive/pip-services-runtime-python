# -*- coding: utf-8 -*-
"""
    tests.build.test_DummyBuilder
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.config import MicroserviceConfig
from pip_services_runtime.config import ConfigReader
from pip_services_runtime.build import Builder
from .DummyFactory import DummyFactory

build_config = MicroserviceConfig.from_tuples(
    "logs.descriptor.type", "console",
    "counters.descriptor.type", "log",
    "cache.descriptor.type", "memory",
    "persistence.descriptor.type", "file",
    "persistence.options.path", "dummies.json",
    "persistence.options.data", [],
    "controllers.descriptor.type", "*"
    # "services.descriptor.type", "rest",
    # "services.descriptor.version", "1.0",
    # "services.endpoint.port", 3000
)

class TestDummyBuilder:

    def test_build_defaults(self):
        config = MicroserviceConfig()
        components = Builder.build(DummyFactory.Instance, config)
        assert len(components.get_all_ordered()) == 3

    def test_build_with_config(self):
        config = build_config
        components = Builder.build(DummyFactory.Instance, config)
        assert len(components.get_all_ordered()) == 5

    def test_build_with_file(self):
        config = ConfigReader.read('./test/build/config.json')
        components = Builder.build(DummyFactory.Instance, config)
        assert len(components.get_all_ordered()) == 5
