import terminal


# # takes [boards] returns for x=='won_game' in [boards]
# def player_X(board):


# def player_O(board):
#     if board.check_victory():
#         return board
#     else:
#         unplayed_spots = board.unplayed_spots
#         player_O(board)
#     return [board]


def possible_boards(current_board):
    unplayed_spots = current_board.unplayed_spots
    poss_boards = []
    grid = [list(row) for row in current_board.rows]
    for spot in unplayed_spots:
        new_board = terminal.Board(grid)
        new_board.place_char(spot[0],spot[1])
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

def calc_util(end_states, player):
    outcomes = [end[1] for end in end_states]
    util = 0
    for result in outcomes:
        if result == 'tie':
            pass
        elif result == player:
            util += 1
        else:
            util -= 1
    return util

def best_move(board):
    poss_boards = possible_boards(board)
    board_utils = []
    for board in poss_boards:
        ends = final_boards(board)
        util = calc_util(ends, board.turn)
        board_utils.append((board,util))
    best_next = best_move_helper(board_utils)
    row, col = best_next.find_diff(board)
    return (row,col)

def best_move_helper(pairs):
    best = pairs[0][0]
    for pair in pairs:
        if pair[1] > best[1]:
            best = pair[0]
    return best


other_board = [
            ['O','X','O'],
            ['X','O','O'],
            ['X','O','X']
           ]

start_board = terminal.Board(other_board)

ends = final_boards(start_board)

print calc_util(ends, 'O')

# poss_boards = possible_boards(start_board)

# for board in poss_boards:
#     next_poss_board = possible_boards(board)
#     board.print_board()
#     for next_board in next_poss_board:
#         next_board.print_board()
