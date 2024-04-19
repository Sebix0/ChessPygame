from Piece import Pieces

class MovePlate:
  def __init__(self):
    self.Pieces = Pieces()
    self.moves = []
  
  def LineMovePlate(self, Board, pieceColor, piecePos, vx, vy):
    col, row = piecePos
    while (-1 <= row and row < 9) and (-1 <= col and col < 9):
      if row + vy >= 8 or col + vx >= 8 or row + vy < 0 or col + vx < 0: # validate the next move
        return  # if erroneous then return
      next = [col+vx, row+vy]
      nextPiece = Board.getPieceOnBoard(next)
      if nextPiece != 0: # if the next piece is a piece
        if self.Pieces.getColor(nextPiece) == pieceColor:
          return  # if it is the same color then return all movePlates up until that piece
        elif self.Pieces.getColor(nextPiece) != pieceColor:
          self.moves.append((next[0], next[1], True))
          return  # if a different color then return all movePlates including the oppositely colored piece
      else:
        self.moves.append((next[0], next[1], False)) # if no piece there then just add on to the list
        col = next[0]
        row = next[1]
    