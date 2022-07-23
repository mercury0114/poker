class Player:
    def __init__(self, name):
        self.name_ = name
        self.all_players_names = None
        self.state = None
        self.position = None
        self.cards = None
        self.board = None
        self.stack = None

    def get_players_count(self):
        return len(self.all_players_names)

    def update_board_state(self, board, state):
        self.board = board
        self.state = state

    def set_all_players_names(self, all_players_names):
        self.all_players_names = all_players_names
        self.position = 0
        while all_players_names[self.position] != self.name_:
            self.position += 1
