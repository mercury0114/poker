from cards.evaluator import read_evaluation_table
from casino.hand import play_hand_return_wins


def play_next_hand():
    print("Type 'y' to play next hand")
    return input() == "y"


class Table:
    def __init__(self, players):
        self.rotate_positions = True
        self.__players = players
        self.__table = read_evaluation_table()

    def play(self):
        hands_played = 0
        balance = {player.name_: 0 for player in self.__players}
        while play_next_hand():
            wins = play_hand_return_wins(self.__players, self.__table)
            for i, win in enumerate(wins):
                balance[self.__players[i].name_] += win
            hands_played += 1
            if self.rotate_positions:
                self.__players = self.__players[1:] + self.__players[:1]
        if not hands_played:
            return
        print(f"played {hands_played} hands")
        print(f"total balance:   {balance}")
        average = {name: balance[name] // hands_played for name in balance}
        print(f"average balance: {average}")
