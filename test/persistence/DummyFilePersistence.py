# -*- coding: utf-8 -*-
"""
    pip_services_runtime.persistence.DummyFilePersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy file-based persistence implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.persistence import FilePersistence
from pip_services_runtime.config import Category
from pip_services_runtime.config import ComponentDescriptor
from pip_services_runtime.data import FilterParams

DummyFilePersistenceDescriptor = ComponentDescriptor(
    Category.Persistence, "pip-services-dummies", "file", "*"
)

class DummyFilePersistence(FilePersistence):

    def __init__(self, descriptor = None):
        descriptor = descriptor if descriptor != None else DummyFilePersistenceDescriptor
        super(DummyFilePersistence, self).__init__(descriptor)

    def get_dummies(self, correlation_id, filter, paging):
        filter = filter if filter != None else FilterParams()
        key = filter.get_nullable_string("key")

        def filter_dummy(obj):
            if key != None and obj['key'] != key:
                return False
            return True
            
        return self.get_page(correlation_id, filter_dummy, paging, None, None)
        
    def get_dummy_by_id(self, correlation_id, dummy_id):
        return self.get_by_id(correlation_id, dummy_id)
        
    def create_dummy(self, correlation_id, dummy):
        return self.create(correlation_id, dummy)

    def update_dummy(self, correlation_id, dummy_id, dummy):
        return self.update(correlation_id, dummy_id, dummy)

    def delete_dummy(self, correlation_id, dummy_id):
        return self.delete(correlation_id, dummy_id)

DummyFilePersistence.Descriptor = DummyFilePersistenceDescriptor