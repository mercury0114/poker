from sys import path
path[0] = "../../"

from unittest import main
from unittest import TestCase

from utils.round_state import CALL
from utils.round_state import CHECK
from utils.round_state import FOLD
from utils.round_state import PENDING
from utils.round_state import RAISE
from utils.round_state import update_round_state


class Unit(TestCase):
    def test1(self):
        state = [(CALL, 2), (PENDING, 2), (CALL, 2)]
        update_round_state(state, 1, 0)
        self.assertEqual(state, [(CALL, 2), (CHECK, 2), (CALL, 2)])

    def test2(self):
        state = [(PENDING, 0), (PENDING, 0)]
        update_round_state(state, 0, 0)
        self.assertEqual(state, [(CHECK, 0), (PENDING, 0)])

    def test3(self):
        state = [(PENDING, 0), (PENDING, 0)]
        update_round_state(state, 1, 0)
        self.assertEqual(state, [(PENDING, 0), (CHECK, 0)])

    def test4(self):
        state = [(PENDING, 0), (PENDING, 0)]
        update_round_state(state, 0, 1)
        self.assertEqual(state, [(RAISE, 1), (PENDING, 0)])

    def test5(self):
        state = [(RAISE, 1), (PENDING, 0)]
        update_round_state(state, 1, 1)
        self.assertEqual(state, [(RAISE, 1), (CALL, 1)])

    def test6(self):
        state = [(PENDING, 1), (RAISE, 2)]
        update_round_state(state, 0, 2)
        self.assertEqual(state, [(RAISE, 3), (PENDING, 2)])

    def test7(self):
        state = [(PENDING, 1), (RAISE, 2)]
        update_round_state(state, 0, 0)
        self.assertEqual(state, [(FOLD, 1), (RAISE, 2)])

    def test8(self):
        state = [(PENDING, 1), (RAISE, 2), (CALL, 2), (PENDING, 0)]
        update_round_state(state, 3, 0)
        expected = [(PENDING, 1), (RAISE, 2), (CALL, 2), (FOLD, 0)]
        self.assertEqual(state, expected)

    def test9(self):
        state = [(PENDING, 1), (RAISE, 2), (CALL, 2), (FOLD, 0)]
        update_round_state(state, 0, 3)
        expected = [(RAISE, 4), (PENDING, 2), (PENDING, 2), (FOLD, 0)]
        self.assertEqual(state, expected)

    def test10(self):
        state = [(RAISE, 4), (PENDING, 2), (PENDING, 2), (FOLD, 0)]
        update_round_state(state, 1, 2)
        expected = [(RAISE, 4), (CALL, 4), (PENDING, 2), (FOLD, 0)]
        self.assertEqual(state, expected)

    def test11(self):
        state = [(RAISE, 4), (CALL, 4), (PENDING, 2), (FOLD, 0)]
        update_round_state(state, 2, 2)
        expected = [(RAISE, 4), (CALL, 4), (CALL, 4), (FOLD, 0)]
        self.assertEqual(state, expected)


if __name__ == "__main__":
    main()
