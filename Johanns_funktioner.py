import numpy as np



def tree_explorer(board, t, depth = 0, move_list = None):
	if win(board) != 0: # Break recursion
		return win(board)
	elif depth > 5:   # We cap at 5
		return 0
	else:
		avail = availible_moves(board, t)
		for a in avail:
			






def win(board):
	glob_board = np.array(glob_update(board))
	ones, twos = glob_board == 1, glob_board == 2
	if any(np.sum(ones, axis = 0)) == 3 \
		or any(np.sum(ones, axis = 1) == 3) \
		or np.trace(ones) == 3 \
		or np.trace(np.rot90(ones)) == 3:
		return 1

	elif any(np.sum(twos, axis = 0)) == 3 \
		or any(np.sum(twos, axis = 1) == 3) \
		or np.trace(twos) == 3 \
		or np.trace(np.rot90(twos)) == 3:
		return 2

	else:
		return 0



def glob_update(board):
	glob_board = []
	for i in range(len(board)):
		arr = np.array(board[i]).reshape(3,3)
		ones, twos = arr == 1, arr == 2
		if any(np.sum(ones, axis = 0)) == 3 \
			or any(np.sum(ones, axis = 1) == 3) \
			or np.trace(ones) == 3 \
			or np.trace(np.rot90(ones)) == 3:
			glob_board.append(1)

		elif any(np.sum(twos, axis = 0)) == 3 \
			or any(np.sum(twos, axis = 1) == 3) \
			or np.trace(twos) == 3 \
			or np.trace(np.rot90(twos)) == 3:
			glob_board.append(2)
		else:
			glob_board.append(0)
	return glob_board


def availible_moves(board, t):
	# Return all availible moves in a, b format.
	# Return None if no moves are availible

	if t == 9: # Return all availible fields if no board is forced
		moves = []
		glob = glob_update(board)
		for i in range(len(board)):
			if glob[i] == 0:
				bs = np.array(board[i]) == 0
				moves.extend([(i, b) for b in bs.nonzero()[0]])
		return moves

	else:	 # Return field in the forced board
		local = board[t]
		a = t
		bs = np.array(local) == 0
		if np.sum(bs) == 0:
			return None
		else:
			return [(a, b) for b in bs.nonzero()[0]]


def Player1(B, t, won):
	
	if t == 9:
		avail_glob = np.array(won) == 0
		# print(avail_glob)
		a = np.random.choice(avail_glob.nonzero()[0])
	else:
		a = t

	loc = np.array(B[a])

	avail = loc == 0

	b = np.random.choice(avail.nonzero()[0])

	return a, b


def Player2(B, t, won):

	if t == 9:
		avail_glob = np.array(won) == 0
		# print(avail_glob)
		a = np.random.choice(avail_glob.nonzero()[0])
	else:
		a = t

	loc = np.array(B[a])

	avail = loc == 0

	b = np.random.choice(avail.nonzero()[0])

	return a, b


def display(board):
    # This can be used to display the current board
    new_board = [np.array(b).reshape(3,3) for b in board]
    new_board = np.vstack([np.hstack([new_board[j * 3 + i] for i in range(3)]) for j in range(3)])  
    print("Board: \n", new_board)
    won = glob_update(board)
    print("Global_board: \n", np.array(won).reshape(3, 3) )
