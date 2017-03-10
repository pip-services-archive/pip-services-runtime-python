# -*- coding: utf-8 -*-
"""
    tests.logs.LoggerFixture
    ~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime import LogLevel

class TestClass:
    abc = "ABC"

class LoggerFixture:
    
    _logger = None

    def __init__(self, logger):
        self._logger = logger

    def test_log_level(self):
        assert self._logger.get_level() >= LogLevel.Nothing
        assert self._logger.get_level() <= LogLevel.Trace

    def test_text_output(self):
        self._logger.log(LogLevel.Fatal, "ABC", "123", ["Fatal error..."])
        self._logger.log(LogLevel.Error, "ABC", "123", ["Recoverable error..."])
        self._logger.log(LogLevel.Warn, "ABC", "123", ["Warning..."])
        self._logger.log(LogLevel.Info, "ABC", "123", ["Information message..."])
        self._logger.log(LogLevel.Debug, "ABC", "123", ["Debug message..."])
        self._logger.log(LogLevel.Trace, "ABC", "123", ["Trace message..."])
        
    def test_mixed_output(self):
        obj = TestClass()

        self._logger.log(LogLevel.Fatal, "ABC", "123", [123, "ABC", obj])
        self._logger.log(LogLevel.Error, "ABC", "123", [123, "ABC", obj])
        self._logger.log(LogLevel.Warn, "ABC", "123", [123, "ABC", obj])
        self._logger.log(LogLevel.Info, "ABC", "123", [123, "ABC", obj])
        self._logger.log(LogLevel.Debug, "ABC", "123", [123, "ABC", obj])
        self._logger.log(LogLevel.Trace, "ABC", "123", [123, "ABC", obj])
