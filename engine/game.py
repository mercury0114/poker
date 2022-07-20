from round_state import cheating
from round_state import initial_state
from round_state import update_round_state
from round_state import players_left
from round_state import round_ended
from round_state import player_to_act
from round_state import refresh
from utils.stack import valid_stack

BOARD = "Board"
REVEAL_CARDS = [0, 3, 4, 5]


def update_players(players, state, revealed_board):
    for player in players:
        player.set_board(revealed_board)
        player.update_state(state)


def play_hand_return_remaining(players, stack, board, players_cards):
    assert valid_stack(stack), f"{stack} is not valid"
    state = initial_state(len(players))
    for i, s in enumerate(state):
        stack[i] -= s[1]

    next_player = 2 % len(players)
    round_number = 0
    for i, player in enumerate(players):
        player.set_players_count(len(players))
        player.set_cards(players_cards[i])
        player.set_position(i)
        player.set_stack(stack[i])

    while round_number < len(REVEAL_CARDS):
        update_players(players, state, board[:REVEAL_CARDS[round_number]])
        bet = 0 if not stack[next_player] else players[next_player].bet()
        if cheating(state, next_player, bet, stack[next_player]):
            bet = 0
        stack[next_player] -= bet
        players[next_player].set_stack(stack[next_player])
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
