from game import min_amount_to_call


class Player:
    def __init__(self):
        self.history = None
        self.cards = None

    def update_history(self, history):
        self.history = history

    def show_cards(self, cards):
        self.cards = cards


class HumanPlayer(Player):
    def show_cards(self, cards):
        print(cards)

    def bet(self):
        print(self.history)
        return int(input())


class CallPlayer(Player):
    def __init__(self, position):
        super().__init__()
        self.position = position

    def bet(self):
        call_amount = min_amount_to_call(self.position, self.history)
        return call_amount


class CheckFoldPlayer(Player):
    @staticmethod
    def bet():
        return 0


class AllInPlayer(Player):
    @staticmethod
    def bet():
        return 100
