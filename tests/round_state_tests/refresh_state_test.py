from unittest import main
from unittest import TestCase

from utils.round_state import ALL_IN
from utils.round_state import CALL
from utils.round_state import CHECK
from utils.round_state import FOLD
from utils.round_state import PENDING
from utils.round_state import refresh


class Unit(TestCase):
    def test1(self):
        state = refresh([(FOLD, 1), (CHECK, 2), (CALL, 2)])
        self.assertEqual(state, [(FOLD, 0), (PENDING, 0), (PENDING, 0)])

    def test2(self):
        state = refresh([(CALL, 2), (CHECK, 2), (CALL, 2)])
        self.assertEqual(state, [(PENDING, 0), (PENDING, 0), (PENDING, 0)])

    def test3(self):
        state = refresh([(CALL, 5), (ALL_IN, 2), (CALL, 5)])
        self.assertEqual(state, [(PENDING, 0), (ALL_IN, 0), (PENDING, 0)])


if __name__ == "__main__":
    main()
