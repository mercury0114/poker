from time import sleep

from cards_dealer import display_cards
from game import play_hand_return_remaining
from game import players_status
from game import last_investment
from players import AllInPlayer
from players import CallPlayer
from players import Player


def display_row(row_name, row):
    formatted_row = [entry.ljust(8) for entry in row]
    print(f"{row_name}:".ljust(14) + ' '.join(formatted_row))


class Human(Player):
    def show_cards(self, name, cards):
        display_cards(name, cards)

    @staticmethod
    def bet():
        return int(input())

    def display_names(self):
        names = [f"player{i}" for i in range(self.players_count)]
        names[self.position] = "You"
        display_row("Name", names)

    def display_investments(self):
        investments = last_investment(self.players_count, self.history)
        display_row("Invested", [str(money) for money in investments])

    def display_statuses(self):
        statuses = players_status(self.players_count, self.history)
        display_row("Status", statuses)

    def display_new_action(self):
        self.display_names()
        self.display_investments()
        self.display_statuses()
        print("")
        sleep(3)

    def update_history(self, history):
        super().update_history(history)
        self.display_new_action()


players = [Human(), AllInPlayer(), CallPlayer()]
print(play_hand_return_remaining(players))
