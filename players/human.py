from cards.displayer import display_cards
from cards.displayer import display_row
from players.player import Player
from utils.request_input import request_input


class Human(Player):
    @staticmethod
    def bet():
        print("Enter your bet amount")
        return int(request_input(lambda x: x.isdigit()))

    @staticmethod
    def get_name():
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

    def update_state(self, state):
        super().update_state(state)
        self.display_new_action()

    def set_cards(self, cards):
        super().set_cards(cards)
        display_cards("Your cards", cards)
