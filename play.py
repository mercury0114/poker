from players import CheckFoldPlayer
from players import HumanPlayer

from game import play_hand_return_remaining

players = [HumanPlayer(), CheckFoldPlayer(), CheckFoldPlayer()]
print(play_hand_return_remaining(players))
