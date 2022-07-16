from sys import path
path.append("../../../")

from game import FULL_STACK
from game import play_hand_return_remaining
from players import CallPlayer
from players import FoldPlayer
from players import Player
from round_state import call_amount


class CallOneLessCheater(Player):
    def bet(self):
        return max(0, call_amount(self.state, self.position) - 1)


class BetMoreThanStackCheater(Player):
    @staticmethod
    def bet():
        return FULL_STACK


players = [CallPlayer(), FoldPlayer(), CallOneLessCheater()]
assert play_hand_return_remaining(players) == [0, 1]

players = [BetMoreThanStackCheater(), FoldPlayer(), CallPlayer()]
assert play_hand_return_remaining(players) == [1, 2]

print("Passed")
