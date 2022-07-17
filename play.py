from time import sleep

from cards_dealer import deal_cards
from cards_dealer import display_cards
from evaluator import read_evaluation_table
from game import play_hand_return_remaining
from players import AllInPlayer
from players import CallPlayer
from players import Player
from round_state import FOLD
from stack import compute_pot
from stack import full_stack_for_all
from utils import determine_winners


def display_row(row_name, row):
    formatted_row = [entry.ljust(10) for entry in row]
    print(f"{row_name}:".ljust(10) + ' '.join(formatted_row))


class Human(Player):
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


evaluation_table = read_evaluation_table()
players = [Human(), AllInPlayer(), CallPlayer()]
board, cards = deal_cards(len(players))
stack = full_stack_for_all(len(players))
old_stack = stack.copy()
remaining_players = play_hand_return_remaining(players, stack, board, cards)
remaining_names = [f"player{i}" for i in remaining_players]
remaining_cards = [cards[p] for p in remaining_players]

for i, cards in enumerate(remaining_cards):
    display_cards(remaining_names[i], cards)

winners = determine_winners(board, remaining_cards, evaluation_table)
pot = compute_pot(old_stack, stack)
winner_names = [f"{remaining_names[i]}" for i in winners]
print(f"Winners: {winner_names}")
human_earnings = stack[0] - old_stack[0]
if "player0" in winner_names:
    human_earnings += pot // len(winners)
    print(f"You won {human_earnings} small-blinds")
else:
    print(f"You lost {-human_earnings} small-blinds")
