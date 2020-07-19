
import pandas as pd

model = pd.read_pickle("models/model000")

def glob_update(board):
    glob_board = []
    for i in range(len(board)):
        arr = np.array(board[i]).reshape(3,3)
        ones, twos = arr == 1, arr == 2
        if any(np.sum(ones, axis = 0)) == 3             or any(np.sum(ones, axis = 1) == 3)             or np.trace(ones) == 3             or np.trace(np.rot90(ones)) == 3:
            glob_board.append(1)

        elif any(np.sum(twos, axis = 0)) == 3             or any(np.sum(twos, axis = 1) == 3)             or np.trace(twos) == 3             or np.trace(np.rot90(twos)) == 3:
            glob_board.append(2)
        else:
            glob_board.append(0)
    return glob_board

def availible_moves(board, t, won):
    # Return all availible moves in a, b format.
    # Return None if no moves are availible

    if t == 9: # Return all availible fields if no board is forced
        moves = []
        for i in range(len(board)):
            if won[i] == 0:
                bs = np.array(board[i]) == 0
                moves.extend([i * 9 + b for b in bs.nonzero()[0]])
        return moves
    else:    # Return field in the forced board
        local = board[t]
        a = t
        bs = np.array(local) == 0
        if np.sum(bs) == 0:
            return None
        else:
            return [a * 9 +  b for b in bs.nonzero()[0]]

def Player(board, t, won):
    avail = availible_moves(board, t, won)
    
    x = np.concatenate([np.array([board]).ravel(), np.array(t).ravel(), np.array(won).ravel()])
    y = model.predict_proba(x.reshape(1, 91))[0][avail]
    
    choice = np.random.choice(avail, p = y / sum(y))

    return choice // 9, choice % 9

Player2 = Player
from Johanns_funktioner import Player1
