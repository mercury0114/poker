from unittest import main
from unittest import TestCase

from cards.dealer import deal_cards
from cards.evaluator import read_evaluation_table
from casino.hand import play_hand_return_remaining
from casino.hand import play_hand_return_wins
from players.donkeys import FoldPlayer
from players.player import Player
from utils.round_state import call_amount
from utils.stack import full_stack_for_all


class CallLess10Player(Player):
    def bet(self):
        amount = call_amount(self.state, self.position)
        return amount if amount < 10 else 0


class Bet10Player(Player):
    @staticmethod
    def bet():
        return 10


class Unit(TestCase):
    def test1(self):
        players = [CallLess10Player("p0"), FoldPlayer("p1"), Bet10Player("p2")]
        board, cards = deal_cards(len(players))
        stack = full_stack_for_all(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [2])

    def test2(self):
        players = [CallLess10Player("p0"), FoldPlayer("p1"), Bet10Player("p2")]
        evaluation_table = read_evaluation_table()
        stacks = full_stack_for_all(len(players))
        wins = play_hand_return_wins(players, stacks, evaluation_table)
        self.assertEqual(wins, [-10, -2, 12])


main()
