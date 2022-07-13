from cards_dealer import deal_flop_and_turn
from fast_evaluator import read_evaluation_table
from odds_calculator import loosing_odds
from odds_calculator import similar_odds
from simulator import perform_simulations

evaluation_table = read_evaluation_table()
while True:
    board_cards, players = deal_flop_and_turn(2)
    print(board_cards)
    for player in players:
        print(player, players[player])
    win_count = perform_simulations(board_cards, players, evaluation_table)
    worst_player = min(win_count, key=lambda p: win_count[p])
    print(f"Enter loosing odds for {worst_player}, type 'a' for an answer:")
    odds = loosing_odds(win_count, worst_player)
    user_odds = input()
    while user_odds != "a":
        if similar_odds(user_odds, odds):
            break
        print("try again")
        user_odds = input()
    if user_odds == "a":
        print(odds)