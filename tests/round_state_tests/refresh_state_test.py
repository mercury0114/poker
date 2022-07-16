from sys import path
path.append("../../")

from round_state import CALL
from round_state import CHECK
from round_state import FOLD
from round_state import PENDING
from round_state import refresh

state = [(FOLD, 1), (CHECK, 2), (CALL, 2)]
assert refresh(state) == [(FOLD, 0), (PENDING, 0), (PENDING, 0)]

state = [(CALL, 2), (CHECK, 2), (CALL, 2)]
assert refresh(state) == [(PENDING, 0), (PENDING, 0), (PENDING, 0)]

print("Passed")
