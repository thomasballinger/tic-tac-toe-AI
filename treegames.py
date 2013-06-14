import terminal as board


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
	for spot in unplayed_spots:
		new_board = board.Board(current_board.grid)
		new_board.place_char(spot[0],spot[1], new_board.turn)
		poss_boards.append(new_board)
	return poss_boards
# since you never 

new_board = board.Board()

for i in possible_boards(new_board):
	i.print_board()