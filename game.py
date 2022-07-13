from cards_dealer import deal_cards

PLAYING_WITH_BLINDS = True
GAME_WINNER = "Game winner"
NEXT_ROUND = "Next round"
SAME_ROUND = "Same round"
REVEAL_CARDS = [0, 3, 4, 5]


def first_not_folded(index, folded):
    while folded[index % len(folded)]:
        index += 1
    return index % len(folded)


def remaining_players(number_of_players, history):
    active_count = number_of_players
    folded = [False for _ in range(number_of_players)]
    action_left = number_of_players
    max_invested = 0
    invested = [0 for _ in range(number_of_players)]
    for index, bet in history:
        if action_left == 0:
            action_left = active_count
        # Fold
        if invested[index] + bet < max_invested:
            folded[index] = True
            active_count -= 1
            if active_count == 1:
                return (GAME_WINNER, [first_not_folded(0, folded)])
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
    playing = [index for index, val in enumerate(folded) if not val]
    if action_left:
        first = playing.index(first_not_folded(next_index, folded))
        playing = playing[first:] + playing[:first]
    return (SAME_ROUND, playing) if action_left else (NEXT_ROUND, playing)


def min_amount_to_call(player_index, history):
    investments = {player_index: 0}
    for player, bet in history:
        investments.setdefault(player, 0)
        investments[player] += bet
    return max(investments.values()) - investments[player_index]


def play_hand_return_remaining(players):
    history = [(0, 1), (1, 2)]
    next_player = 2 % len(players)
    round_number = 0
    board_cards, players_cards = deal_cards(len(players))
    for i, player in enumerate(players):
        name = f"player{i}"
        player.show_cards(name, players_cards[name])
    while True:
        players[next_player].update_history(history)
        bet = players[next_player].bet()
        history.append((next_player, bet))
        next_players = remaining_players(len(players), history)
        if next_players[0] != SAME_ROUND:
            if next_players[0] == GAME_WINNER:
                return next_players[1]
            round_number += 1
            if round_number == len(REVEAL_CARDS):
                for player in players:
                    for index in next_players[1]:
                        name = f"player{index}"
                        player.show_cards(name, players_cards[name])
                return next_players[1]
            for player in players:
                player.show_cards("board:",
                                  board_cards[:REVEAL_CARDS[round_number]])
        next_player = next_players[1][0]
