from sys import path
path[0] = "../../"

from unittest import main
from unittest import TestCase

from utils.round_state import CALL
from utils.round_state import CHECK
from utils.round_state import PENDING
from utils.round_state import RAISE
from utils.round_state import round_ended


class Unit(TestCase):
    def test1(self):
        round_state = [(PENDING, 0), (PENDING, 0)]
        self.assertFalse(round_ended(round_state))

    def test2(self):
        round_state = [(RAISE, 1), (CALL, 1)]
        self.assertTrue(round_ended(round_state))

    def test3(self):
        round_state = [(CALL, 2), (PENDING, 2)]
        self.assertFalse(round_ended(round_state))

    def test4(self):
        round_state = [(CALL, 2), (CHECK, 2)]
        self.assertTrue(round_ended(round_state))


if __name__ == "__main__":
    main()
