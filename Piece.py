class Pieces:
  def __init__(self):
    self.NAN = 0 # assign each piece a value
    self.King = 1
    self.Pawn = 2
    self.Bishop = 3
    self.Knight = 4
    self.Rook = 5
    self.Queen = 6
    self.MovePlate = 7

    self.White = 8 # assign each color a value
    self.Black = 16

    self.images = { # store the location of each pieces sprite
      'whiteRook': 'Assets/whiteRook.png',
      'whiteKnight': 'Assets/whiteKnight.png',
      'whiteBishop': 'Assets/whiteBishop.png',
      'whiteQueen': 'Assets/whiteQueen.png',
      'whiteKing': 'Assets/whiteKing.png',
      'whitePawn': 'Assets/whitePawn.png',

      'blackRook': 'Assets/blackRook.png',
      'blackKnight': 'Assets/blackKnight.png',
      'blackBishop': 'Assets/blackBishop.png',
      'blackQueen': 'Assets/blackQueen.png',
      'blackKing': 'Assets/blackKing.png',
      'blackPawn': 'Assets/blackPawn.png'
    } 

  def getPiece(self, num):
    num = num%8
    if num == 0:
      return None
    elif num == 1:
      return "King"
    elif num == 2:
      return "Pawn"
    elif num == 3:
      return "Bishop"
    elif num == 4:
      return "Knight"
    elif num == 5:
      return "Rook"
    elif num == 6:
      return "Queen"
    elif num == 7:
      return "MovePlate" # might change this later or just remove it

  def getColor(self, num):
    num = num - (num%8) # num%8 is the value of the piece, a piece = piece.color + piece.value
    if num == 16:
      return "black"
    elif num == 8:
      return "white"
    else:
      return None # if it is neither then the piece is none