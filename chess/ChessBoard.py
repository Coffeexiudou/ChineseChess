from chess.Piece import Piece

chinese_map = {
    'rj': '俥',
    'rm': '傌',
    'rx': '象',
    'rs': '士',
    'rk': '帥',
    'rp': '炮',
    'rz': '兵',
    'bj': '車',
    'bm': '马',
    'bx': '象',
    'bs': '士',
    'bk': '将',
    'bp': '砲',
    'bz': '卒'
}


class Board:

    BOARD_WIDTH = 9
    BOARD_HEIGHT = 10
    red_pieces = []
    black_pieces = []
    cells = []
    pieces = {}

    def __init__(self):
        self._init_board()

    def _init_black_pieces(self):
        self.black_pieces = [
            Piece('bj1', [0, 0]),
            Piece('bj2', [0, 8]),
            Piece('bm1', [0, 1]),
            Piece('bm2', [0, 7]),
            Piece('bx1', [0, 2]),
            Piece('bx2', [0, 6]),
            Piece('bs1', [0, 3]),
            Piece('bs2', [0, 5]),
            Piece('bp1', [2, 1]),
            Piece('bp2', [2, 7]),
            Piece('bz1', [3, 0]),
            Piece('bz2', [3, 2]),
            Piece('bz3', [3, 4]),
            Piece('bz4', [3, 6]),
            Piece('bz5', [3, 8]),
            Piece('bk0', [0, 4])
        ]

    def _init_red_pieces(self):
        self.red_pieces = [
            Piece('rj1', [9, 0]),
            Piece('rj2', [9, 8]),
            Piece('rm1', [9, 1]),
            Piece('rm2', [9, 7]),
            Piece('rx1', [9, 2]),
            Piece('rx2', [9, 6]),
            Piece('rs1', [9, 3]),
            Piece('rs2', [9, 5]),
            Piece('rp1', [7, 1]),
            Piece('rp2', [7, 7]),
            Piece('rz1', [6, 0]),
            Piece('rz2', [6, 2]),
            Piece('rz3', [6, 4]),
            Piece('rz4', [6, 6]),
            Piece('rz5', [6, 8]),
            Piece('rk0', [9, 4])
        ]

    def _init_pieces(self):
        self._init_red_pieces()
        self._init_black_pieces()
        for piece in self.red_pieces:
            self.pieces[piece.name] = piece
        for piece in self.black_pieces:
            self.pieces[piece.name] = piece

    def _init_cells(self):
        self.cells = [[Piece(None, None)] * self.BOARD_WIDTH
                      for _ in range(self.BOARD_HEIGHT)]
        self._init_pieces()
        for red_piece in self.red_pieces:
            self.cells[red_piece.pos[0]][red_piece.pos[1]] = red_piece
        for black_piece in self.black_pieces:
            self.cells[black_piece.pos[0]][black_piece.pos[1]] = black_piece

    def _init_board(self):
        self._init_pieces()
        self._init_cells()

    def __str__(self):
        str_print = ''
        for i, pieces in enumerate(self.cells):
            str_line = ''
            for piece in pieces:
                if piece.is_piece():
                    str_line += chinese_map[piece.name[:-1]] + ' '
                else:
                    str_line += '   '
            str_print += str_line + '\n'
            if i == 4:
                str_print += '      楚河  汉界\n'
        return str_print

    def is_inside(self, pos):
        """
        check pos validity
        """
        x = pos[0]
        y = pos[1]
        if x < 0 or x >= self.BOARD_HEIGHT or y < 0 or y >= self.BOARD_WIDTH:
            return False
        return True

    def is_empty(self, pos):
        """
        check pos with or without piece
        """
        return self.is_inside(pos) and not self.cells[pos[0]][pos[1]].is_piece()

    def get_piece(self, pos):
        """
        get pos piece,maybe empty
        """
        return self.cells[pos[0]][pos[1]]

    def update_board(self, piece, pos):
        """
        move piece to pos
        """
        pos_piece = self.get_piece(pos)
        if pos_piece.is_piece():
            self.pieces.pop(pos_piece.name)
        self.cells[piece.pos[0]][piece.pos[1]] = Piece(None, None)
        piece.pos = pos
        self.cells[pos[0]][pos[1]] = piece
        return pos_piece

    def back_board_piece(self, piece):
        """
        put the piece on the board
        """
        self.cells[piece.pos[0]][piece.pos[1]] = piece



if __name__ == "__main__":
    pass
