import unittest
from Algorithms.TwoSum import TwoSum


class TwoSumIndexTest(unittest.TestCase):

    def testTwoSum(self):
        actual_result = TwoSum().twoSumIndex([2, 7, 11, 15], 9)
        self.assertEqual(actual_result, [0, 1])

    def testTwoSum3246(self):
        actual_result = TwoSum().twoSumIndex([3, 2, 4], 6)
        self.assertEqual(actual_result, [1, 2])

    def testTwoSum336(self):
        actual_result = TwoSum().twoSumIndex([3, 3], 6)
        self.assertEqual(actual_result, [0, 1])

    def testTwoSumNoAnswer(self):
        actual_result = TwoSum().twoSumIndex([2, 7, 11, 15], 19)
        self.assertEqual(actual_result, "There are no matching numbers")


class TwoSumTest(unittest.TestCase):

    def testTwoSum(self):
        actual_result = TwoSum().twoSum([2, 7, 11, 15], 9)
        self.assertEqual(actual_result, [0, 1])

    def testTwoSum3246(self):
        actual_result = TwoSum().twoSum([3, 2, 4], 6)
        self.assertEqual(actual_result, [1, 2])

    def testTwoSum336(self):
        actual_result = TwoSum().twoSum([3, 3], 6)
        self.assertEqual(actual_result, [0, 1])

    def testTwoSumNoAnswer(self):
        actual_result = TwoSum().twoSum([2, 7, 11, 15], 19)
        self.assertEqual(actual_result, "There are no matching numbers")

