import random
import sys

RANKS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
SUITS = ["H", "D", "C", "S"]

def ReadCards(file_name):
    cards_file = open(file_name, "r")
    community_cards = cards_file.readline().split()[1:]
    players = {}
    for line in cards_file:
        players[line.split()[0]] = line.split()[1:]
    return community_cards, players

def ValidCard(card):
    rank, suit = card[:-1], card[-1]
    if rank not in RANKS or suit not in SUITS:
        print("{} is invalid".format(card))
        return False
    return True

def GetAllCards(community_cards, players):
    all_cards = [card for card in community_cards if card != "?"]
    for player in players:
        all_cards += [card for card in players[player] if card != "?"]
    return all_cards

def CheckCardsAreValid(community_cards, players):
    if (len(community_cards) != 5):
        print("Community cards must be 5, unknown should be marked with ?")
        exit()
    for player in players:
        if len(players[player]) != 2:
            print("Each player needs to have 2 cards, unknown should be marked with ?")
            exit()
    all_cards = GetAllCards(community_cards, players)
    if not all(ValidCard(card) for card in all_cards):
        exit()
    if len(set(all_cards)) != len(all_cards):
        print("Duplicate cards are not allowed")
        exit()
    if len(players) < 2 or len(players) > 10:
        print("At least 2 players, at most 10 players")
        exit()

def SelectNewCard(used_cards):
    while True:
        card = random.choice(RANKS) + random.choice(SUITS)
        if card not in used_cards:
            used_cards.append(card)
            return card

def SelectUnknownCards(cards, used_cards):
    return [SelectNewCard(used_cards) if card == "?" else card \
            for card in cards]

def SimulateGame(community_cards, players):
    used_cards = GetAllCards(community_cards, players)
    selected_community = SelectUnknownCards(community_cards, used_cards)
    selected_players = {}
    for player in players:
        selected_players[player] = SelectUnknownCards(players[player], used_cards)
    return selected_community, selected_players

def Flush(cards):
    return len(set([card[1] for card in cards])) == 1

# Returns highest straight card, None if no straight
def Straight(cards):
    ranks = [card[0] for card in cards]
    ranks.sort(key = lambda e : RANKS.index(e))
    string = "".join(ranks)
    if string in ["A5432", "65432", "76543", "87654", "98765", "T9876", "JT987", \
                  "QJT98", "KQJT9", "AKQJT"]:
        return "5" if string == "A5432" else string[0]

def Fours(cards):
    ranks = [card[0] for card in cards]
    counts = {}
    for rank in ranks:
        counts.setdefault(rank, 0)
        counts[rank] += 1
    return 4 in counts.values()

def Score(cards):
    ranks = [card[0] for card in cards]
    score1 = 0
    counts = {}
    for rank in ranks:
        score += len(RANKS) - RANKS.index(rank) - 1
        score *= 13
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

def DetermineWinner(community_cards, players):
    return

# PROGRAM STARTS HERE
if (len(sys.argv) != 2):
    print("usage:")
    print("python3 main.py [position_file.txt]")
    exit()

community_cards, players = ReadCards(sys.argv[1])
CheckCardsAreValid(community_cards, players)

print("Cards file read succesfully, performing simulations...")
c, p = SimulateGame(community_cards, players)
