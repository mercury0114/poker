from sys import path
path[0] = "../../"

from round_state import PENDING
from round_state import players_left
from round_state import update_round_state

round_state = [(PENDING, 1), (PENDING, 2), (PENDING, 0)]
assert players_left(round_state) == [0, 1, 2]
update_round_state(round_state, 2, 0)
assert players_left(round_state) == [0, 1]
update_round_state(round_state, 0, 0)
assert players_left(round_state) == [1]

print("Passed")
