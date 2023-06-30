from unittest import main
from unittest import TestCase

from utils.round_state import ALL_IN
from utils.round_state import CALL
from utils.round_state import FOLD
from utils.round_state import PENDING
from utils.round_state import RAISE
from utils.round_state import update_round_state


class Unit(TestCase):
    def test1(self):
        state = [(RAISE, 4), (CALL, 4), (PENDING, 2), (FOLD, 0)]
        update_round_state(state, 2, 2, 2)
        expected = [(RAISE, 4), (CALL, 4), (ALL_IN, 4), (FOLD, 0)]
        self.assertEqual(state, expected)

    def test2(self):
        state = [(PENDING, 0), (ALL_IN, 10), (PENDING, 5)]
        update_round_state(state, 2, 3, 3)
        expected = [(PENDING, 0), (ALL_IN, 10), (ALL_IN, 8)]
        self.assertEqual(state, expected)

    def test3(self):
        state = [(RAISE, 5), (ALL_IN, 3), (PENDING, 0)]
        update_round_state(state, 2, 10)
        expected = [(PENDING, 5), (ALL_IN, 3), (RAISE, 10)]
        self.assertEqual(state, expected)

    def test4(self):
        state = [(PENDING, 5), (ALL_IN, 3), (RAISE, 10)]
        update_round_state(state, 0, 3, 3)
        expected = [(ALL_IN, 8), (ALL_IN, 3), (RAISE, 10)]
        self.assertEqual(state, expected)


main()
