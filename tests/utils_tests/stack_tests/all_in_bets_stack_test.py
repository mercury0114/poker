from unittest import TestCase
from unittest import main

from cards.dealer import deal_cards
from casino.hand import play_hand_return_remaining
from players.donkeys import AllInPlayer


class Test(TestCase):
    def test1(self):
        players = [AllInPlayer('p0'), AllInPlayer('p1')]
        stacks = [50, 50]
        board, cards = deal_cards(len(players))
        play_hand_return_remaining(players, stacks, board, cards)
        self.assertEqual(players[0].get_stack(), 0)
        self.assertEqual(players[1].get_stack(), 0)


if __name__ == '__main__':
    main()
