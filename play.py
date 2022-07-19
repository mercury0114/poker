from game_engine import play
from players.human import Human
from players.with_pair_player import WithPairPlayer

# In this example case:
# - 6 players
# - you will always play in the first (small blind) position
# - 5 opponents are "WithPairPlayer" players, read the
#   players/with_pair_player.py file to see how they play
#
# If you want to customise your opponent, you have to write your own class
# implementing the Player interface found in players/player.py
you = Human()
big_blind = WithPairPlayer()
utg = WithPairPlayer()
utg_plus1 = WithPairPlayer()
utg_plus2 = WithPairPlayer()
button = WithPairPlayer()
players = [you, big_blind, utg, utg_plus1, utg_plus2, button]
play(players)
