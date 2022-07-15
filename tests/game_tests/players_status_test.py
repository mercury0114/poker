from sys import path
path.append("../../")

from game import FOLDED
from game import PLAYING
from game import players_status

history = [(0, 1), (1, 2), (2, 10)]
assert players_status(3, history) == [PLAYING, PLAYING, PLAYING]
history += [(0, 0), (1, 8)]
assert players_status(3, history) == [FOLDED, PLAYING, PLAYING]

heads_up_history = [(0, 1), (1, 2), (0, 1), (1, 0), (1, 0), (0, 1), (1, 0)]
assert players_status(2, heads_up_history) == [PLAYING, FOLDED]

print("Passed")
