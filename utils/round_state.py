# An example round state:
# [ (FOLD, 0), (CHECK, 0), (RAISE, 6), (CALL, 6), (ALL_IN, 0), (PENDING, 0) ]
# means that:
# Player 0 has folded (in the previous round)
# Player 1 has checked
# Player 2 has raised to 6
# Player 3 has called a raise
# Player 4 has moved all in with his last 6 chips
# Player 5 has still left to act

ALL_IN = "ALL_IN"
CALL = "CALL"
CHECK = "CHECK"
FOLD = "FOLD"
PENDING = "PENDING"
RAISE = "RAISE"

SMALL_BLIND = (PENDING, 1)
BIG_BLIND = (PENDING, 2)


def call_amount(state, player):
    return max(s[1] for s in state) - state[player][1]


def cheating(state, player, bet, stack):
    if not bet or bet == stack:
        return False
    max_investment = max(s[1] for s in state)
    return bet > stack or state[player][1] + bet < max_investment


def initial_state(players_number):
    state = [(PENDING, 0)] * players_number
    state[0] = SMALL_BLIND
    state[1] = BIG_BLIND
    return state


def player_to_act(state):
    if state == initial_state(len(state)):
        return 2 % len(state)
    if round_ended(state):
        state = refresh(state)
    index = (state == refresh(state) and len(state) == 2)
    generator = (i for i, v in enumerate(state)
                 if v[0] not in (ALL_IN, FOLD, PENDING))
    index = next(generator, index)
    while state[index][0] != PENDING:
        index = (index + 1) % len(state)
    return index


def players_left(state):
    return [i for i, s in enumerate(state) if s[0] != FOLD]


def round_ended(state):
    return all(s[0] != PENDING for s in state)


def refresh(state):
    refreshed = state.copy()
    for i, s in enumerate(refreshed):
        status = s[0] if s[0] in [ALL_IN, FOLD] else PENDING
        refreshed[i] = (status, 0)
    return refreshed


def update_round_state(state, player, bet, stack=1000000):
    max_investment = max(s[1] for s in state)
    player_investment = state[player][1] + bet
    if player_investment < max_investment:
        state[player] = (FOLD, state[player][1])
    if bet == 0 and player_investment == max_investment:
        state[player] = (CHECK, player_investment)
    if bet > 0 and player_investment == max_investment:
        state[player] = (CALL, player_investment)
    if player_investment > max_investment:
        for i, s in enumerate(state):
            if s[0] not in (ALL_IN, FOLD):
                state[i] = (PENDING, s[1])
        state[player] = (RAISE, player_investment)
    if bet == stack:
        state[player] = (ALL_IN, player_investment)
