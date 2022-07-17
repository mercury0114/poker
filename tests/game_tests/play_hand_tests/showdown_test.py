from sys import path
path.append("../../../")

from unittest import TestCase
from unittest import main

from cards_dealer import deal_cards
from game import play_hand_return_remaining
from players import CallPlayer
from stack import full_stack_for_all


class Unit(TestCase):
    def test1(self):
        players = [CallPlayer(), CallPlayer()]
        board, cards = deal_cards(len(players))
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0, 1])

    def test2(self):
        players = [CallPlayer(), CallPlayer(), CallPlayer()]
        board, cards = deal_cards(len(players))
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0, 1, 2])


if __name__ == '__main__':
    main()
