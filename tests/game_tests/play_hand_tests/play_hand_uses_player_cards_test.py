from sys import path
path[0] = "../../../"

from unittest import main
from unittest import TestCase

from game import play_hand_return_remaining
from players.donkeys import FoldPlayer
from players.player import Player
from stack import full_stack_for_all
from round_state import call_amount


class CallWithAce(Player):
    def bet(self):
        if (self.cards[0][0] == "A" or self.cards[1][0] == "A"):
            return call_amount(self.state, self.position)
        return 0


class Unit(TestCase):
    def test1(self):
        players = [CallWithAce(), FoldPlayer()]
        board = ["2s", "3s", "4s", "5s", "6s"]
        cards = [["As", "Ks"], ["Qs", "Js"]]
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0, 1])

    def test2(self):
        players = [CallWithAce(), FoldPlayer()]
        board = ["2s", "3s", "4s", "5s", "6s"]
        cards = [["2h", "Ks"], ["Qs", "Js"]]
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [1])


if __name__ == '__main__':
    main()
