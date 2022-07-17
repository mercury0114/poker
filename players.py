from time import sleep

from stack import FULL_STACK
from cards_dealer import display_cards
from cards_dealer import display_row
from round_state import FOLD


class Player:
    def __init__(self):
        self.state = None
        self.position = None
        self.players_count = None
        self.cards = None
        self.board = None

    def update_state(self, state):
        self.state = state

    def set_cards(self, cards):
        self.cards = cards

    def set_board(self, board):
        self.board = board

    def set_position(self, position):
        self.position = position

    def set_players_count(self, count):
        self.players_count = count

    def get_name(self):
        return f"player{self.position}"


class Human(Player):
    @staticmethod
    def bet():
        return int(input())

    def get_name(self):
        return "You"

    def display_names(self):
        names = [f"player{i}" for i in range(self.players_count)]
        names[self.position] = "You"
        display_row("Name", names)

    def display_investments(self):
        investments = [s[1] for s in self.state]
        display_row("Invested", [str(money) for money in investments])

    def display_statuses(self):
        statuses = [s[0] for s in self.state]
        display_row("Status", statuses)

    def display_new_action(self):
        display_cards("Board", self.board)
        self.display_names()
        self.display_investments()
        self.display_statuses()
        print("")
        if self.state[self.position][0] != FOLD:
            sleep(1)

    def set_position(self, position):
        super().set_position(position)
        print(f"You are player{position}\n")

    def update_state(self, state):
        super().update_state(state)
        self.display_new_action()

    def set_cards(self, cards):
        super().set_cards(cards)
        display_cards("Your cards", cards)


class CallPlayer(Player):
    def bet(self):
        return max(s[1] for s in self.state) - self.state[self.position][1]


class FoldPlayer(Player):
    @staticmethod
    def bet():
        return 0


class AllInPlayer(Player):
    def bet(self):
        return FULL_STACK - self.state[self.position][1]
