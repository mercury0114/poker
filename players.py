from game import FULL_STACK


class Player:
    def __init__(self):
        self.state = None
        self.position = None
        self.players_count = None
        self.cards = {}

    def update_state(self, state):
        self.state = state

    def show_cards(self, name, cards):
        self.cards[name] = cards

    def set_position(self, position):
        self.position = position

    def set_players_count(self, count):
        self.players_count = count


class CallPlayer(Player):
    def bet(self):
        return max(s[1] for s in self.state) - self.state[self.position][1]


class FoldPlayer(Player):
    @staticmethod
    def bet():
        return 0


class AllInPlayer(Player):
    def bet(self):
        return FULL_STACK - self.state[self.position][1]
