import terminal


# # takes [boards] returns for x=='won_game' in [boards]
# def player_X(board):


# def player_O(board):
# 	if board.check_victory():
# 		return board
# 	else: 
# 		unplayed_spots = board.unplayed_spots()
# 		player_O(board)
# 	return [board]


def possible_boards(current_board):
	unplayed_spots = current_board.unplayed_spots()
	poss_boards = []
	grid = current_board.grid
	for spot in unplayed_spots:
		new_board = terminal.Board(grid)
		new_board.place_char(spot[0],spot[1], new_board.turn)
		poss_boards.append(new_board)
	return poss_boards

start_board = terminal.Board()
# new_board.print_board()
# new_board.place_char(0,0,'X')
# new_board.print_board()

# new_board2 = terminal.Board()
# new_board2.print_board()
# new_board2.place_char(1,0,'X')
# new_board2.print_board()

poss_boards = possible_boards(start_board)

for i in poss_boards:
	i.print_board()

