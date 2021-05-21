from collections import Counter

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
SUITS = ["h", "d", "c", "s"]
COMBOS = ["High card", "Pair", "Two pairs", "Three of a kind", "Straight", "Flush", \
          "Full house", "Four of a kind", "Straight flush"]

def Flush(cards):
    return all([card[1] == cards[0][1] for card in cards])

# returns a list of sorted card ranks, lowest card 2 has a rank 0, ace has a rank 12, e.g:
# SortedRanks(["Jh", "Ad", "2c", "2h", "2s"]) = [12, 8, 0, 0, 0]
def SortedRanks(cards):
    ranks = [RANKS.index(card[0]) for card in cards]
    ranks.sort(reverse=True)
    return ranks

def Straight(cards):
    ranks = SortedRanks(cards)
    return ranks == list(range(ranks[0], ranks[0]-5, -1)) or ranks == [12, 3, 2, 1, 0]

def Counts(cards):
    ranks = [card[0] for card in cards]
    return dict(Counter(ranks)).values()

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
    ranks = SortedRanks(cards)
    straight = Straight(cards)
    flush = Flush(cards)
    if straight and flush:
        # for straight, tiebreaker is the top straight card
        return (8, ranks[0])
    if Four(cards):
        return (7, ranks)
    if Three(cards) and PairsCount(cards) == 1:
        return (6, ranks)
    if flush:
        return (5, ranks)
    if straight:
        # for straight, tiebreaker is the top straight card
        return (4, ranks[0])
    if Three(cards):
        return (3, ranks)
    if PairsCount(cards) == 2:
        return (2, ranks)
    if PairsCount(cards) == 1:
        return (1, ranks)
    return (0, ranks)

print(Evaluate(["2h", "Jh", "Qh", "Th", "3c"]))
print(Evaluate(["2s", "Jc", "Td", "Qs", "3d"]))
