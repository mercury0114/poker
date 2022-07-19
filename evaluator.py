from os.path import dirname
from collections import Counter
from itertools import combinations

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
SUITS = ["h", "d", "c", "s"]
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
        return (8, ranks)
    if 4 in counts:
        return (7, ranks)
    if 3 in counts and pairs == 1:
        return (6, ranks)
    if flush:
        return (5, ranks)
    if straight:
        return (4, ranks)
    return (3 in counts) + pairs, ranks


def best_hand_evaluation(board_cards, player_cards):
    number = len(board_cards) + len(player_cards)
    all_hands = combinations(board_cards + player_cards, min(number, 5))
    evaluations = [evaluate(hand) for hand in all_hands]
    return max(evaluations)


def read_evaluation_table():
    table_path = dirname(__file__) + "/evaluation_table.txt"
    f = open(table_path)
    rows = [row.split() for row in f]
    f.close()
    return {row[1]: int(row[0]) for row in rows}


def evaluate_with_table(cards, table):
    ranks = "".join([RANKS[rank] for rank in sorted_ranks(cards)])
    score = table[ranks]
    return score + FLUSH_SCORE if check_flush(cards) else score
