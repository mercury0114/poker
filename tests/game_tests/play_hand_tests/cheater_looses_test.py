from sys import path
path.append("../../../")

from game import FULL_STACK
from game import min_amount_to_call
from game import play_hand_return_remaining
from players import CallPlayer
from players import FoldPlayer
from players import Player


class CallOneLessCheater(Player):
    def bet(self):
        call_amount = min_amount_to_call(self.position, self.history)
        if call_amount > 0:
            call_amount -= 1
        return call_amount


class BetMoreThanStackCheater(Player):
    @staticmethod
    def bet():
        return FULL_STACK


players = [CallPlayer(), FoldPlayer(), CallOneLessCheater()]
assert play_hand_return_remaining(players) == [0, 1]

players = [BetMoreThanStackCheater(), FoldPlayer(), CallPlayer()]
assert play_hand_return_remaining(players) == [1, 2]

print("Passed")
