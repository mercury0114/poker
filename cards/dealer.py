from cards.notation import get_free_cards
from utils.simulator import simulate_game


def deal_cards(players_number):
    board_cards = ["?", "?", "?", "?", "?"]
    players = [["?", "?"]] * players_number
    free_cards = get_free_cards(board_cards, players)
    return simulate_game(board_cards, players, free_cards)


def deal_flop_and_turn(players_number):
    board_cards, players = deal_cards(players_number)
    board_cards[4] = "?"
    return board_cards, players
