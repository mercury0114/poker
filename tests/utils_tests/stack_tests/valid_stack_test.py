from unittest import TestCase
from unittest import main

from utils.stack import valid_stack


class Test(TestCase):
    def test1(self):
        self.assertTrue(valid_stack([2, 2]))

    def test2(self):
        self.assertFalse(valid_stack([2, 1]))

    def test3(self):
        self.assertFalse(valid_stack([2]))

    def test4(self):
        ten_players = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        eleven_players = ten_players + [2]
        self.assertTrue(valid_stack(ten_players))
        self.assertFalse(valid_stack(eleven_players))


if __name__ == '__main__':
    main()
