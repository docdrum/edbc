import unittest

from util.dse.dse10 import DSE10

class DSE5Test(unittest.TestCase):
    def testInit(self):
        d = DSE10()
        self.assertEqual(d.get(), '')
        self.assertFalse(d.wait_for_more)
        self.assertEqual(d.currentChar(), None)
        self.assertEqual(d.current_button, -1)

    def testOnePress(self):
        d = DSE10()
        d.pressButton(2)
        self.assertEqual(d.get(), '')
        self.assertTrue(d.wait_for_more)
        self.assertEqual(d.currentChar(), 'A')
        self.assertEqual(d.current_button, 2)

    def testDoublePress(self):
        d = DSE10()
        d.pressButton(2)
        d.pressButton(2)
        self.assertEqual(d.get(), '')
        self.assertTrue(d.wait_for_more)
        self.assertEqual(d.currentChar(), 'B')
        self.assertEqual(d.current_button, 2)

    def testRollAround(self):
        d = DSE10()
        for i in range(0, 4):
            d.pressButton(2)
        self.assertEqual(d.currentChar(), '2')
        self.assertEqual(d.current_count, 3)
        d.pressButton(2)
        self.assertEqual(d.currentChar(), 'A')
        self.assertEqual(d.current_count, 0)

    def testSecondButton(self):
        d = DSE10()
        d.pressButton(2)
        d.pressButton(3)
        self.assertEqual(d.get(), 'A')
        self.assertTrue(d.wait_for_more)
        self.assertEqual(d.currentChar(), 'D')
        self.assertEqual(d.current_button, 3)

    def testTimeOut(self):
        d = DSE10()
        d.pressButton(2)
        d.pressButton(2)
        d.timeOut()
        self.assertEqual(d.get(), 'B')
        self.assertFalse(d.wait_for_more)

    def testEnterWord(self):
        d = DSE10()
        d.pressButton(8)
        d.pressButton(3)
        d.pressButton(3)
        d.pressButton(7)
        d.pressButton(7)
        d.pressButton(7)
        d.pressButton(7)
        d.pressButton(8)
        d.timeOut()
        self.assertEqual(d.get(), 'TEST')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
