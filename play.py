from time import sleep

from cards_dealer import deal_cards
from cards_dealer import display_cards
from evaluator import read_evaluation_table
from game import play_hand_return_remaining
from players import AllInPlayer
from players import CallPlayer
from players import Player
from round_state import FOLD
from stack import full_stack_for_all
from utils import determine_winners


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
        if self.state[self.position][0] != FOLD:
            sleep(3)

    def set_position(self, position):
        super().set_position(position)
        print(f"You are player{position}\n")

    def update_state(self, state):
        super().update_state(state)
        self.display_new_action()


players = [Human(), AllInPlayer(), CallPlayer()]
board, cards = deal_cards(len(players))
stack = full_stack_for_all(len(players))
remaining_players = play_hand_return_remaining(players, stack, board, cards)
print(remaining_players)
remaining_cards = [cards[p] for p in remaining_players]

evaluation_table = read_evaluation_table()
winners = determine_winners(board, remaining_cards, evaluation_table)
print([remaining_players[winner] for winner in winners])
names = [f"player{i}" for i in remaining_players]
