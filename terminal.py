import itertools

BLANK_BOARD = ['   ',
               '   ',
               '   ']

class Board:
    def __init__(self, grid=None):
        if grid is None:
            self.rows = [list(row) for row in BLANK_BOARD]
        else:
            self.rows = [list(row) for row in grid]
    def place_char(self, row, col):
        if self.rows[row][col] != ' ':
            print 'Invalid move. A player has already marked that spot'
        else:
            self.rows[row][col] = self.turn
    turns_left = property(lambda self: len(self.unplayed_spots))
    turn = property(lambda self: 'X' if self.turns_left % 2 == 1 else 'O')
    def __str__(self):
        template = (
                '     |     |     \n'
                '  {}  |  {}  |  {}  \n'
                '     |     |     \n'
                '-----------------\n'
                '     |     |     \n'
                '  {}  |  {}  |  {}  \n'
                '     |     |     \n'
                '-----------------\n'
                '     |     |     \n'
                '  {}  |  {}  |  {}  \n'
                '     |     |     \n')
        return template.format(*[c for row in self.rows for c in row])
    def check_victory(self):
        return any(self.all_same(comb)
                for comb in itertools.chain(self.rows, self.columns, self.diags))
    @property
    def columns(self):
        return zip(*self.rows)
    @property
    def diags(self):
        return zip(*[(row[i], row[2-i]) for i, row in enumerate(self.rows)])
    def all_same(self, items):
        if items[0] == ' ':
            return False
        return all(x==items[0] for x in items)
    def valid_character(self, char):
        return char in ['O', 'X']

    @property
    def unplayed_spots(self):
        return [(r, c)
                for r in range(3) for c in range(3)
                if self.valid_character(self.rows[r][c])]

    def find_diff(self, next_board):
        return [(r, c)
                for r in range(3) for c in range(3)
                if next_board.rows[r][c] != self.rows[r][c]]

my_board = Board()
print my_board.diags

def play_game(num_humans):
    if num_humans == 2:
        while (True):
            turn = my_board.turn
            print my_board
            input_var = input(turn + " Enter [row, col]: ")
            my_board.place_char(input_var[0],input_var[1])
            if my_board.check_victory():
                print my_board
                print "player " + turn + " has won!"
                break
if __name__ == '__main__':
    play_game(2)

    test_board = ['OXO',
                  'XOO',
                  'XOX']

