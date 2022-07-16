from sys import path
path.append("../../../")

from cards_dealer import deal_cards
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
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [0, 1]

players = [BetMoreThanStackCheater(), FoldPlayer(), CallPlayer()]
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [1, 2]

print("Passed")
