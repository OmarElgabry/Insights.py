'''

@author: Omar
'''

from sqlite3 import ProgrammingError, Row
from insights.database import Database
import unittest

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        self._db = Database()
        self._table = 'users'
        self.assertCreate()
        self.assertInsert()
        
    def assertCreate(self):
        d = dict(
             id     = dict(type='INTEGER', auto = True, primary = True),
             name   = dict(type='TEXT', not_null = True),
             age    = dict(type='INT') 
        )
        
        self._db.create(self._table, d)
    
    def assertInsert(self):

        rows = [
                dict(name = 'alex', age = 22),
                dict(name = 'jason', age = 23),
                dict(name = 'albert', age = 21),
                dict(name = 'henry', age = 21),
                dict(name = 'mark', age = 21),
                dict(name = 'daniel', age = 22),
                dict(name = 'esra', age = 22)
            ]
        
        for row in rows:
            self._db.insert(self._table, row)

    def test_fetchAll(self):
        lst = self._db.getAll(self._table).fetchAll()
        assert type(lst) == list
        
    def test_fetch(self):
        obj = self._db.getById('users', 1).fetch()
        assert type(obj) == Row
                
    def test_iterate(self):
        db = self._db.getAll(self._table)
        for row in db.iterate():
            assert type(row) == Row 
        
    def test_query(self):
        db = self._db.query('UPDATE {} SET age = ? WHERE id = ?'.format(self._table), (29, 1))
        assert db is self._db
        
    def test_get(self):
        db = self._db.query('SELECT id, name FROM {} WHERE id =  ?'.format(self._table), 3)
        db.fetchAll()
        assert db is self._db
        
    def test_getAll(self):
        db = self._db.getAll(self._table)
        db.fetchAll()
        assert db is self._db
    
    def test_getById(self):
        db = self._db.getById(self._table, 1)
        db.fetchAll()
        assert db is self._db
        
    def test_create(self):
        d = dict(
             id     = dict(type='INTEGER', auto = True, primary = True),
             name   = dict(type='TEXT', not_null = True),
             age    = dict(type='INT') 
        )
        
        db = self._db.create(self._table, d)
        assert db is self._db
        
    def test_insert(self):
        rows = [
                dict(name = 'omar', age = 22),
                dict(name = 'adel', age = 23),
                dict(name = 'ahmed', age = 21)
            ]
        
        for row in rows:
            db = self._db.insert(self._table, row)
            assert db is self._db
        
    def test_updateById(self):
        db = self._db.updateById(self._table, dict(name='AhMeD', age = 25), 2) 
        assert db is self._db
    
    def test_deleteAll(self):
        db = self._db.deleteAll(self._table)
        assert db is self._db
        
    def test_deleteById(self):
        db = self._db.deleteById(self._table, 5)
        assert db is self._db
    
    def test_countAll(self):
        self.assertEqual(self._db.countAll(self._table), 7)
    
    def test_count(self):
        self.assertEqual(self._db.count(self._table, dict(age='22')), 3)        
        
    def test_rowsAffected(self):
        self._db.deleteAll(self._table)
        self.assertEqual(self._db.rowsAffected(), 7)
        
    def test_lastInsertedId(self):
        self._db.insert(self._table, dict(name = 'robert', age = 24))
        self.assertEqual(self._db.lastInsertedId(), 8)
    
    def test_printAll(self):
        db = self._db.printAll(self._table)
        assert db is self._db

    def test_printResult(self):
        db = self._db.getAll(self._table).printResult()
        assert db is self._db
                    
    def test_close(self):
        try:
            self._db.close()
            self._db.printAll(self._table)
        except ProgrammingError:
            assert self._db is not Database()
            self._db = Database()
        else:
            raise AssertionError("database connection not closed")

if __name__ == "__main__": unittest.main()
