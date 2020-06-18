import unittest
from Algorithms.MostRepeatedChar import MostRepeatedChar


class MostRepeatedCharTest(unittest.TestCase):

    def testMostRepeatedChar(self):
        given_string = 'qwewrty'
        expected_result = 'w'
        actual_result = MostRepeatedChar().most_repeated_char(given_string)
        self.assertEqual(expected_result, actual_result)

    def testMostRepeatedCharOne(self):
        given_string = 'q'
        expected_result = 'q'
        actual_result = MostRepeatedChar().most_repeated_char(given_string)
        self.assertEqual(expected_result, actual_result)

    def testMostRepeatedCharDigits(self):
        given_string = 'qwewrty123334'
        expected_result = '3'
        actual_result = MostRepeatedChar().most_repeated_char(given_string)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
