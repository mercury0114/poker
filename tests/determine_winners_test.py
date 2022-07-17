from sys import path
path.append("../")

from unittest import main
from unittest import TestCase

from evaluator import read_evaluation_table
from utils import determine_winners


class Unit(TestCase):
    def test1(self):
        evaluation_table = read_evaluation_table()
        board = ["Qd", "As", "Qs", "Qh", "4c"]
        player0 = ["Ks", "5s"]
        player1 = ["Jc", "6s"]
        players_cards = [player0, player1]
        winners = determine_winners(board, players_cards, evaluation_table)
        self.assertEqual(winners, [0])


if __name__ == '__main__':
    main()
