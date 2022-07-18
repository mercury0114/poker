from itertools import combinations
from itertools import product

from evaluator import RANKS
from evaluator import SUITS
from evaluator import evaluate
from evaluator import evaluate_with_table


def best_hand(board_cards, player_cards):
    all_hands = combinations(board_cards + player_cards, 5)
    evaluations = [evaluate(hand) for hand in all_hands]
    return max(evaluations)


def determine_winners(board_cards, players_cards, evaluation_table):
    best_hands = [0] * len(players_cards)
    for i, player in enumerate(players_cards):
        seven_cards = board_cards + player
        evaluations = [evaluate_with_table(hand, evaluation_table)
                       for hand in combinations(seven_cards, 5)]
        best_hands[i] = max(evaluations)
    winning = max(best_hands)
    return [i for i, hand in enumerate(best_hands) if hand == winning]


def get_free_cards(board_cards, players):
    all_cards = [rank + suit for rank, suit in product(RANKS, SUITS)]
    used_cards = get_used_cards(board_cards, players)
    return [c for c in all_cards if c not in used_cards]


def get_used_cards(board_cards, players):
    used_cards = [card for card in board_cards if card != "?"]
    for player in players:
        used_cards += [card for card in player if card != "?"]
    return used_cards
