from random import choice

from cards.evaluator import best_hand_evaluation
from players.player import Player
from round_state import call_amount


LETTERS = ["Q", "K", "A"]


def reraise():
    return choice([0, 0, 0, 1])


# Calls preflop if:
#     a) not more than 10 to call
#     b) has a pair or Q/K/A
# Calls postflop if has a pair or better
# Raises 25% of the time with a good hand
class WithPairPlayer(Player):
    def good_hand(self):
        if len(self.board) == 0:
            if self.cards[0][0] == self.cards[1][0]:
                return True
            rank1 = self.cards[0][0]
            rank2 = self.cards[1][0]
            return rank1 in LETTERS or rank2 in LETTERS
        board_evaluation = best_hand_evaluation(self.board, [])[0]
        hand_evaluation = best_hand_evaluation(self.board, self.cards)[0]
        return hand_evaluation > board_evaluation or hand_evaluation > 3

    def bet(self):
        amount = call_amount(self.state, self.position)
        if self.good_hand():
            return amount * 2 + 5 if reraise() else amount
        return amount if amount <= 10 else 0
