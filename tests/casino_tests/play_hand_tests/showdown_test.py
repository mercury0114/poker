from unittest import TestCase
from unittest import main

from cards.dealer import deal_cards
from casino.hand import play_hand_return_remaining
from players.donkeys import CallPlayer
from utils.stack import full_stack_for_all


class Unit(TestCase):
    def test1(self):
        players = [CallPlayer('p0'), CallPlayer('p1')]
        board, cards = deal_cards(len(players))
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0, 1])

    def test2(self):
        players = [CallPlayer('p0'), CallPlayer('p1'), CallPlayer('p2')]
        board, cards = deal_cards(len(players))
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0, 1, 2])


if __name__ == '__main__':
    main()
