from cards.evaluator import read_evaluation_table
from casino.hand import play_hand_return_wins


def play_next_hand():
    print("Type 'y' to play next hand")
    return input() == "y"


class Table:
    def __init__(self, players):
        self.rotate_positions = True
        self.players = players
        self.table = read_evaluation_table()

    def play(self):
        hands_played = 0
        balance = {player.name: 0 for player in self.players}
        while play_next_hand():
            wins = play_hand_return_wins(self.players, self.table)
            for i, win in enumerate(wins):
                balance[self.players[i].name] += win
            hands_played += 1
            if self.rotate_positions:
                self.players = self.players[1:] + self.players[:1]
        if not hands_played:
            return
        print(f"played {hands_played} hands")
        print(f"total balance:   {balance}")
        average = {name: balance[name] // hands_played for name in balance}
        print(f"average balance: {average}")
