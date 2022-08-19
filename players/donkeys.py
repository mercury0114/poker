from players.player import Player


class CallPlayer(Player):
    def bet(self):
        return max(s[1] for s in self.state) - self.state[self.position][1]


class FoldPlayer(Player):
    @staticmethod
    def bet():
        return 0


class AllInPlayer(Player):
    def bet(self):
        return self.stacks[self.position]
