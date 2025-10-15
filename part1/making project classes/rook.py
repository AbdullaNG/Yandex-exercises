BLACK = 2
WHITE = 1


class King:
    def __init__(self, color):
        self.color = color
        self.row = 0 if color == 1 else 7
        self.col = 3
        self.go = 1

    def can_move(self, board, row, col, row1, col1):
        return True if abs(col - col1) <= 1 and abs(row - row1) <= 1 else False

    def get_color(self):
        return self.color

    def char(self):
        return "K"

    def set_position(self, row1, col1):
        self.go = 0
        self.row = row1
        self.col = col1


class Queen:
    def __init__(self, color):
        self.color = color
        self.row = 0 if color == 1 else 7
        self.col = 3

    def can_move(self, board, row, col, row1, col1):
        if row == row1 and col == col1:
            return False
        if abs(col - col1) == abs(row - row1) or col == col1 or row == row1:
            if row == row1 or col == col1:
                m = rook(row, col, row1, col1)
            else:
                m = bishop(row, col, row1, col1)
            return m_check(board, row, col, row1, col1, m)

    def get_color(self):
        return self.color

    def char(self):
        return "Q"

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1


class Rook:
    def __init__(self, color):
        self.color = color
        self.go = 1

    def set_position(self, row, col):
        self.go = 0
        self.row = row
        self.col = col

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        return m_check(board, row, col, row1, col1, rook(row, col, row1, col1))


class Bishop:
    def __init__(self, color):
        self.color = color

    def can_move(self, board, row, col, row1, col1):
        if abs(col - col1) == abs(row - row1):
            m = bishop(row, col, row1, col1)
            return m_check(board, row, col, row1, col1, m)

    def get_color(self):
        return self.color

    def char(self):
        return "B"

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1


class Knight:
    def __init__(self, color):
        self.color = color

    def can_move(self, board, row, col, row1, col1):
        return True if {abs(col - col1), abs(row - row1)} == {1, 2} and (
                board.field[row1][col1] is None or board.field[row1][col1].get_color() !=
                board.field[row][col].get_color()) else False

    def get_color(self):
        return self.color

    def char(self):
        return "N"

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1


class Pawn:
    def __init__(self, color):
        self.color = color
    
    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.color

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        if abs(row1 - row) == 1 and abs(col - col1) == 1 and board.field[row1][col1] and \
                board.field[row1][col1].get_color() != board.field[row][col].get_color():
            return True
        if col != col1:
            return False
        if self.color == WHITE:
            dir = 1
            strow = 1
        else:
            dir = -1
            strow = 6

        if row + dir == row1:
            return True
        if (row == strow
                and row + 2 * dir == row1
                and board.field[row + dir][col] is None):
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        dir = 1 if (self.color == WHITE) else -1
        return (row + dir == row1
                and (col + 1 == col1 or col - 1 == col1))


def m_check(board, row, col, row1, col1, m):
    if (row, col) in m:
        m.remove((row, col))
    for i in m:
        if i != (row1, col1) and board.field[i[0]][i[1]] is not None:
            return False
    if board.field[row1][col1]:
        if board.field[row][col].get_color() == board.field[row1][col1].get_color():
            return False
    return True


class Black:
    def __eq__(self, other):
        return isinstance(other, Black)

    def opponent(self):
        return White()

    def is_black(self):
        return True

    def is_white(self):
        return False


class White:
    def __eq__(self, other):
        return isinstance(other, White)

    def opponent(self):
        return Black()

    def is_black(self):
        return False

    def is_white(self):
        return True


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


def straightline(rc, rc1):
    return range(min(rc, rc1), max(rc, rc1))


def rook(row, col, row1, col1):
    m1 = list(straightline(min(row, row1), max(row, row1) + 1))
    m2 = list(straightline(min(col, col1), max(col, col1) + 1))
    m = []
    if len(m1) > 1:
        m = list(map(lambda x: (x, col), m1))
    elif len(m2) > 1:
        m = list(map(lambda x: (row, x), m2))
    if m and (row, col) not in m:
        m = [(row, col)] + m + [(row1, col1)]
    return m


def bishop(row, col, row1, col1):
    m1 = list(straightline(min(row, row1), max(row, row1) + 1))
    m2 = list(straightline(min(col, col1), max(col, col1) + 1))
    if (row < row1 and col < col1) or (row > row1 and col > col1):
        return list(zip(m1, m2))
    else:
        return list(zip(m1, m2[::-1]))


class PieceColor:
    def __init__(self, color):
        self.color = color

    def opponent(self):
        if self.color == WHITE:
            return PieceColor(BLACK)
        return PieceColor(WHITE)

    def is_black(self):
        return self.color == BLACK

    def is_white(self):
        return self.color == WHITE

    def __eq__(self, other):
        return self.color == other.color


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if not self.field[row][col] or not self.field[row][col].__class__.__name__ == "Pawn":
            return False
        if not self.field[row][col].can_move(self, row, col, row1, col1):
            return False
        if self.field[row1][col1] and col == col1:
            return False
        if char not in ["Q", "B", "R", "N"]:
            return False
        colour = self.field[row][col].get_color()
        self.field[row][col] = None
        figure = {"Q": "Queen", "B": "Bishop", "R": "Rook", "N": "Knight"}[char]
        self.field[row1][col1] = eval(f'{figure}({colour})')
        self.color = opponent(self.color)
        return True

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if piece.can_attack(self, row, col, row1, col1):
                return True
        else:
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def get_piece(self, row, col):
        return self.field[row][col]

    def castling0(self):
        if self.color == 1:
            cc = 0
        else:
            cc = 7
        if not (self.field[cc][4] and self.field[cc][4].__class__.__name__ == "King"):
            return False
        if not (self.field[cc][0] and self.field[cc][0].__class__.__name__ == "Rook"):
            return False
        if not (self.field[cc][4].go and self.field[cc][0].go):
            return False
        if not (self.field[cc][1] is None and self.field[0][2] is None and self.field[0][3] is None):
            return False
        king = self.field[cc][4]
        rook = self.field[cc][0]
        self.field[cc][4] = None
        self.field[cc][0] = None
        self.field[cc][2] = king
        self.field[cc][3] = rook
        king.set_position(cc, 2)
        rook.set_position(cc, 3)
        self.color = opponent(self.color)
        return True

    def castling7(self):
        if self.color == 1:
            cc = 0
        else:
            cc = 7
        if not (self.field[cc][4] and self.field[cc][4].__class__.__name__ == "King"):
            return False
        if not (self.field[cc][7] and self.field[cc][7].__class__.__name__ == "Rook"):
            return False
        if not (self.field[cc][4].go and self.field[cc][7].go):
            return False
        if not (self.field[cc][5] is None and self.field[cc][6] is None):
            return False
        king = self.field[cc][4]
        rook = self.field[cc][7]
        self.field[cc][4] = None
        self.field[cc][7] = None
        self.field[cc][6] = king
        self.field[cc][5] = rook
        king.set_position(cc, 6)
        rook.set_position(cc, 5)
        self.color = opponent(self.color)
        return True


def print_board(board):
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    board = Board()
    while True:
        print_board(board)
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход черных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')