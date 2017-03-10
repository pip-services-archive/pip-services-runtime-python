# -*- coding: utf-8 -*-
"""
    tests.config.test_IdGenerator
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_runtime.data import IdGenerator

class TestIdGenerator:

    def test_short(self):
        id1 = IdGenerator.short()
        assert id1 != None
        assert len(id1) >= 9

        id2 = IdGenerator.short()
        assert id2 != None
        assert len(id2) >= 9
        assert id1 != id2

    def test_uuid(self):
        id1 = IdGenerator.uuid()
        assert id1 != None
        assert len(id1) == 32

        id2 = IdGenerator.uuid()
        assert id2 != None
        assert len(id2) == 32
        assert id1 != id2
        