import unittest
from Tasks.AlgoExpertTasks.BinarySearch import binary_search, recursive_binary_search


class BinarySearchTest(unittest.TestCase):

    def testBinarySearch(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 33
        expected_result = 3
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch2(self):
        array = [1, 5, 23, 111]
        target = 111
        expected_result = 3
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch3(self):
        array = [1, 5, 23, 111]
        target = 5
        expected_result = 1
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch4(self):
        array = [1, 5, 23, 111]
        target = 35
        expected_result = -1
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch5(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 0
        expected_result = 0
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch6(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 1
        expected_result = 1
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch7(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 21
        expected_result = 2
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch8(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 45
        expected_result = 4
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch9(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 61
        expected_result = 6
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch10(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 71
        expected_result = 7
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch11(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 72
        expected_result = 8
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch12(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 73
        expected_result = 9
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch13(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 70
        expected_result = -1
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch14(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
        target = 355
        expected_result = 10
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch15(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
        target = 354
        expected_result = -1
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch16(self):
        array = [1, 5, 23, 111]
        target = 120
        expected_result = -1
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testBinarySearch17(self):
        array = [5, 23, 111]
        target = 3
        expected_result = -1
        actual_result = binary_search(array, target)
        self.assertEqual(actual_result, expected_result)


class RecursiveBinarySearchTest(unittest.TestCase):

    def testRecursiveBinarySearch(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 33
        expected_result = 3
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch2(self):
        array = [1, 5, 23, 111]
        target = 111
        expected_result = 3
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch3(self):
        array = [1, 5, 23, 111]
        target = 5
        expected_result = 1
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch4(self):
        array = [1, 5, 23, 111]
        target = 35
        expected_result = -1
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch5(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 0
        expected_result = 0
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch6(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 1
        expected_result = 1
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch7(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 21
        expected_result = 2
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch8(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 45
        expected_result = 4
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch9(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 61
        expected_result = 6
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch10(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 71
        expected_result = 7
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch11(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 72
        expected_result = 8
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch12(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 73
        expected_result = 9
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch13(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 70
        expected_result = -1
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch14(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
        target = 355
        expected_result = 10
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch15(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
        target = 354
        expected_result = -1
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch16(self):
        array = [1, 5, 23, 111]
        target = 120
        expected_result = -1
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)

    def testRecursiveBinarySearch17(self):
        array = [5, 23, 111]
        target = 3
        expected_result = -1
        actual_result = recursive_binary_search(array, target)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
