from sys import path
path.append("../../")

from cards_reader import read_cards
from evaluator import read_evaluation_table
from simulator import perform_simulations
from odds_calculator import loosing_odds
from odds_calculator import similar_odds

table = read_evaluation_table()
board_cards, names, players = read_cards("data/adam_loosing_odds_5_to_1.txt")
win_count = perform_simulations(board_cards, names, players, table)
assert similar_odds(loosing_odds(win_count, "Adam"), 5)
print("Passed")
