from sys import path
path.append("../../")

from game import play_hand_return_remaining
from players import AllInPlayer
from players import CheckFoldPlayer

check_fold_player = CheckFoldPlayer()
all_in_player = AllInPlayer()

assert play_hand_return_remaining([all_in_player, check_fold_player]) == [0]
assert play_hand_return_remaining([check_fold_player, all_in_player]) == [1]

print("check_fold_looses_test.py passed")
