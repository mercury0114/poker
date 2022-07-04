from itertools import product

from evaluator import RANKS
from evaluator import SUITS


def get_free_cards(board_cards, players):
    all_cards = [rank + suit for rank, suit in product(RANKS, SUITS)]
    used_cards = get_used_cards(board_cards, players)
    return [c for c in all_cards if c not in used_cards]


def get_used_cards(board_cards, players):
    used_cards = [card for card in board_cards if card != "?"]
    for player in players:
        used_cards += [card for card in players[player] if card != "?"]
    return used_cards
