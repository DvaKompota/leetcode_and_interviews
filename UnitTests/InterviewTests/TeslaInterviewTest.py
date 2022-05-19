import unittest
from Tasks.InterviewTasks.TeslaInterview import TeslaInterview


class TeslaInterviewCodilityFirstMissingPositiveTest(unittest.TestCase):

    def testTeslaInterviewCodilityFirstMissingPositive1(self):
        given_array = [3, 4, -1, 1]
        expected_result = 2
        actual_result = TeslaInterview().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityFirstMissingPositive2(self):
        given_array = [1, 2, 0]
        expected_result = 3
        actual_result = TeslaInterview().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityFirstMissingPositive3(self):
        given_array = [1, 3, 6, 4, 1, 2]
        expected_result = 5
        actual_result = TeslaInterview().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityFirstMissingPositive4(self):
        given_array = [1, 2, 3]
        expected_result = 4
        actual_result = TeslaInterview().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityFirstMissingPositive5(self):
        given_array = [-1, -3]
        expected_result = 1
        actual_result = TeslaInterview().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityFirstMissingPositive6(self):
        given_array = [7, 8, 9, 11, 12]
        expected_result = 1
        actual_result = TeslaInterview().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)


class TeslaInterviewCodilityLongestBinaryGapTest(unittest.TestCase):

    def testTeslaInterviewCodilityLongestBinaryGap1(self):
        given_integer = 9
        expected_result = 2
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap2(self):
        given_integer = 529
        expected_result = 4
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap3(self):
        given_integer = 20
        expected_result = 1
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap4(self):
        given_integer = 15
        expected_result = 0
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap5(self):
        given_integer = 32
        expected_result = 0
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap6(self):
        given_integer = 1041
        expected_result = 5
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap7(self):
        given_integer = 328
        expected_result = 2
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap8(self):
        given_integer = 1162
        expected_result = 3
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap9(self):
        given_integer = 51712
        expected_result = 2
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap10(self):
        given_integer = 66561
        expected_result = 9
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap11(self):
        given_integer = 6291457
        expected_result = 20
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap12(self):
        given_integer = 74901729
        expected_result = 4
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap13(self):
        given_integer = 805306373
        expected_result = 25
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap14(self):
        given_integer = 1376796946
        expected_result = 5
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityLongestBinaryGap15(self):
        given_integer = 1610612737
        expected_result = 28
        actual_result = TeslaInterview().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
