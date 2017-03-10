# -*- coding: utf-8 -*-
"""
    tests.portability.test_Converter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from datetime import *
import iso8601
import pytz

from pip_services_runtime.portability import Converter

class TestClass(object):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

class TestConverter:

    def test_to_string(self):
        assert Converter.to_nullable_string(None) == None
        assert "xyz" == Converter.to_string("xyz")
        assert "123" == Converter.to_string(123)
        assert "True" == Converter.to_string(True)
        #assert "{ prop = xyz }" == Converter.to_string(new { prop = "xyz" }, "xyz"));

        assert "xyz" == Converter.to_string_with_default(None, "xyz")
    
    def test_to_boolean(self):
        assert Converter.to_boolean(True)
        assert Converter.to_boolean(1)
        assert Converter.to_boolean("True")
        assert Converter.to_boolean("yes")
        assert Converter.to_boolean("1")
        assert Converter.to_boolean("Y")

        assert not Converter.to_boolean(False)
        assert not Converter.to_boolean(0)
        assert not Converter.to_boolean("False")
        assert not Converter.to_boolean("no")
        assert not Converter.to_boolean("0")
        assert not Converter.to_boolean("N")

        assert not Converter.to_boolean(123)
        assert Converter.to_boolean_with_default("XYZ", True)
        
    def test_to_integer(self):
        assert 123 == Converter.to_integer(123)
        assert 123 == Converter.to_integer(123.456)
        assert 123 == Converter.to_integer("123")
        assert 123 == Converter.to_integer("123.465")

        assert 123 == Converter.to_integer_with_default(None, 123)
        assert 0 == Converter.to_integer_with_default(False, 123)
        assert 123 == Converter.to_integer_with_default("ABC", 123)
        
    def test_to_float(self):
        assert abs(123 - Converter.to_float(123)) < 0.001
        assert abs(123.456 - Converter.to_float(123.456)) < 0.001
        assert abs(123.456 - Converter.to_float("123.456")) < 0.001

        assert abs(123 - Converter.to_float_with_default(None, 123)) < 0.001
        assert abs(0 - Converter.to_float_with_default(False, 123)) < 0.001
        assert abs(123 - Converter.to_float_with_default("ABC", 123)) < 0.001

    def test_to_date(self):
        assert Converter.to_date(None) == None

        date1 = datetime(1975, 4, 8, 0, 0)
        assert date1 == Converter.to_date_with_default(None, date1)
        assert date1 == Converter.to_date(datetime(1975, 4, 8))
        
        date2 = datetime.fromtimestamp(123456)
        assert date2 == Converter.to_date(123456)
        
        date3 = datetime(1975, 4, 8, 0, 0, 0, 0, pytz.utc)
        assert date3 == Converter.to_date("1975-04-08T00:00:00Z")
        #assert date1 == Converter.to_date("1975/04/08")
        
        assert Converter.to_date("XYZ") == None
        
    def test_to_array(self):
        value = Converter.list_to_array(None)
        assert type(value) == list
        assert len(value) == 0
        
        value = Converter.list_to_array(123)
        assert type(value) == list
        assert len(value) == 1
        assert 123 == value[0] 

        value = Converter.list_to_array([123])
        assert type(value) == list
        assert len(value) == 1
        assert 123 == value[0] 
 
        value = Converter.list_to_array('123')
        assert type(value) == list
        assert len(value) == 1
        assert '123' == value[0] 

        value = Converter.list_to_array(u'123,456')
        assert type(value) == list
        assert len(value) == 2
        assert '123' == value[0] 
        assert '456' == value[1] 
        
    def test_object_to_map(self):
        # Handling nulls
        value = None
        result = Converter.to_nullable_map(value)
        assert result == None
        
        # Handling simple objects
        value = TestClass(123, 234)
        result = Converter.to_nullable_map(value)
        assert 123 == result["value1"]
        assert 234 == result["value2"]

        # Handling dictionaries
        # value = DynamicMap()
        # result = Converter.to_nullable_map(value)
        # assert value == result

        # Non-recursive conversion
        # value = TestClass(123, TestClass(111, 222))
        # result = Converter.to_map(value, None, False)
        # assert result != None
        # assert 123 == result["value1"]
        # assert result["value2"] != None
        # assert not isinstance(result["value2"], dict)
        # assert instanceof(result["value2"], TestClass)

        # Recursive conversion
        value = TestClass(123, TestClass(111, 222))
        result = Converter.to_nullable_map(value)
        assert result != None
        assert 123 == result["value1"]
        assert result["value2"] != None
        assert isinstance(result["value2"], dict)

        # Handling arrays
        value = TestClass([ TestClass(111, 222) ], None)
        result = Converter.to_nullable_map(value)
        assert result != None
        assert type(result["value1"]) == list
        resultElements = result["value1"]
        resultElement0 = resultElements[0]
        assert resultElement0 != None
        assert 111 == resultElement0["value1"]
        assert 222 == resultElement0["value2"]

    def test_json_to_map(self):
        # Handling simple objects
        value = '{ "value1":123, "value2":234 }'
        result = Converter.to_nullable_map(value)
        assert 123 == result["value1"]
        assert 234 == result["value2"]

        # Recursive conversion
        value = '{ "value1":123, "value2": { "value1": 111, "value2": 222 } }'
        result = Converter.to_nullable_map(value)
        assert result != None
        assert 123 == result["value1"]
        assert result["value2"] != None
        assert isinstance(result["value2"], dict)

        # Handling arrays
        value = '{ "value1": [{ "value1": 111, "value2": 222 }] }'
        result = Converter.to_nullable_map(value)
        assert result != None
        assert type(result["value1"]) == list
        resultElements = result["value1"]
        resultElement0 = resultElements[0]
        assert resultElement0 != None
        assert 111 == resultElement0["value1"]
        assert 222 == resultElement0["value2"]
        