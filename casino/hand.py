from cards.dealer import deal_cards
from cards.displayer import display_cards
from cards.evaluator import rank_players
from utils.round_state import ALL_IN
from utils.round_state import PENDING
from utils.round_state import cheating
from utils.round_state import update_round_state
from utils.round_state import players_left
from utils.round_state import round_ended
from utils.round_state import player_to_act
from utils.round_state import refresh
from utils.stack import split_pot

BOARD = "Board"
REVEAL_CARDS = [0, 3, 4, 5]


def update_players(players, state, revealed_board, stacks):
    for player in players:
        player.update_board_state(revealed_board, state, stacks)


def play_hand_return_remaining(players, stacks, board, players_cards):
    state = [(PENDING, 0)] * len(players)
    update_round_state(state, 0, 1, stacks[0])
    update_round_state(state, 1, min(2, stacks[1]), stacks[1])
    for i, s in enumerate(state):
        stacks[i] -= s[1]
        if state[i][0] != ALL_IN:
            state[i] = (PENDING, state[i][1])

    next_player = 2 % len(players)
    round_number = 0
    for i, player in enumerate(players):
        player.set_cards(players_cards[i])
        player.stacks = stacks
        player.set_all_players_names([player.name for player in players])

    while round_number < len(REVEAL_CARDS):
        revealed = board[:REVEAL_CARDS[round_number]]
        update_players(players, state, revealed, stacks)
        bet = 0 if not stacks[next_player] else players[next_player].bet()
        if cheating(state, next_player, bet, stacks[next_player]):
            print(f"{players[next_player].name} cheats: bet={bet}")
            bet = 0
        update_round_state(state, next_player, bet, stacks[next_player])
        stacks[next_player] -= bet
        left = players_left(state)
        if len(left) == 1 or all(state[p][0] == ALL_IN for p in left):
            update_players(players, state, revealed, stacks)
            return left
        if round_ended(state):
            update_players(players, state, revealed, stacks)
            round_number += 1
            state = refresh(state)
        next_player = player_to_act(state)
    return players_left(state)


def play_hand_return_wins(players, old_stacks, evaluation_table):
    board, cards = deal_cards(len(players))
    stacks = old_stacks.copy()
    remaining = play_hand_return_remaining(players, stacks, board, cards)
    remaining_cards = [cards[p] for p in remaining]

    if len(remaining) > 1:
        print("SHOWDOWN:")
        for i, c in enumerate(remaining_cards):
            display_cards(players[remaining[i]].name, c)
        print("")

    ranks = rank_players(board, cards, evaluation_table)
    for i, _ in enumerate(ranks):
        if i not in remaining:
            ranks[i] = len(players)
    pot_split = split_pot(old_stacks, stacks.copy(), ranks)
    return [p - o + s for p, o, s in zip(pot_split, old_stacks, stacks)]
