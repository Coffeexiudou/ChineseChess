from engine.algorithm.Strategy import Move
from engine.evaluation.EvalModel import Eval
from engine.util.Timer import clock


class MinMax(Move):
    """
    Depth-first traversal of the game tree

    Suppose the opponent is prefect,it will give you the worst response(min)
    to every decision(moves) you make,choose the best result(max) from your
    opponent's response,the branch corresponding to this result is the branch
    you should choose

    example:
     if depth == 0, become a greedy algorithm,choose the best one of the moves
     (max)else,when it is your turn, max; when it is opponent's turn, min
     attention:the evaluation values(max or min value) are calculated from your
     perspective

    """

    @staticmethod
    @clock
    def search_next_move(board, player_color, depth=1):
        first_moves = MinMax.generate_all_moves(board, player_color)
        best_move = None
        is_max = False
        alpha = -100000
        beta = 100000
        for move in first_moves:
            eaten_piece = board.update_board(move.piece, move.pos_to)
            move.val = MinMax._min_max(depth, board, alpha, beta,
                                       player_color, player_color, is_max)
            if best_move is None or move.val >= best_move.val:
                best_move = move

            board.update_board(move.piece, move.pos_from)
            if eaten_piece.is_piece():
                board.pieces[eaten_piece.name] = eaten_piece
                board.back_board_piece(eaten_piece)
        return best_move

    @staticmethod
    def _min_max(depth, board, alpha, beta, player_color, color,  is_max):
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
        return alpha if is_max else beta


if __name__ == '__main__':
    pass
