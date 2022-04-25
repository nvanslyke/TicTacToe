import pygame
import sys
import numpy as np
import random
import time

print("Tic-Tac-Toe by Nathan Van Slyke")
print()
print()
width = 500
height = 500
BG = (30,150,150)
BLACK = (0,0,0)
PieceColor = (65, 89, 148)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")
rows= 3
cols= 3
lineThickness = 10
player= 1
board = np.zeros((rows,cols))
taken = np.zeros((rows,cols))
computer = False
computer2 = False



def turn(row, col):
    global player
    global computer
    global computer2
    if isAvailable(row,col):
        board[row][col] = player
        taken[row][col] = 1
        drawPlay()

    if player == 1:
        if computer == True: 
            player = 2
            playcomp()
            drawPlay()
        elif computer2 == True:
            player = 2
            playcomp()
            drawPlay()
        else:
            player = 2
    elif player ==2:
        if computer2 == True:
            player = 1
            playcomp()
        
        else:
            player =1
        
    
def playcomp():
    global computer
    global computer2
    w = True
    drawPlay()
    if checkWinner() == 1:
        drawPlay()
        pygame.display.update()
        time.sleep(.5)
        display_slide(window, 'player1win.jpg')
        if computer2 == True:
            time.sleep(.5)
            restartbaord()
            drawGame() 
            time.sleep(.5)
            x = random.randrange(3)
            y = random.randrange(3)
            turn(x,y)
                
    elif checkWinner() == 2:
        drawPlay()
        pygame.display.update()
        time.sleep(.5)
        display_slide(window, 'player2win.jpg')
        if computer2 == True:
            time.sleep(.5)
            restartbaord()
            drawGame() 
            time.sleep(.5)
            x = random.randrange(3)
            y = random.randrange(3)
            turn(x,y)
    elif fullBoard():
        drawPlay()
        pygame.display.update()
        time.sleep(.5)
        display_slide(window, 'tie_game.png')
        if computer2 == True:
            time.sleep(.5)
            restartbaord()
            drawGame() 
            time.sleep(.5)
            x = random.randrange(3)
            y = random.randrange(3)
            turn(x,y)

    pygame.display.update()
    while w:
        x = random.randrange(3)
        y = random.randrange(3)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    computer = False
                    computer2 = False
                    print("Computers are no longer playng")
                    pygame.display.set_caption("Tic-Tac-Toe")
                    main()
        if board[x][y] == 0:
            turn(x,y) 
            w = False
        elif fullBoard():
            break
        
        
def CompvComp():
    p = True
    while p:
        q = random.randrange(3)
        w = random.randrange(3)
        if board[q][w] == 0:
            turn(q,w)
        elif fullBoard():
            break
        
    


def findFreeSpaces():
    choices = []
    for row in range(rows):
       for col in range(cols):
           if isAvailable(row, col):
                choices += board[row][col]
    return choices
           
def isAvailable(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def fullBoard():
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                return False
    return True

def onClick(xOfMouse, yOfMouse):
    if xOfMouse < 162 and yOfMouse < 162 and isAvailable(0,0):
        turn(0,0)
    elif xOfMouse > 162 and xOfMouse < 339 and yOfMouse < 162 and isAvailable(0,1):
        turn(0,1)
    elif xOfMouse > 339 and xOfMouse < 500 and yOfMouse < 162 and isAvailable(0,2):
        turn(0,2)
    elif xOfMouse < 160 and yOfMouse > 162 and yOfMouse < 338 and isAvailable(1,0):
        turn(1,0)
    elif xOfMouse > 160 and xOfMouse < 339 and yOfMouse < 338 and yOfMouse > 160 and isAvailable(1,1):
        turn(1,1)
    elif xOfMouse > 339 and xOfMouse < 500 and yOfMouse > 160 and yOfMouse < 338 and isAvailable(1,2):
        turn(1,2)
    elif xOfMouse < 162 and yOfMouse > 338 and isAvailable(2,0):
        turn(2,0)
    elif xOfMouse > 162 and xOfMouse < 339 and yOfMouse > 338 and isAvailable(2,1):
        turn(2,1)
    elif xOfMouse > 339 and yOfMouse > 339 and isAvailable(2,2):
        turn(2,2)
    
def checkWinner():
    if board[0][0] == board[0][1] == board[0][2] and board[0][1] != 0:
        print(board[0][1])
        return board[0][1]
    elif board[0][0] == board[1][0] == board[2][0] and board[1][0] != 0:
        print(board[1][0])
        return board[1][0]
    elif board[0][1] == board[1][1] == board[2][1] and board[1][1] != 0:
        print(board[1][1])
        return board[1][1]
    elif board[0][2] == board[1][2] == board[2][2] and board[1][2] != 0:
        print(board[1][2])
        return board[1][2]
    elif board[1][0] == board[1][1] == board[1][2] and board[1][1] != 0:
        print(board[1][1])
        return board[1][1]
    elif board[2][0] == board[2][1] == board[2][2] and board[2][1] != 0:
        print(board[2][1])
        return board[2][1]
    elif board[0][0] == board[1][1] == board[2][2] and board[1][1] != 0:
        print(board[1][1])
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != 0:
        print(board[1][1])
        return board[1][1]
      


def drawPlay():
    global computer
    global computer2
    global player
    xrad = 0
    yrad = 0  
    for row in range(rows):
        for col in range(cols):
            if row == 0:
                yrad = 81
            elif row == 1:
                yrad = 250
            elif row == 2:
                yrad = 419
            if col == 0:
                xrad = 81
            elif col == 1:
                xrad = 250
            elif col == 2:
                xrad = 419
            if board[row][col] == 1:
                if computer2 == True:
                    pygame.draw.line(window, PieceColor, (col * 162 + 30, row * 162 + 30), (col * 162 + 146, row * 162 + 146), 10)
                    pygame.draw.line(window, PieceColor, (col * 162 + 146, row * 162 + 30), (col * 162 + 30, row * 162 + 146), 10)
                else:
                    pygame.draw.line(window, PieceColor, (col * 162 + 30, row * 162 + 30), (col * 162 + 146, row * 162 + 146), 10)
                    pygame.draw.line(window, PieceColor, (col * 162 + 146, row * 162 + 30), (col * 162 + 30, row * 162 + 146), 10)

                
                
            elif board[row][col] == 2:
                if computer == True or computer2 == True:
                    pygame.draw.circle(window, PieceColor, (xrad, yrad), 55, 10)
                else:
                    pygame.draw.circle(window, PieceColor, (xrad, yrad), 55, 10)

                
                
            

def restartbaord():
    for row in range(rows):
        for col in range(cols): 
            board[row][col] = 0               


def drawGame():
    window.fill(BG)
    pygame.draw.line(window, BLACK, (162,10), (162, 490),lineThickness)
    pygame.draw.line(window, BLACK, (338,10), (338, 490),lineThickness)
    pygame.draw.line(window, BLACK, (490,338), (10, 338),lineThickness)
    pygame.draw.line(window, BLACK, (10,162), (490, 162),lineThickness)
    pygame.display.update()

def display_slide(screen, filename):
    
    image = pygame.image.load(filename)
    screen.blit(image, (0,0))
    pygame.display.flip()
    



def main():
    global computer
    global player
    global computer2
    player = 1
    restartbaord()
    drawGame() 
    
    running = True
 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                xOfMouse = event.pos[0]
                yOfMouse = event.pos[1]

                onClick(xOfMouse,yOfMouse)
                print(xOfMouse)
                print(yOfMouse)
                
                drawPlay()
                pygame.display.update()
                print(board)
                print()
                if checkWinner() == 1:
                    time.sleep(.2)
                    display_slide(window, 'player1win.jpg')
                elif checkWinner() == 2:
                    time.sleep(.2)
                    display_slide(window, 'player2win.jpg')
                
                if fullBoard() and checkWinner() != 1 and checkWinner() != 2:
                    print("Full Board")
                    display_slide(window, 'tie_game.png')
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    computer = False
                    computer2 = False
                    main()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if computer == True:
                        computer = False
                        print("You are no longer playing against a computer")
                        main()
                    else:
                        computer2 = False
                        computer = True
                        print("You are now playing against a computer")
                        main()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    if computer2 == True:
                        computer2 = False
                        print("Computers are no longer playng")
                        main()
                    else:
                        computer = False
                        computer2 = True
                        print("Computers are now playing")
                        pygame.display.set_caption("Press Space to Stop")
                        x = random.randrange(3)
                        y = random.randrange(3)
                        restartbaord()
                        drawGame() 
                        turn(x,y)



            

                    



        
    pygame.quit()

if __name__ == "__main__":
    main()