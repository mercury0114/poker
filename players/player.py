class Player:
    def __init__(self):
        self.state = None
        self.position = None
        self.players_count = None
        self.cards = None
        self.board = None
        self.stack = None

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

    def set_stack(self, stack):
        self.stack = stack

    def get_name(self):
        return f"player{self.position}"

    def get_stack(self):
        return self.stack
