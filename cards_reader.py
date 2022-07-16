from evaluator import RANKS
from evaluator import SUITS
from utils import get_used_cards


def read_cards(file_name):
    f = open(file_name)
    board_cards = replace_10_by_t(f.readline().split()[1:])
    # Filling remaining board cards with question marks
    board_cards += ["?"] * (5 - len(board_cards))
    rows = list(f)
    names = [row.split()[0] for row in rows]
    players_cards = [replace_10_by_t(row.split()[1:]) for row in rows]
    return board_cards, names, players_cards


def replace_10_by_t(cards):
    return [card.replace("10", "T") for card in cards]


def check_cards_are_valid(board_cards, players):
    if len(board_cards) > 5:
        print("Too many board cards")
        exit()
    if not all(len(player) == 2 for player in players):
        print("Each player needs to have 2 cards, mark unknown with ?")
        exit(1)
    used_cards = get_used_cards(board_cards, players)
    if not all(valid_card(card) for card in used_cards):
        exit(1)
    if len(set(used_cards)) != len(used_cards):
        print("Duplicate cards are not allowed")
        exit(1)
    if len(players) < 2 or len(players) > 10:
        print("At least 2 players, at most 10 players")
        exit(1)


def valid_card(card):
    if card[0] not in RANKS or card[1] not in SUITS:
        print(f"{card} is invalid")
        return False
    return True
