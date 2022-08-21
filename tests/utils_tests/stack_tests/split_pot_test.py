from sys import path
path[0] = "../../../"

from unittest import main
from unittest import TestCase

from utils.stack import split_pot


class Unit(TestCase):
    def test1(self):
        old_stack = [200, 200]
        stack = [0, 198]
        ranks = [0, 1]
        pot_split = split_pot(old_stack, stack, ranks)
        self.assertEqual(pot_split, [202, 0])

    def test2(self):
        old_stack = [200, 200]
        stack = [100, 100]
        ranks = [0, 0]
        pot_split = split_pot(old_stack, stack, ranks)
        self.assertEqual(pot_split, [100, 100])

    def test3(self):
        old_stack = [200, 100]
        stack = [0, 0]
        ranks = [0, 0]
        pot_split = split_pot(old_stack, stack, ranks)
        self.assertEqual(pot_split, [200, 100])

    def test4(self):
        old_stack = [200, 100, 50]
        stack = [0, 0, 0]
        ranks = [0, 2, 0]
        pot_split = split_pot(old_stack, stack, ranks)
        self.assertEqual(pot_split, [275, 0, 75])

    def test5(self):
        old_stack = [200, 100, 50]
        stack = [120, 20, 0]
        ranks = [0, 2, 0]
        pot_split = split_pot(old_stack, stack, ranks)
        self.assertEqual(pot_split, [135, 0, 75])

    def test6(self):
        old_stack = [200, 200, 100, 100, 40]
        stack = [50, 50, 0, 0, 0]
        ranks = [1, 3, 1, 4, 0]
        pot_split = split_pot(old_stack, stack, ranks)
        self.assertEqual(pot_split, [220, 0, 120, 0, 200])

    def test7(self):
        old_stack = [200, 200]
        stack = [0, 198]
        ranks = [1, 2]
        pot_split = split_pot(old_stack, stack, ranks)
        self.assertEqual(pot_split, [202, 0])

    def test8(self):
        old_stack = [10, 40, 160]
        stack = [0, 0, 0]
        ranks = [0, 0, 2]
        pot_split = split_pot(old_stack, stack, ranks)
        self.assertEqual(pot_split, [15, 75, 120])


main()
