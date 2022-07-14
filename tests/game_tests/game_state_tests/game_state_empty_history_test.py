from sys import path
path.append("../../../")

from game import game_state
from game import SAME_ROUND

assert game_state(2, [(0, 1), (1, 2)]) == (SAME_ROUND, [0, 1])
assert game_state(3, [(0, 1), (1, 2)]) == (SAME_ROUND, [2, 0, 1])
assert game_state(4, [(0, 1), (1, 2)]) == (SAME_ROUND, [2, 3, 0, 1])

print("Passed")
