from sys import path
path[0] = "../../"

from unittest import TestCase
from unittest import main

from utils.stack import compute_pot
from utils.stack import full_stack_for_all


class Test(TestCase):
    def test1(self):
        players_number = 5
        stack = full_stack_for_all(players_number)
        new_stack = [s - 10 for s in stack]
        self.assertEqual(compute_pot(stack, new_stack), 10 * players_number)


if __name__ == '__main__':
    main()
