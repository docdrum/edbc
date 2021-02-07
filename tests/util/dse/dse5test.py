'''
Created on 5 Feb 2021

@author: cstft
'''
import unittest

from util.dse.dse5 import DSE5
from util.dse.dseerror import DSEError

class DSE5Test(unittest.TestCase):
    def testInit(self):
        d = DSE5()
        self.assertEqual(d.get(), '')
        self.assertFalse(d.wait_for_more)
        self.assertEqual(d.currentChar(), None)
        self.assertEqual(d.current_button, -1)

    def testInvalidButton(self):
        d = DSE5()
        with self.assertRaises(DSEError):
            d.pressButton(6)
            
    def testOnePress(self):
        d = DSE5()
        d.pressButton(0)
        self.assertEqual(d.get(), '')
        self.assertTrue(d.wait_for_more)
        self.assertEqual(d.currentChar(), 'A')
        self.assertEqual(d.current_button, 0)

    def testDoublePress(self):
        d = DSE5()
        d.pressButton(0)
        d.pressButton(0)
        self.assertEqual(d.get(), '')
        self.assertTrue(d.wait_for_more)
        self.assertEqual(d.currentChar(), 'B')
        self.assertEqual(d.current_button, 0)
        
    def testRollAround(self):
        d = DSE5()
        for i in range(0, 7):
            d.pressButton(0)
        self.assertEqual(d.currentChar(), 'G')
        self.assertEqual(d.current_count, 6)
        d.pressButton(0)
        self.assertEqual(d.currentChar(), 'A')
        self.assertEqual(d.current_count, 0)
        
    def testSecondButton(self):
        d = DSE5()
        d.pressButton(0)
        d.pressButton(1)
        self.assertEqual(d.get(), 'A')
        self.assertTrue(d.wait_for_more)
        self.assertEqual(d.currentChar(), 'H')
        self.assertEqual(d.current_button, 1)

    def testTimeOut(self):
        d = DSE5()
        d.pressButton(0)
        d.pressButton(0)
        d.timeOut()
        self.assertEqual(d.get(), 'B')
        self.assertFalse(d.wait_for_more)
        
    def testEnterWord(self):
        d = DSE5()
        d.pressButton(3)
        d.pressButton(0)
        d.pressButton(0)
        d.pressButton(0)
        d.pressButton(0)
        d.pressButton(0)
        d.pressButton(2)
        d.pressButton(2)
        d.pressButton(2)
        d.pressButton(2)
        d.pressButton(2)
        d.pressButton(2)
        d.pressButton(3)
        d.timeOut()
        self.assertEqual(d.get(), 'TEST')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()