=================
Insights |travis|
=================

.. |travis| image:: https://travis-ci.org/OmarElGabry/Insights.py.png
   :alt: Build Status
   :target: https://travis-ci.org/OmarElGabry/Insights.py
   
A Python package for reading, storing, & analyzing data from Public Data APIs.

It provides modules for reading & parsing data from URL, storing data using a wrapper for SQLite, and performing some statistics.

Index
======================

+ `Web Data`_
+ `SQLite Database`_
+ `Statistics`_
+ `Trade Application`_
+ `Support`_
+ `Contribute`_
+ `License`_

Web Data
======================

WebData class for reading data returned from URL, and parsing JSON to dictionary object.

.. sourcecode:: python

	import insights
	data = insights.webdata.WebData("http://www.json-generator.com/api/json/get/bMUULAzmaa?indent=2")
	print(data.parseJson())

SQLite Database
======================

Database class acts like a wrapper SQLite. It provides variety of methods that hides complexity.
 
.. sourcecode:: python

	import insights
	db = insights.database.Database()
    d = dict(
             id     = dict(type='INTEGER', auto = True, primary = True),
             name   = dict(type='TEXT', not_null = True),
             age    = dict(type='INT') 
        )
    
    # create table
    db.create('users', d)
    
    # insert rows
    db.insert('users', dict(name = 'omar', age = 22))
    db.insert('users', dict(name = 'alex', age = 23))
    db.insert('users', dict(name = 'peter', age = 21))
    
    # last inserted id
    print(db.lastInsertedId())
    
    # print users
    db.getAll('users').printResult()
    db.getById('users', '1').printResult()
    
    # counting 
    print(db.count('users', dict(age='22')))
    print(db.countAll('users'))
    
    # delete
    db.deleteById('users', '2')
    
    # update     
    db.updateById('users', dict(name='ALEX', age = 25), 2) 
    
    # number of affected rows by last query
    print(db.rowsAffected())
    
    # close connection
    db.close()
	
Statistics
======================

Stats class for performing some simple statistics on a list of values. 

.. sourcecode:: python
	import insights
	lst     = [6, 3 , 11 , 16 , 8 , 6 , 15 , 7]
    Stats   = insights.stats.Stats
    
    print("Average\t", Stats.average(lst))   
    print("MD\t", Stats.meanDeviation(lst))   
    print("Count 7\t", Stats.count(lst, 7))   
    print("Length\t", Stats.length(lst))   
    print("Max\t", Stats.max(lst))   
    print("Min\t", Stats.min(lst))   
    print("Range\t", Stats.range(lst))   
    print("Sum\t", Stats.sum(lst))   
    print("Sort\t", Stats.sort(lst))   
    print("Variance", Stats.variance(lst))   
    print("SD\t", Stats.standardDeviation(lst))   
    print("Median\t", Stats.median(lst))  
    
Trade Application
======================
Trade class is an application that uses insights package to retrieve data about Exports & Imports grouped by Commodity.

It fetches the data(JSON string) from URL, saves it to SQLite database, and perform some statistics.

The generated table will look like(doesn't include all data, nor all statistics)::

	========  =======  =======  =======  =======
	Date      E::Oil   I::Oil   E::Tea   I::Tea
	========  =======  =======  =======  =======
	2013      12006.2  12495.7  14.0     239.4
	2012      11225.0  11774.5  12.7     180.1
	........  .......  .......  .......  .......
	average   10064.2  2183.83  7.72     151.14
	variance  9037043  1077840  22.89    2585.42
	SD        3006.17  3283.05  4.78     50.85
	max       14472.6  12495.7  14.7     239.4
	min       3910.3   2549.7   2.0      88.1
	========  =======  =======  =======  =======

**NOTE** Trade application is inside ``app/`` folder.

Support
======================
I've written this package in my free time during my studies. If you find it useful, please support the project by spreading the word.

Contribute
======================
Contribute by creating new issues, sending pull requests on Github or you can send an email at: omar.elgabry.93@gmail.com

License
======================
Built under `MIT <http://www.opensource.org/licenses/mit-license.php>`_ license.
