from sys import path
path.append("../../../")

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
assert play_hand_return_remaining(players) == [2]

print("Passed")
