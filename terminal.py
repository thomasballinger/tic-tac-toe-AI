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
        if self.grid[row][col] != '_' and self.grid[row][col] != ' ':
            print 'Invalid move. A player has already marked that spot'
        else:
            self.grid[row][col] = self.turn
            self.turn = 'X' if self.turns_left % 2 == 0 else 'O'
            self.turns_left -= 1
    def print_board(self):
        upper = '   |   |   \n'
        for row in range(3):
            row_string = ''
            if row == 2:
                row_ground = ' '
            else:
                row_ground = '_'
            for col in range(3):
                if col == 2:
                    col_close = row_ground
                else:
                    col_close = row_ground + "|"
                patch = row_ground + self.grid[row][col] + col_close
                row_string += patch
            print upper + row_string
        print '\n'
    def check_victory(self):
        # check for 3 in a single row
        for row in self.grid:
            if self.all_same(row):
                return True
        for col in range(3):
            if self.all_same(self.get_column(col)):
                return True
        diags = self.get_diags()
        if self.all_same(diags[0]) or self.all_same(diags[1]):
            return True
        return False
    def get_column(self, number):
        col = []
        for row in self.grid:
            col.append(row[number])
        return col
    def get_diags(self):
        diag1 = []
        diag2 = []
        for ind in range(3):
            diag1.append(self.grid[ind][ind])
            diag2.append(self.grid[2-ind][ind])
        return (diag1,diag2)
    def all_same(self, items):
        if items[0] == '_' or items[0] == ' ':
            return False
        return all(x==items[0] for x in items)
    def valid_character(self, char):
        return (char == 'O' or char == 'X')

    @property
    def unplayed_spots(self):
        unplayed_spots = []
        for row in range(3):
            for col in range(3):
                # is there a way to use list comprehension for this?
                if not self.valid_character(self.grid[row][col]):
                    unplayed_spots.append((row,col))
        return unplayed_spots

    def find_diff(self, next_board):
        next_grid = next_board.grid
        for row in range(3):
            for col in range(3):
                if next_grid[row][col] != self.grid[row][col]:
                    return (row,col)

my_board = Board()

def play_game(num_humans):
    if num_humans == '2':
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
    play_game('2')

