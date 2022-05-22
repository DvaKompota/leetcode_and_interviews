import unittest
from Tasks.InterviewTasks.TeslaInterview import CodilityTasks


class TeslaInterviewCodilityTasksFirstMissingPositiveTest(unittest.TestCase):

    def testTeslaInterviewCodilityTasksFirstMissingPositive1(self):
        given_array = [3, 4, -1, 1]
        expected_result = 2
        actual_result = CodilityTasks().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingPositive2(self):
        given_array = [1, 2, 0]
        expected_result = 3
        actual_result = CodilityTasks().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingPositive3(self):
        given_array = [1, 3, 6, 4, 1, 2]
        expected_result = 5
        actual_result = CodilityTasks().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingPositive4(self):
        given_array = [1, 2, 3]
        expected_result = 4
        actual_result = CodilityTasks().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingPositive5(self):
        given_array = [-1, -3]
        expected_result = 1
        actual_result = CodilityTasks().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingPositive6(self):
        given_array = [7, 8, 9, 11, 12]
        expected_result = 1
        actual_result = CodilityTasks().first_missing_positive(given_array)
        self.assertEqual(expected_result, actual_result)


class TeslaInterviewCodilityTasksLongestBinaryGapTest(unittest.TestCase):

    def testTeslaInterviewCodilityTasksLongestBinaryGap1(self):
        given_integer = 9
        expected_result = 2
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap2(self):
        given_integer = 529
        expected_result = 4
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap3(self):
        given_integer = 20
        expected_result = 1
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap4(self):
        given_integer = 15
        expected_result = 0
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap5(self):
        given_integer = 32
        expected_result = 0
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap6(self):
        given_integer = 1041
        expected_result = 5
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap7(self):
        given_integer = 328
        expected_result = 2
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap8(self):
        given_integer = 1162
        expected_result = 3
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap9(self):
        given_integer = 51712
        expected_result = 2
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap10(self):
        given_integer = 66561
        expected_result = 9
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap11(self):
        given_integer = 6291457
        expected_result = 20
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap12(self):
        given_integer = 74901729
        expected_result = 4
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap13(self):
        given_integer = 805306373
        expected_result = 25
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap14(self):
        given_integer = 1376796946
        expected_result = 5
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksLongestBinaryGap15(self):
        given_integer = 1610612737
        expected_result = 28
        actual_result = CodilityTasks().longest_binary_gap(given_integer)
        self.assertEqual(expected_result, actual_result)


class TeslaInterviewCodilityTasksArrayOfUniqueIntegersWithZeroSumTest(unittest.TestCase):

    def testTeslaInterviewCodilityTasksArrayOfUniqueIntegersWithZeroSum1(self):
        given_integer = 1
        actual_result = CodilityTasks().array_of_unique_integers_with_zero_sum(given_integer)
        self.assertEqual(len(actual_result), given_integer)  # length of the result array is equal to the given integer
        self.assertEqual(len(actual_result), len(set(actual_result)))  # all integers in the result array are unique
        self.assertEqual(sum(actual_result), 0)  # sum of all integers in the result array is equal to zero

    def testTeslaInterviewCodilityTasksArrayOfUniqueIntegersWithZeroSum2(self):
        given_integer = 2
        actual_result = CodilityTasks().array_of_unique_integers_with_zero_sum(given_integer)
        self.assertEqual(len(actual_result), given_integer)  # length of the result array is equal to the given integer
        self.assertEqual(len(actual_result), len(set(actual_result)))  # all integers in the result array are unique
        self.assertEqual(sum(actual_result), 0)  # sum of all integers in the result array is equal to zero

    def testTeslaInterviewCodilityTasksArrayOfUniqueIntegersWithZeroSum3(self):
        given_integer = 3
        actual_result = CodilityTasks().array_of_unique_integers_with_zero_sum(given_integer)
        self.assertEqual(len(actual_result), given_integer)  # length of the result array is equal to the given integer
        self.assertEqual(len(actual_result), len(set(actual_result)))  # all integers in the result array are unique
        self.assertEqual(sum(actual_result), 0)  # sum of all integers in the result array is equal to zero

    def testTeslaInterviewCodilityTasksArrayOfUniqueIntegersWithZeroSum4(self):
        given_integer = 4
        actual_result = CodilityTasks().array_of_unique_integers_with_zero_sum(given_integer)
        self.assertEqual(len(actual_result), given_integer)  # length of the result array is equal to the given integer
        self.assertEqual(len(actual_result), len(set(actual_result)))  # all integers in the result array are unique
        self.assertEqual(sum(actual_result), 0)  # sum of all integers in the result array is equal to zero

    def testTeslaInterviewCodilityTasksArrayOfUniqueIntegersWithZeroSum9(self):
        given_integer = 9
        actual_result = CodilityTasks().array_of_unique_integers_with_zero_sum(given_integer)
        self.assertEqual(len(actual_result), given_integer)  # length of the result array is equal to the given integer
        self.assertEqual(len(actual_result), len(set(actual_result)))  # all integers in the result array are unique
        self.assertEqual(sum(actual_result), 0)  # sum of all integers in the result array is equal to zero

    def testTeslaInterviewCodilityTasksArrayOfUniqueIntegersWithZeroSum10(self):
        given_integer = 10
        actual_result = CodilityTasks().array_of_unique_integers_with_zero_sum(given_integer)
        self.assertEqual(len(actual_result), given_integer)  # length of the result array is equal to the given integer
        self.assertEqual(len(actual_result), len(set(actual_result)))  # all integers in the result array are unique
        self.assertEqual(sum(actual_result), 0)  # sum of all integers in the result array is equal to zero

    def testTeslaInterviewCodilityTasksArrayOfUniqueIntegersWithZeroSum999(self):
        given_integer = 999
        actual_result = CodilityTasks().array_of_unique_integers_with_zero_sum(given_integer)
        self.assertEqual(len(actual_result), given_integer)  # length of the result array is equal to the given integer
        self.assertEqual(len(actual_result), len(set(actual_result)))  # all integers in the result array are unique
        self.assertEqual(sum(actual_result), 0)  # sum of all integers in the result array is equal to zero

    def testTeslaInterviewCodilityTasksArrayOfUniqueIntegersWithZeroSum1000(self):
        given_integer = 1000
        actual_result = CodilityTasks().array_of_unique_integers_with_zero_sum(given_integer)
        self.assertEqual(len(actual_result), given_integer)  # length of the result array is equal to the given integer
        self.assertEqual(len(actual_result), len(set(actual_result)))  # all integers in the result array are unique
        self.assertEqual(sum(actual_result), 0)  # sum of all integers in the result array is equal to zero


class TeslaInterviewCodilityTasksGetSuccessRateTest(unittest.TestCase):

    def testTeslaInterviewCodilityTasksGetSuccessRate1(self):
        tests_array = ["codility1", "codility3", "codility2", "codility4b", "codility4a"]
        results_array = ["Wrong answer", "OK", "OK", "Runtime error", "OK"]
        expected_result = 50
        actual_result = CodilityTasks().get_success_rate(tests_array, results_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksGetSuccessRate2(self):
        tests_array = ["test1a", "test2", "test1b", "test1c", "test3"]
        results_array = ["Wrong answer", "OK", "Runtime error", "OK", "Time limit exceeded"]
        expected_result = 33
        actual_result = CodilityTasks().get_success_rate(tests_array, results_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksGetSuccessRate3(self):
        tests_array = ["test1c", "test2a", "test1a", "test2b", "test3", "test4b", "test1b", "test6", "test5", "test4a"]
        results_array = ["Wrong answer", "OK", "Runtime error", "OK", "Time limit exceeded", "OK", "Runtime error",
                         "OK", "Time limit exceeded", "OK"]
        expected_result = 50
        actual_result = CodilityTasks().get_success_rate(tests_array, results_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksGetSuccessRate4(self):
        tests_array = ["test1b", "test2", "test1a"]
        results_array = ["Time limit exceeded", "Runtime error", "OK"]
        expected_result = 0
        actual_result = CodilityTasks().get_success_rate(tests_array, results_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksGetSuccessRate5(self):
        tests_array = ["test1b", "test2a", "test1a", "test2b", "test3"]
        results_array = ["OK", "OK", "OK", "Wrong answer", "OK"]
        expected_result = 66
        actual_result = CodilityTasks().get_success_rate(tests_array, results_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksGetSuccessRate6(self):
        tests_array = ["test1b", "test2", "test1a"]
        results_array = ["OK", "OK", "OK"]
        expected_result = 100
        actual_result = CodilityTasks().get_success_rate(tests_array, results_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksGetSuccessRate7(self):
        tests_array = ["test1"]
        results_array = ["OK"]
        expected_result = 100
        actual_result = CodilityTasks().get_success_rate(tests_array, results_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksGetSuccessRate8(self):
        tests_array = ["test1"]
        results_array = ["Runtime error"]
        expected_result = 0
        actual_result = CodilityTasks().get_success_rate(tests_array, results_array)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
