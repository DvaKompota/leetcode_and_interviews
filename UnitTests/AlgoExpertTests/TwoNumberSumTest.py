import unittest
from Tasks.AlgoExpertTasks.TwoNumberSum import two_number_sum


class TwoNumberSumTest(unittest.TestCase):

    def testTwoNumberSum(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        target = 10
        expected_result = [11, -1]
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSum46(self):
        array = [4, 6]
        target = 10
        expected_result = [4, 6]
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSum461(self):
        array = [4, 6, 1]
        target = 5
        expected_result = [4, 1]
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSum461minus3(self):
        array = [4, 6, 1, -3]
        target = 3
        expected_result = [6, -3]
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSum1to9(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 17
        expected_result = [8, 9]
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSum1to9and15(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
        target = 18
        expected_result = [3, 15]
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSumNegativeTarget(self):
        array = [-7, -5, -3, -1, 0, 1, 3, 5, 7]
        target = -5
        expected_result = [-5, 0]
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSumNegativeSecond(self):
        array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
        target = 163
        expected_result = [210, -47]
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSumNotFound(self):
        array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
        target = 164
        expected_result = []
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSumNotFound2(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        target = 15
        expected_result = []
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSumNotFound3(self):
        array = [14]
        target = 15
        expected_result = []
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)

    def testTwoNumberSumNotFound4(self):
        array = [15]
        target = 15
        expected_result = []
        actual_result = two_number_sum(array, target)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
