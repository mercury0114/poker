from sys import path
path.append("../../")

from game import remaining_players
from game import NEXT_ROUND
from game import SAME_ROUND


def check(number, history, expected_result):
    assert remaining_players(number, history) == expected_result


check(3, [(0, 1), (1, 2), (2, 2), (0, 1), (1, 0)], (NEXT_ROUND, [0, 1, 2]))
check(3, [(0, 1), (1, 2), (2, 0), (0, 1), (1, 0)], (NEXT_ROUND, [0, 1]))
check(3, [(0, 1), (1, 2), (2, 4), (0, 0), (1, 2)], (NEXT_ROUND, [1, 2]))
check(3, [(0, 1), (1, 2), (2, 4), (0, 3), (1, 0)], (NEXT_ROUND, [0, 2]))
check(3, [(0, 1), (1, 2), (2, 4), (0, 0), (1, 2)], (NEXT_ROUND, [1, 2]))

history = [(0, 1), (1, 2), (2, 0), (3, 2), (0, 1), (1, 0), (0, 0), (1, 10)]
check(4, history, (SAME_ROUND, [3, 0, 1]))

history = [(0, 1), (1, 2), (2, 10), (0, 9), (1, 0), (0, 0)]
check(3, history, (SAME_ROUND, [2, 0]))
print("remaining_players_preflop_complete_test.py passed")
