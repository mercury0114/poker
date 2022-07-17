from cards_dealer import deal_cards
from cards_dealer import display_cards
from evaluator import read_evaluation_table
from game import play_hand_return_remaining
from players import AllInPlayer
from players import Human
from players import CallPlayer
from stack import compute_pot
from stack import full_stack_for_all
from utils import determine_winners


def play(players):
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
    losses = [s - old_stack[i] for i, s in enumerate(stack)]
    for i, loss in enumerate(losses):
        name = players[i].get_name()
        if name in winner_names:
            print(f"{name} won {loss + pot // len(winners)} blinds")
        else:
            print(f"{name} lost {-loss} blinds")


you = Human()
players = [you, AllInPlayer(), CallPlayer()]
play(players)
