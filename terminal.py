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
        for row in range(3):
            char = self.grid[row][0]
            if self.valid_character(char):
                print char
                for col in range(3):
                    next_char = self.grid[row][col]
                    if (char != next_char):
                        return False
        # check for 3 in a single column
        for col in range(3):
            char = self.grid[0][col]
            if self.valid_character(char):
                for row in range(3):
                    next_char = self.grid[row][col]
                    if (char != next_char):
                        return False
        # check diagonals
        char = self.grid[0][0]
        if self.valid_character(char):
            for diag in range (3):
                next_char = self.grid[diag][diag]
                if (char != next_char):
                    return False
        char = self.grid[2][0]
        if self.valid_character(char):
            for diag in range (3):
                next_char = self.grid[2-diag][diag]
                if (char != next_char):
                    return False
        return True
        # as currently written return true for empty board or any 
        # board with all invalid playable characters

    def valid_character(self, char):
        return (char == 'O' or char == 'X')

myBoard = Board(blank_board)

while (True):
    input_var = input("Enter [row, col, char]: ")
    myBoard.place_char(input_var[0],input_var[1],input_var[2])
    myBoard.print_board()
    if (myBoard.check_victory):
        print "The character playing " + input_var[2] + " has won!"
        break

