from players.player import Player
from round_state import call_amount
from utils import best_hand

LETTERS = ["J", "Q", "K", "A"]


# Calls preflop if:
#     a) less than 20 to call
#     b) has a pair or J/Q/K/A
# Calls postflop if has a pair or better
class WithPairPlayer(Player):
    def bet(self):
        amount = call_amount(self.state, self.position)
        if len(self.board) == 0:
            if self.cards[0][0] == self.cards[1][0]:
                return amount
            suit1 = self.cards[0][0]
            suit2 = self.cards[1][0]
            if suit1 in LETTERS or suit2 in LETTERS:
                return amount
            return amount if amount < 20 else 0
        hand = best_hand(self.board, self.cards)
        return amount if hand[0] >= 1 else 0
