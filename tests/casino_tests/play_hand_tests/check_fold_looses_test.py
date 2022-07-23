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
        players = [AllInPlayer('p0'), FoldPlayer('p1')]
        stack = full_stack_for_all(2)
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0])

    def test2(self):
        players = [FoldPlayer('p0'), AllInPlayer("p1")]
        stack = full_stack_for_all(2)
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [1])


if __name__ == '__main__':
    main()
