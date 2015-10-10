'''

@author: Omar
'''

import insights
import re

class Trade():
    """
    Trade class is an application that uses insights package to retrieve data about Exports & Imports grouped by Commodity.
    It fetches the data(JSON string) from URL, saves it to SQLite database, and perform some statistics.
    """
    
    _database       = insights.database.Database()
    _stats          = insights.stats.Stats
    _webData        = None
    _column_names   = None
    _table_names    = dict(exports='exports', imports='imports')
    
    def __init__(self):
        pass
    
    @staticmethod
    def fetch():
        urls = dict(exports = "https://www.quandl.com/api/v3/datasets/CBE/FT_EB.json", 
                    imports = "https://www.quandl.com/api/v3/datasets/CBE/FT_IBCG.json")
        
        # fetch exports and imports data
        # for each fetched dataset, call _get() method
        for k in urls:
            __class__._webData = insights.webdata.WebData(urls[k])
            __class__._get(__class__._table_names[k])
            
        return __class__
    
    @staticmethod
    def _get(trade_type):
        
        # parse fetched data, and get rows and columns from data fetched
        data    = __class__._webData.parseJson()
        rows    = data['dataset']['data']
        cols    = data['dataset']['column_names']
        
        # clean up column names
        for i, c in enumerate(cols):
            cols[i] = re.sub('[^\w]', '', c.title())
        
        if __class__._column_names == None:
            __class__._column_names  = cols
        
        # save data to database
        __class__._save(trade_type, rows, __class__._column_names)
    
    @staticmethod
    def _save(trade_type, rows, cols):
        
        schema = dict()
        # schema['id'] = dict(type='INTEGER', auto = True, primary = True)
        
        for c in cols:
            if c == 'Date':
                schema[c] = dict(type = 'INTEGER', not_null = True) 
            else:                                
                schema[c] = dict(type = 'REAL', not_null = True) 
            
        # create table for each trade(i.e. exports/imports)
        __class__._database.create(trade_type, schema)
            
        for r in rows:
            d = dict()
            for i, v in enumerate(r):
                if cols[i] == 'Date':
                    d[cols[i]] = int((v).split('-')[0])
                else:
                    d[cols[i]] = float(v)
                    
            # insert row 
            __class__._database.insert(trade_type, d)
            
    @staticmethod
    def viewData():
        
        # selects all data for exports and imports in database in a specific order
        exports = __class__._database.query("SELECT {} FROM {}"
                            .format(', '.join(__class__._column_names), __class__._table_names['exports'])).fetchAll()
        imports = __class__._database.query("SELECT {} FROM {}"
                            .format(', '.join(__class__._column_names), __class__._table_names['imports'])).fetchAll()
        
        cunt                = 1
        exports_by_column   = dict()    # list for every commodity item by column(item => list)
        imports_by_column   = dict()    # list for every commodity item by column(item => list)
        max_header_len      = 10        # max length >= 4 
        
        print("""
                Foreign Trade Data (i.e. Exports and Imports) grouped by Commodity. 
                Currency is in Million USD.
            """)
        for row_exports, row_imports in zip(exports, imports):
            
            if cunt == 1:
                # print headers
                for h in __class__._column_names:
                    h = h[:max_header_len]
                    if h == 'Date':
                        print("{: <10}".format(h), end='\t')
                        continue
                    print("E::{: <10}".format(h), end='\t')
                    print("I::{: <10}".format(h), end='\t')
                print()
            
            cunt += 1
            
            for c in __class__._column_names:
                if c == 'Date':
                    print("{: <10}".format(row_exports[c]), end='\t')
                    continue
                    
                print("{: <10}".format(row_exports[c]), end='\t')
                print("{: <10}".format(row_imports[c]), end='\t')
                
                # for each commodity, create a list of column values,
                # this will be used later in showing some statistics for each commodity item.
                if c not in exports_by_column and c not in imports_by_column:
                    exports_by_column[c] = [row_exports[c]]
                    imports_by_column[c] = [row_imports[c]]
                else:
                    exports_by_column[c].append(row_exports[c])
                    imports_by_column[c].append(row_imports[c])
                
            print()
        if cunt > 1: print()
                    
        __class__._appendStats(exports_by_column, imports_by_column)
    
    @staticmethod
    def _appendStats(exports, imports):
        
        # prepare all statistic methods
        lst_methods = [__class__._stats.average, __class__._stats.meanDeviation, __class__._stats.median, 
                       __class__._stats.variance, __class__._stats.standardDeviation, 
                       __class__._stats.max, __class__._stats.min, __class__._stats.range, __class__._stats.sum]
        
        for m in lst_methods:
            # for each method, loop through each commodity item values
            for c in __class__._column_names:
                if c == 'Date': 
                    print("{: <10}".format(m.__name__[:10]), end='\t')
                    continue
                print("{: <10}".format(round(m(exports[c]), 2)), end='\t')
                print("{: <10}".format(round(m(imports[c]), 2)), end='\t')
            print()
    
def main():
    Trade.fetch().viewData()

if __name__ == "__main__": main()

    