from unittest import main
from unittest import TestCase

from cards.notation import get_all_cards


class Unit(TestCase):
    # Test get_all_cards returns 52 cards (equal to full deck size)
    def test1(self):
        all_cards = get_all_cards()
        self.assertEqual(len(all_cards), 52)

    # Test get_all_cards() returns no duplicate cards
    def test2(self):
        all_cards = get_all_cards()
        self.assertEqual(len(all_cards), len(set(all_cards)))


main()
