# -*- coding: utf-8 -*-
"""
    tests.persistence.DummyPersistenceFixture
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

DUMMY1 = { 'id': None, 'key': 'Key 1', 'content': 'Content 1' }
DUMMY2 = { 'id': None, 'key': 'Key 2', 'content': 'Content 2' }

class DummyPersistenceFixture:
    
    _db = None

    def __init__(self, db):
        self._db = db

    def test_crud_operations(self):
        # Create one dummy
        dummy1 = self._db.create_dummy(None, DUMMY1)

        assert dummy1 != None
        assert dummy1['id'] != None
        assert DUMMY1['key'] == dummy1['key']
        assert DUMMY1['content'] == dummy1['content']

        # Create another dummy
        dummy2 = self._db.create_dummy(None, DUMMY2)

        assert dummy2 != None
        assert dummy2['id'] != None
        assert DUMMY2['key'] == dummy2['key']
        assert DUMMY2['content'] == dummy2['content']

        # Get all dummies
        dummies = self._db.get_dummies(None, None, None)
        assert dummies != None
        assert 2 == len(dummies['data'])

        # Update the dummy
        dummy = self._db.update_dummy(
            None,
            dummy1['id'],
            { "content": "Updated Content 1" }
        )

        assert dummy != None
        assert dummy1['id'] == dummy['id']
        assert dummy1['key'] == dummy['key']
        assert "Updated Content 1" == dummy['content']

        # Delete the dummy
        self._db.delete_dummy(None, dummy1['id'])

        # Try to get deleted dummy
        dummy = self._db.get_dummy_by_id(None, dummy1['id'])
        assert dummy == None
