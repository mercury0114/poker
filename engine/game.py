from utils.round_state import cheating
from utils.round_state import initial_state
from utils.round_state import update_round_state
from utils.round_state import players_left
from utils.round_state import round_ended
from utils.round_state import player_to_act
from utils.round_state import refresh
from utils.stack import valid_stack

BOARD = "Board"
REVEAL_CARDS = [0, 3, 4, 5]


def update_players(players, state, revealed_board):
    for player in players:
        player.board = revealed_board
        player.state = state


def play_hand_return_remaining(players, stack, board, players_cards):
    assert valid_stack(stack), f"{stack} is not valid"
    state = initial_state(len(players))
    for i, s in enumerate(state):
        stack[i] -= s[1]

    next_player = 2 % len(players)
    round_number = 0
    for i, player in enumerate(players):
        player.cards = players_cards[i]
        player.set_all_players_names([player.name_ for player in players])
        player.stack = stack[i]

    while round_number < len(REVEAL_CARDS):
        update_players(players, state, board[:REVEAL_CARDS[round_number]])
        bet = 0 if not stack[next_player] else players[next_player].bet()
        if cheating(state, next_player, bet, stack[next_player]):
            print(f"{players[next_player].name_} cheats: bet={bet}")
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
