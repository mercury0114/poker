from sys import path
path[0] = "../../"

from unittest import main
from unittest import TestCase

from cards.evaluator import read_evaluation_table
from cards.evaluator import rank_players


class Unit(TestCase):
    def test1(self):
        table = read_evaluation_table()
        board = ["Qd", "As", "Qs", "Qh", "4s"]
        players = [["Ks", "5d"], ["Kd", "5c"], ["2s", "3s"]]
        ranks = rank_players(board, players, table)
        self.assertEqual(ranks, [1, 1, 0])

    def test2(self):
        table = read_evaluation_table()
        board = ["Qd", "As", "Qs", "Qh", "4s"]
        players = [["Ks", "5d"], ["Kd", "5c"], ["2c", "3h"], ["2s", "3s"]]
        ranks = rank_players(board, players, table)
        self.assertEqual(ranks, [1, 1, 3, 0])

    def test3(self):
        table = read_evaluation_table()
        board = ["2s", "3s", "4s", "5s", "6s"]
        players = [["Ah, Ad"], ["Kh, Kd"], ["Qh, Qd"]]
        ranks = rank_players(board, players, table)
        self.assertEqual(ranks, [0, 0, 0])


main()
