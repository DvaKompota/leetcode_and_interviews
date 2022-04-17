import unittest
from Tasks.AlgoExpertTasks.IsPalindrome import is_palindrome


class IsPalindromeTest(unittest.TestCase):

    def testIsPalindrome(self):
        string = "abcdcba"
        expected_result = True
        actual_result = is_palindrome(string)
        self.assertEqual(actual_result, expected_result)

    def testIsPalindrome_a(self):
        string = "a"
        expected_result = True
        actual_result = is_palindrome(string)
        self.assertEqual(actual_result, expected_result)

    def testIsPalindrome_ab(self):
        string = "ab"
        expected_result = False
        actual_result = is_palindrome(string)
        self.assertEqual(actual_result, expected_result)

    def testIsPalindrome_aba(self):
        string = "aba"
        expected_result = True
        actual_result = is_palindrome(string)
        self.assertEqual(actual_result, expected_result)

    def testIsPalindrome_abb(self):
        string = "abb"
        expected_result = False
        actual_result = is_palindrome(string)
        self.assertEqual(actual_result, expected_result)

    def testIsPalindrome_abba(self):
        string = "abba"
        expected_result = True
        actual_result = is_palindrome(string)
        self.assertEqual(actual_result, expected_result)

    def testIsPalindrome_abcdefghhgfedcba(self):
        string = "abcdefghhgfedcba"
        expected_result = True
        actual_result = is_palindrome(string)
        self.assertEqual(actual_result, expected_result)

    def testIsPalindrome_abcdefghihgfedcba(self):
        string = "abcdefghihgfedcba"
        expected_result = True
        actual_result = is_palindrome(string)
        self.assertEqual(actual_result, expected_result)

    def testIsPalindrome_abcdefghihgfeddcba(self):
        string = "abcdefghihgfeddcba"
        expected_result = False
        actual_result = is_palindrome(string)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
