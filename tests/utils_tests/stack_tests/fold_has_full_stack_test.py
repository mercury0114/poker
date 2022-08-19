from sys import path
path[0] = "../../../"

from unittest import main
from unittest import TestCase

from cards.dealer import deal_cards
from casino.hand import play_hand_return_remaining
from players.donkeys import FoldPlayer
from utils.stack import full_stack_for_all
from utils.stack import FULL_STACK


class Unit(TestCase):
    def test1(self):
        player0 = FoldPlayer('p0')
        player1 = FoldPlayer('p1')
        player2 = FoldPlayer('p2')
        players = [player0, player1, player2]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(player0.get_stack(), FULL_STACK - 1)
        self.assertEqual(player2.get_stack(), FULL_STACK)

    def test2(self):
        player0 = FoldPlayer('p0')
        player1 = FoldPlayer('p1')
        player2 = FoldPlayer('p2')
        players = [player0, player1, player2]
        stack = [50, 50, 50]
        board, cards = deal_cards(len(players))
        play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(player0.get_stack(), 49)
        self.assertEqual(player1.get_stack(), 48)
        self.assertEqual(player2.get_stack(), 50)


if __name__ == '__main__':
    main()
