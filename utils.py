from itertools import combinations
from itertools import product

from evaluator import RANKS
from evaluator import SUITS
from evaluator import evaluate_with_table


def determine_winners(board_cards, players, evaluation_table):
    best_hands = {}
    for player in players:
        seven_cards = get_used_cards(board_cards, {player: players[player]})
        evaluations = [evaluate_with_table(hand, evaluation_table)
                       for hand in combinations(seven_cards, 5)]
        best_hands[player] = max(evaluations)
    winning_hand = max(best_hands.values())
    return [player for player in players if best_hands[player] == winning_hand]


def get_free_cards(board_cards, players):
    all_cards = [rank + suit for rank, suit in product(RANKS, SUITS)]
    used_cards = get_used_cards(board_cards, players)
    return [c for c in all_cards if c not in used_cards]


def get_used_cards(board_cards, players):
    used_cards = [card for card in board_cards if card != "?"]
    for player in players:
        used_cards += [card for card in players[player] if card != "?"]
    return used_cards
