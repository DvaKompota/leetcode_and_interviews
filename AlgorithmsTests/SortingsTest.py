import unittest
from Algorithms.Sortings import Sortings


class BubbleSortTest(unittest.TestCase):

    def testBubbleSort(self):
        given_array = [100, 0, 12, 3, 8, 1]
        expected_result = [0, 1, 3, 8, 12, 100]
        actual_result = Sortings().bubble_sort(given_array)
        self.assertEqual(expected_result, actual_result)

    def testBubbleSortNegative(self):
        given_array = [0, 12, 3, -8, 1]
        expected_result = [-8, 0, 1, 3, 12]
        actual_result = Sortings().bubble_sort(given_array)
        self.assertEqual(expected_result, actual_result)

    def testBubbleSortDuplicates(self):
        given_array = [5, 1, 1, 2, 0, 0]
        expected_result = [0, 0, 1, 1, 2, 5]
        actual_result = Sortings().bubble_sort(given_array)
        self.assertEqual(expected_result, actual_result)


class SelectionSortTest(unittest.TestCase):

    def testSelectionSort(self):
        given_array = [100, 0, 12, 3, 8, 1]
        expected_result = [0, 1, 3, 8, 12, 100]
        actual_result = Sortings().selection_sort(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSelectionSortNegative(self):
        given_array = [0, 12, 3, -8, 1]
        expected_result = [-8, 0, 1, 3, 12]
        actual_result = Sortings().selection_sort(given_array)
        self.assertEqual(expected_result, actual_result)

    def testSelectionSortDuplicates(self):
        given_array = [5, 1, 1, 2, 0, 0]
        expected_result = [0, 0, 1, 1, 2, 5]
        actual_result = Sortings().selection_sort(given_array)
        self.assertEqual(expected_result, actual_result)


class CountingSortTest(unittest.TestCase):

    def testCountingSort(self):
        given_array = [100, 0, 12, 3, 8, 1]
        expected_result = [0, 1, 3, 8, 12, 100]
        actual_result = Sortings().counting_sort(given_array)
        self.assertEqual(expected_result, actual_result)

    def testCountingSortNegative(self):
        given_array = [0, 12, 3, -8, 1]
        expected_result = "Counting sorting does not support negative integers"
        actual_result = Sortings().counting_sort(given_array)
        self.assertEqual(expected_result, actual_result)

    def testCountingSortDuplicates(self):
        given_array = [5, 1, 1, 2, 0, 0]
        expected_result = [0, 0, 1, 1, 2, 5]
        actual_result = Sortings().counting_sort(given_array)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
