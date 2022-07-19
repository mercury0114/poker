from sys import path
path[0] = "../../"

from cards_dealer import deal_cards
from cards_reader import check_cards_are_valid

for number in range(2, 8):
    board_cards, players = deal_cards(number)
    check_cards_are_valid(board_cards, players)
    assert len(players) == number

print("Passed")
