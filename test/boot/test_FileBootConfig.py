# -*- coding: utf-8 -*-
"""
    tests.boot.test_FileBootConfig
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime import ComponentSet
from pip_services_runtime.boot import FileBootConfig
from pip_services_runtime.config import ComponentConfig
from pip_services_runtime.portability import DynamicMap

class TestFileBootConfig:

    config_reader = None

    def setup(self):
        self.config_reader = FileBootConfig()
        config = ComponentConfig.from_tuples(
            "options.path", "./test/boot/options.json"
        )
        self.config_reader.configure(config)
        self.config_reader.link(DynamicMap(), ComponentSet())
        self.config_reader.open()

    def test_read(self):
        config = self.config_reader.read_config()
        options = config.get_raw_content()

        assert options != None
        assert 123 == options.get_integer("test")

        array = options.get_nullable_array("array")
        assert array != None
        assert 111 == int(array[0])
        assert 222 == int(array[1])
        