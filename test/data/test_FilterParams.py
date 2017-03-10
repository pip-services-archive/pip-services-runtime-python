# -*- coding: utf-8 -*-
"""
    tests.config.test_FilterParams
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.data import FilterParams

class TestFilterParams:

    def test_object(self):
        filter = FilterParams.from_value({ \
            'ids': [1, 2, 3, 4], \
            'search': 'ABC', \
            'or': { \
                'value1': 123, \
                'value2': 234 \
            } \
        })
        
        assert filter.has('ids')
        assert 1 == filter['ids'][0]
        assert 1 == filter.get('ids')[0]

        assert filter.has('search')
        assert 'ABC' == filter['search']
        assert 'ABC' == filter.get_string('search')
        
        assert filter.has('or.value1')
        assert 123 == filter['or']['value1']
        assert 123 == filter.get_integer('or.value1')

        assert not filter.has('or.value3')
        assert not filter.has('x.value1')
        
    def test_from_other_filter_params(self):
        other_filter = FilterParams.from_value({
            'ids': [1, 2, 3, 4],
            'search': 'ABC',
            'or': {
                'value1': 123,
                'value2': 234
            }
        })
        filter = FilterParams(other_filter)
        
        assert filter.has('ids')
        assert 1 == filter['ids'][0]
        assert 1 == filter.get('ids')[0]

        assert filter.has('search')
        assert 'ABC' == filter['search']
        assert 'ABC' == filter.get_string('search')
        
        assert filter.has('or.value1')
        assert 123 == filter['or']['value1']
        assert 123 == filter.get_integer('or.value1')

        assert not filter.has('or.value3')
        assert not filter.has('x.value1')
        