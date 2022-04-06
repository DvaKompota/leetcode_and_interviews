import unittest
from Tasks.AlgoExpertTasks.SortedSquaredArray import sorted_squared_array


class SortedSquaredArrayTest(unittest.TestCase):

    def testSortedSquaredArray(self):
        array = [1, 2, 3, 5, 6, 8, 9]
        expected_result = [1, 4, 9, 25, 36, 64, 81]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayOne(self):
        array = [1]
        expected_result = [1]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayOneTwo(self):
        array = [1, 2]
        expected_result = [1, 4]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayOneToFive(self):
        array = [1, 2, 3, 4, 5]
        expected_result = [1, 4, 9, 16, 25]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayZero(self):
        array = [0]
        expected_result = [0]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayTen(self):
        array = [10]
        expected_result = [100]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayMinusOne(self):
        array = [-1]
        expected_result = [1]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayMinusOneTwo(self):
        array = [-2, -1]
        expected_result = [1, 4]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayMinusOneToMinusFive(self):
        array = [-5, -4, -3, -2, -1]
        expected_result = [1, 4, 9, 16, 25]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayMinusTen(self):
        array = [-10]
        expected_result = [100]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayMinusTenToTen(self):
        array = [-10, -5, 0, 5, 10]
        expected_result = [0, 25, 25, 100, 100]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayMinusSevenToThirty(self):
        array = [-7, -3, 1, 9, 22, 30]
        expected_result = [1, 9, 49, 81, 484, 900]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayMinusFiftyToTwenty(self):
        array = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
        expected_result = [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayZeroes(self):
        array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayMinusOneToFourWithDuplicates(self):
        array = [-1, -1, 2, 3, 3, 3, 4]
        expected_result = [1, 1, 4, 9, 9, 9, 16]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)

    def testSortedSquaredArrayMinusThreeToMinusOne(self):
        array = [-3, -2, -1]
        expected_result = [1, 4, 9]
        actual_result = sorted_squared_array(array)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
