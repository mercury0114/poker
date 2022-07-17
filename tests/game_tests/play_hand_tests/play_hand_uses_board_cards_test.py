from sys import path
path.append("../../../")

from unittest import main
from unittest import TestCase

from game import play_hand_return_remaining
from players.player import Player
from round_state import call_amount
from stack import full_stack_for_all


class Bet10Player(Player):
    @staticmethod
    def bet():
        return 10


class CallIfFirstBoardCardAce(Player):
    def bet(self):
        if len(self.board) == 0 or self.board[0][0] == "A":
            return call_amount(self.state, self.position)
        return 0


class Unit(TestCase):
    def test1(self):
        players = [CallIfFirstBoardCardAce(), Bet10Player()]
        board = ["Ah", "3s", "4s", "5s", "6s"]
        cards = [["As", "Ks"], ["Qs", "Js"]]
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0, 1])

    def test2(self):
        players = [CallIfFirstBoardCardAce(), Bet10Player()]
        board = ["2s", "3s", "4s", "5s", "6s"]
        cards = [["2h", "Ks"], ["Qs", "Js"]]
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [1])


if __name__ == '__main__':
    main()
