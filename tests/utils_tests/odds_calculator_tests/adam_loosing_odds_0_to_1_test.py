from unittest import main
from unittest import TestCase

from cards.reader import read_cards
from cards.evaluator import read_evaluation_table
from utils.odds_calculator import loosing_odds
from utils.simulator import perform_simulations


class Unit(TestCase):
    def test1(self):
        table = read_evaluation_table()
        board, names, cards = read_cards(
            "tests/utils_tests/odds_calculator_tests/data/adam_loosing_odds_0_to_1.txt")
        win_count = perform_simulations(board, names, cards, table)
        self.assertEqual(loosing_odds(win_count, "Adam"), 0)
        self.assertEqual(loosing_odds(win_count, "Opponent"), "inf")


if __name__ == "__main__":
    main()
