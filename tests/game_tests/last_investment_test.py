from sys import path
path.append("../../")

from game import last_investment

# Miscalleneous history
assert last_investment(3, [(0, 1), (1, 2), (2, 10)]) == [1, 2, 10]
assert last_investment(3, [(0, 1), (1, 2), (2, 10), (0, 9)]) == [10, 2, 10]
assert last_investment(2, [(0, 1), (1, 2), (0, 3), (1, 2)]) == [0, 0]

# Game 1
history = [(0, 1), (1, 2), (2, 2), (0, 1)]
assert last_investment(3, history) == [2, 2, 2]
history.append((1, 0))
assert last_investment(3, history) == [0, 0, 0]

# Game 2
history = [(0, 1), (1, 2), (2, 4), (0, 0)]
assert last_investment(3, history) == [1, 2, 4]
history.append((1, 2))
assert last_investment(3, history) == [0, 0, 0]
history.append((1, 2))
assert last_investment(3, history) == [0, 2, 0]
history.append((2, 2))
assert last_investment(3, history) == [0, 0, 0]

# Game 3
history = [(0, 1), (1, 2)]
assert last_investment(2, history) == [1, 2]
history.append((0, 1))
assert last_investment(2, history) == [2, 2]
history.append((1, 0))
assert last_investment(2, history) == [0, 0]
history.append((0, 1))
assert last_investment(2, history) == [1, 0]
history.append((1, 2))
assert last_investment(2, history) == [1, 2]
history.append((0, 1))
assert last_investment(2, history) == [0, 0]

print("Passed")
