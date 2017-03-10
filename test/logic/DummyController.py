# -*- coding: utf-8 -*-
"""
    pip_services_runtime.logic.DummyController
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy controller implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.config import Category
from pip_services_runtime.config import ComponentDescriptor
from pip_services_runtime.logic.AbstractController import AbstractController

from .IDummyBusinessLogic import IDummyBusinessLogic
from .DummyCommandSet import DummyCommandSet

DummyControllerDescriptor = ComponentDescriptor( \
    Category.Controllers, "pip-services-dummies", "*", "*" \
)

class DummyController(AbstractController, IDummyBusinessLogic):
    _db = None

    def __init__(self):
        super(DummyController, self).__init__(DummyControllerDescriptor)

    def link(self, context, components):
        # Locate reference to dummy persistence component
        self._db = components.get_one_required( \
            ComponentDescriptor(Category.Persistence, "pip-services-dummies", "*", "*")
        )

        super(DummyController, self).link(context, components)
        
        # Add commands
        commands = DummyCommandSet(self)
        self._add_command_set(commands)

    def get_dummies(self, correlation_id, filter, paging):
        timing = self._instrument(correlation_id, "dummy.get_dummies")
        try:
            return self._db.get_dummies(correlation_id, filter, paging)
        finally:
            timing.end_timing()

    def get_dummy_by_id(self, correlation_id, dummy_id):
        timing = self._instrument(correlation_id, "dummy.get_dummy_by_id")
        try:
            return self._db.get_dummy_by_id(correlation_id, dummy_id)
        finally:
            timing.end_timing()

    def create_dummy(self, correlation_id, dummy):
        timing = self._instrument(correlation_id, "dummy.create_dummy")
        try:
            return self._db.create_dummy(correlation_id, dummy)
        finally:
            timing.end_timing()

    def update_dummy(self, correlation_id, dummy_id, dummy):
        timing = self._instrument(correlation_id, "dummy.update_dummy")
        try:
            return self._db.update_dummy(correlation_id, dummy_id, dummy)
        finally:
            timing.end_timing()

    def delete_dummy(self, correlation_id, dummy_id):
        timing = self._instrument(correlation_id, "dummy.delete_dummy")
        try:
            self._db.delete_dummy(correlation_id, dummy_id)
        finally:
            timing.end_timing()

DummyController.Descriptor = DummyControllerDescriptor