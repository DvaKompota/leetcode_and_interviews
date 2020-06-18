import unittest
from Algorithms.SumElementsInArray import SumElementsInArray


class SumElementsInArrayTest(unittest.TestCase):

    def testSumElementsInArray(self):
        actual_result = SumElementsInArray().sum_elements([1, 2, 3])
        self.assertEqual(actual_result, 6)

    def testSumElementsInEmptyArray(self):
        actual_result = SumElementsInArray().sum_elements([])
        self.assertEqual(actual_result, "Array is empty!")

    def testSumElementsInNegativeArray(self):
        actual_result = SumElementsInArray().sum_elements([1, 2, -4])
        self.assertEqual(actual_result, -1)


if __name__ == '__main__':
    unittest.main()
