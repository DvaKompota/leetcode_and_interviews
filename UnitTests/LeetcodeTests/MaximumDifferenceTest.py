import unittest
from Tasks.LeetcodeTasks.MaximumDifference import MaximumDifference


class MaximumDifferenceTest(unittest.TestCase):

    def testMaximumDifference(self):
        given_array = [3, 0, 12, 3, 1]
        expected_result = 12
        actual_result = MaximumDifference().maximum_difference(given_array)
        self.assertEqual(expected_result, actual_result)

    def testMaximumDifferenceOne(self):
        given_array = [3]
        expected_result = 0
        actual_result = MaximumDifference().maximum_difference(given_array)
        self.assertEqual(expected_result, actual_result)

    def testMaximumDifferenceNegative(self):
        given_array = [3, 0, 12, -3, 1]
        expected_result = 15
        actual_result = MaximumDifference().maximum_difference(given_array)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
