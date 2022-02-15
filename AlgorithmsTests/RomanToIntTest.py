import unittest
from Algorithms.RomanToInt import RomanToInt


class RomanToIntTest(unittest.TestCase):

    def testRomanToIntTest3(self):
        given_string = 'III'
        expected_result = 3
        actual_result = RomanToInt().roman_to_int(given_string)
        self.assertEqual(expected_result, actual_result)

    def testRomanToIntTest58(self):
        given_string = 'LVIII'
        expected_result = 58
        actual_result = RomanToInt().roman_to_int(given_string)
        self.assertEqual(expected_result, actual_result)

    def testRomanToIntTest1994(self):
        given_string = 'MCMXCIV'
        expected_result = 1994
        actual_result = RomanToInt().roman_to_int(given_string)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
