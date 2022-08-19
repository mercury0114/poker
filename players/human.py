from cards.displayer import display_cards
from cards.displayer import display_row
from players.player import Player
from utils.request_input import request_input


class Human(Player):
    @staticmethod
    def bet():
        print("Enter your bet amount")
        return int(request_input(lambda x: x.isdigit()))

    def display_investments(self):
        investments = [s[1] for s in self.state]
        display_row("Round pot", [str(money) for money in investments])

    def display_statuses(self):
        statuses = [s[0] for s in self.state]
        display_row("Statuses", statuses)

    def display_new_action(self):
        display_cards("Board", self.board)
        display_row("Names", self.all_players_names)
        display_row("Stacks", [str(stack) for stack in self.stacks])
        self.display_statuses()
        self.display_investments()
        print("")

    def update_board_state(self, board, state, stacks):
        super().update_board_state(board, state, stacks)
        self.display_new_action()

    def set_cards(self, cards):
        super().set_cards(cards)
        display_cards("Your cards", cards)
