def game(): 
 print("			WELCOME TO PEG SOLITAIRE")
 print("RRULES:")
 print("1.PEG - 'O'	HOLE - '_'")
 print("1.A PEG IS MOVED TO A HOLE")
 print("2.A PEG MUST JUMP OVER AN ADJACENT PEG")
 print("3.A PEG SHOULD NOT JUMP OVER A HOLE")
 print("4.A PEG CAN MOVE EITHER VERTICALLY OR HORIZONTALLY")
 print("5.NO CROSS MOVES ARE ALLOWED")

def initial_board():
 a = [[' ', 1, 2, 3, 4, 5, 6, 7], [1, ' ',' ','O','O','O',' ',' '], [2, ' ',' ','O','O','O',' ',' '], [3, 'O','O','O','O','O','O','O'], [4, 'O','O','O','_','O','O','O'], [5, 'O','O','O','O','O','O','O'], [6, ' ',' ','O','O','O',' ',' '], [7, ' ',' ','O','O','O',' ',' ']]
 return a

def print_board(board):
 for i in board:
  print('                                   ', end = "")
  print('  '.join([str(elem) for elem in i]))

def win(board):
 c = 0
 for i in board:
  for j in i:
   if (j == 'O'):
    c = c + 1
 if(c == 1 and board[4][4] == 'O'):
  return True
 return False

def can_move(board, row, col):
 if(col <= 5 and board[row][col + 1] == 'O' and board[row][col + 2] == '_'):
  return 1
 if(col >= 3 and board[row][col - 1] == 'O' and board[row][col - 2] == '_'):
  return 1
 if(row <= 5 and board[row + 1][col] == 'O' and board[row + 2][col] == '_'):
  return 1
 if(row >= 3 and board[row - 1][col] == 'O' and board[row - 2][col] == '_'):
  return 1
 return 0

def lose(board):
 for i in range(1, 8):
  for j in range(1, 8):
   if(board[i][j] == 'O'):
    if(can_move(board, i, j)):
     return 0
 return 1

def invalid():
 print("INVALID MOVE!Only one peg can be jumped over.")

def not_peg():
 print("INVALID MOVE!A peg can't jump over a hole.")

def same_row(board, s_row, s_col, d_row, d_col):
 if(s_col - d_col == -2):
  if(board[s_row][s_col + 1] == 'O'):
   board[d_row][d_col] = 'O'
   board[s_row][s_col] = '_'
   board[s_row][s_col + 1] = '_'
  else:
   not_peg()
 elif(s_col - d_col == 2):
  if(board[s_row][s_col - 1] == 'O'):
   board[d_row][d_col] = 'O'
   board[s_row][s_col] = '_'
   board[s_row][s_col - 1] = '_'
  else:
   not_peg()
 else:
  invalid()
 return board

def same_column(board, s_row, s_col, d_row, d_col):
 if(s_row - d_row == -2):
  if(board[s_row + 1][s_col] == 'O'):
   board[d_row][d_col] = 'O'
   board[s_row][s_col] = '_'
   board[s_row + 1][s_col] = '_'
  else:
   not_peg()
 elif(s_row - d_row == 2):
  if(board[s_row - 1][s_col] == 'O'):
   board[d_row][d_col] = 'O'
   board[s_row][s_col] = '_'
   board[s_row - 1][s_col] = '_'
  else:
   not_peg()
 else:
  invalid()
 return board

def update_board(board, s_row, s_col, d_row, d_col):
 if(s_row < 1 or s_row > 7 or s_col < 1 or s_col > 7 or d_row < 1 or d_row > 7 or d_col < 1 or d_col > 7):
  print("OOPS!YOU ARE OUT OF BOARD!")
 elif(board[s_row][s_col] != 'O'):
  print("ONLY A PEG CAN BE MOVED!")
 elif(board[d_row][d_col] != '_'):
  print("PEG SHOULD BE MOVED TO A HOLE")
 else:
  if(s_row == d_row and s_col == d_col):
   print("THE PEG DID NOT JUMP OVER A HOLE!")
  elif(s_row == d_row):
   board = same_row(board, s_row, s_col, d_row, d_col)
  elif(s_col == d_col):
   board = same_column(board, s_row, s_col, d_row, d_col)
  else:
   print("CROSS MOVES ARE NOT ALLOWED!")
 print_board(board)

game()
in_board = initial_board()
print_board(in_board)
while(win(in_board) is False):
 if(lose(in_board) == 1):
  print("OOPS!NO MOVES LEFT!YOU LOST!")
  exit(0)
 s_row = int(input("SOURCE ROW:"))
 s_col = int(input("SOURCE COLUMN:"))
 d_row = int(input("DEST ROW:"))
 d_col = int(input("DEST COLUMN:"))
 update_board(in_board, s_row, s_col, d_row, d_col)
print("HURRAY!YOU WON!Added this!Friends!")
print("Added this now!")
