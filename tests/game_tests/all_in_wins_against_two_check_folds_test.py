from sys import path
path.append("../../")

from game import play_hand_return_remaining
from players import AllInPlayer
from players import CheckFoldPlayer

players = [CheckFoldPlayer(), CheckFoldPlayer(), AllInPlayer()]
assert play_hand_return_remaining(players) == [2]

players = [CheckFoldPlayer(), AllInPlayer(), CheckFoldPlayer()]
assert play_hand_return_remaining(players) == [1]

players = [AllInPlayer(), CheckFoldPlayer(), CheckFoldPlayer()]
assert play_hand_return_remaining(players) == [0]

print("all_in_wins_against_two_check_folds_test.py passed")
