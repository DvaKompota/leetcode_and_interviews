import unittest
from Algorithms.ListPrimes import ListPrimes


class ListPrimesTest(unittest.TestCase):

    def testListPrimes10(self):
        actual_result = ListPrimes().listPrimes(10)
        self.assertEqual(actual_result, [2, 3, 5, 7])

    def testListPrimes0(self):
        actual_result = ListPrimes().listPrimes(0)
        self.assertEqual(actual_result, [])

    def testListPrimes1(self):
        actual_result = ListPrimes().listPrimes(1)
        self.assertEqual(actual_result, [])

    def testListPrimes2(self):
        actual_result = ListPrimes().listPrimes(2)
        self.assertEqual(actual_result, [])

    def testListPrimes3(self):
        actual_result = ListPrimes().listPrimes(3)
        self.assertEqual(actual_result, [2])

    def testListPrimes11(self):
        actual_result = ListPrimes().listPrimes(11)
        self.assertEqual(actual_result, [2, 3, 5, 7])

    def testListPrimes12(self):
        actual_result = ListPrimes().listPrimes(12)
        self.assertEqual(actual_result, [2, 3, 5, 7, 11])

    def testListPrimes100(self):
        actual_result = ListPrimes().listPrimes(100)
        self.assertEqual(actual_result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                                         43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

