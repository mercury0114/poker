from sys import path
path[0] = "../../../"

from unittest import main
from unittest import TestCase

from cards.evaluator import read_evaluation_table
from casino.hand import play_hand_return_wins
from players.donkeys import AllInPlayer
from players.donkeys import FoldPlayer
from utils.stack import FULL_STACK


class Unit(TestCase):
    def test1(self):
        players = [AllInPlayer('p0'), AllInPlayer('p1'), FoldPlayer('p2')]
        stacks = [300, 300, FULL_STACK]
        evaluation_table = read_evaluation_table()
        wins = play_hand_return_wins(players, stacks, evaluation_table)
        assert wins[0] in [300, -300, 0], f"wrong wins[0]:{wins[0]}"
        assert wins[1] in [300, -300, 0], f"wrong wins[1]:{wins[1]}"
        self.assertEqual(wins[2], 0)

    def test2(self):
        players = [AllInPlayer('p0'), AllInPlayer('p1'), FoldPlayer('p3')]
        stacks = [300, 50, FULL_STACK]
        evaluation_table = read_evaluation_table()
        wins = play_hand_return_wins(players, stacks, evaluation_table)
        assert wins[0] in [50, -50, 0], f"wrong wins[0]:{wins[0]}"
        assert wins[1] in [50, -50, 0], f"wrong wins[1]:{wins[1]}"
        self.assertEqual(wins[2], 0)

    def test3(self):
        players = [AllInPlayer('p0'), AllInPlayer('p1'), AllInPlayer('p2')]
        stacks = [10, 40, 160]
        evaluation_table = read_evaluation_table()
        wins = play_hand_return_wins(players, stacks, evaluation_table)
        assert wins[0] in [20, 5, 0, -10], f"wrong wins[0]:{wins[0]}"
        assert wins[1] in [50, 35, 20, 5, 0, -40], f"wrong wins[1]:{wins[1]}"
        assert wins[2] in [50, 35, 20, 5, 0, -40], f"wrong wins[2]:{wins[2]}"
        self.assertEqual(wins[0] + wins[1] + wins[2], 0)


main()
