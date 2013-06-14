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
	grid = [list(row) for row in current_board.grid]
	for spot in unplayed_spots:
		new_board = terminal.Board(grid)
		new_board.place_char(spot[0],spot[1], new_board.turn)
		poss_boards.append(new_board)
	return poss_boards

def final_boards(current_board):
	fin_boards = []
	if current_board.check_victory():
		turn = current_board.turn
		fin_boards.append((current_board,turn))
		return fin_boards
	elif current_board.turns_left == 0:
		fin_boards.append((current_board,'tie'))
		return fin_boards
	else:
		poss_boards = possible_boards(current_board)
		for board in poss_boards:
			fin_boards = fin_boards + final_boards(board)
	return fin_boards


one_left_board = [
            ['X','O','O'], 
            ['O','X','O'], 
            ['_','_','_'] 
        ]

start_board = terminal.Board()


ends = final_boards(start_board)

for i in ends:
	i[0].print_board()
	print i[1]

# poss_boards = possible_boards(start_board)

# for board in poss_boards:
# 	next_poss_board = possible_boards(board)
# 	board.print_board()
# 	for next_board in next_poss_board:
# 		next_board.print_board()