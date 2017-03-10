# -*- coding: utf-8 -*-
"""
    tests.portability.test_DynamicMap
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_runtime.portability import DynamicMap

class TestClass(object):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

class TestDynamicMap:

    def test_merge(self):
        result = DynamicMap.from_tuples( \
            "value1", 123, \
            "value2", 234 \
        )
        defaults = DynamicMap.from_tuples( \
            "value2", 432, \
            "value3", 345 \
        )
        result = result.merge(defaults, False)
        assert 3 == len(result)
        assert 123 == result.get("value1")
        assert 234 == result.get("value2")
        assert 345 == result.get("value3")

    def test_merge_recursive(self):
        result = DynamicMap.from_value(
            '{ "value1": 123, "value2": { "value21": 111, "value22": 222 } }'
        )
        defaults = DynamicMap.from_value(
            '{ "value2": { "value22": 777, "value23": 333 }, "value3": 345 }'
        )
        result = result.merge(defaults, True)

        assert 3 == len(result)
        assert 123 == result.get("value1")
        assert 345 == result.get("value3")

        deep_result = result.get_map("value2")
        assert 3 == len(deep_result)
        assert 111 == deep_result.get("value21")
        assert 222 == deep_result.get("value22")
        assert 333 == deep_result.get("value23")

    def test_merge_with_nulls(self):
        result = DynamicMap.from_value(
            '{ "value1": 123, "value2": 234 }'
        )
        result = result.merge(None, True)

        assert 2 == len(result)
        assert 123 == result.get("value1")
        assert 234 == result.get("value2")

    def test_assign(self):
        value = TestClass(None, None)
        new_values = DynamicMap.from_value(
            '{ "value1": 123, "value2": "ABC", "value3": 456 }'
        )
        
        new_values.assign_to(value)
        assert value.value1 != None
        assert 123 == value.value1
        assert value.value2 != None
        assert "ABC" == value.value2

    def test_get(self):
        config = DynamicMap.from_value(
            '{ "value1": 123, "value2": { "value21": 111, "value22": 222 } }'
        )

        value = config.get("")
        assert value == None

        value = config.get("value1")
        assert value != None
        assert 123 == value

        value = config.get("value2")
        assert value != None

        value = config.get("value3")
        assert value == None

        value = config.get("value2.value21")
        assert value != None
        assert 111 == value

        value = config.get("value2.value31")
        assert value == None

        value = config.get("value2.value21.value211")
        assert value == None

        value = config.get("valueA.valueB.valueC")
        assert value == None
        
    def test_has(self):
        config = DynamicMap.from_value(
            '{ "value1": 123, "value2": { "value21": 111, "value22": 222 } }'
        )

        has = config.has("")
        assert not has

        has = config.has("value1")
        assert has

        has = config.has("value2")
        assert has

        has = config.has("value3")
        assert not has

        has = config.has("value2.value21")
        assert has

        has = config.has("value2.value31")
        assert not has

        has = config.has("value2.value21.value211")
        assert not has

        has = config.has("valueA.valueB.valueC")
        assert not has
        
    def test_set(self):
        config = DynamicMap()
        
        config.set(None, 123)
        assert 0 == len(config)
        
        config.set("field1", 123)
        assert 1 == len(config)
        assert 123 == config.get("field1")

        config.set("field2", "ABC")
        assert 2 == len(config)
        assert "ABC" == config.get("field2")

        config.set("field2.field1", 123)
        assert "ABC" == config.get("field2")

        config.set("field3.field31", 456)
        assert 3 == len(config)
        subConfig = config.get_nullable_map("field3")
        assert subConfig != None
        assert 456 == subConfig.get("field31")
        
        config.set("field3.field32", "XYZ")
        assert "XYZ" == config.get("field3.field32")
        