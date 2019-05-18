from engine.algorithm.MinMax import MinMax
from engine.evaluation.EvalModel import Eval
import timeit


class IterativeDeepeningABpruning(MinMax):
    """
    alpha-beta pruning with iterative deepening

    may allow deeper search within a specified time

    examlpe:
        1) if there are fewer branches (fewer moves),spend less time
        to take one more step
        2) if there are more branches (more moves),spend more time
        than specified time,stop the iteration and return last result
    """

    time_out = 20

    @staticmethod
    def _min_max(depth, board, alpha, beta, player_color, color,  is_max):
        start_time = timeit.default_timer()
        val = -100000
        for depth in range(depth):
            val = IterativeDeepeningABpruning._alpha_beta_pruning(depth, board,
                                      alpha, beta, player_color, color, is_max)
            t = timeit.default_number() - start_time
            if t > IterativeDeepeningABpruning.time_out:
                break
        return val


    @staticmethod
    def _alpha_beta_pruning(depth, board, alpha, beta, player_color,
                            color, is_max):
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
