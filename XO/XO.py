


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

  # ------------ Start Execution -------------
play_game()
