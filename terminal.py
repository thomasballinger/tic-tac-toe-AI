blank_board = [[' ',' ',' '],
               [' ',' ',' '],
               [' ',' ',' ']]

other_board = [['O','X','O'],
               ['X','O','O'],
               ['X','O','X']]

class Board:
    def __init__(self, grid=None):
        if grid is None:
            self.grid = [list(row) for row in blank_board]
        else:
            self.grid = [list(row) for row in grid]
    def place_char(self, row, col):
        if self.grid[row][col] != ' ':
            print 'Invalid move. A player has already marked that spot'
        else:
            self.grid[row][col] = self.turn
    turns_left = property(lambda self: len(self.unplayed_spots))
    turn = property(lambda self: 'X' if self.turns_left % 2 == 1 else 'O')
    def print_board(self):
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
        print template.format(*[c for row in self.grid for c in row])
    def check_victory(self):
        if any(self.all_same(row) for row in self.grid):
            return True
        if any(self.all_same(col) for col in self.columns):
            return True
        if any(self.all_same(diag) for diag in self.diags):
            return True
        return False
    @property
    def columns(self):
        return zip(*self.grid)
    @property
    def diags(self):
        return zip(*[(row[i], row[2-i]) for i, row in enumerate(self.grid)])
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
                if self.valid_character(self.grid[r][c])]

    def find_diff(self, next_board):
        return [(r, c)
                for r in range(3) for c in range(3)
                if next_board.grid[r][c] != self.grid[r][c]]

my_board = Board()
print my_board.diags

def play_game(num_humans):
    if num_humans == 2:
        while (True):
            turn = my_board.turn
            my_board.print_board()
            input_var = input(turn + " Enter [row, col]: ")
            my_board.place_char(input_var[0],input_var[1])
            if my_board.check_victory():
                my_board.print_board()
                print "player " + turn + " has won!"
                break
if __name__ == '__main__':
    play_game(2)

