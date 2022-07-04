from simulator import simulate_game
from utils import get_free_cards


def deal_cards():
    board_cards = ["?", "?", "?", "?", "?"]
    players = {"Me": ["?", "?"], "You": ["?", "?"]}
    free_cards = get_free_cards(board_cards, players)
    return simulate_game(board_cards, players, free_cards)


def deal_flop_and_turn():
    board_cards, players = deal_cards()
    board_cards[4] = "?"
    return board_cards, players
