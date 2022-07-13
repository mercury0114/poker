from sys import path
path.append("../../")

from game import min_amount_to_call
from game import play_hand_return_remaining
from players import CheckFoldPlayer
from players import Player


class CallLess10Player(Player):
    def __init__(self, position):
        self.position = position

    def bet(self):
        call_amount = min_amount_to_call(self.position, self.history)
        return call_amount if call_amount < 10 else 0


class Bet10Player(Player):
    @staticmethod
    def bet():
        return 10


players = [CallLess10Player(0), CheckFoldPlayer(), Bet10Player()]
assert play_hand_return_remaining(players) == [2]

print("call_once_does_not_win_test.py passed")
