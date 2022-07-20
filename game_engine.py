from cards.dealer import deal_cards
from cards.displayer import display_cards
from cards.evaluator import read_evaluation_table
from game import play_hand_return_remaining
from stack import compute_pot
from stack import full_stack_for_all
from utils import determine_winners


def play_hand_return_wins(players):
    evaluation_table = read_evaluation_table()
    board, cards = deal_cards(len(players))
    stack = full_stack_for_all(len(players))
    old_stack = stack.copy()
    remaining = play_hand_return_remaining(players, stack, board, cards)
    remaining_cards = [cards[p] for p in remaining]

    print("SHOWDOWN:")
    for i, cards in enumerate(remaining_cards):
        display_cards(players[remaining[i]].get_name(), cards)
    print("")

    winners = determine_winners(board, remaining_cards, evaluation_table)
    pot = compute_pot(old_stack, stack)
    winner_names = [players[remaining[i]].get_name() for i in winners]
    wins = [s - old_stack[i] for i, s in enumerate(stack)]

    for i, _ in enumerate(wins):
        name = players[i].get_name()
        if name in winner_names:
            wins[i] += pot // len(winners)
            print(f"{name} won {wins[i]} blinds")
        else:
            print(f"{name} lost {-wins[i]} blinds")
    print("")
    return wins


def play_next_hand():
    print("Type 'y' to play next hand")
    return input() == "y"


def play(players):
    hands_played = 0
    balance = [0] * len(players)
    while play_next_hand():
        hands_played += 1
        wins = play_hand_return_wins(players)
        balance = [x + y for x, y in zip(wins, balance)]
    if not hands_played:
        return
    print(f"played {hands_played} hands")
    print(f"total balance:   {balance}")
    print(f"average balance: {[win // hands_played for win in balance]}")
