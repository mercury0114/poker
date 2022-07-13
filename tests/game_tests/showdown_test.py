from sys import path
path.append("../../")

from game import play_hand_return_remaining
from players import CallPlayer

players = [CallPlayer(0), CallPlayer(1)]
assert play_hand_return_remaining(players) == [0, 1]

players = [CallPlayer(0), CallPlayer(1), CallPlayer(2)]
assert play_hand_return_remaining(players) == [0, 1, 2]

print("showdown_test.py passed")
