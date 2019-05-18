from engine.algorithm.MinMax import MinMax
from engine.evaluation.EvalModel import Eval


class ABpruning(MinMax):
    """
    similar with min-max algorithm,alpha-beta pruning cut branch
    if beta <= alpha,more efficient
    """

    @staticmethod
    def _min_max(depth, board, alpha, beta, player_color, color, is_max):
        if depth == 0 or Eval.has_win(board) != 'x':
            return Eval.get_score(board, player_color)
        color = 'r' if color == 'b' else 'b'
        all_moves = MinMax.generate_all_moves(board, color)
        for move in all_moves:
            eaten_piece = board.update_board(move.piece, move.pos_to)
            if is_max:
                alpha = max(alpha, MinMax._min_max(depth-1, board, alpha, beta,
                                                   player_color, color, False))
            else:
                beta = min(beta, MinMax._min_max(depth-1, board, alpha, beta,
                                                 player_color, color, True))
            board.update_board(move.piece, move.pos_from)
            if eaten_piece.is_piece():
                board.pieces[eaten_piece.name] = eaten_piece
                board.back_board_piece(eaten_piece)
            if beta <= alpha:
                break
        return alpha if is_max else beta


if __name__ == '__main__':
    pass

