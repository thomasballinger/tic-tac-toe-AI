blank_board = [
            ['_','_','_'], 
            ['_','_','_'], 
            [' ',' ',' '] 
        ]

class Board:
    def __init__(self, grid):
        self.grid = grid
    def place_char (self, row, col, char):
        if (not self.valid_character(char)):
            print 'Invalid character. Please enter \'X\' or \'O\''
            return
        if self.grid[row][col] != '_' and self.grid[row][col] != ' ':
            print 'Invalid move. A player has already marked that spot'
            return 
        else: self.grid[row][col] = char
    def print_board (self):
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
    def check_victory (self):
        # check for 3 in a single row
        for row in self.grid:
            if self.all_same(row):
                print row
                return True
        for col in range(3):
            if self.all_same(self.get_column(col)):
                print self.get_column(col)
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

my_board = Board(blank_board)
turn = 'X'

while (True):
    my_board.print_board()
    input_var = input(turn + " Enter [row, col]: ")
    my_board.place_char(input_var[0],input_var[1],turn)
    if my_board.check_victory():
        my_board.print_board()
        print "player " + turn + " has won!"
        break
    if turn == 'X': 
        turn = 'O'
    else: turn = 'X'
