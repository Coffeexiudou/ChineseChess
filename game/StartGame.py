from chess.ChessBoard import Board
from player.AiPlayer import AiPlayer
from engine.evaluation.EvalModel import Eval


class Game:

    @staticmethod
    def init():
        """
        build game
        """
        board = Board()
        player1 = AiPlayer(board, 'r', 'easy')
        player2 = AiPlayer(board, 'b', 'medium')
        return board, player1, player2

    @staticmethod
    def start_game():
        board = Board()
        player1 = AiPlayer(board, 'r', 'hard')
        player2 = AiPlayer(board, 'b', 'medium')
        print('start game...')
        print(board)
        i = 0
        while Eval.has_win(board) == 'x':
            print('第{}回合'.format(i))
            res = player1.next_move()
            print('{} move {} to {}'.format(player1.color,res.piece,res.pos_to))
            p = board.get_piece(res.pos_to)
            if p.is_piece():
                print('{} eat {}'.format(res.piece, p))
            board.update_board(res.piece, res.pos_to)
            print(board)
            res1 = player2.next_move()

            print('{} move {} to {}'.format(player2.color, res1.piece, res1.pos_to))
            p1 = board.get_piece(res1.pos_to)
            if p1.is_piece():
                print('{} eat {}'.format(res1.piece, p1))
            board.update_board(res1.piece, res1.pos_to)
            print(board)
            i += 1
            print('-'*10)
        print('Game over')
        if Eval.has_win(board) == 'r':
            print('player1 win')
        else:
            print('player2 win')

if __name__ == '__main__':
    Game.start_game()
