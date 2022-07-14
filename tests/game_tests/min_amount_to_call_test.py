from sys import path
path.append("../../")

from game import min_amount_to_call

assert min_amount_to_call(0, [(0, 1), (1, 2), (2, 10)]) == 9
assert min_amount_to_call(1, [(0, 1), (1, 2), (2, 10)]) == 8
assert min_amount_to_call(2, [(0, 1), (1, 2), (2, 10)]) == 0

print("Passed")
