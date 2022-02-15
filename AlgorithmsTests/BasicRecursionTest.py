import unittest
from Algorithms.BasicRecursion import BasicRecursion


class IterativeFibonacciTest(unittest.TestCase):

    def testFibo9(self):
        given_number = 9
        expected_result = 34
        actual_result = BasicRecursion().iterative_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo50(self):
        given_number = 100
        expected_result = 354224848179261915075
        actual_result = BasicRecursion().iterative_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo3(self):
        given_number = 3
        expected_result = 2
        actual_result = BasicRecursion().iterative_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo2(self):
        given_number = 2
        expected_result = 1
        actual_result = BasicRecursion().iterative_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo1(self):
        given_number = 1
        expected_result = 1
        actual_result = BasicRecursion().iterative_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo0(self):
        given_number = 0
        expected_result = "Invalid index in fibonacci sequence"
        actual_result = BasicRecursion().iterative_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFiboMinusOne(self):
        given_number = -1
        expected_result = "Invalid index in fibonacci sequence"
        actual_result = BasicRecursion().iterative_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)


class RecursiveFibonacciTest(unittest.TestCase):

    def testFibo9(self):
        given_number = 9
        expected_result = 34
        actual_result = BasicRecursion().recursive_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo35(self):
        given_number = 35
        expected_result = 9227465
        actual_result = BasicRecursion().recursive_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo3(self):
        given_number = 3
        expected_result = 2
        actual_result = BasicRecursion().recursive_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo2(self):
        given_number = 2
        expected_result = 1
        actual_result = BasicRecursion().recursive_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo1(self):
        given_number = 1
        expected_result = 1
        actual_result = BasicRecursion().recursive_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo0(self):
        given_number = 0
        expected_result = "Invalid index in fibonacci sequence"
        actual_result = BasicRecursion().recursive_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFiboMinusOne(self):
        given_number = -1
        expected_result = "Invalid index in fibonacci sequence"
        actual_result = BasicRecursion().recursive_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)


class MemoizationFibonacciTest(unittest.TestCase):

    def testFibo9(self):
        given_number = 9
        expected_result = 34
        actual_result = BasicRecursion().memoization_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo100(self):
        given_number = 100
        expected_result = 354224848179261915075
        actual_result = BasicRecursion().memoization_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo3(self):
        given_number = 3
        expected_result = 2
        actual_result = BasicRecursion().memoization_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo2(self):
        given_number = 2
        expected_result = 1
        actual_result = BasicRecursion().memoization_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo1(self):
        given_number = 1
        expected_result = 1
        actual_result = BasicRecursion().memoization_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFibo0(self):
        given_number = 0
        expected_result = "Invalid index in fibonacci sequence"
        actual_result = BasicRecursion().memoization_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFiboMinusOne(self):
        given_number = -1
        expected_result = "Invalid index in fibonacci sequence"
        actual_result = BasicRecursion().memoization_fibonacci(given_number)
        self.assertEqual(expected_result, actual_result)


class FactorialTest(unittest.TestCase):

    def testFactorial9(self):
        given_number = 5
        expected_result = 120
        actual_result = BasicRecursion().factorial(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFactorial35(self):
        given_number = 50
        expected_result = 30414093201713378043612608166064768844377641568960512000000000000
        actual_result = BasicRecursion().factorial(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFactorial3(self):
        given_number = 3
        expected_result = 6
        actual_result = BasicRecursion().factorial(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFactorial2(self):
        given_number = 2
        expected_result = 2
        actual_result = BasicRecursion().factorial(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFactorial1(self):
        given_number = 1
        expected_result = 1
        actual_result = BasicRecursion().factorial(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFactorial0(self):
        given_number = 0
        expected_result = "Invalid input for factorial"
        actual_result = BasicRecursion().factorial(given_number)
        self.assertEqual(expected_result, actual_result)

    def testFactorialMinusOne(self):
        given_number = -1
        expected_result = "Invalid input for factorial"
        actual_result = BasicRecursion().factorial(given_number)
        self.assertEqual(expected_result, actual_result)


class SumOfDigitsTest(unittest.TestCase):

    def testSumOfDigits30414(self):
        given_number = 30414
        expected_result = 12
        actual_result = BasicRecursion().sum_of_digits(given_number)
        self.assertEqual(expected_result, actual_result)

    def testSumOfDigitsMany(self):
        given_number = 234567808765432
        expected_result = 70
        actual_result = BasicRecursion().sum_of_digits(given_number)
        self.assertEqual(expected_result, actual_result)

    def testSumOfDigits11(self):
        given_number = 11
        expected_result = 2
        actual_result = BasicRecursion().sum_of_digits(given_number)
        self.assertEqual(expected_result, actual_result)

    def testSumOfDigits10(self):
        given_number = 10
        expected_result = 1
        actual_result = BasicRecursion().sum_of_digits(given_number)
        self.assertEqual(expected_result, actual_result)

    def testSumOfDigits9(self):
        given_number = 9
        expected_result = 9
        actual_result = BasicRecursion().sum_of_digits(given_number)
        self.assertEqual(expected_result, actual_result)

    def testSumOfDigits2(self):
        given_number = 2
        expected_result = 2
        actual_result = BasicRecursion().sum_of_digits(given_number)
        self.assertEqual(expected_result, actual_result)

    def testSumOfDigits1(self):
        given_number = 1
        expected_result = 1
        actual_result = BasicRecursion().sum_of_digits(given_number)
        self.assertEqual(expected_result, actual_result)

    def testSumOfDigits0(self):
        given_number = 0
        expected_result = "Invalid input for adding digits"
        actual_result = BasicRecursion().sum_of_digits(given_number)
        self.assertEqual(expected_result, actual_result)

    def testSumOfDigitsMinusOne(self):
        given_number = -1
        expected_result = "Invalid input for adding digits"
        actual_result = BasicRecursion().sum_of_digits(given_number)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
