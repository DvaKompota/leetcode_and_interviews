import unittest
from Tasks.AlgoExpertTasks.NonConstructibleChange import non_constructible_change


class NonConstructibleChangeTest(unittest.TestCase):

    def testTournamentWinnerPython(self):
        coins = [5, 7, 1, 1, 2, 3, 22]
        expected_result = 20
        actual_result = non_constructible_change(coins)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
