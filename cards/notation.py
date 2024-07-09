from itertools import product

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
SUITS = ["h", "d", "c", "s"]


def get_all_cards():
    return [rank + suit for rank, suit in product(RANKS, SUITS)]


def get_free_cards(board_cards, players):
    used_cards = get_used_cards(board_cards, players)
    return [c for c in get_all_cards() if c not in used_cards]


def get_used_cards(board_cards, players):
    used_cards = [card for card in board_cards if card != "?"]
    for player in players:
        used_cards += [card for card in player if card != "?"]
    return used_cards
