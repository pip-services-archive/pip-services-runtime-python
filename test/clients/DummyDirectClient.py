# -*- coding: utf-8 -*-
"""
    pip_services_runtime.clients.DummyDirectClient
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy direct client implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.portability import DynamicMap
from pip_services_runtime.clients import DirectClient
from pip_services_runtime.config import Category
from pip_services_runtime.config import ComponentDescriptor
from pip_services_runtime.data import FilterParams
from .IDummyClient import IDummyClient

DummyDirectClientDescriptor = ComponentDescriptor(
    Category.Clients, "pip-services-dummies", "direct", "1.0"
)

class DummyDirectClient(DirectClient, IDummyClient):

    _controller = None

    def __init__(self):
        super(DummyDirectClient, self).__init__(DummyDirectClientDescriptor)

    def link(self, context, components):
        super(DummyDirectClient, self).link(context, components)
        
        self._controller = components.get_one_required(
            ComponentDescriptor(Category.BusinessLogic, "pip-services-dummies", "*", "*")
        )

    def get_dummies(self, correlation_id, filter, paging):
        return self._controller.execute(
            "get_dummies",
            correlation_id,
            DynamicMap.from_tuples(
                "filter", filter,
                "paging", paging
            )
        )
        
    def get_dummy_by_id(self, correlation_id, dummy_id):
        return self._controller.execute(
            "get_dummy_by_id",
            correlation_id,
            DynamicMap.from_tuples(
                "dummy_id", dummy_id
            )
        )
        
    def create_dummy(self, correlation_id, dummy):
        return self._controller.execute(
            "create_dummy",
            correlation_id,
            DynamicMap.from_tuples(
                "dummy", dummy
            )
        )

    def update_dummy(self, correlation_id, dummy_id, dummy):
        return self._controller.execute(
            "update_dummy",
            correlation_id,
            DynamicMap.from_tuples(
                "dummy_id", dummy_id,
                "dummy", dummy
            )
        )

    def delete_dummy(self, correlation_id, dummy_id):
        self._controller.execute(
            "delete_dummy",
            correlation_id,
            DynamicMap.from_tuples(
                "dummy_id", dummy_id
            )
        )

DummyDirectClient.Descriptor = DummyDirectClientDescriptor