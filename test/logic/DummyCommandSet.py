# -*- coding: utf-8 -*-
"""
    pip_services_runtime.logic.DummyCommandSet
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Command set implementation for dummy business logic
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.commands.CommandSet import CommandSet
from pip_services_runtime.commands.Command import Command
from pip_services_runtime.validation.Schema import Schema
from pip_services_runtime.data.FilterParams import FilterParams
from pip_services_runtime.data.PagingParams import PagingParams

class DummyCommandSet(CommandSet):
    _logic = None

    def __init__(self, logic):
        super(DummyCommandSet, self).__init__()

        # Set reference to the business logic
        self._logic = logic

        # Register commands to the database
        self.add_command(self._make_get_dummies_command())
        self.add_command(self._make_get_dummy_by_id_command())
        self.add_command(self._make_create_dummy_command())
        self.add_command(self._make_update_dummy_command())
        self.add_command(self._make_delete_dummy_command())

    def _make_get_dummies_command(self):
        def execute(correlation_id, args):
            filter = FilterParams.from_value(args.get("filter"))
            paging = PagingParams.from_value(args.get("paging"))
            return self._logic.get_dummies(correlation_id, filter, paging)
        
        return Command(
            self._logic,
            "get_dummies",
            Schema() \
                .with_optional_property("filter", "FilterParams") \
                .with_optional_property("paging", "PagingParams"),
            execute
        )

    def _make_get_dummy_by_id_command(self):
        def execute(correlation_id, args):
            dummy_id = args.get_nullable_string("dummy_id")
            return self._logic.get_dummy_by_id(correlation_id, dummy_id)

        return Command(
            self._logic,
            "get_dummy_by_id",
            Schema() \
                .with_property("dummy_id", "string"),
            execute
        )

    def _make_create_dummy_command(self):
        def execute(correlation_id, args):
            dummy = args.get("dummy")
            return self._logic.create_dummy(correlation_id, dummy)

        return Command(
            self._logic,
            "create_dummy",
            Schema() \
                .with_property("dummy", "Dummy"),
            execute
        )

    def _make_update_dummy_command(self):
        def execute(correlation_id, args):
            dummy_id = args.get_nullable_string("dummy_id")
            dummy = args.get("dummy")
            return self._logic.update_dummy(correlation_id, dummy_id, dummy)

        return Command(
            self._logic,
            "update_dummy",
            Schema() \
                .with_property("dummy_id", "string") \
                .with_property("dummy", "any"),
            execute
        )

    def _make_delete_dummy_command(self):
        def execute(correlation_id, args):
            dummy_id = args.get_nullable_string("dummy_id")
            self._logic.delete_dummy(correlation_id, dummy_id)
            return None

        return Command(
            self._logic,
            "delete_dummy",
            Schema() \
                .with_property("dummy_id", "string"),
            execute
        )
