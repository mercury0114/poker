class Player:
    def __init__(self, name):
        self.name = name
        self.all_players_names = None
        self.state = None
        self.position = None
        self.cards = None
        self.board = None
        self.stack = None

    def update_state(self, state):
        self.state = state

    def set_all_players_names(self, all_players_names):
        self.all_players_names = all_players_names
        self.position = 0
        while all_players_names[self.position] != self.name:
            self.position += 1

    def set_cards(self, cards):
        self.cards = cards

    def set_board(self, board):
        self.board = board

    def get_players_count(self):
        return len(self.all_players_names)
