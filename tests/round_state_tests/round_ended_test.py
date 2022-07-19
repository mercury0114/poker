from sys import path
path[0] = "../../"

from round_state import CALL
from round_state import CHECK
from round_state import PENDING
from round_state import RAISE
from round_state import round_ended

round_state = [(PENDING, 0), (PENDING, 0)]
assert not round_ended(round_state)

round_state = [(RAISE, 1), (CALL, 1)]
assert round_ended(round_state)

round_state = [(CALL, 2), (PENDING, 2)]
assert not round_ended(round_state)

round_state = [(CALL, 2), (CHECK, 2)]
assert round_ended(round_state)

print("Passed")
