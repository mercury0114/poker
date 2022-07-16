from sys import path
path.append("../../../")

from cards_dealer import deal_cards
from game import play_hand_return_remaining
from players import FoldPlayer
from players import Player
from round_state import call_amount


class CallLess10Player(Player):
    def __init__(self, position):
        super().__init__()
        self.position = position

    def bet(self):
        amount = call_amount(self.state, self.position)
        return amount if amount < 10 else 0


class Bet10Player(Player):
    @staticmethod
    def bet():
        return 10


players = [CallLess10Player(0), FoldPlayer(), Bet10Player()]
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [2]

print("Passed")
