from sys import path
path[0] = "../"

from unittest import main
from unittest import TestCase

from cards.evaluator import determine_winners
from cards.evaluator import read_evaluation_table


class Unit(TestCase):
    def test1(self):
        evaluation_table = read_evaluation_table()
        board = ["Qd", "As", "Qs", "Qh", "4c"]
        player0 = ["Ks", "5s"]
        player1 = ["Jc", "6s"]
        players_cards = [player0, player1]
        winners = determine_winners(board, players_cards, evaluation_table)
        self.assertEqual(winners, [0])

    def test2(self):
        evaluation_table = read_evaluation_table()
        board = ['Ks', 'As', '3h', '3c', '7h']
        player0 = ['4d', 'Qh']
        player1 = ['9c', '5s']
        player2 = ['5c', '6s']
        players_cards = [player0, player1, player2]
        winners = determine_winners(board, players_cards, evaluation_table)
        self.assertEqual(winners, [0])

    def test3(self):
        evaluation_table = read_evaluation_table()
        board = ['2c', '5d', '5c', '3h', '3c']
        player0 = ['9c', '4h']
        player1 = ['Th', 'Jd']
        players_cards = [player0, player1]
        winners = determine_winners(board, players_cards, evaluation_table)
        self.assertEqual(winners, [1])

    def test4(self):
        evaluation_table = read_evaluation_table()
        board = ['Th', '4h', '7s', '4c', 'Ah']
        player0 = ['5s', '9s']
        player1 = ['8s', 'Td']
        players_cards = [player0, player1]
        winners = determine_winners(board, players_cards, evaluation_table)
        self.assertEqual(winners, [1])

    def test5(self):
        evaluation_table = read_evaluation_table()
        board = ['2s', '5c', '6c', '3h', 'Js']
        player0 = ['Qh', '4h']
        player1 = ['4d', '5d']
        players_cards = [player0, player1]
        winners = determine_winners(board, players_cards, evaluation_table)
        self.assertEqual(winners, [0, 1])


if __name__ == '__main__':
    main()
