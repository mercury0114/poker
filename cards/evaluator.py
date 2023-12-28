from os.path import dirname
from collections import Counter
from itertools import combinations

from cards.notation import RANKS

COMBOS = ["High card", "Pair", "Two pairs", "Three of a kind", "Straight",
          "Flush", "Full house", "Four of a kind", "Straight flush"]
WHEEL = [3, 2, 1, 0, 12]
FLUSH_SCORE = 5863


def check_flush(cards):
    if len(cards) != 5:
        return False
    return all(map(lambda card: card[1] == cards[0][1], cards))


def check_straight(ranks):
    if len(ranks) != 5:
        return False
    return ranks in [list(range(ranks[0], ranks[0] - 5, -1)), WHEEL]


# returns a list of ranks in a tiebreaking order,
# "two" has a rank 0, "ace" has a rank 12, e.g:
# SortedRanks(["Jh", "Ad", "2c", "2h", "2s"]) = [0, 0, 0, 12, 9]
def sorted_ranks(cards):
    ranks = [RANKS.index(card[0]) for card in cards]
    counter = Counter(ranks)
    ranks.sort(key=lambda rank: (counter[rank], rank), reverse=True)
    # Careful with the lowest straight, "five" is the top card, not "ace"
    return WHEEL if ranks == [12, 3, 2, 1, 0] else ranks


# Returns (combo_index, tiebreaker).
# You can compare hands using regular >, ==, < comparators:
# Evaluate(hand1) > Evaluate(hand2) means hand1 is stronger than hand2.
# Evaluate(hand1) == Evaluate(hand2) means hand1 and hand2 are equally strong.
# combo_index is an index to the COMBOS array. e.g. 4 means "Straight".
def evaluate(cards):
    ranks = sorted_ranks(cards)
    straight = check_straight(ranks)
    flush = check_flush(cards)
    counts = dict(Counter(ranks)).values()
    pairs = list(counts).count(2)
    if straight and flush:
        return (COMBOS.index("Straight flush"), ranks)
    if 4 in counts:
        return (COMBOS.index("Four of a kind"), ranks)
    if 3 in counts and pairs == 1:
        return (COMBOS.index("Full house"), ranks)
    if flush:
        return (COMBOS.index("Flush"), ranks)
    if straight:
        return (COMBOS.index("Straight"), ranks)
    return (3 in counts) * 3 + pairs, tuple(ranks)


def determine_winners(board_cards, players_cards, evaluation_table):
    best_hands = [0] * len(players_cards)
    for i, player in enumerate(players_cards):
        seven_cards = board_cards + player
        evaluations = [evaluate_with_table(hand, evaluation_table)
                       for hand in combinations(seven_cards, 5)]
        best_hands[i] = max(evaluations)
    winning = max(best_hands)
    return [i for i, hand in enumerate(best_hands) if hand == winning]


def rank_players(board, cards, table):
    evaluations = [best_evaluation_with_table(board, c, table) for c in cards]
    return [sorted(evaluations, reverse=True).index(e) for e in evaluations]


def best_evaluation(board_cards, player_cards):
    number = len(board_cards) + len(player_cards)
    all_hands = combinations(board_cards + player_cards, min(number, 5))
    evaluations = [evaluate(hand) for hand in all_hands]
    return max(evaluations)


# board + player must contain >= 5 cards
def best_evaluation_with_table(board, player, table):
    all_hands = combinations(board + player, 5)
    evaluations = (evaluate_with_table(hand, table) for hand in all_hands)
    return max(evaluations)


def read_evaluation_table():
    table_path = dirname(__file__) + "/evaluation_table.txt"
    f = open(table_path)
    rows = [row.split() for row in f]
    f.close()
    return {row[1]: int(row[0]) for row in rows}


# Better hand will be evaluated to a higher number. Number output does not
# have a meaning, unlike output of the evaluate(cards) function
def evaluate_with_table(cards, table):
    ranks = "".join([RANKS[rank] for rank in sorted_ranks(cards)])
    score = table[ranks]
    return score + FLUSH_SCORE if check_flush(cards) else score
