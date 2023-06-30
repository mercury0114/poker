from unittest import main
from unittest import TestCase

from cards.evaluator import best_evaluation


class Unit(TestCase):
    def test1(self):
        board = ["Qc", "9h", "Jd", "4c", "9s"]
        player = ["As", "3s"]
        evaluation = best_evaluation(board, player)
        self.assertEqual(evaluation[0], 1)

    def test2(self):
        board = ["Qc", "9c", "Kc"]
        player = ["Qd", "8s"]
        board_evaluation = best_evaluation(board, [])
        player_evaluation = best_evaluation(board, player)
        self.assertLess(board_evaluation, player_evaluation)


if __name__ == '__main__':
    main()
