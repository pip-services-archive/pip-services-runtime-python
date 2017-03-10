# -*- coding: utf-8 -*-
"""
    tests.config.test_ConfigReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
import os.path

from pip_services_runtime.config import ConfigReader

class TestConfigReader:

    def test_read_json(self):
        config = ConfigReader.read('test/config/options.json')
        content = config.get_raw_content()

        assert config != None
        assert 123 == content.get_integer('test')

    def test_read_yaml(self):
        config = ConfigReader.read('test/config/options.yaml')
        content = config.get_raw_content()

        assert config != None
        assert 123 == content.get_integer('test')        