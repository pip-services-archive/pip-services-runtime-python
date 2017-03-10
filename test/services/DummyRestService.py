# -*- coding: utf-8 -*-
"""
    pip_services_runtime.services.DummyRestService
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy REST service implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.config import Category
from pip_services_runtime.config import ComponentDescriptor
from pip_services_runtime.errors import UnsupportedError
from pip_services_runtime.services.RestService import RestService

DummyRestServiceDescriptor = ComponentDescriptor(
    Category.Services, "pip-services-dummies", "rest", "1.0"
)

class DummyRestService(RestService):
    _logic = None

    def __init__(self):
        super(DummyRestService, self).__init__(DummyRestServiceDescriptor)

    def link(self, context, components):
        # Locate reference to dummy persistence component
        self._logic = components.get_one_prior(
            self,
            ComponentDescriptor(Category.BusinessLogic, "pip-services-dummies", "*", "*")
        )

        super(DummyRestService, self).link(context, components)

    def get_dummies(self):
        correlation_id = self.get_correlation_id()
        filter = self.get_filter_params()
        paging = self.get_paging_params()
        return self.send_result(self._logic.get_dummies(correlation_id, filter, paging))

    def get_dummy_by_id(self, dummy_id):
        correlation_id = self.get_correlation_id()
        return self.send_result(self._logic.get_dummy_by_id(correlation_id, dummy_id))

    def create_dummy(self):
        correlation_id = self.get_correlation_id()
        dummy = self.get_data()
        return self.send_created_result(self._logic.create_dummy(correlation_id, dummy))

    def update_dummy(self, dummy_id):
        correlation_id = self.get_correlation_id()
        dummy = self.get_data()
        print('$$$$', dummy)
        return self.send_result(self._logic.update_dummy(correlation_id, dummy_id, dummy))

    def delete_dummy(self, dummy_id):
        correlation_id = self.get_correlation_id()
        self._logic.delete_dummy(correlation_id, dummy_id)
        return self.send_deleted_result()

    def handled_error(self):
        raise UnsupportedError('NotSupported', 'Test handled error')

    def unhandled_error(self):
        raise TypeError('Test unhandled error')

    def register(self):
        self.register_route('get', '/dummies', self.get_dummies)
        self.register_route('get', '/dummies/<dummy_id>', self.get_dummy_by_id)
        self.register_route('post', '/dummies', self.create_dummy)
        self.register_route('put', '/dummies/<dummy_id>', self.update_dummy)
        self.register_route('delete', '/dummies/<dummy_id>', self.delete_dummy)
        self.register_route('get', '/dummies/handled_error', self.handled_error)
        self.register_route('get', '/dummies/unhandled_error', self.unhandled_error)

DummyRestService.Descriptor = DummyRestServiceDescriptor