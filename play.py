from time import sleep

from cards_dealer import deal_cards
from cards_dealer import display_cards
from game import play_hand_return_remaining
from players import AllInPlayer
from players import CallPlayer
from players import Player


def display_row(row_name, row):
    formatted_row = [entry.ljust(10) for entry in row]
    print(f"{row_name}:".ljust(10) + ' '.join(formatted_row))


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
        investments = [s[1] for s in self.state]
        display_row("Invested", [str(money) for money in investments])

    def display_statuses(self):
        statuses = [s[0] for s in self.state]
        display_row("Status", statuses)

    def display_new_action(self):
        self.display_names()
        self.display_investments()
        self.display_statuses()
        print("")
        sleep(3)

    def set_position(self, position):
        super().set_position(position)
        print(f"You are player{position}\n")

    def update_state(self, state):
        super().update_state(state)
        self.display_new_action()


players = [Human(), AllInPlayer(), CallPlayer()]
board, cards = deal_cards(len(players))
remaining = play_hand_return_remaining(players, board, cards)
