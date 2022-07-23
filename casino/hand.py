from cards.dealer import deal_cards
from cards.displayer import display_cards
from cards.evaluator import determine_winners
from utils.round_state import cheating
from utils.round_state import initial_state
from utils.round_state import update_round_state
from utils.round_state import players_left
from utils.round_state import round_ended
from utils.round_state import player_to_act
from utils.round_state import refresh
from utils.stack import compute_pot
from utils.stack import full_stack_for_all
from utils.stack import valid_stack

BOARD = "Board"
REVEAL_CARDS = [0, 3, 4, 5]


def update_players(players, state, revealed_board):
    for player in players:
        player.update_board_state(revealed_board, state)


def play_hand_return_remaining(players, stack, board, players_cards):
    assert valid_stack(stack), f"{stack} is not valid"
    state = initial_state(len(players))
    for i, s in enumerate(state):
        stack[i] -= s[1]

    next_player = 2 % len(players)
    round_number = 0
    for i, player in enumerate(players):
        player.set_cards(players_cards[i])
        player.set_all_players_names([player.name for player in players])
        player.stack = stack[i]

    while round_number < len(REVEAL_CARDS):
        update_players(players, state, board[:REVEAL_CARDS[round_number]])
        bet = 0 if not stack[next_player] else players[next_player].bet()
        if cheating(state, next_player, bet, stack[next_player]):
            print(f"{players[next_player].name} cheats: bet={bet}")
            bet = 0
        stack[next_player] -= bet
        players[next_player].stack = stack[next_player]
        update_round_state(state, next_player, bet)
        left = players_left(state)
        if len(left) == 1:
            return left
        if round_ended(state):
            update_players(players, state, board[:REVEAL_CARDS[round_number]])
            round_number += 1
            state = refresh(state)
        next_player = player_to_act(state)
    return players_left(state)


def play_hand_return_wins(players, evaluation_table):
    board, cards = deal_cards(len(players))
    stack = full_stack_for_all(len(players))
    old_stack = stack.copy()
    remaining = play_hand_return_remaining(players, stack, board, cards)
    remaining_cards = [cards[p] for p in remaining]

    print("SHOWDOWN:")
    for i, cards in enumerate(remaining_cards):
        display_cards(players[remaining[i]].name, cards)
    print("")

    winners = determine_winners(board, remaining_cards, evaluation_table)
    pot = compute_pot(old_stack, stack)
    winner_names = [players[remaining[i]].name for i in winners]
    wins = [s - old_stack[i] for i, s in enumerate(stack)]

    for i, _ in enumerate(wins):
        name = players[i].name
        if name in winner_names:
            wins[i] += pot // len(winners)
            print(f"{name} won {wins[i]} blinds")
        else:
            print(f"{name} lost {-wins[i]} blinds")
    print("")
    return wins
