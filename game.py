import numpy as np

class game:
    """
    Setup the game and play it.
    """

    sup_board = np.zeros(shape = (3, 3))

    def __init__(self, player_1 = 'manual', player_2 = 'manual', board = np.zeros( shape = (9,9)), starting_player = 1):
        # Set board. filled with zeros if not specified and update the super board
        self.board = board
        self.update_sup_board()

        # Set the players, given functions that decide on a move. Manual player as standard.
        if player_1 == 'manual':
            self.player_1 = self.manual
        else:
            self.player_1 = player_1
        if player_2 == 'manual':
            self.player_2 = self.manual
        else:
            self.player_2 = player_2

        self.turn = starting_player 
        # Other parameters coming later, such as saving game and displaying
        # Maybe plotting, so the game can be followed visually


    def play(self):
        self.winner = self.update_sup_board()

        while self.winner == 0:
            self.player_move(self.turn)
            self.turn = self.turn % 2 + 1
            self.winner = self.update_sup_board()




    def availible_moves(self):
        availible = np.ones(shape = (9, 9))
        availible[np.repeat(np.repeat(self.sup_board, 2, axis = 0), 2, axis = 1) != 0] = 0 
        availible[self.board != 0] = 0
        self.availible = availible


    def player_move(self, number = 1):
        player = [self.player_1, self.player_2][number - 1]
        move = player()

        self.board[move] = number


    def eval_board(self, board):
        # Check if player 1 has three in a row
        ones = board == 1
        hori = np.max(np.sum(ones, axis = 0))
        vert = np.max(np.sum(ones, axis = 1))
        diag = np.max([np.sum([ones[i, i] for i in range(3)]), np.sum([ones[i, 2 -i] for i in range(2)])])

        longest_1 = np.max([hori, vert, diag])
        
        if longest_1 == 3:
            return 1
        
        # Heck if player 2 has three in a row
        twos = board == 2

        hori = np.max(np.sum(twos, axis = 0))
        vert = np.max(np.sum(twos, axis = 1))
        diag = np.max([np.sum([twos[i, i] for i in range(3)]), np.sum([twos[i, 2 -i] for i in range(2)])])

        longest_2 = np.max([hori, vert, diag])

        if longest_2 == 3:
            return 2
        else:
            return 0


    def update_sup_board(self):
        """
        Update the super_board
        """
        # Updating the super board by looking at 3x3 fields of the total board
        for i, value in np.ndenumerate(self.sup_board):
            if value != 0:
                self.sup_board[i] = self.eval_board(self.board[i[0] * 3: (i[0] +1) * 3, i[1] * 3 : (i[1]+1) * 3])
            else:
                continue
        
        # Check for tal winner
        return self.eval_board(self.sup_board)


    def manual(self):
        """
        Play in manual mode. Print the board and enter the desired output.
        """
        print("Manual move, see board: \n ", self.board)
        valid = False
        while not valid:
            move_row = input("Which row?")
            move_col = input("Which col?")
            try:
                move = (int(move_row) % 9, int(move_col) % 9)
                return move
            except:
                print("Enter valid move")
                continue
