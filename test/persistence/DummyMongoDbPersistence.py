# -*- coding: utf-8 -*-
"""
    pip_services_runtime.persistence.DummyMongoDbPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy mongodb-based persistence implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.persistence import MongoDbPersistence
from pip_services_runtime.config import Category
from pip_services_runtime.config import ComponentDescriptor
from pip_services_runtime.data import FilterParams

DummyMongoDbPersistenceDescriptor = ComponentDescriptor(
    Category.Persistence, "pip-services-dummies", "mongodb", "*"
)

class DummyMongoDbPersistence(MongoDbPersistence):

    def __init__(self):
        super(DummyMongoDbPersistence, self).__init__(DummyMongoDbPersistenceDescriptor, "dummies")

    def get_dummies(self, correlation_id, filter, paging):
        filter = filter if filter != None else FilterParams()
        filter = filter.pick('key')
            
        return self.get_page(correlation_id, filter, paging, None, None)
        
    def get_dummy_by_id(self, correlation_id, dummy_id):
        return self.get_by_id(correlation_id, dummy_id)
        
    def create_dummy(self, correlation_id, dummy):
        return self.create(correlation_id, dummy)

    def update_dummy(self, correlation_id, dummy_id, dummy):
        return self.update(correlation_id, dummy_id, dummy)

    def delete_dummy(self, correlation_id, dummy_id):
        return self.delete(correlation_id, dummy_id)

DummyMongoDbPersistence.Descriptor = DummyMongoDbPersistenceDescriptor