'''

@author: Omar
'''

import sqlite3

class Singleton(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]
    
class Database(metaclass=Singleton):
    """
    Database class acts like a wrapper SQLite. 
    It provides variety of methods that hides complexity.
    
    So, you can perform CRUD queries in a very handy way.
    """

    _filename = ':memory:'
    
    def __init__(self, **kwargs):
        """
        Constructor method.
            filename is a string for the database file, defaults is in memory.
        """
        __class__._filename         = kwargs.get('filename', ':memory:')
        self._result                = None
        self._database              = sqlite3.connect(__class__._filename)
        self._database.row_factory  = sqlite3.Row
    
    def fetchAll(self):
        """
        Fetches all rows after executing a query, returning a list of rows, each of type sqlite3.Row.
        """
        return self._result.fetchall()
    
    def fetch(self):
        """
        Fetches only the next row after executing a query, returning a sqlite3.Row object.
        """
        return self._result.fetchone()
    
    def iterate(self):
        """
        Iterates over all rows after executing a query.
        """
        for row in self.fetchAll():
            yield row
    
    def query(self, sql, params = ()):
        """
        Executes a non-select query(create, update, delete).
        Returns a reference to current object.
        """
        if type(params) != tuple: 
            params = (params,)
            
        self._result = self._database.execute(sql, params)
        self._database.commit()
        return self
        
    def get(self, sql):
        """
        Executes a select query.
        Returns a reference to current object.
        """
        self._result = self._database.execute(sql)
        return self
    
    def getAll(self, _table):
        """
        Executes a select query; select all rows and columns from a table.
        Returns a reference to current object.
        """
        self._result = self._database.execute('SELECT * FROM {} '.format(_table))
        return self
    
    def getById(self, _table, _id):
        """
        Executes a select query; select a row by column id
        Returns a reference to current object.
        """
        self._result = self._database.execute('SELECT * FROM {} WHERE id = ? LIMIT 1'.format(_table), (_id,))
        return self
    
    def create(self, _table, _schema):
        """
        Creates a table. 
            _table is a string for table name
            _schema is a dictionary object for definition of table.
        Keys allowed in schema are: type(str), primary(bool), auto-increment(bool), not null(bool).
        Existing tables with same name will be dropped before creating the new one.
        Returns a reference to current object.
        """
        cols = []
        for col in _schema:
            q = str(col) + ' '
            opt = _schema[col]
            if 'type' in opt:
                q += opt['type'] + ' '
            if 'primary' in opt and opt['primary'] == True:
                q += 'PRIMARY KEY '
            if 'auto' in opt and opt['auto'] == True:
                q += 'AUTOINCREMENT '
            if 'not_null' in opt and opt['not_null'] == True:
                q += 'NOT NULL '
            cols.append(q)
                        
        self.query('DROP TABLE IF EXISTS {} '.format(_table))
        self.query('CREATE TABLE {} ({})'.format(_table, ', '.join(cols)))
        return self
    
    def insert(self, _table, _row):
        """
        Inserts row(s) in a table.
            _row is a dictionary object with key as column name, and value 
        Returns a reference to current object.
        """
        cols = list(_row.keys())
        values = [ _row[v] for v in cols ]
            
        query = 'INSERT INTO {} ({}) VALUES ({})'.format(
            _table,
            ', '.join(cols),
            ', '.join([['?'] * len(values)][0])
        )
        
        self._result = self._database.execute(query, values)
        self._database.commit()
        
        return self
    
    def updateById(self, _table, _row, _id):
        """
        Updates a row by Id.
            _row is a dictionary object with key as column name, and value 
        Returns a reference to current object.
        """
        cols = list(_row.keys())
        values = [ _row[v] for v in cols ]
        
        # don't update id
        for i, k in enumerate(cols):
            if k == 'id':
                del cols[i]
                del values[i]
                break

        query = 'UPDATE {} SET {} WHERE id = ?'.format(
            _table,
            ', '.join(k + ' = ?' for k in cols)
        )
        
        self._result = self._database.execute(query, values + [_id])
        self._database.commit()

        return self
    
    def deleteAll(self, _table):
        """
        Deletes all data in a table.
        Returns a reference to current object.
        """
        self._result = self._database.execute('DELETE FROM {}'.format(_table))
        self._database.commit()
        return self
    
    def deleteById(self, _table, _id):
        """
        Deletes a row by Id.
        Returns a reference to current object.
        """
        self._result = self._database.execute('DELETE FROM {} WHERE id = ?'.format(_table), (_id,))
        self._database.commit()
        return self

    def countAll(self, _table):
        """
        Counts all rows in a table
        Returns a an integer; number of rows.
        """
        self._result = self._database.execute('SELECT COUNT(*) FROM {}'.format(_table))
        return int(self.fetch()[0])
    
    def count(self, _table, _opt):
        """
        Counts all rows in a table by using WHERE clause.
        Returns a an integer; number of rows.
        """
        cols = list(_opt.keys())
        values = [ _opt[v] for v in cols ]
        query = 'SELECT COUNT(*) FROM {} WHERE {}'.format(
            _table,
            ' AND '.join(k + ' = ?' for k in cols)
        )

        self._result = self._database.execute(query, values)        
        return int(self.fetch()[0])
    
    def rowsAffected(self):
        """
        Returns number of rows affected by last query.
        """
        return self._result.rowcount
    
    def lastInsertedId(self):
        """
        Returns the id(primary, auto-incremented column) of the last inserted row.
        """
        return self._result.lastrowid
    
    def printAll(self, _table):
        """
        Selects all rows, and displaying them.
        """
        return self.getAll(_table).printResult()
    
    def printResult(self):
        """
        Displays all rows and columns returned from the last query. 
        """
        cunt  = 1
        for row in self.fetchAll():
            
            if cunt == 1:
                for h in row.keys():
                    print("{: <10}".format(h), end='\t')
                print()
            
            cunt += 1
            
            for value in row:
                print("{: <10}".format(value), end='\t')
            print()
        if cunt > 1: print()
        
        return self
    
    def close(self):
        """
        Closes database connection and deletes the current Database Singleton object.
        """
        self._database.close()
        del __class__._instances[__class__]

