from cards.evaluator import read_evaluation_table
from casino.hand import play_hand_return_wins

SMALL_BLIND_POSITION = 0


def play_next_hand():
    print("Type 'y' to play next hand")
    return input() == "y"


def folded_hand(position, win):
    if position == SMALL_BLIND_POSITION:
        return win == -1
    # TODO(mercury0114): handle big blind position correctly
    return win == 0


def print_statistics(hands_count, hands_folded, balance):
    if not hands_count:
        return
    print(f"{hands_count} hands")
    print(f"hands folded: {hands_folded}")
    print(f"total balance:   {balance}")
    average = {name: balance[name] // hands_count for name in balance}
    print(f"average balance: {average}")


class Table:
    def __init__(self, players):
        self.rotate_positions = True
        self.players = players
        self.table = read_evaluation_table()

    def play(self):
        hands_count = 0
        balance = {player.name: 0 for player in self.players}
        hands_folded = {player.name: 0 for player in self.players}
        while play_next_hand():
            wins = play_hand_return_wins(self.players, self.table)
            for i, win in enumerate(wins):
                balance[self.players[i].name] += win
                hands_folded[self.players[i].name] += folded_hand(i, win)
            hands_count += 1
            if self.rotate_positions:
                self.players = self.players[1:] + self.players[:1]
        print_statistics(hands_count, hands_folded, balance)
