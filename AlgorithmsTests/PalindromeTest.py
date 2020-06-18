import unittest
from Algorithms.Palindrome import Palindrome


class PalindromeTest(unittest.TestCase):

    def testPalindrome(self):
        given_string = "racecar"
        expected_result = True
        actual_result = Palindrome().is_palindrome(given_string)
        self.assertEqual(expected_result, actual_result)

    def testEvenPalindrome(self):
        given_string = "raccar"
        expected_result = True
        actual_result = Palindrome().is_palindrome(given_string)
        self.assertEqual(expected_result, actual_result)

    def testEmptyPalindrome(self):
        given_string = ""
        expected_result = "The string is empty!"
        actual_result = Palindrome().is_palindrome(given_string)
        self.assertEqual(expected_result, actual_result)

    def testOnePalindrome(self):
        given_string = "r"
        expected_result = True
        actual_result = Palindrome().is_palindrome(given_string)
        self.assertEqual(expected_result, actual_result)

    def testFalsePalindrome(self):
        given_string = "racear"
        expected_result = False
        actual_result = Palindrome().is_palindrome(given_string)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
