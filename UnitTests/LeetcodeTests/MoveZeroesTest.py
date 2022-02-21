import unittest
from Tasks.LeetcodeTasks.MoveZeroes import MoveZeroes


class MoveZeroesTest(unittest.TestCase):

    def testMoveZeroes(self):
        given_array = [0, 1, 0, 3, 12]
        expected_array = [1, 3, 12, 0, 0]
        MoveZeroes().moveZeroes(given_array)
        self.assertEqual(given_array, expected_array)

    def testMoveZeroesMoved(self):
        given_array = [1, 3, 12, 0, 0]
        expected_array = [1, 3, 12, 0, 0]
        MoveZeroes().moveZeroes(given_array)
        self.assertEqual(given_array, expected_array)

    def testMoveZeroesOnlyOne(self):
        given_array = [1]
        expected_array = [1]
        MoveZeroes().moveZeroes(given_array)
        self.assertEqual(given_array, expected_array)

    def testMoveZeroesOnlyZero(self):
        given_array = [0]
        expected_array = [0]
        MoveZeroes().moveZeroes(given_array)
        self.assertEqual(given_array, expected_array)

    def testMoveZeroesNoZeroes(self):
        given_array = [6, 1, 22, 3]
        expected_array = [6, 1, 22, 3]
        MoveZeroes().moveZeroes(given_array)
        self.assertEqual(given_array, expected_array)

    def testMoveZeroesOnlyZeroes(self):
        given_array = [0, 0, 0]
        expected_array = [0, 0, 0]
        MoveZeroes().moveZeroes(given_array)
        self.assertEqual(given_array, expected_array)


if __name__ == '__main__':
    unittest.main()
