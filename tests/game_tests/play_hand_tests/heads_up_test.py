from sys import path
path.append("../../../")

from cards_dealer import deal_cards
from round_state import call_amount
from game import play_hand_return_remaining
from players import FoldPlayer
from players import Player


class BetLess10Player(Player):
    def bet(self):
        return 9 if call_amount(self.state, self.position) < 10 else 0


class BetIfNotCallPlayer(Player):
    def bet(self):
        amount = call_amount(self.state, self.position)
        return amount if amount else 20


players = [BetLess10Player(), BetIfNotCallPlayer()]
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [1]

players = [BetIfNotCallPlayer(), BetLess10Player()]
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [0, 1]

# Non heads up
players = [BetIfNotCallPlayer(), BetLess10Player(), FoldPlayer()]
board, cards = deal_cards(len(players))
assert play_hand_return_remaining(players, board, cards) == [0]

print("Passed")
