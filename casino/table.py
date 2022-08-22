from cards.evaluator import read_evaluation_table
from casino.hand import play_hand_return_wins
from utils.stack import FULL_STACK

SMALL_BLIND_POSITION = 0
BIG_BLIND_POSITION = 1


def play_next_hand():
    print("Type 'y' to play next hand")
    return input() == "y"


def folded_hand(position, win):
    if position == SMALL_BLIND_POSITION:
        return win == -1
    if position == BIG_BLIND_POSITION:
        return win == -2
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
        self.change_stacks = True
        self.rotate_positions = True
        self.stacks = [FULL_STACK] * len(players)
        self.players = players
        self.table = read_evaluation_table()

    def display_hand_results(self, wins):
        for i, win in enumerate(wins):
            name = self.players[i].name
            print(f"{name} hand balance: {win} blinds")
        print("")

    def play(self):
        hands_count = 0
        balance = {player.name: 0 for player in self.players}
        hands_folded = {player.name: 0 for player in self.players}
        while play_next_hand():
            wins = play_hand_return_wins(self.players, self.stacks, self.table)
            self.display_hand_results(wins)
            for i, win in enumerate(wins):
                balance[self.players[i].name] += win
                hands_folded[self.players[i].name] += folded_hand(i, win)
            hands_count += 1
            if self.change_stacks:
                self.stacks = [self.stacks[i] + wins[i] for i, _ in enumerate(wins)]
                for player, stack in zip(self.players, self.stacks):
                    if not stack:
                        player.leave_table()
                self.players = [self.players[i] for i, _ in enumerate(wins) if self.stacks[i]]
                self.stacks = [stack for stack in self.stacks if stack]
            if self.rotate_positions:
                self.players = self.players[1:] + self.players[:1]
                self.stacks = self.stacks[1:] + self.stacks[:1]
        print_statistics(hands_count, hands_folded, balance)
