import unittest
from Algorithms.IntegerPalindrome import IntegerPalindromeFirstDraft
from Algorithms.IntegerPalindrome import IntegerPalindrome


class IntegerPalindromeFirstDraftTest(unittest.TestCase):

    def testIntegerPalindrome(self):
        actual_result = IntegerPalindromeFirstDraft().is_palindrome(12345654321)
        self.assertEqual(actual_result, True)

    def testEvenIntegerPalindrome(self):
        actual_result = IntegerPalindromeFirstDraft().is_palindrome(1234554321)
        self.assertEqual(actual_result, True)

    def testZeroIntegerPalindrome(self):
        actual_result = IntegerPalindromeFirstDraft().is_palindrome(0)
        self.assertEqual(actual_result, True)

    def testOneIntegerPalindrome(self):
        actual_result = IntegerPalindromeFirstDraft().is_palindrome(1)
        self.assertEqual(actual_result, True)

    def testEmptyIntegerPalindrome(self):
        actual_result = IntegerPalindromeFirstDraft().is_palindrome()
        self.assertEqual(actual_result, False)

    def testNoneIntegerPalindrome(self):
        actual_result = IntegerPalindromeFirstDraft().is_palindrome(None)
        self.assertEqual(actual_result, False)

    def testNegativeIntegerPalindrome(self):
        actual_result = IntegerPalindromeFirstDraft().is_palindrome(-1)
        self.assertEqual(actual_result, False)

    def testFalseIntegerPalindrome(self):
        actual_result = IntegerPalindromeFirstDraft().is_palindrome(1234)
        self.assertEqual(actual_result, False)


class IntegerPalindromeTest(unittest.TestCase):

    def testIntegerPalindrome(self):
        actual_result = IntegerPalindrome().is_palindrome(12345654321)
        self.assertEqual(actual_result, True)

    def testEvenIntegerPalindrome(self):
        actual_result = IntegerPalindrome().is_palindrome(1234554321)
        self.assertEqual(actual_result, True)

    def testZeroIntegerPalindrome(self):
        actual_result = IntegerPalindrome().is_palindrome(0)
        self.assertEqual(actual_result, True)

    def testOneIntegerPalindrome(self):
        actual_result = IntegerPalindrome().is_palindrome(1)
        self.assertEqual(actual_result, True)

    def testNegativeIntegerPalindrome(self):
        actual_result = IntegerPalindrome().is_palindrome(-1)
        self.assertEqual(actual_result, False)

    def testFalseIntegerPalindrome(self):
        actual_result = IntegerPalindrome().is_palindrome(1234)
        self.assertEqual(actual_result, False)


if __name__ == '__main__':
    unittest.main()
