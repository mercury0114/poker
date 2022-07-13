from sys import path
path.append("../../")

from game import remaining_players
from game import NEXT_ROUND
from game import SAME_ROUND


def check(number, history, expected_result):
    assert remaining_players(number, history) == expected_result


check(2, [(0, 1), (1, 2), (0, 1)], (SAME_ROUND, [1, 0]))
check(3, [(0, 1), (1, 2), (2, 0)], (SAME_ROUND, [0, 1]))
check(4, [(0, 1), (1, 2), (2, 0)], (SAME_ROUND, [3, 0, 1]))
check(3, [(0, 1), (1, 2), (2, 2), (0, 3), (1, 0)], (SAME_ROUND, [2, 0]))

history = [(0, 1), (1, 2), (2, 4), (3, 4), (4, 4), (0, 3), (1, 0)]
check(5, history, (NEXT_ROUND, [0, 2, 3, 4]))

history = [(0, 1), (1, 2), (2, 4), (3, 6), (4, 6), (0, 5), (1, 0)]
check(5, history, (SAME_ROUND, [2, 3, 4, 0]))

print("remaining_players_preflop_test.py passed")
