from simulator import simulate_game
from utils import get_free_cards

SYMBOLS = {"h": "\u2764\uFE0F ",
           "d": "\u2666\uFE0F ",
           "s": "\u26AA",
           "c": ".%"}


def card_string(card):
    rank = "10" if card[0] == "T" else card[0]
    return rank + SYMBOLS[card[1]]


def display_row(row_name, row):
    formatted_row = [entry.ljust(10) for entry in row]
    print(f"{row_name}:".ljust(10) + ' '.join(formatted_row))


def display_cards(name, cards):
    string = name + ": " + '  '.join([card_string(card) for card in cards])
    print(string)


def deal_cards(number):
    board_cards = ["?", "?", "?", "?", "?"]
    players = [["?", "?"]] * number
    free_cards = get_free_cards(board_cards, players)
    return simulate_game(board_cards, players, free_cards)


def deal_flop_and_turn(number):
    board_cards, players = deal_cards(number)
    board_cards[4] = "?"
    return board_cards, players
