from sys import path
path.append("../../")

from cards_reader import read_cards
from fast_evaluator import read_evaluation_table
from odds_calculator import loosing_odds
from simulator import perform_simulations

table = read_evaluation_table()
board_cards, players = read_cards("data/adam_loosing_odds_0_to_1.txt")
win_count = perform_simulations(board_cards, players, table)
assert loosing_odds(win_count, "Adam") == 0
assert loosing_odds(win_count, "Opponent") == "inf"
print("adam_loosing_odds_0_to_1_test.py passed")
