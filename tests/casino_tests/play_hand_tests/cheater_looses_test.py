from sys import path
path[0] = "../../../"

from unittest import main
from unittest import TestCase

from cards.dealer import deal_cards
from casino.hand import play_hand_return_remaining
from players.donkeys import CallPlayer
from players.donkeys import FoldPlayer
from players.player import Player
from utils.round_state import call_amount
from utils.stack import FULL_STACK
from utils.stack import full_stack_for_all


class CallOneLessCheater(Player):
    def bet(self):
        return max(0, call_amount(self.state, self.position) - 1)


class BetMoreThanStackCheater(Player):
    @staticmethod
    def bet():
        return FULL_STACK


class Unit(TestCase):
    def test1(self):
        players = [CallPlayer('p0'),
                   FoldPlayer('p1'),
                   CallOneLessCheater('p2')]
        board, cards = deal_cards(len(players))
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0, 1])

    def test2(self):
        players = [BetMoreThanStackCheater('p0'),
                   FoldPlayer('p1'),
                   CallPlayer('p2')]
        board, cards = deal_cards(len(players))
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [1, 2])


if __name__ == '__main__':
    main()
