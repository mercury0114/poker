from cards.dealer import deal_flop_and_turn
from cards.evaluator import read_evaluation_table
from utils.odds_calculator import loosing_odds
from utils.odds_calculator import similar_odds
from utils.simulator import perform_simulations

evaluation_table = read_evaluation_table()
print("type 'a' for an answer")
print("type 'q' to quit\n")
while True:
    board_cards, players_cards = deal_flop_and_turn(2)
    print(board_cards)
    names = [f"player{i}" for i in range(len(players_cards))]
    for name, cards in zip(names, players_cards):
        print(f"{name}: {cards}")
    win_count = perform_simulations(board_cards,
                                    names,
                                    players_cards,
                                    evaluation_table)
    worst_player = min(win_count, key=lambda p: win_count[p])
    print(f"Enter loosing odds for {worst_player}")
    odds = loosing_odds(win_count, worst_player)
    user_odds = input()
    while user_odds not in ["a", "q"]:
        if similar_odds(user_odds, odds):
            break
        print("try again")
        user_odds = input()
    if user_odds == "a":
        print(odds)
    if user_odds == "q":
        exit()
