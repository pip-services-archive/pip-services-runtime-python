# -*- coding: utf-8 -*-
"""
    tests.config.test_PagingParams
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.data import PagingParams

class TestPagingParams:

    def test_paging(self):
        paging = PagingParams(123, 234, True)

        assert 123 == paging['skip']
        assert 234 == paging['take']
        assert paging['total']
        
    def test_from_strings(self):
        paging = PagingParams("123", "234", "yes")
        
        assert 123 == paging['skip']
        assert 234 == paging['take']
        assert paging['total']
        
    def test_from_object(self):
        paging = PagingParams.from_value({ 'skip': 123, 'take': 234, 'paging': True })
        
        assert 123 == paging['skip']
        assert 234 == paging['take']
        assert paging['total']
