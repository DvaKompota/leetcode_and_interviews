import unittest
from Tasks.InterviewTasks.TeslaInterview2 import CodilityTasks, FirstInterviewTask


class TeslaInterviewCodilityTasksFirstMissingIntegerTest(unittest.TestCase):

    def testTeslaInterviewCodilityTasksFirstMissingInteger_1(self):
        given_array = [3, 4, -1, 1]
        expected_result = 2
        actual_result = CodilityTasks().first_missing_integer(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingInteger_2(self):
        given_array = [1, 2, 0]
        expected_result = 3
        actual_result = CodilityTasks().first_missing_integer(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingInteger_3(self):
        given_array = [1, 3, 6, 4, 1, 2]
        expected_result = 5
        actual_result = CodilityTasks().first_missing_integer(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingInteger_4(self):
        given_array = [1, 2, 3]
        expected_result = 4
        actual_result = CodilityTasks().first_missing_integer(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingInteger_5(self):
        given_array = [-1, -3]
        expected_result = 1
        actual_result = CodilityTasks().first_missing_integer(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingInteger_6(self):
        given_array = [7, 8, 9, 11, 12]
        expected_result = 1
        actual_result = CodilityTasks().first_missing_integer(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingInteger_7(self):
        given_array = [90353, -918308, -533754, 531479, 13995, 6752, 49775, -427473, -203440, -718891]
        expected_result = 1
        actual_result = CodilityTasks().first_missing_integer(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksFirstMissingInteger_8(self):
        given_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
        expected_result = 10
        actual_result = CodilityTasks().first_missing_integer(given_array)
        self.assertEqual(expected_result, actual_result)


class TeslaInterviewCodilityTasksIntegerMatchingOccurrences(unittest.TestCase):

    def testTeslaInterviewCodilityTasksIntegerMatchingOccurrences_1(self):
        given_array = []
        expected_result = 0
        actual_result = CodilityTasks().integer_matching_occurrences(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksIntegerMatchingOccurrences_2(self):
        given_array = [0]
        expected_result = 0
        actual_result = CodilityTasks().integer_matching_occurrences(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksIntegerMatchingOccurrences_3(self):
        given_array = [2]
        expected_result = 0
        actual_result = CodilityTasks().integer_matching_occurrences(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksIntegerMatchingOccurrences_4(self):
        given_array = [1]
        expected_result = 1
        actual_result = CodilityTasks().integer_matching_occurrences(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksIntegerMatchingOccurrences_5(self):
        given_array = [2, 1, 3, 2]
        expected_result = 2
        actual_result = CodilityTasks().integer_matching_occurrences(given_array)
        self.assertEqual(expected_result, actual_result)


class TeslaInterviewCodilityTasksReplaceQuestionMarks(unittest.TestCase):

    def testTeslaInterviewCodilityTasksReplaceQuestionMarks_1(self):
        given_string = ""
        expected_result = ""
        actual_result = CodilityTasks().replace_question_marks(given_string)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksReplaceQuestionMarks_2(self):
        given_string = "?"
        expected_result = "a"
        actual_result = CodilityTasks().replace_question_marks(given_string)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksReplaceQuestionMarks_3(self):
        given_string = "??"
        expected_result = "ab"
        actual_result = CodilityTasks().replace_question_marks(given_string)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksReplaceQuestionMarks_4(self):
        given_string = "a"
        expected_result = "a"
        actual_result = CodilityTasks().replace_question_marks(given_string)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksReplaceQuestionMarks_5(self):
        given_string = "ab"
        expected_result = "ab"
        actual_result = CodilityTasks().replace_question_marks(given_string)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksReplaceQuestionMarks_6(self):
        given_string = "aa"
        expected_result = "aa"
        actual_result = CodilityTasks().replace_question_marks(given_string)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksReplaceQuestionMarks_7(self):
        given_string = "a?b"
        expected_result = "acb"
        actual_result = CodilityTasks().replace_question_marks(given_string)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksReplaceQuestionMarks_8(self):
        given_string = "a?a"
        expected_result = "aba"
        actual_result = CodilityTasks().replace_question_marks(given_string)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksReplaceQuestionMarks_9(self):
        given_string = "a?b??c?cda??a?d"
        expected_result = "acbabcacdabcabd"
        actual_result = CodilityTasks().replace_question_marks(given_string)
        self.assertEqual(expected_result, actual_result)


class TeslaInterviewCodilityTasksSquareFromWoodenSticks(unittest.TestCase):

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_1(self):
        first_stick = 10
        second_stick = 21
        expected_result = 7
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_2(self):
        first_stick = 13
        second_stick = 11
        expected_result = 5
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_3(self):
        first_stick = 2
        second_stick = 1
        expected_result = 0
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_4(self):
        first_stick = 1
        second_stick = 8
        expected_result = 2
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_5(self):
        first_stick = 10
        second_stick = 10
        expected_result = 5
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_6(self):
        first_stick = 1_000_000_000
        second_stick = 1
        expected_result = 250_000_000
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_7(self):
        first_stick = 1
        second_stick = 1_000_000_000
        expected_result = 250_000_000
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_8(self):
        first_stick = 999_999_999
        second_stick = 999_999_999
        expected_result = 499_999_999
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_9(self):
        first_stick = 1_000_000_000
        second_stick = 333_333_333
        expected_result = 333_333_333
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_10(self):
        first_stick = 999_999_999
        second_stick = 333_333_333
        expected_result = 333_333_333
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewCodilityTasksSquareFromWoodenSticks_11(self):
        first_stick = 999_999_998
        second_stick = 333_333_333
        expected_result = 333_333_332
        actual_result = CodilityTasks().square_from_wooden_sticks(first_stick, second_stick)
        self.assertEqual(expected_result, actual_result)


class TeslaInterviewFirstInterviewTaskSecondLowestNumber(unittest.TestCase):

    def testTeslaInterviewFirstInterviewTaskSecondLowestNumber_1(self):
        given_array = [2, 1]
        expected_result = 2
        actual_result = FirstInterviewTask().second_lowest_number(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewFirstInterviewTaskSecondLowestNumber_2(self):
        given_array = [1, 2]
        expected_result = 2
        actual_result = FirstInterviewTask().second_lowest_number(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewFirstInterviewTaskSecondLowestNumber_3(self):
        given_array = [0, 0]
        expected_result = 0
        actual_result = FirstInterviewTask().second_lowest_number(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewFirstInterviewTaskSecondLowestNumber_4(self):
        given_array = [21, 1, 2, 5, 8]
        expected_result = 2
        actual_result = FirstInterviewTask().second_lowest_number(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewFirstInterviewTaskSecondLowestNumber_5(self):
        given_array = [2, 3, -4, 54, 0, 5]
        expected_result = 0
        actual_result = FirstInterviewTask().second_lowest_number(given_array)
        self.assertEqual(expected_result, actual_result)

    def testTeslaInterviewFirstInterviewTaskSecondLowestNumber_6(self):
        given_array = [2, 3, -4, 54, 0, -5]
        expected_result = -4
        actual_result = FirstInterviewTask().second_lowest_number(given_array)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
