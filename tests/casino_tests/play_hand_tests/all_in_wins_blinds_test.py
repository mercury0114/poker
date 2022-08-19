from sys import path
path[0] = "../../../"

from unittest import TestCase
from unittest import main

from cards.evaluator import read_evaluation_table
from casino.hand import play_hand_return_wins
from players.donkeys import AllInPlayer
from players.donkeys import FoldPlayer
from utils.stack import full_stack_for_all


class Unit(TestCase):
    def test1(self):
        evaluation_table = read_evaluation_table()
        all_in_player = AllInPlayer('p0')
        fold_player = FoldPlayer('p1')
        players = [all_in_player, fold_player]
        stacks = full_stack_for_all(len(players))
        wins = play_hand_return_wins(players, stacks, evaluation_table)
        self.assertEqual(wins, [2, -2])

    def test2(self):
        evaluation_table = read_evaluation_table()
        all_in_player = AllInPlayer('p0')
        fold_player = FoldPlayer('p1')
        players = [fold_player, all_in_player]
        stacks = full_stack_for_all(len(players))
        wins = play_hand_return_wins(players, stacks, evaluation_table)
        self.assertEqual(wins, [-1, 1])


if __name__ == '__main__':
    main()
