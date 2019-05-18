from chess.Rules import Rules


class MoveNode:
    """
    game tree node
    """
    def __init__(self, piece, pos_from, pos_to):
        self.piece = piece
        self.pos_from = pos_from
        self.pos_to = pos_to
        self.val = 0


class Move:
    """
    generate all the moves of red or black
    """
    @staticmethod
    def generate_all_moves(board, color):
        moves = []
        for _, piece in board.pieces.items():
            if piece.color == color:
                for move in Rules.get_next_move(piece, board):
                    moves.append(MoveNode(piece, piece.pos, move))
        return moves




