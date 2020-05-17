import unittest
from Algorithms.TwoSum import TwoSumFirstDraft
from Algorithms.TwoSum import TwoSum


class TwoSumFirstDraftTest(unittest.TestCase):

    def testTwoSumFirstDraft(self):
        actual_result = TwoSumFirstDraft().two_sum_function([2, 7, 11, 15], 18)
        self.assertEqual(actual_result, [1, 2])

    def testTwoSumFirstDraftNoAnswer(self):
        actual_result = TwoSumFirstDraft().two_sum_function([2, 7, 11, 15], 19)
        self.assertEqual(actual_result, "There are no matching numbers")

    def testTwoSumFirstDraftEmptyArray(self):
        actual_result = TwoSumFirstDraft().two_sum_function([], 18)
        self.assertEqual(actual_result, "Please provide a valid input")

    def testTwoSumFirstDraftNoTarget(self):
        actual_result = TwoSumFirstDraft().two_sum_function([])
        self.assertEqual(actual_result, "Please provide a valid input")


class TwoSumTest(unittest.TestCase):

    def testTwoSum(self):
        actual_result = TwoSum().two_sum_function([2, 7, 11, 15], 18)
        self.assertEqual(actual_result, [1, 2])

    def testTwoSumNoAnswer(self):
        actual_result = TwoSum().two_sum_function([2, 7, 11, 15], 19)
        self.assertEqual(actual_result, "There are no matching numbers")

    def testTwoSumEmptyArray(self):
        actual_result = TwoSum().two_sum_function([], 18)
        self.assertEqual(actual_result, "Please provide a valid input")

    def testTwoSumNoTarget(self):
        actual_result = TwoSum().two_sum_function([])
        self.assertEqual(actual_result, "Please provide a valid input")

