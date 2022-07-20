from sys import path
path[0] = "../../"

from unittest import main
from unittest import TestCase

from cards.dealer import deal_cards
from engine.game import play_hand_return_remaining
from players.donkeys import CallPlayer
from utils.stack import full_stack_for_all


class Unit(TestCase):
    def test1(self):
        player0, player1 = CallPlayer(), CallPlayer()
        players = [player0, player1]
        stack = full_stack_for_all(len(players))
        board, cards = deal_cards(len(players))
        play_hand_return_remaining(players, stack, board, cards)

        self.assertEqual(player0.position, 0)
        self.assertEqual(player1.position, 1)
        self.assertEqual(player0.players_count, 2)
        self.assertEqual(player1.players_count, 2)


if __name__ == '__main__':
    main()
