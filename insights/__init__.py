"""
    ==================
    Insights
    ==================
    
    A Python package for analyzing data from Public Data APIs.
    It provides modules for reading & parsing data from URL, storing data using a wrapper for SQLite, and performing some statistics.
    
    :license: MIT
"""

from insights.database  import Database
from insights.stats     import Stats
from insights.webdata   import WebData