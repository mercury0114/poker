from utils.round_state import PENDING
from utils.round_state import initial_state

assert initial_state(2) == [(PENDING, 1), (PENDING, 2)]
assert initial_state(3) == [(PENDING, 1), (PENDING, 2), (PENDING, 0)]

print("Passed")
