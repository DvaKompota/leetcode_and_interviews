import unittest
from Tasks.LeetcodeTasks.PrimeNumberQuantity import PrimeNumberQuantityBruteForce
from Tasks.LeetcodeTasks.PrimeNumberQuantity import PrimeNumberQuantity


class PrimeNumberQuantityBruteForceTest(unittest.TestCase):

    def testPrimeNumberQuantityBruteForce10(self):
        actual_result = PrimeNumberQuantityBruteForce().prime_number_quantity(10)
        self.assertEqual(actual_result, 4)

    def testPrimeNumberQuantityBruteForce0(self):
        actual_result = PrimeNumberQuantityBruteForce().prime_number_quantity(0)
        self.assertEqual(actual_result, 0)

    def testPrimeNumberQuantityBruteForce1(self):
        actual_result = PrimeNumberQuantityBruteForce().prime_number_quantity(1)
        self.assertEqual(actual_result, 0)

    def testPrimeNumberQuantityBruteForce2(self):
        actual_result = PrimeNumberQuantityBruteForce().prime_number_quantity(2)
        self.assertEqual(actual_result, 0)

    def testPrimeNumberQuantityBruteForce3(self):
        actual_result = PrimeNumberQuantityBruteForce().prime_number_quantity(3)
        self.assertEqual(actual_result, 1)

    def testPrimeNumberQuantityBruteForce100(self):
        actual_result = PrimeNumberQuantityBruteForce().prime_number_quantity(100)
        self.assertEqual(actual_result, 25)


class PrimeNumberQuantityTest(unittest.TestCase):

    def testPrimeNumberQuantity10(self):
        actual_result = PrimeNumberQuantity().prime_number_quantity(10)
        self.assertEqual(actual_result, 4)

    def testPrimeNumberQuantity0(self):
        actual_result = PrimeNumberQuantity().prime_number_quantity(0)
        self.assertEqual(actual_result, 0)

    def testPrimeNumberQuantity1(self):
        actual_result = PrimeNumberQuantity().prime_number_quantity(1)
        self.assertEqual(actual_result, 0)

    def testPrimeNumberQuantity2(self):
        actual_result = PrimeNumberQuantity().prime_number_quantity(2)
        self.assertEqual(actual_result, 0)

    def testPrimeNumberQuantity3(self):
        actual_result = PrimeNumberQuantity().prime_number_quantity(3)
        self.assertEqual(actual_result, 1)

    def testPrimeNumberQuantity11(self):
        actual_result = PrimeNumberQuantity().prime_number_quantity(11)
        self.assertEqual(actual_result, 4)

    def testPrimeNumberQuantity12(self):
        actual_result = PrimeNumberQuantity().prime_number_quantity(12)
        self.assertEqual(actual_result, 5)

    def testPrimeNumberQuantity100(self):
        actual_result = PrimeNumberQuantity().prime_number_quantity(100)
        self.assertEqual(actual_result, 25)


if __name__ == '__main__':
    unittest.main()
