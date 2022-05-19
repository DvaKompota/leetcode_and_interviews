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


if __name__ == '__main__':
    unittest.main()
