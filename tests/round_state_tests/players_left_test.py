from sys import path
path[0] = "../../"

from unittest import main
from unittest import TestCase

from utils.round_state import ALL_IN
from utils.round_state import FOLD
from utils.round_state import PENDING
from utils.round_state import players_left
from utils.round_state import update_round_state


class Unit(TestCase):
    def test1(self):
        state = [(PENDING, 1), (PENDING, 2), (PENDING, 0)]
        self.assertEqual(players_left(state), [0, 1, 2])
        update_round_state(state, 2, 0)
        self.assertEqual(state, [(PENDING, 1), (PENDING, 2), (FOLD, 0)])

    def test2(self):
        state = [(PENDING, 1), (PENDING, 2), (FOLD, 0)]
        self.assertEqual(players_left(state), [0, 1])
        update_round_state(state, 0, 0)
        self.assertEqual(state, [(FOLD, 1), (PENDING, 2), (FOLD, 0)])

    def test3(self):
        state = [(FOLD, 1), (PENDING, 2), (FOLD, 0)]
        self.assertEqual(players_left(state), [1])

    def test4(self):
        state = [(FOLD, 1), (PENDING, 10), (ALL_IN, 5)]
        self.assertEqual(players_left(state), [1, 2])


if __name__ == "__main__":
    main()
