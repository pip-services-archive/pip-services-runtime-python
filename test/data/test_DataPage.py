# -*- coding: utf-8 -*-
"""
    tests.config.test_DataPage
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.data import DataPage

class TestDataPage:

    def test_from_params(self):
        page = DataPage([], 123)
        
        assert type(page['data']) == list
        assert 123 == page['total']
        
    def test_from_object(self):
        page = DataPage({ 'data': [], 'total': 123})
        
        assert type(page['data']) == list
        assert 123 == page['total']
        