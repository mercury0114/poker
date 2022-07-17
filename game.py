from cards_dealer import deal_cards
from stack import valid_stack
from round_state import cheating
from round_state import initial_state
from round_state import update_round_state
from round_state import players_left
from round_state import round_ended
from round_state import player_to_act
from round_state import refresh

BOARD = "Board"
REVEAL_CARDS = [0, 3, 4, 5]


def update_players(players, state, board, round_number):
    for player in players:
        player.show_cards(BOARD, board[:REVEAL_CARDS[round_number]])
        player.update_state(state)


def play_hand_return_remaining(players, stack, board, players_cards):
    assert valid_stack(stack), f"{stack} is not valid"
    state = initial_state(len(players))
    for i, s in enumerate(state):
        stack[i] -= s[1]

    next_player = 2 % len(players)
    round_number = 0
    board, players_cards = deal_cards(len(players))
    for i, player in enumerate(players):
        name = f"player{i}"
        player.set_players_count(len(players))
        player.show_cards(name, players_cards[i])
        player.set_position(i)

    while round_number < len(REVEAL_CARDS):
        update_players(players, state, board, round_number)
        bet = players[next_player].bet()
        if cheating(state, next_player, bet, stack[next_player]):
            bet = 0
        stack[next_player] -= bet
        update_round_state(state, next_player, bet)
        left = players_left(state)
        if len(left) == 1:
            return left
        if round_ended(state):
            update_players(players, state, board, round_number)
            round_number += 1
            state = refresh(state)
        next_player = player_to_act(state)

    for player in players:
        for index in players_left(state):
            name = f"player{index}"
            player.show_cards(name, players_cards[index])
    return players_left(state)
