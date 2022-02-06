import unittest
from Algorithms.LongestCommonPrefix import LongestCommonPrefix


class LongestCommonPrefixTest(unittest.TestCase):

    def testLongestCommonPrefixYes(self):
        given_array = ["flower", "flow", "flight"]
        expected_result = 'fl'
        actual_result = LongestCommonPrefix().longest_common_prefix(given_array)
        self.assertEqual(expected_result, actual_result)

    def testLongestCommonPrefixNo(self):
        given_array = ["dog", "racecar", "car"]
        expected_result = ''
        actual_result = LongestCommonPrefix().longest_common_prefix(given_array)
        self.assertEqual(expected_result, actual_result)
