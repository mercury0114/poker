from sys import path
path[0] = "../../"

from utils.round_state import PENDING
from utils.round_state import RAISE
from utils.round_state import cheating

round_state = [(RAISE, 5), (PENDING, 2)]
assert cheating(round_state, 1, 2, 100)
assert cheating(round_state, 1, 200, 100)
assert cheating(round_state, 1, 3, 2)
assert not cheating(round_state, 1, 3, 100)
assert not cheating(round_state, 1, 3, 3)
assert not cheating(round_state, 1, 0, 1)

print("Passed")
