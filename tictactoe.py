class Board:
  def __init__(self):
    self.board = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:",":seven:", ":eight:", ":nine:"]

  def printBoard(self):
    # boardy is the emojis to be printed
    # using emojis cuz it looks better
    return(' '.join(self.board[:3])+"\n"+' '.join(self.board[3:6])+"\n"+' '.join(self.board[6:9]))    

  def VerticalCheck(self):
    #checks every column to see if all 3 cases
    #correspond to a certain letter
        for Column in range(3):
            if self.board[Column::3] == [":o:"]*3 or self.board[Column::3] == [":x:"]*3:
                return True  
        return False
  def HorizontalCheck(self):
    #checks every row to see if all 3 cases
    #correspond to a certain letter
        for row in range(3):
            if self.board[row*3:row*3+3] == [":o:"]*3 or self.board[row*3:row*3+3] == [":x:"]*3:
              return True
        return False
  def DiagonalCheck(self):
    #checks diagonally to see if all 3 cases
    #correspond to a certain letter
        if self.board[0::4] == [":o:"]*3 or self.board[-3:1:-2] == [":o:"]*3 or self.board[0::4] == [":x:"]*3 or self.board[-3:1:-2] == [":x:"]*3:
            return True
        return False
  def checkWin(self):
    #checks vertically, horizontally then diagonally
    #returns True if there is a winner, False if none
        win = self.VerticalCheck()
        if win == False:
            win = self.HorizontalCheck()
        if win == False:
            win = self.DiagonalCheck()
        return win
  def checkEmpty(self, position):
      if position.content == "forfeit":
        return True
      if position.content.isnumeric() == False:
        return False
      if int(position.content) not in list(range(1,10)): 
        return False
      if self.board[int(position.content)-1] not in [":o:", ":x:"]:
        return True
      return False
  def appendBoard(self, position, player):
      self.board[int(position.content)-1] = ':' + player + ':'