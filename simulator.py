import random
import sys
from itertools import combinations
from evaluator import RANKS, SUITS
from fast_evaluator import ReadEvaluationTable, EvaluateWithTable

SIMULATION_COUNT = 10000

def Replace10ByT(cards):
    return [card.replace("10", "T") for card in cards]

def ReadCards(file_name):
    cards_file = open(file_name, "r")
    community_cards = Replace10ByT(cards_file.readline().split()[1:])
    # Filling remaining community cards with question marks
    community_cards += ["?"] * (5 - len(community_cards))
    players = {}
    for line in cards_file:
        players[line.split()[0]] = Replace10ByT(line.split()[1:])
    return community_cards, players

def ValidCard(card):
    if card[0] not in RANKS or card[1] not in SUITS:
        print("{} is invalid".format(card))
        return False
    return True

def GetAllCards(community_cards, players):
    all_cards = [card for card in community_cards if card != "?"]
    for player in players:
        all_cards += [card for card in players[player] if card != "?"]
    return all_cards

def CheckCardsAreValid(community_cards, players):
    if (len(community_cards) > 5):
        print("Too many community cards")
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
    return [SelectNewCard(used_cards) if card == "?" else card for card in cards]

def SimulateGame(community_cards, players):
    used_cards = GetAllCards(community_cards, players)
    selected_community = SelectUnknownCards(community_cards, used_cards)
    selected_players = {}
    for player in players:
        selected_players[player] = SelectUnknownCards(players[player], used_cards)
    return selected_community, selected_players

def DetermineWinners(community_cards, players, evaluation_table):
    best_hands = {}
    for player in players:
        seven_cards = GetAllCards(community_cards, {player : players[player]})
        evaluations = [EvaluateWithTable(hand, evaluation_table) \
                       for hand in combinations(seven_cards, 5)]
        best_hands[player] = max(evaluations)
    winning_hand = max(best_hands.values())
    return [player for player in players if best_hands[player] == winning_hand]

# PROGRAM STARTS HERE
if (len(sys.argv) != 2):
    print("usage:")
    print("python3 main.py [cards_file.txt]")
    exit()

community_cards, players = ReadCards(sys.argv[1])
CheckCardsAreValid(community_cards, players)

print("Successfully read cards, performing simulations...")
evaluation_table = ReadEvaluationTable()
win_count = {}
for i in range(SIMULATION_COUNT):
    if (i % (SIMULATION_COUNT // 20) == 0):
        print("{}% done".format(100 * i / SIMULATION_COUNT))
    c, p = SimulateGame(community_cards, players)
    winners = DetermineWinners(c, p, evaluation_table)
    for winner in winners:
        win_count.setdefault(winner, 0)
        win_count[winner] += 1

print("All simulations completed, final results:")
for player in players:
    win_count.setdefault(player, 0)
    print("{}: {}%".format(player, (win_count[player] / SIMULATION_COUNT) * 100))
