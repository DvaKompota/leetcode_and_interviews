import unittest
from Tasks.AlgoExpertTasks.ValidateSubsequence import is_valid_subsequence


class ValidateSubsequenceTest(unittest.TestCase):

    def testValidateSubsequence(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        expected_result = True
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceFullMatch(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 25, 6, -1, 8, 10]
        expected_result = True
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceMissingOne(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 6, -1, 8, 10]
        expected_result = True
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceMiddle(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [22, 25, 6]
        expected_result = True
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpread(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, 10]
        expected_result = True
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceEndSeparate(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 10]
        expected_result = True
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceStartSeparate(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, -1, 8, 10]
        expected_result = True
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceOneItem(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [25]
        expected_result = True
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceAllOnes(self):
        array = [1, 1, 1, 1, 1]
        sequence = [1, 1, 1]
        expected_result = True
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpareEnd(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 25, 6, -1, 8, 10, 12]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpareStart(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [4, 5, 1, 22, 25, 6, -1, 8, 10]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpareMiddle(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 23, 6, -1, 8, 10]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpareDuplicate(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 22, 25, 6, -1, 8, 10]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpareDuplicateMissingOne(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 22, 6, -1, 8, 10]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpareDuplicateEnd(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, -1]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpareDuplicateMiddle(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, -1, 10]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpareEndNegative(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, -2]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceOneOut(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [26]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceWrongOrderMiddle(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 25, 22, 6, -1, 8, 10]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceSpareMiddleShort(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 26, 22, 8]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceWrongOrderWithDuplicates(self):
        array = [1, 1, 6, 1]
        sequence = [1, 1, 1, 6]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceAllOfWithDuplicates(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10, 11, 11, 11, 11]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceOneDuplicateEnd(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 25, 6, -1, 8, 10, 10]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)

    def testValidateSubsequenceWrongOrderEnd(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 5]
        expected_result = False
        actual_result = is_valid_subsequence(array, sequence)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
