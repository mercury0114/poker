from sys import path
path.append("../../")

from cards_reader import read_cards
from evaluator import read_evaluation_table
from odds_calculator import loosing_odds
from simulator import perform_simulations

table = read_evaluation_table()
board_cards, names, players = read_cards("data/adam_loosing_odds_0_to_1.txt")
win_count = perform_simulations(board_cards, names, players, table)
assert loosing_odds(win_count, "Adam") == 0
assert loosing_odds(win_count, "Opponent") == "inf"
print("Passed")
