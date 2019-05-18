
class Rules:
    """
    ChineseChess rules
    """

    @staticmethod
    def get_next_move(piece, board):
        key = piece.key
        moves = []
        if key == 'j':
            moves = Rules.j_rules(piece, board)
        elif key == 'm':
            moves = Rules.m_rules(piece, board)
        elif key == 'p':
            moves = Rules.p_rules(piece, board)
        elif key == 'x':
            moves = Rules.x_rules(piece, board)
        elif key == 's':
            moves = Rules.s_rules(piece, board)
        elif key == 'z':
            moves = Rules.z_rules(piece, board)
        elif key == 'k':
            moves = Rules.k_rules(piece, board)
        return moves

    @staticmethod
    def j_rules(piece, board):
        y_offsets = [1, 2, 3, 4, 5, 6, 7, 8]
        x_offsets = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = piece.pos[0]
        y = piece.pos[1]
        moves = []
        for y_offset in y_offsets:
            r_move = [x, y + y_offset]
            if board.is_empty(r_move):
                moves.append(r_move)
            elif board.is_inside(r_move) and \
                    board.get_piece(r_move).color != piece.color:
                moves.append(r_move)
                break
            else:
                break
        for y_offset in y_offsets:
            l_move = [x, y - y_offset]
            if board.is_empty(l_move):
                moves.append(l_move)
            elif board.is_inside(l_move) and \
                    board.get_piece(l_move).color != piece.color:
                moves.append(l_move)
                break
            else:
                break

        for x_offset in x_offsets:
            u_move = [x - x_offset, y]
            if board.is_empty(u_move):
                moves.append(u_move)
            elif board.is_inside(u_move) and \
                    board.get_piece(u_move).color != piece.color:
                moves.append(u_move)
                break
            else:
                break

        for x_offset in x_offsets:
            d_move = [x + x_offset, y]
            if board.is_empty(d_move):
                moves.append(d_move)
            elif board.is_inside(d_move) and \
                    board.get_piece(d_move).color != piece.color:
                moves.append(d_move)
                break
            else:
                break
        return moves

    @staticmethod
    def m_rules(piece, board):
        target_offset = [[1, -2], [1, 2], [-1, 2], [-1, -2],
                         [2, 1], [2, -1], [-2, 1], [-2, -1]]
        obstacle = [[0, -1], [0, 1], [0, 1], [0, -1],
                    [1, 0], [1, 0], [-1, 0], [-1, 0]]
        moves = []
        x = piece.pos[0]
        y = piece.pos[1]
        for offset1, offset2 in zip(target_offset, obstacle):
            move = [x + offset1[0], y + offset1[1]]
            side = [x + offset2[0], y + offset2[1]]
            if not board.is_inside(move):
                continue
            if board.is_empty(side):
                if board.is_empty(move):
                    moves.append(move)
                elif board.get_piece(move).color != piece.color:
                    moves.append(move)
        return moves


    @staticmethod
    def p_rules(piece, board):
        y_offsets = [1, 2, 3, 4, 5, 6, 7, 8]
        x_offsets = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        x = piece.pos[0]
        y = piece.pos[1]
        moves = []
        rr, ll, uu, dd = False, False, False, False
        for y_offset in y_offsets:
            r_move = [x, y + y_offset]
            if not board.is_inside(r_move):
                break
            no_piece = board.is_empty(r_move)
            if not rr:
                if no_piece:
                    moves.append(r_move)
                else:
                    rr = True
            elif not no_piece:
                if board.get_piece(r_move).color != piece.color:
                    moves.append(r_move)
                break
        for y_offset in y_offsets:
            l_move = [x, y - y_offset]
            if not board.is_inside(l_move):
                break
            no_piece = board.is_empty(l_move)
            if not ll:
                if no_piece:
                    moves.append(l_move)
                else:
                    ll = True
            elif not no_piece:
                if board.get_piece(l_move).color != piece.color:
                    moves.append(l_move)
                break
        for x_offset in x_offsets:
            u_move = [x - x_offset, y]
            if not board.is_inside(u_move):
                break
            no_piece = board.is_empty(u_move)
            if not uu:
                if no_piece:
                    moves.append(u_move)
                else:
                    uu = True
            elif not no_piece:
                if board.get_piece(u_move).color != piece.color:
                    moves.append(u_move)
                break
        for x_offset in x_offsets:
            d_move = [x + x_offset, y]
            if not board.is_inside(d_move):
                break
            no_piece = board.is_empty(d_move)
            if not dd:
                if no_piece:
                    moves.append(d_move)
                else:
                    dd = True
            elif not no_piece:
                if board.get_piece(d_move).color != piece.color:
                    moves.append(d_move)
                break
        return moves

    @staticmethod
    def x_rules(piece, board):
        target_offset = [[-2, -2], [-2, 2], [2, -2], [2, 2]]
        obstacle = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        moves = []
        x = piece.pos[0]
        y = piece.pos[1]
        for offset1, offset2 in zip(target_offset, obstacle):
            move = [x + offset1[0], y + offset1[1]]
            side = [x + offset2[0], y + offset2[1]]
            if not board.is_inside(move) or (move[0] > 4 and
                    piece.color == 'b') or (move[0] < 5 and piece.color == 'r'):
                continue
            if board.is_empty(side):
                if board.is_empty(move):
                    moves.append(move)
                elif board.get_piece(move).color != piece.color:
                    moves.append(move)
        return moves

    @staticmethod
    def s_rules(piece, board):
        offsets = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
        x = piece.pos[0]
        y = piece.pos[1]
        moves = []
        for offset in offsets:
            move = [x + offset[0], y + offset[1]]
            if (not board.is_inside(move) or ((move[0] > 2 or move[1] < 3 or
            move[1] > 5) and piece.color == 'b')) or ((move[0] < 7 or
                        move[1] < 3 or move[1] > 5)and piece.color == 'r'):
                continue
            if board.is_empty(move):
                moves.append(move)
            elif board.get_piece(move).color != piece.color:
                moves.append(move)
        return moves

    @staticmethod
    def z_rules(piece, board):
        r_offset = [[0, 1], [0, -1], [-1, 0]]
        b_offset = [[0, 1], [0, -1], [1, 0]]
        moves = []
        x = piece.pos[0]
        y = piece.pos[1]
        if piece.color == 'r':
            if x > 4:
                move = [x - 1, y]
                if board.is_empty(move):
                    moves.append(move)
                elif board.get_piece(move).color != piece.color:
                    moves.append(move)
            else:
                for offset in r_offset:
                    move = [x + offset[0], y + offset[1]]
                    if not board.is_inside(move):
                        continue
                    if board.is_empty(move):
                        moves.append(move)
                    elif board.get_piece(move).color != piece.color:
                        moves.append(move)
        if piece.color == 'b':
            if x < 5:
                move = [x + 1, y]
                if board.is_empty(move):
                    moves.append(move)
                elif board.get_piece(move).color != piece.color:
                    moves.append(move)
            else:
                for offset in b_offset:
                    move = [x + offset[0], y + offset[1]]
                    if not board.is_inside(move):
                        continue
                    if board.is_empty(move):
                        moves.append(move)
                    elif board.get_piece(move).color != piece.color:
                        moves.append(move)

        return moves

    @staticmethod
    def k_rules(piece, board):
        offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        x = piece.pos[0]
        y = piece.pos[1]
        moves = []
        for offset in offsets:
            move = [x + offset[0], y + offset[1]]
            if (not board.is_inside(move) or ((move[0] > 2 or move[1] < 3
                or move[1] > 5)and piece.color == 'b') or ((move[0] < 7 or
                        move[1] < 3 or move[1] > 5) and piece.color == 'r')):
                continue
            if board.is_empty(move):
                moves.append(move)
            elif board.get_piece(move).color != piece.color:
                moves.append(move)
        flag = True
        oppo_k_pos = board.pieces.get('bk0').pos if piece.color == 'r' \
            else board.pieces.get('rk0').pos
        if oppo_k_pos[1] == move[1]:
            for i in range(min(oppo_k_pos[0], x) + 1, max(oppo_k_pos[0], x)):
                if board.get_piece([i, y]).is_piece():
                    flag = False
                    break
            if flag:
                moves.append(oppo_k_pos)
        return moves

if __name__ == '__main__':
    pass
