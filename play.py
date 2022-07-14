from players import FoldPlayer
from players import Player

from game import play_hand_return_remaining


class Human(Player):
    def show_cards(self, name, cards):
        print(f"{name}: {cards}")

    @staticmethod
    def bet():
        return int(input())

    def update_history(self, history):
        super().update_history(history)
        print(history)


players = [Human(), FoldPlayer(), FoldPlayer()]
print(play_hand_return_remaining(players))
