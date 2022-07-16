from sys import path
path.append("../../../")

from cards_dealer import deal_cards
from game import play_hand_return_remaining
from players import CallPlayer

players = [CallPlayer(), CallPlayer()]
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [0, 1]

players = [CallPlayer(), CallPlayer(), CallPlayer()]
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [0, 1, 2]

print("Passed")
