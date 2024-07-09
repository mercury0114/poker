from sys import argv

from cards.reader import read_cards
from cards.evaluator import read_evaluation_table
from utils.simulator import perform_simulations
from utils.simulator import SIMULATION_COUNT

if len(argv) != 2:
    print("usage:")
    print("python3 analyzer.py [cards_file.txt]")
    exit(1)

board_cards, names, players = read_cards(argv[1])
evaluation_table = read_evaluation_table()

print("Succesfully read cards, performing simulations...")
win_count = perform_simulations(board_cards, names, players, evaluation_table)

print("All simulations completed, final results:")
for name in names:
    print(f"{name}: {(win_count[name] / SIMULATION_COUNT) * 100}%")
