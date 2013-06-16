blank_board = [
            ['_','_','_'],
            ['_','_','_'],
            [' ',' ',' ']
        ]

other_board = [
            ['O','X','O'],
            ['X','O','O'],
            ['X','O','X']
        ]

class Board:
    def __init__(self, grid=None):
        if grid is None:
            self.grid = [list(row) for row in blank_board]
        else:
            self.grid = [list(row) for row in grid]
        self.turns_left = len(self.unplayed_spots)
        self.turn = 'X' if self.turns_left % 2 == 1 else 'O'
    def place_char(self, row, col):
        if self.grid[row][col] not in ['_', ' ']:
            print 'Invalid move. A player has already marked that spot'
        else:
            self.grid[row][col] = self.turn
            self.turn = 'X' if self.turns_left % 2 == 0 else 'O'
            self.turns_left -= 1
    def print_board(self):
        upper = '   |   |   \n'
        for i, row in enumerate(self.grid):
            row_string = ''
            if i == 2:
                row_ground = ' '
            else:
                row_ground = '_'
            for j, char in enumerate(row):
                if j == 2:
                    col_close = row_ground
                else:
                    col_close = row_ground + "|"
                patch = row_ground + char + col_close
                row_string += patch
            print upper + row_string
        print '\n'
    def check_victory(self):
        # check for 3 in a single row
        if any(self.all_same(row) for row in self.grid):
            return True
        if any(self.all_same(self.get_column(col)) for col in range(3)):
            return True
        diags = self.get_diags()
        if self.all_same(diags[0]) or self.all_same(diags[1]):
            return True
        return False
    def get_column(self, number):
        return [row[number] for row in self.grid]
    def get_diags(self):
        return zip([(row[i], row[2-i]) for i, row in enumerate(self.grid)])
    def all_same(self, items):
        if items[0] in ['_', ' ']:
            return False
        return all(x==items[0] for x in items)
    def valid_character(self, char):
        return char in ['O', 'X']

    @property
    def unplayed_spots(self):
        return [(r, c)
                for r in range(3) for c in range(3)
                if self.valid_characters(self.grid[r][c])]

    def find_diff(self, next_board):
        return [(r, c)
                for r in range(3) for c in range(3)
                if next_board.grid[r][c] != self.grid[r][c]]

my_board = Board()

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

