# -*- coding: utf-8 -*-
"""
    tests.validation.test_Schema
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.validation import Schema
from pip_services_runtime.validation import PropertySchema

class TestSchema:

    def test_create_schema(self):
        schema = Schema() \
            .with_property('id', 'string') \
            .with_array('tags', 'string')
            
        assert schema != None
