from sys import path
path[0] = "../../"

from cards_dealer import deal_cards
from cards_reader import check_cards_are_valid

for _ in range(100):
    board_cards, players = deal_cards(2)
    check_cards_are_valid(board_cards, players)

print("Passed")
