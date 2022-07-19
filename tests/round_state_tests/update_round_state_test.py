from sys import path
path[0] = "../../"

from round_state import CALL
from round_state import CHECK
from round_state import FOLD
from round_state import PENDING
from round_state import RAISE
from round_state import update_round_state

round_state = [(CALL, 2), (PENDING, 2), (CALL, 2)]
update_round_state(round_state, 1, 0)
assert round_state == [(CALL, 2), (CHECK, 2), (CALL, 2)]

round_state = [(PENDING, 0), (PENDING, 0)]
update_round_state(round_state, 0, 0)
assert round_state == [(CHECK, 0), (PENDING, 0)]

round_state = [(PENDING, 0), (PENDING, 0)]
update_round_state(round_state, 1, 0)
assert round_state == [(PENDING, 0), (CHECK, 0)]

round_state = [(PENDING, 0), (PENDING, 0)]
update_round_state(round_state, 0, 1)
assert round_state == [(RAISE, 1), (PENDING, 0)]

round_state = [(RAISE, 1), (PENDING, 0)]
update_round_state(round_state, 1, 1)
assert round_state == [(RAISE, 1), (CALL, 1)]

round_state = [(PENDING, 1), (RAISE, 2)]
update_round_state(round_state, 0, 2)
assert round_state == [(RAISE, 3), (PENDING, 2)]

round_state = [(PENDING, 1), (RAISE, 2)]
update_round_state(round_state, 0, 0)
assert round_state == [(FOLD, 1), (RAISE, 2)]

round_state = [(PENDING, 1), (RAISE, 2), (CALL, 2), (PENDING, 0)]
update_round_state(round_state, 3, 0)
assert round_state == [(PENDING, 1), (RAISE, 2), (CALL, 2), (FOLD, 0)]
update_round_state(round_state, 0, 3)
assert round_state == [(RAISE, 4), (PENDING, 2), (PENDING, 2), (FOLD, 0)]
update_round_state(round_state, 1, 2)
assert round_state == [(RAISE, 4), (CALL, 4), (PENDING, 2), (FOLD, 0)]
update_round_state(round_state, 2, 2)
assert round_state == [(RAISE, 4), (CALL, 4), (CALL, 4), (FOLD, 0)]

print("Passed")
