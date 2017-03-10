# -*- coding: utf-8 -*-
"""
    tests.errors.test_MicroserviceError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.errors import MicroserviceError

class TestMicroserviceError:

    def test_create_error(self):
        error = MicroserviceError('Undefined', 'TestComponent', 'TestError', 'Test error')
            
        assert 'TestComponent' == error.component
        assert 'TestError' == error.code
        assert 'Test error' == error.message
        
        error = MicroserviceError().for_component('TestComponent')
        
        assert 'Undefined' == error.code
        assert 'Unknown error' == error.message