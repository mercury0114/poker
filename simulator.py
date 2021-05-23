import sys
from random import shuffle
from itertools import combinations, product
from evaluator import RANKS, SUITS
from fast_evaluator import ReadEvaluationTable, EvaluateWithTable

SIMULATION_COUNT = 10000

def Replace10ByT(cards):
    return [card.replace("10", "T") for card in cards]

def ReadCards(file_name):
    f = open(file_name)
    board_cards = Replace10ByT(f.readline().split()[1:])
    # Filling remaining board cards with question marks
    board_cards += ["?"] * (5 - len(board_cards))
    players = {line.split()[0] : Replace10ByT(line.split()[1:]) for line in f}
    return board_cards, players

def ValidCard(card):
    if card[0] not in RANKS or card[1] not in SUITS:
        print("{} is invalid".format(card))
        return False
    return True

def GetUsedCards(board_cards, players):
    used_cards = [card for card in board_cards if card != "?"]
    for player in players:
        used_cards += [card for card in players[player] if card != "?"]
    return used_cards

def CheckCardsAreValid(board_cards, players):
    if (len(board_cards) > 5):
        print("Too many board cards")
        exit()
    if not all(len(players[player]) == 2 for player in players):
        print("Each player needs to have 2 cards, unknown should be marked with ?")
        exit()
    used_cards = GetUsedCards(board_cards, players)
    if not all(ValidCard(card) for card in used_cards):
        exit()
    if len(set(used_cards)) != len(used_cards):
        print("Duplicate cards are not allowed")
        exit()
    if len(players) < 2 or len(players) > 10:
        print("At least 2 players, at most 10 players")
        exit()

def ChooseUnknownCards(cards, free_cards):
    return [free_cards.pop() if card == "?" else card for card in cards]

# WARNING: function modifies free_cards list
def SimulateGame(board_cards, players, free_cards):
    shuffle(free_cards)
    chosen_board = ChooseUnknownCards(board_cards, free_cards)
    chosen_players = {p : ChooseUnknownCards(players[p], free_cards) for p in players}
    return chosen_board, chosen_players

def DetermineWinners(board_cards, players, evaluation_table):
    best_hands = {}
    for player in players:
        seven_cards = GetUsedCards(board_cards, {player : players[player]})
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

board_cards, players = ReadCards(sys.argv[1])
CheckCardsAreValid(board_cards, players)

used_cards = GetUsedCards(board_cards, players)
all_cards = [rank + suit for rank, suit in product(RANKS, SUITS)]
free_cards = [c for c in all_cards if c not in used_cards]

print("Successfully read cards, performing simulations...")
evaluation_table = ReadEvaluationTable()
win_count = {}
for i in range(SIMULATION_COUNT):
    if (i % (SIMULATION_COUNT // 20) == 0):
        print("{}% done".format(100 * i // SIMULATION_COUNT))
    chosen_board, chosen_players = SimulateGame(board_cards, players, free_cards.copy())
    winners = DetermineWinners(chosen_board, chosen_players, evaluation_table)
    for winner in winners:
        win_count.setdefault(winner, 0)
        win_count[winner] += 1

print("All simulations completed, final results:")
for player in players:
    win_count.setdefault(player, 0)
    print("{}: {}%".format(player, (win_count[player] / SIMULATION_COUNT) * 100))
