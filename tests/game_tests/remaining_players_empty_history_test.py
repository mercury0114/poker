from sys import path
path.append("../../")

from game import remaining_players
from game import SAME_ROUND

assert remaining_players(2, [(0, 1), (1, 2)]) == (SAME_ROUND, [0, 1])
assert remaining_players(3, [(0, 1), (1, 2)]) == (SAME_ROUND, [2, 0, 1])
assert remaining_players(4, [(0, 1), (1, 2)]) == (SAME_ROUND, [2, 3, 0, 1])

print("remaining_players_empty_hisory_test.py passed")
