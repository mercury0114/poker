from cards_dealer import deal_cards

FULL_STACK = 200
PLAYING_WITH_BLINDS = True
GAME_ENDED = "Game ended"
NEXT_ROUND = "Next round"
SAME_ROUND = "Same round"
BOARD = "Board"
PLAYING = "PLAYING"
FOLDED = "FOLDED"
REVEAL_CARDS = [0, 3, 4, 5]


def players_status(number, history):
    _, remaining = game_state(number, history)
    return [PLAYING if p in remaining else FOLDED for p in range(number)]


def last_investment(number, history):
    invested = [0] * number
    max_invested = 0
    active_count = number
    action_left = number
    invested_up_to_this_round = 0
    for index, bet in history:
        # Fold
        if invested[index] + bet < max_invested:
            active_count -= 1
            action_left -= 1
        # Call
        if invested[index] + bet == max_invested:
            action_left -= 1
        # Raise
        if invested[index] + bet > max_invested:
            action_left = active_count - 1
            if PLAYING_WITH_BLINDS and index == 1 and invested[index] == 0:
                action_left = active_count
        invested[index] += bet
        max_invested = max(max_invested, invested[index])
        if action_left == 0:
            invested_up_to_this_round = max_invested
    return [max(0, money - invested_up_to_this_round) for money in invested]


def find_playing(index, playing):
    while not playing[index % len(playing)]:
        index += 1
    return index % len(playing)


def cheating(bet, player, history):
    if 0 < bet < min_amount_to_call(player, history):
        return True
    invested = sum([money for index, money in history if index == player])
    return invested + bet > FULL_STACK


# returns (round_state, list of remaining players)
def game_state(number_of_players, history):
    active_count = number_of_players
    playing = [True] * number_of_players
    action_left = number_of_players
    max_invested = 0
    invested = [0] * number_of_players
    for index, bet in history:
        if action_left == 0:
            action_left = active_count
        # Fold
        if invested[index] + bet < max_invested:
            playing[index] = False
            active_count -= 1
            if active_count == 1:
                return (GAME_ENDED, [find_playing(0, playing)])
            action_left -= 1
        # Call
        if invested[index] + bet == max_invested:
            action_left -= 1
        # Raise
        if invested[index] + bet > max_invested:
            action_left = active_count - 1
            if PLAYING_WITH_BLINDS and index == 1 and invested[index] == 0:
                action_left = active_count
        invested[index] += bet
        max_invested = max(max_invested, invested[index])
    next_index = history[-1][0] + 1 if action_left else 0
    remaining = [index for index, val in enumerate(playing) if val]
    if action_left:
        first = remaining.index(find_playing(next_index, playing))
        remaining = remaining[first:] + remaining[:first]
    else:
        if number_of_players == 2 and len(remaining) == 2:
            remaining = [1, 0]
    return (SAME_ROUND, remaining) if action_left else (NEXT_ROUND, remaining)


def min_amount_to_call(player_index, history):
    investments = {player_index: 0}
    for player, bet in history:
        investments.setdefault(player, 0)
        investments[player] += bet
    return max(investments.values()) - investments[player_index]


def update_players(players, history, board, round_number):
    for player in players:
        player.show_cards(BOARD, board[:REVEAL_CARDS[round_number]])
        player.update_history(history)


def play_hand_return_remaining(players):
    history = [(0, 1), (1, 2)]
    next_player = 2 % len(players)
    round_number = 0
    board, players_cards = deal_cards(len(players))
    for i, player in enumerate(players):
        name = f"player{i}"
        player.show_cards(name, players_cards[name])
        player.set_position(i)
        player.set_players_count(len(players))

    while round_number < len(REVEAL_CARDS):
        update_players(players, history, board, round_number)
        bet = players[next_player].bet()
        if cheating(bet, next_player, history):
            bet = 0
        history.append((next_player, bet))
        state = game_state(len(players), history)
        if state[0] == GAME_ENDED:
            return state[1]
        round_number += (state[0] == NEXT_ROUND)
        next_player = state[1][0]

    for player in players:
        for index in state[1]:
            name = f"player{index}"
            player.show_cards(name, players_cards[name])
    return sorted(state[1])
