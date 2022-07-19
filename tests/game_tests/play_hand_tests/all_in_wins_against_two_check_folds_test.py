from sys import path
path[0] = "../../../"

from unittest import main
from unittest import TestCase

from cards_dealer import deal_cards
from game import play_hand_return_remaining
from players.donkeys import AllInPlayer
from players.donkeys import FoldPlayer
from stack import full_stack_for_all


class Unit(TestCase):
    def test1(self):
        players = [FoldPlayer(), FoldPlayer(), AllInPlayer()]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [2])

    def test2(self):
        players = [FoldPlayer(), AllInPlayer(), FoldPlayer()]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [1])

    def test3(self):
        players = [AllInPlayer(), FoldPlayer(), FoldPlayer()]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0])


if __name__ == '__main__':
    main()
