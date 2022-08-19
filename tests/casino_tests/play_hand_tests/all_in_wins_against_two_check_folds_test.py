from sys import path
path[0] = "../../../"

from unittest import main
from unittest import TestCase

from cards.dealer import deal_cards
from casino.hand import play_hand_return_remaining
from players.donkeys import AllInPlayer
from players.donkeys import FoldPlayer
from utils.stack import full_stack_for_all


class Unit(TestCase):
    def test1(self):
        players = [FoldPlayer('p0'), FoldPlayer('p1'), AllInPlayer('p2')]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [2])

    def test2(self):
        players = [FoldPlayer('p0'), AllInPlayer('p1'), FoldPlayer('p2')]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [1])

    def test3(self):
        players = [AllInPlayer('p0'), FoldPlayer('p1'), FoldPlayer('p2')]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0])


main()
