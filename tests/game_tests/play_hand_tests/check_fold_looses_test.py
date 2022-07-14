from sys import path
path.append("../../../")

from game import play_hand_return_remaining
from players import AllInPlayer
from players import FoldPlayer

assert play_hand_return_remaining([AllInPlayer(), FoldPlayer()]) == [0]
assert play_hand_return_remaining([FoldPlayer(), AllInPlayer()]) == [1]

print("Passed")
