# This is the driver file that will handling user input and the current game state
import pygame as p
import ChessEngine
import os

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # For Animation
IMAGES = {}

"""
initialize a global dict of images that will be called only once during the whole run
"""
def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR', 'bP', 'wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN',
              'wR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))


"""
The main driver for this game. This will handle user input and updating the graphics
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(os. getcwd())
    loadImages()  # only once before the while loop
    running = True
    sqSelected = ()  # no square is selected, keep track of the last click of the user, tuple(row, col)
    playerClicks = [] # keep track of the player's click 2 tuples [(6, 4), (4, 4)]

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_rel()    # (x,y) location of mouse
                col = location[0]//SQ_SIZE
                row = location[0]//SQ_SIZE
                if sqSelected == (row, col):    # the user clicked the same square twice
                    sqSelected = () # deselect
                    playerClicks = []   # cleared clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # append for both 1st and 2nd clicks
                if len(playerClicks) == 2:  # after 2nd click
                    

            drawGameState(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()


'''
responsible for all graphics in current game state
'''
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


'''
draw squares on the board
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
draw pieces using current gs.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
