from cards.dealer import deal_cards
from cards.evaluator import read_evaluation_table
from utils.simulator import determine_winners
from utils.simulator import get_free_cards
from itertools import combinations


def _next_round():
    print("Type 'y' for next round")
    return input() == "y"


def _opponent_won(board, player_and_opponent, evaluation_table):
    return determine_winners(board, player_and_opponent, evaluation_table) == [1]


def _find_better_hands(evaluation_table, board, your_cards):
    free_cards = get_free_cards(board, [your_cards])
    better_hands = []
    for opponent in combinations(free_cards, 2):
        if _opponent_won(board, [your_cards, list(opponent)], evaluation_table):
            better_hands.append(opponent)
    return better_hands


evaluation_table = read_evaluation_table()
while _next_round():
    board, players = deal_cards(players_number=1)
    better_hands = _find_better_hands(
        evaluation_table, board, your_cards=players[0])
    while len(better_hands) > 50:  # search until we find an interesting hand
        board, players = deal_cards(players_number=1)
        better_hands = _find_better_hands(
            evaluation_table, board, your_cards=players[0])

    print(board, players[0])
    if int(input()) == len(better_hands):
        print("Correct")
    else:
        print(f"Incorrect, correct answer was {len(better_hands)}")
        print(better_hands)
