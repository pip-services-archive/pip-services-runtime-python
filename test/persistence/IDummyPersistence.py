# -*- coding: utf-8 -*-
"""
    pip_services_runtime.persistence.IDummyPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Interface for dummy persistence implementations
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.IPersistence import IPersistence

class IDummyPersistence(IPersistence):
    def get_dummies(self, correlation_id, filter, paging):
        raise NotImplementedError('Method from interface definition')
        
    def get_dummy_by_id(self, correlation_id, dummy_id):
        raise NotImplementedError('Method from interface definition')
        
    def create_dummy(self, correlation_id, dummy):
        raise NotImplementedError('Method from interface definition')

    def update_dummy(self, correlation_id, dummy_id, dummy):
        raise NotImplementedError('Method from interface definition')

    def delete_dummy(self, correlation_id, dummy_id):
        raise NotImplementedError('Method from interface definition')
