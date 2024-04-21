from Piece import Pieces

class MovePlate:
  def __init__(self):
    self.Piece = Pieces()
    self.moves = []
  
  def LineMovePlate(self, Board, pieceColor, piecePos, vx, vy, movesList=None):
    col, row = piecePos
    while (0 <= row and row < 8) and (0 <= col and col < 8):
      if row + vy >= 8 or col + vx >= 8 or row + vy < 0 or col + vx < 0: # validate the next move
        return  # if erroneous then return
      next = [col+vx, row+vy]
      nextPiece = Board.getPieceOnBoard(next)
      if nextPiece != 0: # if the next piece is a piece
        if self.Piece.getColor(nextPiece) == pieceColor:
          return  # if it is the same color then return all movePlates up until that piece
        elif self.Piece.getColor(nextPiece) != pieceColor:
          self.moves.append((next[0], next[1], True))
          return  # if a different color then return all movePlates including the oppositely colored piece
      else:
        self.moves.append((next[0], next[1], False)) # if no piece there then just add on to the list
        col = next[0]
        row = next[1]
    if movesList != None:
      movesList = self.moves
      self.moves = []
  

  def PawnMovePlate(self, Board, pieceColor, piecePos, movesList=None):
    col, row = piecePos
    moveTwice = False
    moveAhead = True
    moveDirection = 1
    if pieceColor == "white":
      moveDirection = -1

    if (row == 7 and moveDirection == -1) or (row == 0 and moveDirection == 1):
      return

    if (pieceColor == "white" and row == 6) or (pieceColor == "black" and row == 1):
      moveTwice = True

    if Board.getPieceOnBoard(col, row+moveDirection) == 0:
      self.moves.append((col, row+moveDirection, False))
      if moveTwice:
        if Board.getPieceOnBoard(col, row+(2*moveDirection)) == 0:
          self.moves.append((col, row+(2*moveDirection), False))
          
    if col != 0:
      pieceLeft = Board.getPieceOnBoard((col-1, row+moveDirection))
    else:
      pieceLeft = 0

    if pieceLeft != 0 and self.Piece.getColor(pieceLeft) != pieceColor:
      self.moves.append((col-1, row+moveDirection, True))

    if col != 7:  
      pieceRight = Board.getPieceOnBoard((col+1, row+moveDirection))
    else:
      pieceRight = 0

    if pieceRight != 0 and self.Piece.getColor(pieceRight) != pieceColor:
      self.moves.append((col+1, row+moveDirection, True))

    if movesList != None:
      movesList = self.moves
      self.moves = []
    

  def SingleMovePlate(self, Board, pieceColor, piecePos, vx, vy, movesList=None):
    col, row = piecePos
    if (0 > col+vx or 7 < col+vx) or (0 > row+vy or 7 < row+vy):
      return
    nextPiece = Board.getPieceOnBoard(col+vx, row+vy)
    if nextPiece != 0 and self.Piece.getColor(nextPiece) != pieceColor:
      self.moves.append((col+vx, row+vy, True))
    elif nextPiece == 0:
      self.moves.append((col+vx, row+vy, False))
    if movesList != None:
      movesList = self.moves
      self.moves = []

  def Castle(self, Board, pieceColor, piecePos, side):
    col, row = piecePos
    if side == "Kingside":
      piecesBetween = [Board.getPieceOnBoard(col+1, row), Board.getPieceOnBoard(col+2, row)]
      if not (piecesBetween[0] or piecesBetween[1]):
        self.moves.append((col+2, row, False))
    elif side == "Queenside":
      piecesBetween = [Board.getPieceOnBoard(col-1, row), Board.getPieceOnBoard(col-2, row), Board.getPieceOnBoard(col-3, row)]
      if not (piecesBetween[0] or piecesBetween[1] or piecesBetween[2]):
        self.moves.append((col-2, row, False))
    

   