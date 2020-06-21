import unittest
from Algorithms.BinarySearch import BinarySearch


class BinarySearchTest(unittest.TestCase):

    def test_search_an_element(self):
        given_array = [10, -39, 100, 3, 6, 19, 2]
        given_target = 19
        expected_result = 5
        actual_result = BinarySearch().search_an_element(given_array, given_target)
        self.assertEqual(expected_result, actual_result)

    def test_binary_search(self):
        given_array = [-39, 2, 3, 6, 10, 19, 100]
        given_target = 19
        expected_result = 5
        actual_result = BinarySearch().binary_search(given_array, given_target)
        self.assertEqual(expected_result, actual_result)

    def test_binary_search_million(self):
        given_array = list(range(1, 1000000))
        given_target = 1
        expected_result = 0
        actual_result = BinarySearch().binary_search(given_array, given_target)
        self.assertEqual(expected_result, actual_result)
