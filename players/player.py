class Player:
    def __init__(self, name):
        self.name = name
        self.stacks = None
        self.state = None
        self.board = None
        self.all_players_names = None
        self.position = None
        self.cards = None

    def get_players_count(self):
        return len(self.all_players_names)

    def update_board_state(self, board, state, stacks):
        self.board = board
        self.state = state
        self.stacks = stacks

    def set_cards(self, cards):
        self.cards = cards

    def set_all_players_names(self, all_players_names):
        self.all_players_names = all_players_names
        self.position = 0
        while all_players_names[self.position] != self.name:
            self.position += 1

    def get_stack(self):
        return self.stacks[self.position]

    @staticmethod
    def leave_table():
        return
