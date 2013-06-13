blank_board = [
            ['_','_','_'], 
            ['_','_','_'], 
            [' ',' ',' '] 
        ]

class Board:
    def __init__(self, grid):
        self.grid = grid
    def placeChar (self, row, col, char):
        if char != 'X' and char != 'O':
            print 'Invalid character. Please enter \'X\' or \'O\''
            return
        if self.grid[row][col] != '_' and self.grid[row][col] != ' ':
            print 'Invalid move. A player has already marked that spot'
            return 
        else: self.grid[row][col] = char
    def printBoard (self):
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

myBoard = Board(blank_board)

while (True):
    myBoard.printBoard()
    input_var = input("Enter [row, col, char]: ")
    myBoard.placeChar(input_var[0],input_var[1],input_var[2])

