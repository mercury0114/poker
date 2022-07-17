from sys import path
path.append("../../../")

from unittest import main
from unittest import TestCase

from cards_dealer import deal_cards
from round_state import call_amount
from game import play_hand_return_remaining
from players.donkeys import FoldPlayer
from players.player import Player
from stack import full_stack_for_all


class BetLess10Player(Player):
    def bet(self):
        return 9 if call_amount(self.state, self.position) < 10 else 0


class BetIfNotCallPlayer(Player):
    def bet(self):
        amount = call_amount(self.state, self.position)
        return amount if amount else 20


class Unit(TestCase):
    def test1(self):
        players = [BetLess10Player(), BetIfNotCallPlayer()]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [1])

    def test2(self):
        players = [BetIfNotCallPlayer(), BetLess10Player()]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0, 1])

    # Non heads up test
    def test3(self):
        players = [BetIfNotCallPlayer(), BetLess10Player(), FoldPlayer()]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        remaining = play_hand_return_remaining(players, stack, board, cards)
        self.assertEqual(remaining, [0])


if __name__ == '__main__':
    main()
