
class Board:
    def __init__(self):
        self.board = []
        self.played = []
        for num in range(0, 3):
            self.board.append([' '] * 3)
    
    def __repr__(self):
        print(" ----- ----- ----- ")
        print("|     |     |     |")
        print("|  {0}  |  {1}  |  {2}  |".format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print("|     |     |     |")
        print(" ----- ----- ----- ")
        print("|     |     |     |")
        print("|  {0}  |  {1}  |  {2}  |".format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print("|     |     |     |")
        print(" ----- ----- ----- ")
        print("|     |     |     |")
        print("|  {0}  |  {1}  |  {2}  |".format(self.board[2][0], self.board[2][1], self.board[2][2]))
        print("|     |     |     |")
        print(" ----- ----- ----- ")
        return ""

    def play_turn(self, coordinates, player):
        rows_played = {0:0, 1:0, 2:0} # Store number of entries in each row
        cols_played = {0:0, 1:0, 2:0} # Store number of entries in each column
        row = int(coordinates[0]) # Convert first num in coordinates to int, serve as row
        col = int(coordinates[1]) # Convert first num in coordinates to int, serve as col

        if coordinates in self.played: # Checks if coordinate is already played
            return 0 # Return 0 if play invalid
        else:
            self.played.append(coordinates) # Add new coordinate to played list
            self.board[row][col] = player # Change row and col in play board to player char (x or o)
            rows_played[row] += 1 # Update number of entries in row
            cols_played[col] += 1 # Update number of entries in column
        
        if len(self.played) > 2: # Check for wins if len of played list greater than 2 entries, will return player if they win
            if rows_played[row] == 3 and self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]:
                # Check if row played by player is full, and if all equal to each other
                return player
            elif cols_played[col] == 3 and self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]:
                # Check if col played by player is full, and if all equal to each other
                return player
            elif self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
                # Check diagonal from left to right
                return player
            elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
                # Check diagonal from right to left
                return player
        return 1 # Return 1 if play was valid and not a winning one

'''
Tests:
test_board = Board()
test = test_board.play_turn("00", 'x')
print(test)
test = test_board.play_turn("11", 'x')
print(test)
test = test_board.play_turn("00", 'x')
print(test)
test = test_board.play_turn("22", 'x')
print(test)
print(test_board)
'''