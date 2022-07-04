from sys import path
path.append("../../")

from cards_dealer import deal_flop_and_turn
from cards_reader import check_cards_are_valid

for _ in range(100):
    board_cards, players = deal_flop_and_turn()
    check_cards_are_valid(board_cards, players)
    assert len(board_cards) == 5
    assert board_cards.count("?") == 1

print("deals_flop_and_turn_test.py passed")
