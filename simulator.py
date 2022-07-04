from itertools import combinations
from random import shuffle

from cards_reader import check_cards_are_valid
from fast_evaluator import evaluate_with_table
from utils import get_free_cards
from utils import get_used_cards

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


def determine_winners(board_cards, players, evaluation_table):
    best_hands = {}
    for player in players:
        seven_cards = get_used_cards(board_cards, {player: players[player]})
        evaluations = [evaluate_with_table(hand, evaluation_table)
                       for hand in combinations(seven_cards, 5)]
        best_hands[player] = max(evaluations)
    winning_hand = max(best_hands.values())
    return [player for player in players if best_hands[player] == winning_hand]


def perform_simulations(board_cards, players, evaluation_table):
    check_cards_are_valid(board_cards, players)
    free_cards = get_free_cards(board_cards, players)
    win_count = {player: 0 for player in players}
    for _ in range(SIMULATION_COUNT):
        chosen_board, chosen_players = simulate_game(board_cards,
                                                     players,
                                                     free_cards.copy())
        for winner in determine_winners(chosen_board,
                                        chosen_players,
                                        evaluation_table):
            win_count[winner] += 1
    return win_count
