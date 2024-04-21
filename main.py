import pygame, sys
from Piece import Pieces
from Board import Board

WIN_WIDTH = 960
WIN_HEIGHT = 960
FPS = 30
  
class Game:
  def __init__(self):
    pygame.init()
    self.WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Chess")
    self.Clock = pygame.time.Clock()

    self.Board = Board()
    
  def run(self):
    for event in pygame.event.get():
      self.Clock.tick(FPS)
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      
      self.Board.handleEvents(event)
    if not self.Board.whiteKing:
      print("Black wins")
      pygame.quit()
      sys.exit()
    elif not self.Board.blackKing:
      print("White wins")
      pygame.quit()
      sys.exit()

      
    self.Board.drawBoard(self.WIN)

    pygame.display.update()
      

if __name__ == "__main__":
  game = Game()
  while True:
    game.run()
