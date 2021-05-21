# Utility script to evaluate hands:
#     hand1 = ["3h", "3c", "Kc", "Jh", "Jd"]
#     hand2 = ["2s", "2d", "Ad", "Qs", "Qd"]
#     hand3 = ["2h", "2s", "Ah", "Qc", "Qh"]
#     Evaluate(hand1) < Evaluate(hand2) # returns True
#     Evaluate(hand2) == Evaluate(hand3) # returns True
#     Evaluate(hand2) > Evaluate(hand3) # returns False
# If you want to know more info about the hand:
#     combo, tiebreaker = Evaluate(hand1)
#     print(COMBOS[combo]) # prints "Two pairs"
from collections import Counter

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
SUITS = ["h", "d", "c", "s"]
COMBOS = ["High card", "Pair", "Two pairs", "Three of a kind", "Straight", "Flush", \
          "Full house", "Four of a kind", "Straight flush"]
WHEEL = [3, 2, 1, 0, 12]

def Flush(cards):
    return all([card[1] == cards[0][1] for card in cards])

# returns a list of ranks in a tiebreaking order, "two" has a rank 0, "ace" has a rank 12, e.g:
# SortedRanks(["Jh", "Ad", "2c", "2h", "2s"]) = [0, 0, 0, 12, 9]
def SortedRanks(cards):
    ranks = [RANKS.index(card[0]) for card in cards]
    counter = Counter(ranks)
    ranks.sort(key=lambda rank: (counter[rank], rank), reverse=True)
    # Care must be taken for the lowest straight, "five" is the top card, not "ace"
    if ranks == [12, 3, 2, 1, 0]:
        return WHEEL
    return ranks

def Straight(cards):
    ranks = SortedRanks(cards)
    return ranks == list(range(ranks[0], ranks[0]-5, -1)) or ranks == WHEEL

def Counts(cards):
    return dict(Counter(SortedRanks(cards))).values()

def Four(cards):
    return 4 in Counts(cards)

def Three(cards):
    return 3 in Counts(cards)

def PairsCount(cards):
    return list(Counts(cards)).count(2)

# Returns (combo_index, tiebreaker). You can compare hands using regular >, ==, < comparators:
# Evaluate(hand1) > Evaluate(hand2) means that hand1 is stronger than hand2.
# Evaluate(hand1) == Evaluate(hand2) means that hand1 and hand2 are equally strong.
# combo_index is an index to the COMBOS array (defined at the top). e.g. 4 means "Straight".
def Evaluate(cards):
    tiebreaker = SortedRanks(cards)
    straight = Straight(cards)
    flush = Flush(cards)
    if straight and flush:
        return (8, tiebreaker)
    if Four(cards):
        return (7, tiebreaker)
    if Three(cards) and PairsCount(cards) == 1:
        return (6, tiebreaker)
    if flush:
        return (5, tiebreaker)
    if straight:
        return (4, tiebreaker)
    if Three(cards):
        return (3, tiebreaker)
    if PairsCount(cards) == 2:
        return (2, tiebreaker)
    if PairsCount(cards) == 1:
        return (1, tiebreaker)
    return (0, tiebreaker)
