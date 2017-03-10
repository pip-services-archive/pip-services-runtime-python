# -*- coding: utf-8 -*-
"""
    pip_services_runtime.persistence.DummyMemoryPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy memory-based persistence implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.config import Category
from pip_services_runtime.config import ComponentDescriptor
from .DummyFilePersistence import DummyFilePersistence

DummyMemoryPersistenceDescriptor = ComponentDescriptor(
    Category.Persistence, "pip-services-dummies", "memory", "*"
)

class DummyMemoryPersistence(DummyFilePersistence):

    def __init__(self):
        super(DummyMemoryPersistence, self).__init__(DummyMemoryPersistenceDescriptor)

    def configure(self, config):
        config = config.with_default_tuples("options.path", "")
        super(DummyMemoryPersistence, self).configure(config)

    def save(self):
        pass

DummyMemoryPersistence.Descriptor = DummyMemoryPersistenceDescriptor