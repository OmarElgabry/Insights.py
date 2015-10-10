'''

@author: Omar
'''

from insights.stats import Stats
import unittest

class TestStats(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.lst = [6, 3 , 11 , 16 , 8 , 6 , 15 , 7]
    
    def test_stats(self):
        
        self.assertEqual(Stats.average(__class__.lst), 9.0)
        self.assertEqual(Stats.meanDeviation(__class__.lst), 3.75)
        self.assertEqual(Stats.count(__class__.lst, 7), 1)
        self.assertEqual(Stats.length(__class__.lst), 8)
        self.assertEqual(Stats.max(__class__.lst), 16)
        self.assertEqual(Stats.min(__class__.lst), 3)
        self.assertEqual(Stats.range(__class__.lst), 13)
        self.assertEqual(Stats.sum(__class__.lst), 72)
        self.assertEqual(Stats.sort(__class__.lst), [3, 6, 6, 7, 8, 11, 15, 16])
        self.assertEqual(Stats.variance(__class__.lst), 18.5)
        self.assertEqual(Stats.standardDeviation(__class__.lst), 4.301162633521313)
        self.assertEqual(Stats.median(__class__.lst), 7.5)
            
if __name__ == "__main__": unittest.main()
