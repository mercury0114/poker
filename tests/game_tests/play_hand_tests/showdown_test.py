from sys import path
path.append("../../../")

from game import play_hand_return_remaining
from players import CallPlayer

players = [CallPlayer(), CallPlayer()]
assert play_hand_return_remaining(players) == [0, 1]

players = [CallPlayer(), CallPlayer(), CallPlayer()]
assert play_hand_return_remaining(players) == [0, 1, 2]

print("Passed")
