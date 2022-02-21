import unittest
from Tasks.LeetcodeTasks.PrimeNumberList import PrimeNumberList


class PrimeNumberListTest(unittest.TestCase):

    def testPrimeNumberList10(self):
        actual_result = PrimeNumberList().prime_number_list(10)
        self.assertEqual(actual_result, [2, 3, 5, 7])

    def testPrimeNumberList0(self):
        actual_result = PrimeNumberList().prime_number_list(0)
        self.assertEqual(actual_result, [])

    def testPrimeNumberList1(self):
        actual_result = PrimeNumberList().prime_number_list(1)
        self.assertEqual(actual_result, [])

    def testPrimeNumberList2(self):
        actual_result = PrimeNumberList().prime_number_list(2)
        self.assertEqual(actual_result, [])

    def testPrimeNumberList3(self):
        actual_result = PrimeNumberList().prime_number_list(3)
        self.assertEqual(actual_result, [2])

    def testPrimeNumberList11(self):
        actual_result = PrimeNumberList().prime_number_list(11)
        self.assertEqual(actual_result, [2, 3, 5, 7])

    def testPrimeNumberList12(self):
        actual_result = PrimeNumberList().prime_number_list(12)
        self.assertEqual(actual_result, [2, 3, 5, 7, 11])

    def testPrimeNumberList100(self):
        actual_result = PrimeNumberList().prime_number_list(100)
        self.assertEqual(actual_result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                                         43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


if __name__ == '__main__':
    unittest.main()
