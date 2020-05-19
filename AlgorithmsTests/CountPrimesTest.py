import unittest
from Algorithms.CountPrimes import CountPrimesBruteForce
from Algorithms.CountPrimes import CountPrimes


class CountPrimesBruteForceTest(unittest.TestCase):

    def testCountPrimesBruteForce10(self):
        actual_result = CountPrimesBruteForce().countPrimes(10)
        self.assertEqual(actual_result, 4)

    def testCountPrimesBruteForce0(self):
        actual_result = CountPrimesBruteForce().countPrimes(0)
        self.assertEqual(actual_result, 0)

    def testCountPrimesBruteForce1(self):
        actual_result = CountPrimesBruteForce().countPrimes(1)
        self.assertEqual(actual_result, 0)

    def testCountPrimesBruteForce2(self):
        actual_result = CountPrimesBruteForce().countPrimes(2)
        self.assertEqual(actual_result, 0)

    def testCountPrimesBruteForce3(self):
        actual_result = CountPrimesBruteForce().countPrimes(3)
        self.assertEqual(actual_result, 1)

    def testCountPrimesBruteForce100(self):
        actual_result = CountPrimesBruteForce().countPrimes(100)
        self.assertEqual(actual_result, 25)


class CountPrimesTest(unittest.TestCase):

    def testCountPrimes10(self):
        actual_result = CountPrimes().countPrimes(10)
        self.assertEqual(actual_result, 4)

    def testCountPrimes0(self):
        actual_result = CountPrimes().countPrimes(0)
        self.assertEqual(actual_result, 0)

    def testCountPrimes1(self):
        actual_result = CountPrimes().countPrimes(1)
        self.assertEqual(actual_result, 0)

    def testCountPrimes2(self):
        actual_result = CountPrimes().countPrimes(2)
        self.assertEqual(actual_result, 0)

    def testCountPrimes3(self):
        actual_result = CountPrimes().countPrimes(3)
        self.assertEqual(actual_result, 1)

    def testCountPrimes11(self):
        actual_result = CountPrimes().countPrimes(11)
        self.assertEqual(actual_result, 4)

    def testCountPrimes12(self):
        actual_result = CountPrimes().countPrimes(12)
        self.assertEqual(actual_result, 5)

    def testCountPrimes100(self):
        actual_result = CountPrimes().countPrimes(100)
        self.assertEqual(actual_result, 25)

