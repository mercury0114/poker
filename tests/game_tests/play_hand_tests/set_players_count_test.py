from sys import path
path.append("../../../")

from game import play_hand_return_remaining
from players import CallPlayer

player0, player1 = CallPlayer(), CallPlayer()

players = [player0, player1]
play_hand_return_remaining(players)

assert player0.position == 0
assert player1.position == 1
assert player0.players_count == 2
assert player1.players_count == 2

print("Passed")
