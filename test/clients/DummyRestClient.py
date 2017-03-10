# -*- coding: utf-8 -*-
"""
    pip_services_runtime.clients.DummyRestClient
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy REST client implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.portability import DynamicMap
from pip_services_runtime.clients import RestClient
from pip_services_runtime.config import Category
from pip_services_runtime.config import ComponentDescriptor
from pip_services_runtime.data import FilterParams
from .IDummyClient import IDummyClient

DummyRestClientDescriptor = ComponentDescriptor(
    Category.Clients, "pip-services-dummies", "rest", "1.0"
)

class DummyRestClient(RestClient, IDummyClient):

    def __init__(self):
        super(DummyRestClient, self).__init__(DummyRestClientDescriptor)

    def get_dummies(self, correlation_id, filter, paging):
        params = {}
        params = self.add_filter_params(params, filter)
        params = self.add_paging_params(params, paging)

        return self.call(
            'GET', 
            '/dummies', 
            correlation_id, 
            params
        )
        
    def get_dummy_by_id(self, correlation_id, dummy_id):
        return self.call(
            'GET', 
            '/dummies/' + str(dummy_id), 
            correlation_id
        )
        
    def create_dummy(self, correlation_id, dummy):
        return self.call(
            'POST', 
            '/dummies', 
            correlation_id, 
            None,
            dummy
        )

    def update_dummy(self, correlation_id, dummy_id, dummy):
        return self.call(
            'PUT', 
            '/dummies/' + str(dummy_id), 
            correlation_id, 
            None,
            dummy
        )

    def delete_dummy(self, correlation_id, dummy_id):
        return self.call(
            'DELETE', 
            '/dummies/' + str(dummy_id), 
            correlation_id
        )

DummyRestClient.Descriptor = DummyRestClientDescriptor