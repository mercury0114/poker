from sys import path
path[0] = "../../"

from round_state import call_amount
from round_state import CALL
from round_state import PENDING
from round_state import RAISE

state = [(PENDING, 0), (PENDING, 0)]
assert call_amount(state, 0) == 0

state = [(RAISE, 1), (CALL, 1)]
assert call_amount(state, 0) == 0


state = [(PENDING, 1), (PENDING, 2)]
assert call_amount(state, 0) == 1
assert call_amount(state, 1) == 0

state = [(PENDING, 2), (RAISE, 5), (RAISE, 10), (PENDING, 0)]
assert call_amount(state, 0) == 8
assert call_amount(state, 1) == 5
assert call_amount(state, 2) == 0
assert call_amount(state, 3) == 10

print("Passed")
