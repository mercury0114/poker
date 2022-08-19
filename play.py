from casino.table import Table
from players.human import Human
from players.with_pair_player import WithPairPlayer
from utils.stack import FULL_STACK

# In this example case:
# - 6 players, you start as a small blind, later rotate positions
# - 5 opponents are "WithPairPlayer" players, read the
#   players/with_pair_player.py file to see how they play
# - If you want to customise your opponent, you have to write your own class
#   implementing the Player interface found in players/player.py
you = Human("You")
big_blind = WithPairPlayer("player1")
utg = WithPairPlayer("player2")
utg_plus1 = WithPairPlayer("player3")
utg_plus2 = WithPairPlayer("player4")
button = WithPairPlayer("player5")
players = [you, big_blind, utg, utg_plus1, utg_plus2, button]

table = Table(players)
# Optionally specifying how much blinds each player brings to the table,
# default is FULL_STACK = 200. Current implementation is such that initial
# stack sizes reset for each new hand.
table.stacks = [100, FULL_STACK, 50, FULL_STACK, 150, FULL_STACK]
# if you want to always play in the same position:
# table.rotate_positions = False
table.play()
