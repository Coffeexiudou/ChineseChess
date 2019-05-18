

class Player:

    def __init__(self, board, color, mode='easy'):
        self.board = board
        self.color = color
        self.mode = mode

    def next_move(self):
        raise NotImplementedError
