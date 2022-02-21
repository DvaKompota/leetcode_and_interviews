import unittest
from Tasks.LeetcodeTasks.SortArrayOfZeroOnes import SortArrayOfZeroOnes


class SortArrayOfZeroOnesTest(unittest.TestCase):

    def testSortArrayOfZeroOnes(self):
        given_array = [1, 0, 0, 0, 1, 1, 0]
        expected_result = [0, 0, 0, 0, 1, 1, 1]
        actual_result = SortArrayOfZeroOnes().sort_array_of_zero_ones(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSortArrayOfZeroOnesMoved(self):
        given_array = [0, 0, 0, 0, 1, 1, 1]
        expected_result = [0, 0, 0, 0, 1, 1, 1]
        actual_result = SortArrayOfZeroOnes().sort_array_of_zero_ones(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSortArrayOfZeroZeroesMoved(self):
        given_array = [1, 1, 1, 0, 0, 0, 0]
        expected_result = [0, 0, 0, 0, 1, 1, 1]
        actual_result = SortArrayOfZeroOnes().sort_array_of_zero_ones(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSortArrayOfZeroOnesOnlyOne(self):
        given_array = [1]
        expected_result = [1]
        actual_result = SortArrayOfZeroOnes().sort_array_of_zero_ones(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSortArrayOfZeroOnesOnlyZero(self):
        given_array = [0]
        expected_result = [0]
        actual_result = SortArrayOfZeroOnes().sort_array_of_zero_ones(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSortArrayOfZeroOnesOnlyOnes(self):
        given_array = [1, 1, 1]
        expected_result = [1, 1, 1]
        actual_result = SortArrayOfZeroOnes().sort_array_of_zero_ones(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSortArrayOfZeroOnesOnlyZeroes(self):
        given_array = [0, 0, 0, 0]
        expected_result = [0, 0, 0, 0]
        actual_result = SortArrayOfZeroOnes().sort_array_of_zero_ones(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSortArrayOfZeroOnesEmpty(self):
        given_array = []
        expected_result = []
        actual_result = SortArrayOfZeroOnes().sort_array_of_zero_ones(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSortArrayOfZeroOnesOtherDigits(self):
        given_array = [0, 1, 0, 3, 12]
        expected_result = "Array contains invalid items!"
        actual_result = SortArrayOfZeroOnes().sort_array_of_zero_ones(given_array)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
