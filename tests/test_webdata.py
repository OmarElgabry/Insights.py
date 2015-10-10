'''

@author: Omar
'''

from insights.webdata import WebData
import unittest

class TestWebData(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data = WebData("https://www.quandl.com/api/v3/datasets/UICT/TELE_ARM.json")
    
    def test_getData(self):
        self.assertIsInstance(__class__.data.getData(), str)
        
    def test_parseJson(self):
        self.assertIsInstance(__class__.data.parseJson(), dict)
        
            
if __name__ == "__main__": unittest.main()
