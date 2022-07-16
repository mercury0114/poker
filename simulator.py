from random import shuffle

from cards_reader import check_cards_are_valid
from utils import determine_winners
from utils import get_free_cards

SIMULATION_COUNT = 10000
NEVER_LOOSE = "never lose"
LESS_THAN_1 = "less than 1"


def choose_unknown_cards(cards, free_cards):
    return [free_cards.pop() if card == "?" else card for card in cards]


# WARNING: function modifies free_cards list
def simulate_game(board_cards, players, free_cards):
    shuffle(free_cards)
    chosen_board = choose_unknown_cards(board_cards, free_cards)
    chosen_players = {p: choose_unknown_cards(players[p], free_cards)
                      for p in players}
    return chosen_board, chosen_players


def perform_simulations(board_cards, players, evaluation_table):
    check_cards_are_valid(board_cards, players)
    free_cards = get_free_cards(board_cards, players)
    win_count = {player: 0 for player in players}
    for _ in range(SIMULATION_COUNT):
        chosen_board, chosen_players = simulate_game(board_cards,
                                                     players,
                                                     free_cards.copy())
        winners = determine_winners(chosen_board,
                                    chosen_players,
                                    evaluation_table)
        if len(winners) == 1:
            win_count[winners[0]] += 1
    return win_count
