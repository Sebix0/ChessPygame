import pygame
from Piece import Pieces
from MovePlate import MovePlate

def checkLetter(fen, Piece):
  fen = fen.lower() # translating fen into numbers
  total = 0
  if fen == 'r':
    total = Piece.Rook
  elif fen == 'n':
    total = Piece.Knight
  elif fen == 'b':
    total = Piece.Bishop
  elif fen == 'q':
    total = Piece.Queen
  elif fen == 'k':
    total = Piece.King
  elif fen == 'p':
    total = Piece.Pawn
  return total



class Board:
  def __init__(self, fen="8/3P4/8/3Q1p2/2b5/8/8/8"):
    self.Piece = Pieces()

    self.currentPieceIndex = None
    self.currentPiece = None
    self.canCastle = True
    self.enPassantSquare = "-"
    self.board = [0 for i in range(64)]
    self.movePlates = MovePlate() # store the current possible moves for the selected piece
    fen = fen.split(' ')[0].split('/') # split fen into each individual row
    for i in range(len(fen)):
      skipped = 0 # store how many squares we skipped over
      for j in range(len(fen[i])):
        total = 0 # store the piece value
        if fen[i][j] in "12345678":
          skipped += int(fen[i][j]) # if it is a number we skipped over some
          continue
        elif fen[i][j].isupper():
          total = self.Piece.White + checkLetter(fen[i][j], self.Piece) # if upper then the piece is white
        elif not fen[i][j].isupper():
          total = self.Piece.Black + checkLetter(fen[i][j], self.Piece) # if lower then the piece is black
        self.board[i*8+skipped] = total # set the board's value
        skipped += 1 # just went past a letter so we add another one
    
  def getPieceOnBoard(self, col, row=None):
    if row == None: # if only one input (tuple or something) then turn it into row and cols
      row = col[1]
      col = col[0]
    return self.board[row*8 + col]

  def drawMovePlate(self, win, color, center, radius):
    targetRect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shapeSurf = pygame.Surface(targetRect.size, pygame.SRCALPHA)
    pygame.draw.circle(shapeSurf, color, (radius, radius), radius)
    win.blit(shapeSurf, targetRect)


  def drawBoard(self, win):
    col, row = 0, 0

    for i in range(len(self.board)):
      piece = ""
      current = self.board[i]

      if (i+row)%2 == 0:
        pygame.draw.rect(win, pygame.Color("#769656"), pygame.Rect((col*120, row*120), (120, 120))) # if even the make it dark
      else:
        pygame.draw.rect(win, pygame.Color("#eeeed2"), pygame.Rect((col*120, row*120), (120, 120))) # if odd then make it light

      if current > 0:
        piece += self.Piece.getColor(current) # add the color of the piece
        piece += self.Piece.getPiece(current) # add the name of the piece 
        pieceImage = pygame.transform.scale(pygame.image.load(self.Piece.images[piece]), (120, 120)) # create the image
        win.blit(pieceImage, (col*120, row*120)) # draw the image

      if len(self.movePlates.moves) > 0:
        for i in range(len(self.movePlates.moves)):
          if self.movePlates.moves[i][2] == True:
            self.drawMovePlate(win, (255, 0, 0), (self.movePlates.moves[i][0]*120+60, self.movePlates.moves[i][1]*120+60), 20)

          else:
            self.drawMovePlate(win, (50, 50, 50), (self.movePlates.moves[i][0]*120+60, self.movePlates.moves[i][1]*120+60), 20)

      

      col += 1
      if col == 8:
        row += 1
        col = 0 # moving along the rows and columns

  def handleEvents(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if not pygame.mouse.get_pressed()[0]:
        return
        
      mx, my = pygame.mouse.get_pos() 
      col, row = mx//120, my//120 # squares 120x120 pixels so we can get the locations in terms of rows and columns

      if len(self.movePlates.moves) > 0:
        if (col, row, True) in self.movePlates.moves or (col, row, False) in self.movePlates.moves:
          self.board[row*8 + col] = self.currentPiece
          self.board[self.currentPieceIndex] = 0
          self.currentPieceIndex = None
          self.currentPiece = None
          self.movePlates.moves = []
          return
        else:
          self.movePlates.moves = []
          return

      pieceClicked = self.getPieceOnBoard(col, row) # get the value of the piece clicked

      if pieceClicked != None:
        self.currentPieceIndex = row*8 + col
        self.currentPiece = pieceClicked
        pieceColor = self.Piece.getColor(pieceClicked)
        pieceName = self.Piece.getPiece(pieceClicked)

        if pieceName == "Queen":
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), -1, -1)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 0, -1)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 1, -1)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), -1, 0)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 1, 0)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), -1, 1)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 0, 1)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 1, 1)

        elif pieceName == "Rook":
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 0, -1)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), -1, 0)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 1, 0)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 0, 1)

        elif pieceName == "Bishop":
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), -1, -1)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 1, -1)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), -1, 1)
          self.movePlates.LineMovePlate(self, pieceColor, (col, row), 1, 1)


        self.movePlates.moves = list(set(self.movePlates.moves))

        

'''
Day 1:

Taking a break
continue by creating movement
Store the piece that was clicked on
get the squares that it can move to
check the legality of the move
Create Move Plates (turn the possible movement squares a different colour)
Create pawn double movement
...


Day 3(i think):
created movement and capturing of pieces for queens, bishops, and rooks
create capturing and movement of the rest of the pieces and create turns
create special moves like moving twice from starting square, maybe en passant and castling

'''