from sys import path
path[0] = "../../"

from unittest import main
from unittest import TestCase

from utils.round_state import call_amount
from utils.round_state import CALL
from utils.round_state import PENDING
from utils.round_state import RAISE


class Unit(TestCase):
    def test1(self):
        state = [(PENDING, 0), (PENDING, 0)]
        self.assertEqual(call_amount(state, 0), 0)

    def test2(self):
        state = [(RAISE, 1), (CALL, 1)]
        self.assertEqual(call_amount(state, 0), 0)

    def test3(self):
        state = [(PENDING, 1), (PENDING, 2)]
        self.assertEqual(call_amount(state, 0), 1)
        self.assertEqual(call_amount(state, 1), 0)

    def test4(self):
        state = [(PENDING, 2), (RAISE, 5), (RAISE, 10), (PENDING, 0)]
        self.assertEqual(call_amount(state, 0), 8)
        self.assertEqual(call_amount(state, 1), 5)
        self.assertEqual(call_amount(state, 2), 0)
        self.assertEqual(call_amount(state, 3), 10)


if __name__ == "__main__":
    main()
