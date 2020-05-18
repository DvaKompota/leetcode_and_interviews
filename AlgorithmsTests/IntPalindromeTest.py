import unittest
from Algorithms.IntPalindrome import IntPalindromeFirstDraft
from Algorithms.IntPalindrome import IntPalindrome


class IntPalindromeFirstDraftTest(unittest.TestCase):

    def testIntPalindrome(self):
        actual_result = IntPalindromeFirstDraft().is_palindrome(12345654321)
        self.assertEqual(actual_result, True)

    def testEvenIntPalindrome(self):
        actual_result = IntPalindromeFirstDraft().is_palindrome(1234554321)
        self.assertEqual(actual_result, True)

    def testZeroIntPalindrome(self):
        actual_result = IntPalindromeFirstDraft().is_palindrome(0)
        self.assertEqual(actual_result, True)

    def testOneIntPalindrome(self):
        actual_result = IntPalindromeFirstDraft().is_palindrome(1)
        self.assertEqual(actual_result, True)

    def testEmptyIntPalindrome(self):
        actual_result = IntPalindromeFirstDraft().is_palindrome()
        self.assertEqual(actual_result, False)

    def testNoneIntPalindrome(self):
        actual_result = IntPalindromeFirstDraft().is_palindrome(None)
        self.assertEqual(actual_result, False)

    def testNegativeIntPalindrome(self):
        actual_result = IntPalindromeFirstDraft().is_palindrome(-1)
        self.assertEqual(actual_result, False)

    def testFalseIntPalindrome(self):
        actual_result = IntPalindromeFirstDraft().is_palindrome(1234)
        self.assertEqual(actual_result, False)


class IntPalindromeTest(unittest.TestCase):

    def testIntPalindrome(self):
        actual_result = IntPalindrome().isPalindrome(12345654321)
        self.assertEqual(actual_result, True)

    def testEvenIntPalindrome(self):
        actual_result = IntPalindrome().isPalindrome(1234554321)
        self.assertEqual(actual_result, True)

    def testZeroIntPalindrome(self):
        actual_result = IntPalindrome().isPalindrome(0)
        self.assertEqual(actual_result, True)

    def testOneIntPalindrome(self):
        actual_result = IntPalindrome().isPalindrome(1)
        self.assertEqual(actual_result, True)

    def testNegativeIntPalindrome(self):
        actual_result = IntPalindrome().isPalindrome(-1)
        self.assertEqual(actual_result, False)

    def testFalseIntPalindrome(self):
        actual_result = IntPalindrome().isPalindrome(1234)
        self.assertEqual(actual_result, False)


if __name__ == '__main__':
    unittest.main()
