from sys import path
path.append("../../../")

from unittest import TestCase
from unittest import main

from stack import FULL_STACK
from stack import full_stack_for_all


class Test(TestCase):
    def test1(self):
        stack = full_stack_for_all(2)
        self.assertEqual(stack, [FULL_STACK, FULL_STACK])

    def test2(self):
        stack = full_stack_for_all(3)
        self.assertEqual(stack, [FULL_STACK, FULL_STACK, FULL_STACK])


if __name__ == '__main__':
    main()
