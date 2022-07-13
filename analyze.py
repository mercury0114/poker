from sys import argv

from cards_reader import read_cards
from fast_evaluator import read_evaluation_table
from simulator import perform_simulations
from simulator import SIMULATION_COUNT

if len(argv) != 2:
    print("usage:")
    print("python3 analyzer.py [cards_file.txt]")
    exit()

board_cards, players = read_cards(argv[1])
evaluation_table = read_evaluation_table()

print("Succesfully read cards, performing simulations...")
win_count = perform_simulations(board_cards, players, evaluation_table)

print("All simulations completed, final results:")
for player in players:
    print(f"{player}: {(win_count[player] / SIMULATION_COUNT) * 100}%")
