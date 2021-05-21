from collections import Counter

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
SUITS = ["h", "d", "c", "s"]
COMBOS = ["High card", "Pair", "Two pairs", "Three of a kind", "Straight", "Flush", \
          "Full house", "Four of a kind", "Straight flush"]

def Flush(cards):
    return len(set([card[1] for card in cards])) == 1

# Returns the highest card index of a straight, None if no straight
def Straight(cards):
    ranks = [card[0] for card in cards]
    ranks.sort(key = lambda e : RANKS.index(e))
    string = "".join(ranks)
    if string in ["2345A", "23456", "34567", "45678", "56789", "6789T", "789TJ", "89TJQ", "9TJQK", "TJQKA"]:
        return RANKS.index("5") if string == "2345A" else RANKS.index(string[-1])

def Counts(cards):
    ranks = [card[0] for card in cards]
    return dict(Counter(ranks)).values()

def Four(cards):
    return 4 in Counts(cards)

def Three(cards):
    return 3 in Counts(cards)

def PairsCount(cards):
    return list(Counts(cards)).count(2)

def Score(cards):
    ranks = [card[0] for card in cards]
    ranks.sort(key = lambda e : -RANKS.index(e))
    score1 = 0
    counts = {}
    for rank in ranks:
        score1 += RANKS.index(rank)
        score1 *= 13
        counts.setdefault(rank, 0)
        counts[rank] += 1
    c = [0, 0, 0, 0]
    for rank in counts:
        c[4-counts[rank]] += 1
    score2 = 0
    for n in c:
        score2 += n
        score2 *= 13
    return score2 * (13 ** 5) + score1

# Returns (combo_index, score). You can compare hands using regular >, ==, < comparators:
# Evaluate(hand1) > Evaluate(hand2) means that hand1 is stronger than hand2.
# Evaluate(hand1) == Evaluate(hand2) means that hand1 and hand2 are equally strong.
#
# combo_index is an index to the COMBOS array (see at the top of the file), for example:
# combo_index == 2 stands for "Two pairs", combo_index == 3 stands for "Three of a kind", thus
# (2, 100) is better than (2, 50)
# (2, 100) is worse than (3, 50)
def Evaluate(cards):
    score = Score(cards)
    straight = Straight(cards)
    flush = Flush(cards)
    if straight and flush:
        return (8, straight)
    if Four(cards):
        return (7, score)
    if Three(cards) and PairsCount(cards) == 1:
        return (6, score)
    if flush:
        return (5, score)
    if straight:
        return (4, straight)
    if Three(cards):
        return (3, score)
    if PairsCount(cards) == 2:
        return (2, score)
    if PairsCount(cards) == 1:
        return (1, score)
    return (0, score)
