from sys import path
path.append("../../../")

from game import play_hand_return_remaining
from players import AllInPlayer
from players import FoldPlayer

players = [FoldPlayer(), FoldPlayer(), AllInPlayer()]
assert play_hand_return_remaining(players) == [2]

players = [FoldPlayer(), AllInPlayer(), FoldPlayer()]
assert play_hand_return_remaining(players) == [1]

players = [AllInPlayer(), FoldPlayer(), FoldPlayer()]
assert play_hand_return_remaining(players) == [0]

print("Passed")
