def print_board(board):
  for row in board:
    print(" | ".join(row))
    print("-" *9)
def check_winner(board):
  for row in board:
    if row[0]==row[1]==row[2]!=" ":
      return True
  for col in range(3):
    if board[0][col]==board[1][col]==board[2][col]!=" ":
      return True
  if board[0][0]==board[1][1]==board[2][2]!=" ":
    return True
  if board[0][2]==board[1][1]==board[2][0]!=" ":
    return True
  return False
board=[[" " for _ in range(3)] for _ in range(3)]
player="X"
for turn in range(9):
  print("\n Current Board: ")
  print_board(board)
  print(f"Player {player}'s turn")
  row=int(input("Enter row(0-2): "))
  col=int(input("enter column(0-2): "))
  if board[row][col]==" ":
    board[row][col]=player
    if check_winner(board):
      print("\n Final Board: ")
      print_board(board)
      print(f"player {player} wins!")
      break
    player="O" if player =="X" else "X"
  else:
    print("Cell already occupied,Try Again")
else:
  print("\nFinal Board:")
  print_board(board)
  print("Game Draw!")
  """ OUTPUT:
  Final Board: 
X | X | X
---------

  | O |  
---------

  |   | O
---------
player X wins """
