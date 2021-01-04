


# board of game
board_game = board = ["-"] * 9

# flags
game_still_playing = True
winner = None
current_player = "X"

# ------------- Functions ---------------
def play_game():
   
  show_board()
  while game_still_playing:
    turning(current_player)
  
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

   



def show_board():
  print("\n")
  print(board_game[0] + " | " + board_game[1] + " | " + board_game[2] + "     1 | 2 | 3")
  print(board_game[3] + " | " + board_game[4] + " | " + board_game[5] + "     4 | 5 | 6")
  print(board_game[6] + " | " + board_game[7] + " | " + board_game[8] + "     7 | 8 | 9")
  print("\n")




def turning(player):

  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  
  IsValid = False
  while not IsValid:

    
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    position = int(position) - 1

    
    if board_game[position] == "-":
      IsValid = True
    else:
      print("You can't play here. play again.")

 
  board_game[position] = player
  show_board()


def check_if_winner():
  
  global winner
 
  winner_with_row = if_win_with_row()
  winner_with_column = if_win_with_columns()
  winner_with_diagonal = if_win_with_diagonals()
  
  if winner_with_row:
    winner = winner_with_row
  elif winner_with_column:
    winner = winner_with_column
  elif winner_with_diagonal:
    winner = winner_with_diagonal
  else:
    winner = None
def if_win_with_row():
  
  global game_still_going
  
  row_1 = board_game[0] == board_game[1] == board_game[2] != "-"
  row_2 = board_game[3] == board_game[4] == board_game[5] != "-"
  row_3 = board_game[6] == board_game[7] == board_game[8] != "-"
  
  if row_1 or row_2 or row_3:
    still_going = False
  
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 

  else:
    return None



def if_win_with_columns():
  
  global still_going
  
  column_1 = board_game[0] == board_game[3] == board_game[6] != "-"
  column_2 = board_game[1] == board_game[4] == board_game[7] != "-"
  column_3 = board_game[2] == board_game[5] == board_game[8] != "-"
 
  if column_1 or column_2 or column_3:
    still_going = False
 
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  
  else:
    return None

def if_win_with_diagonals():
  
  global game_still_playing
  
  diagonal_1 = board_game[0] == board_game[4] == board_game[8] != "-"
  diagonal_2 = board_game[2] == board_game[4] == board[6] != "-"
  
  if diagonal_1 or diagonal_2:
    game_still_playing = False
  
  if diagonal_1:
    return board_game[0] 
  elif diagonal_2:
    return board_game[2]
  
  else:
    return None

def tie_or_not():
  
  global game_still_going
  
  if "-" not in board:
    game_still_playing = False
    return True

  else:
    return False

def flip_player():
  
  global current_player
  if current_player == "X":
    current_player = "O"
  
  elif current_player == "O":
    current_player = "X"
  # ------------ Start Execution -------------
play_game()
