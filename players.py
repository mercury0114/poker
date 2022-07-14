from game import FULL_STACK
from game import min_amount_to_call


class Player:
    def __init__(self):
        self.history = None
        self.position = None
        self.cards = {}

    def update_history(self, history):
        self.history = history

    def show_cards(self, name, cards):
        self.cards[name] = cards

    def set_position(self, position):
        self.position = position


class CallPlayer(Player):
    def bet(self):
        call_amount = min_amount_to_call(self.position, self.history)
        return call_amount


class FoldPlayer(Player):
    @staticmethod
    def bet():
        return 0


class AllInPlayer(Player):
    def bet(self):
        invested = sum([bet for p, bet in self.history if p == self.position])
        return FULL_STACK - invested
