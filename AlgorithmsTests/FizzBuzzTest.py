import unittest
from Algorithms.FizzBuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def testFizzBuzz(self):
        actual_result = FizzBuzz().fizzBuzz(16)
        self.assertEqual(actual_result, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11",
                                         "Fizz", "13", "14", "FizzBuzz", "16"])

    def testFizzBuzzOne(self):
        actual_result = FizzBuzz().fizzBuzz(1)
        self.assertEqual(actual_result, ["1"])

    def testFizzBuzzZero(self):
        actual_result = FizzBuzz().fizzBuzz(0)
        self.assertEqual(actual_result, 'Invalid input')

    def testFizzBuzzNegative(self):
        actual_result = FizzBuzz().fizzBuzz(-1)
        self.assertEqual(actual_result, 'Invalid input')

