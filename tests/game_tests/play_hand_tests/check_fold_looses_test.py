from sys import path
path.append("../../../")

from cards_dealer import deal_cards
from game import play_hand_return_remaining
from players import AllInPlayer
from players import FoldPlayer

players = [AllInPlayer(), FoldPlayer()]
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [0]

players = [FoldPlayer(), AllInPlayer()]
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [1]

print("Passed")
