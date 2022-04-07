import unittest
from Tasks.AlgoExpertTasks.TournamentWinner import tournament_winner


class TournamentWinnerTest(unittest.TestCase):

    def testTournamentWinnerPython(self):
        competitions = [
            ["HTML", "C#"],
            ["C#", "Python"],
            ["Python", "HTML"]
        ]
        results = [0, 0, 1]
        expected_result = "Python"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)

    def testTournamentWinnerJava(self):
        competitions = [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"]
        ]
        results = [0, 1, 1]
        expected_result = "Java"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)

    def testTournamentWinnerC(self):
        competitions = [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"]
        ]
        results = [0, 1, 1, 1, 0, 1]
        expected_result = "C#"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)

    def testTournamentWinnerC2(self):
        competitions = [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"],
            ["SQL", "C#"],
            ["HTML", "SQL"],
            ["SQL", "Python"],
            ["SQL", "Java"]
        ]
        results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
        expected_result = "C#"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)

    def testTournamentWinnerBulls(self):
        competitions = [
            ["Bulls", "Eagles"]
        ]
        results = [1]
        expected_result = "Bulls"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)

    def testTournamentWinnerEagles(self):
        competitions = [
            ["Bulls", "Eagles"],
            ["Bulls", "Bears"],
            ["Bears", "Eagles"]
        ]
        results = [0, 0, 0]
        expected_result = "Eagles"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)

    def testTournamentWinnerBulls2(self):
        competitions = [
            ["Bulls", "Eagles"],
            ["Bulls", "Bears"],
            ["Bulls", "Monkeys"],
            ["Eagles", "Bears"],
            ["Eagles", "Monkeys"],
            ["Bears", "Monkeys"]
        ]
        results = [1, 1, 1, 1, 1, 1]
        expected_result = "Bulls"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)

    def testTournamentWinnerAlgoMasters(self):
        competitions = [
            ["AlgoMasters", "FrontPage Freebirds"],
            ["Runtime Terror", "Static Startup"],
            ["WeC#", "Hypertext Assassins"],
            ["AlgoMasters", "WeC#"],
            ["Static Startup", "Hypertext Assassins"],
            ["Runtime Terror", "FrontPage Freebirds"],
            ["AlgoMasters", "Runtime Terror"],
            ["Hypertext Assassins", "FrontPage Freebirds"],
            ["Static Startup", "WeC#"],
            ["AlgoMasters", "Static Startup"],
            ["FrontPage Freebirds", "WeC#"],
            ["Hypertext Assassins", "Runtime Terror"],
            ["AlgoMasters", "Hypertext Assassins"],
            ["WeC#", "Runtime Terror"],
            ["FrontPage Freebirds", "Static Startup"]
        ]
        results = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
        expected_result = "AlgoMasters"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)

    def testTournamentWinnerSQL(self):
        competitions = [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"],
            ["SQL", "C#"],
            ["HTML", "SQL"],
            ["SQL", "Python"],
            ["SQL", "Java"]
        ]
        results = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
        expected_result = "SQL"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)

    def testTournamentWinnerB(self):
        competitions = [
            ["A", "B"]
        ]
        results = [0]
        expected_result = "B"
        actual_result = tournament_winner(competitions, results)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
