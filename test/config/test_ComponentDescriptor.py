# -*- coding: utf-8 -*-
"""
    tests.config.test_ComponentDescriptor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.config import Category
from pip_services_runtime.config import ComponentDescriptor

class TestComponentDescriptor:

    def test_match(self):
        descriptor = ComponentDescriptor(Category.Controllers, "pip-services-dummies", "default", "1.0")

        # Check match by individual fields
        assert descriptor.match(ComponentDescriptor(Category.Controllers, None, None, None))
        assert descriptor.match(ComponentDescriptor(Category.Controllers, "pip-services-dummies", None, None))
        assert descriptor.match(ComponentDescriptor(Category.Controllers, None, "default", None))
        assert descriptor.match(ComponentDescriptor(Category.Controllers, None, None, "1.0"))

        # Check match by individual "*" fields
        assert descriptor.match(ComponentDescriptor(Category.Controllers, "*", "*", "*"))
        assert descriptor.match(ComponentDescriptor(Category.Controllers, "pip-services-dummies", "*", "*"))
        assert descriptor.match(ComponentDescriptor(Category.Controllers, "*", "default", "*"))
        assert descriptor.match(ComponentDescriptor(Category.Controllers, "*", "*", "1.0"))

        # Check match by all values
        assert descriptor.match(ComponentDescriptor(Category.Controllers, "pip-services-dummies", "default", None))
        assert descriptor.match(ComponentDescriptor(Category.Controllers, None, "default", "1.0"))
        assert descriptor.match(ComponentDescriptor(Category.Controllers, "pip-services-dummies", "default", "1.0"))

        # Check match by special BusinessLogic category
        assert descriptor.match(ComponentDescriptor(Category.BusinessLogic, None, None, None))
        
        # Check mismatch by individual fields
        assert not descriptor.match(ComponentDescriptor(Category.Cache, None, None, None))
        assert not descriptor.match(ComponentDescriptor(Category.Controllers, "pip-services-runtime", None, None))
        assert not descriptor.match(ComponentDescriptor(Category.Controllers, None, "special", None))
        assert not descriptor.match(ComponentDescriptor(Category.Controllers, None, None, "2.0"))


    def test_to_string(self):
        descriptor1 = ComponentDescriptor(Category.Controllers, "pip-services-dummies", "default", "1.0")
        assert "controllers:pip-services-dummies:default:1.0" == str(descriptor1)

        descriptor2 = ComponentDescriptor(Category.Controllers, None, None, None)
        assert "controllers:*:*:*" == str(descriptor2)    
