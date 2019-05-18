class Eval:
    """
    method:
    has_win():
        determine if the game is over
    get_score():
        Calculate the score based on the weight of the piece and the weight of
        the position
    """

    @staticmethod
    def has_win(board):
        red_win = 'r'
        black_win = 'b'
        if board.pieces.get('bk0') is None:
            return red_win
        if board.pieces.get('rk0') is None:
            return black_win
        return 'x'

    @staticmethod
    def get_score(board, color):
        red_piece_val, red_pos_val = 0, 0
        black_piece_val, black_pos_val = 0, 0
        for _, piece in board.pieces.items():
            reverse_pos = [board.BOARD_HEIGHT - 1 - piece.pos[0], piece.pos[1]]
            if piece.key == 'k':
                if piece.color == 'r':
                    red_piece_val += Eval.piece_value('k')
                else:
                    black_piece_val += Eval.piece_value('k')
            elif piece.key == 's':
                if piece.color == 'r':
                    red_piece_val += Eval.piece_value('s')
                else:
                    black_piece_val += Eval.piece_value('s')
            elif piece.key == 'x':
                if piece.color == 'r':
                    red_piece_val += Eval.piece_value('x')
                else:
                    black_piece_val += Eval.piece_value('x')
            elif piece.key == 'm':
                if piece.color == 'r':
                    red_piece_val += Eval.piece_value('m')
                    red_pos_val += Eval.pos_value('m', piece.pos)
                else:
                    black_piece_val += Eval.piece_value('m')
                    black_pos_val += Eval.pos_value('m', reverse_pos)
            elif piece.key == 'j':
                if piece.color == 'r':
                    red_piece_val += Eval.piece_value('j')
                    red_pos_val += Eval.pos_value('j', piece.pos)
                else:
                    black_piece_val += Eval.piece_value('j')
                    black_pos_val += Eval.pos_value('j', reverse_pos)
            elif piece.key == 'p':
                if piece.color == 'r':
                    red_piece_val += Eval.piece_value('p')
                    red_pos_val += Eval.pos_value('p', piece.pos)
                else:
                    black_piece_val += Eval.piece_value('p')
                    black_pos_val += Eval.pos_value('p', reverse_pos)
            elif piece.key == 'z':
                if piece.color == 'r':
                    red_piece_val += Eval.piece_value('z')
                    red_pos_val += Eval.pos_value('z', piece.pos)
                else:
                    black_piece_val += Eval.piece_value('z')
                    black_pos_val += Eval.pos_value('z', reverse_pos)
        red_val = red_piece_val + red_pos_val*8
        black_val = black_piece_val + black_pos_val*8
        if color == 'r':
            return red_val - black_val
        if color == 'b':
            return black_val - red_val
        return -1

    @staticmethod
    def piece_value(key):
        piece_value_dict = {
            'j': 600,
            'm': 300,
            'p': 300,
            'x': 110,
            's': 110,
            'z': 70,
            'k': 1000000
        }
        return piece_value_dict[key]

    @staticmethod
    def pos_value(key, pos):
        p_pos_value = [
            [6, 4, 0, -10, -12, -10, 0, 4, 6],
            [2, 2, 0, -4, -14, -4, 0, 2, 2],
            [2, 2, 0, -10, -8, -10, 0, 2, 2],
            [0, 0, -2, 4, 10, 4, -2, 0, 0],
            [0, 0, 0, 2, 8, 2, 0, 0, 0],
            [-2, 0, 4, 2, 6, 2, 4, 0, -2],
            [0, 0, 0, 2, 4, 2, 0, 0, 0],
            [4, 0, 8, 6, 10, 6, 8, 0, 4],
            [0, 2, 4, 6, 6, 6, 4, 2, 0],
            [0, 0, 2, 6, 6, 6, 2, 0, 0]
        ]
        m_pos_value = [
            [4, 8, 16, 12, 4, 12, 16, 8, 4],
            [4, 10, 28, 16, 8, 16, 28, 10, 4],
            [12, 14, 16, 20, 18, 20, 16, 14, 12],
            [8, 24, 18, 24, 20, 24, 18, 24, 8],
            [6, 16, 14, 18, 16, 18, 14, 16, 6],
            [-4, 12, 16, 14, 12, 14, 16, 12, 4],
            [2, 6, 8, 6, 10, 6, 8, 6, 2],
            [4, 2, 8, 8, 4, 8, 8, 2, 4],
            [0, 2, 4, 4, -2, 4, 4, 2, 0],
            [0, -4, 0, 0, 0, 0, 0, -4, 0]
        ]
        j_pos_value = [
            [14, 14, 12, 18, 16, 18, 12, 14, 14],
            [16, 20, 18, 24, 26, 24, 18, 20, 16],
            [12, 12, 12, 18, 18, 18, 12, 12, 12],
            [12, 18, 16, 22, 22, 22, 16, 18, 12],
            [12, 14, 12, 18, 18, 18, 12, 14, 12],
            [12, 16, 14, 20, 20, 20, 14, 16, 12],
            [6, 10, 8, 14, 14, 14, 8, 10, 6],
            [4, 8, 6, 14, 12, 14, 6, 8, 4],
            [8, 4, 8, 16, 8, 16, 8, 4, 8],
            [-2, 10, 6, 14, 12, 14, 6, 10, -2]
        ]
        z_pos_value = [
            [0, 3, 6, 9, 12, 9, 6, 3, 0],
            [18, 36, 56, 80, 120, 80, 56, 36, 18],
            [14, 26, 42, 60, 80, 60, 42, 26, 14],
            [10, 20, 30, 34, 40, 34, 30, 20, 10],
            [6, 12, 18, 18, 20, 18, 18, 12, 6],
            [2, 0, 8, 0, 8, 0, 8, 0, 2],
            [0, 0, -2, 0, 4, 0, -2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        if key == 'j':
            return j_pos_value[pos[0]][pos[1]]
        if key == 'm':
            return m_pos_value[pos[0]][pos[1]]
        if key == 'p':
            return p_pos_value[pos[0]][pos[1]]
        if key == 'z':
            return z_pos_value[pos[0]][pos[1]]
        return -1
