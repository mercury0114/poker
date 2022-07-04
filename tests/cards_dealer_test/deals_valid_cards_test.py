from sys import path
path.append("../../")

from cards_dealer import deal_cards
from cards_reader import check_cards_are_valid

for _ in range(100):
    board_cards, players = deal_cards()
    check_cards_are_valid(board_cards, players)

print("deals_valid_cards.py passed")
