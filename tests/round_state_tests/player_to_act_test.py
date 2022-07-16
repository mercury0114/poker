from sys import path
path.append("../../")

from round_state import CALL
from round_state import CHECK
from round_state import FOLD
from round_state import PENDING
from round_state import RAISE
from round_state import update_round_state
from round_state import player_to_act

round_state = [(PENDING, 0), (PENDING, 0)]
assert player_to_act(round_state) == 1
update_round_state(round_state, 1, 0)
assert player_to_act(round_state) == 0
update_round_state(round_state, 0, 1)
assert player_to_act(round_state) == 1
update_round_state(round_state, 1, 1)
assert player_to_act(round_state) == 1

round_state = [(PENDING, 1), (RAISE, 2), (PENDING, 0)]
assert player_to_act(round_state) == 2

round_state = [(PENDING, 1), (PENDING, 2), (CALL, 2)]
assert player_to_act(round_state) == 0
update_round_state(round_state, 0, 1)
assert player_to_act(round_state) == 1
update_round_state(round_state, 1, 0)
assert player_to_act(round_state) == 0

round_state = [(PENDING, 1), (PENDING, 2), (RAISE, 4)]
assert player_to_act(round_state) == 0

round_state = [(CHECK, 0), (PENDING, 0), (PENDING, 0)]
assert player_to_act(round_state) == 1
update_round_state(round_state, 1, 0)
assert player_to_act(round_state) == 2
update_round_state(round_state, 2, 0)
assert player_to_act(round_state) == 0

round_state = [(FOLD, 0), (PENDING, 0), (RAISE, 2), (PENDING, 0)]
assert player_to_act(round_state) == 3
update_round_state(round_state, 3, 2)
assert player_to_act(round_state) == 1
update_round_state(round_state, 1, 0)
assert player_to_act(round_state) == 2
update_round_state(round_state, 2, 0)
assert player_to_act(round_state) == 2

print("Passed")
