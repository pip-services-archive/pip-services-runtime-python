# -*- coding: utf-8 -*-
"""
    tests.logs.test_NullLogger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.logs import NullLogger
from .LoggerFixture import LoggerFixture

class TestNullLogger:

    log = None
    fixture = None

    def setup_method(self, method):
        self.log = NullLogger()
        self.fixture = LoggerFixture(self.log)

    def test_log_level(self):
        self.fixture.test_log_level()

    def test_text_output(self):
        self.fixture.test_text_output()

    def test_mixed_output(self):
        self.fixture.test_mixed_output()