class Piece:
    """
    ====attribute====
    name:piece name
    key: piece category
    color: 'r or 'b'
    index: '1' or '2'
    pos: piece position

    ====method====
    is_piece(): check empty or piece

    """

    name = None
    key = None
    color = None
    index = None
    pos = []

    def __init__(self, name, pos):
        if name is not None and pos is not None:
            self.name = name
            self.key = name[1]
            self.color = name[0]
            self.index = name[2]
            self.pos = pos
        else:
            self.name = None

    def is_piece(self):
        if self.name is None:
            return False
        return True

    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return 'empty piece'
