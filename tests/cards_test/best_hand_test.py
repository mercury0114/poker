from unittest import main
from unittest import TestCase

from cards.evaluator import best_evaluation
from cards.evaluator import best_evaluation_with_table
from cards.evaluator import read_evaluation_table


class Unit(TestCase):
    def test1(self):
        board = ["Qd", "As", "Qs", "Qh", "4c"]
        player = ["Ks", "5s"]
        evaluation = best_evaluation(board, player)
        self.assertEqual(evaluation, (3, (10, 10, 10, 12, 11)))

    def test2(self):
        table = read_evaluation_table()
        board = ["Qd", "As", "Qs", "Qh", "4s"]
        trips1 = best_evaluation_with_table(board, ["Ks", "5d"], table)
        trips2 = best_evaluation_with_table(board, ["Kd", "5c"], table)
        self.assertEqual(trips1, trips2)
        flush = best_evaluation_with_table(board, ["Ks", "5s"], table)
        self.assertLess(trips1, flush)


main()
