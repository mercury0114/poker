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
from utils.round_state import player_to_act


class Unit(TestCase):
    def test1(self):
        round_state = [(PENDING, 1), (PENDING, 2), (CALL, 2), (PENDING, 0)]
        self.assertEqual(player_to_act(round_state), 3)
        update_round_state(round_state, 3, 2)
        self.assertEqual(player_to_act(round_state), 0)
        update_round_state(round_state, 0, 0)
        self.assertEqual(player_to_act(round_state), 1)
        update_round_state(round_state, 1, 0)
        self.assertEqual(player_to_act(round_state), 1)

    def test2(self):
        round_state = [(PENDING, 0), (PENDING, 0)]
        self.assertEqual(player_to_act(round_state), 1)
        update_round_state(round_state, 1, 0)
        self.assertEqual(player_to_act(round_state), 0)
        update_round_state(round_state, 0, 1)
        self.assertEqual(player_to_act(round_state), 1)
        update_round_state(round_state, 1, 1)
        self.assertEqual(player_to_act(round_state), 1)

    def test3(self):
        round_state = [(PENDING, 1), (RAISE, 2), (PENDING, 0)]
        self.assertEqual(player_to_act(round_state), 2)

    def test4(self):
        round_state = [(PENDING, 1), (PENDING, 2), (CALL, 2)]
        self.assertEqual(player_to_act(round_state), 0)
        update_round_state(round_state, 0, 1)
        self.assertEqual(player_to_act(round_state), 1)
        update_round_state(round_state, 1, 0)
        self.assertEqual(player_to_act(round_state), 0)

    def test5(self):
        round_state = [(PENDING, 1), (PENDING, 2), (RAISE, 4)]
        self.assertEqual(player_to_act(round_state), 0)

    def test6(self):
        round_state = [(CHECK, 0), (PENDING, 0), (PENDING, 0)]
        self.assertEqual(player_to_act(round_state), 1)
        update_round_state(round_state, 1, 0)
        self.assertEqual(player_to_act(round_state), 2)
        update_round_state(round_state, 2, 0)
        self.assertEqual(player_to_act(round_state), 0)

    def test7(self):
        round_state = [(FOLD, 0), (PENDING, 0), (RAISE, 2), (PENDING, 0)]
        self.assertEqual(player_to_act(round_state), 3)
        update_round_state(round_state, 3, 2)
        self.assertEqual(player_to_act(round_state), 1)
        update_round_state(round_state, 1, 0)
        self.assertEqual(player_to_act(round_state), 2)
        update_round_state(round_state, 2, 0)
        self.assertEqual(player_to_act(round_state), 2)


if __name__ == "__main__":
    main()
