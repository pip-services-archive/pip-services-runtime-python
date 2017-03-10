# -*- coding: utf-8 -*-
"""
    tests.config.test_CommandSet
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.portability import DynamicMap
from pip_services_runtime.commands import Command
from pip_services_runtime.commands import CommandSet

class TestCommandSet:

    def get_value(self, correlation_id, args):
        return args.get('value')

    def make_echo_command(self, name):
        return Command(None, name, None, self.get_value)

    def test_commands(self):
        commands = CommandSet()
        commands.add_command(self.make_echo_command("command1"))
        commands.add_command(self.make_echo_command("command2"))
        
        result = commands.execute("command1", None, DynamicMap.from_tuples("value", 123))
        assert 123 == result
        
        result = commands.execute("command1", None, DynamicMap.from_tuples("value", "ABC"))
        assert "ABC" == result
        
        result = commands.execute("command2", None, DynamicMap.from_tuples("value", 789))
        assert 789 == result

    # def test_intercepters(self):
    #     log = NullLogger()
    #     log.configure(ComponentConfig())
        
    #     loggers = [log]
        
    #     counters = NullCounters()
    #     counters.configure(ComponentConfig())
        
    #     commands = CommandSet()
    #     commands.add_intercepter(TracingIntercepter(loggers, "Testing"));
    #     commands.add_intercepter(TimingIntercepter(counters, "test_time"))
    #     commands.add_command(self.make_echo_command("command1"))
    #     commands.add_command(self.make_echo_command("command2"))
        
    #     result = commands.execute("command1", None, DynamicMap.from_tuples("value", 123))
    #     assert 123 == result
        
    #     result = commands.execute("command1", None, DynamicMap.from_tuples("value", "ABC"))
    #     assert "ABC" == result
        
    #     result = commands.execute("command2", None, DynamicMap.from_tuples("value", 789))
    #     assert 789 == result
        