import turtle

#making the game board
win = turtle.Screen()
win.title("Tic Tac Toe")
win.setup(400,400)
win.bgcolor("white")
win.tracer(0)

pen = turtle.Turtle()
pen.up()
pen.speed(0)
origin = (-170,170)
pen.setpos(origin)
pen.down()
pen.color("black")

def drawSquare(pen,squareSize):
    for i in range(4):
        pen.forward(squareSize)
        pen.rt(90)

def drawRow(pen,length,squareSize):
    for i in range(length):
        drawSquare(pen,squareSize)
        pen.fd(squareSize)

def drawGrid(pen,size,squareSize):
    for i in range(size):
        length = size
        drawRow(pen,length,squareSize)
        pen.up()
        pen.setpos(origin)
        pen.down()
        pen.right(90)
        pen.forward(squareSize*(i+1))
        pen.left(90)

drawGrid(pen, 3, 110)

Button_A1_x = -167.5
Button_A1_y = 62

Button_A2_x = -57.5
Button_A2_y = 62

Button_A3_x = 52.5
Button_A3_y = 62

Button_B1_x = -167.5
Button_B1_y = -48

Button_B2_x = -57.5
Button_B2_y = -48

Button_B3_x = 52.5
Button_B3_y = -48

Button_C1_x = -167.5
Button_C1_y = -158

Button_C2_x = -57.5
Button_C2_y = -158

Button_C3_x = 52.5
Button_C3_y = -158

ButtonLength = 105
ButtonWidth = 105

turtle.colormode(255)
pen.color(238,238,238)

def coloredSquares(x,y):
    pen.penup()
    pen.begin_fill()
    pen.goto(x, y)
    pen.goto(x + ButtonLength, y)
    pen.goto(x + ButtonLength, y + ButtonWidth)
    pen.goto(x, y + ButtonWidth)
    pen.goto(x, y)
    pen.end_fill()

xList = [Button_A1_x, Button_A2_x, Button_A3_x, Button_B1_x, Button_B2_x, Button_B3_x, Button_C1_x, Button_C2_x, Button_C3_x]
yList = [Button_A1_y, Button_A2_y, Button_A3_y, Button_B1_y, Button_B2_y, Button_B3_y, Button_C1_y, Button_C2_y, Button_C3_y]

for i, j in zip(xList, yList):
    x = i
    y = j
    coloredSquares(x,y)

counter = 0
winner = None
gameRunning = True

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    if checkHorizontal(board):
        pen.goto(-200,55)
        pen.fillcolor("white")
        pen.color("black")
        pen.begin_fill()
        for _ in range(2):
            pen.forward(500)
            pen.right(90)
            pen.forward(100)
            pen.right(90)
        pen.end_fill()
        pen.color("white")
        pen.goto(-135, -10)
        pen.write("The winner is " + winner + " !", font=('Arial', 30, 'bold'))

    elif checkRow(board):
        pen.goto(-200,55)
        pen.fillcolor("white")
        pen.color("black")
        pen.begin_fill()
        for _ in range(2):
            pen.forward(500)
            pen.right(90)
            pen.forward(100)
            pen.right(90)
        pen.end_fill()
        pen.color("white")
        pen.goto(-135, -10)
        pen.write("The winner is " + winner + " !", font=('Arial', 30, 'bold'))

    elif checkDiag(board):
        pen.goto(-200,55)
        pen.fillcolor("white")
        pen.color("black")
        pen.begin_fill()
        for _ in range(2):
            pen.forward(500)
            pen.right(90)
            pen.forward(100)
            pen.right(90)
        pen.end_fill()
        pen.color("white")
        pen.goto(-135, -10)
        pen.write("The winner is " + winner + " !", font=('Arial', 30, 'bold'))


def checkIfTie(board):
    if "-" not in board and winner == None:
        pen.goto(-200,55)
        pen.down()
        pen.fillcolor("black")
        pen.begin_fill()
        for _ in range(2):
            pen.forward(500)
            pen.right(90)
            pen.forward(100)
            pen.right(90)
        pen.end_fill()
        pen.color("white")
        pen.goto(-55, -10)
        pen.write("Its a tie!", font=('Arial', 30, 'bold'))

def buttonClicks(x, y):
    global counter
    if Button_A1_x <= x <= Button_A1_x + ButtonLength:
        if Button_A1_y <= y <= Button_A1_y + ButtonWidth:
            if counter % 2 == 0:
                pen.fillcolor('green')            
                pen.begin_fill()
                pen.goto(Button_A1_x, Button_A1_y)
                pen.goto(Button_A1_x + ButtonLength, Button_A1_y)
                pen.goto(Button_A1_x + ButtonLength, Button_A1_y + ButtonWidth)
                pen.goto(Button_A1_x, Button_A1_y + ButtonWidth)
                pen.goto(Button_A1_x, Button_A1_y)
                pen.end_fill()
                pen.write("X", font=('Arial', 110, 'bold'))
                board[0] = "X"
                counter += 1
            else:
                pen.fillcolor('red')
                pen.begin_fill()
                pen.goto(Button_A1_x, Button_A1_y)
                pen.goto(Button_A1_x + ButtonLength, Button_A1_y)
                pen.goto(Button_A1_x + ButtonLength, Button_A1_y + ButtonWidth)
                pen.goto(Button_A1_x, Button_A1_y + ButtonWidth)
                pen.goto(Button_A1_x, Button_A1_y)
                pen.end_fill()
                pen.write("O", font=('Arial', 110, 'bold'))
                board[0] = "O"
                counter += 1


    if Button_A2_x <= x <= Button_A2_x + ButtonLength:
        if Button_A2_y <= y <= Button_A2_y + ButtonWidth:
            if counter % 2 == 0:
                pen.fillcolor('green')            
                pen.begin_fill()
                pen.goto(Button_A2_x, Button_A2_y)
                pen.goto(Button_A2_x + ButtonLength, Button_A2_y)
                pen.goto(Button_A2_x + ButtonLength, Button_A2_y + ButtonWidth)
                pen.goto(Button_A2_x, Button_A2_y + ButtonWidth)
                pen.goto(Button_A2_x, Button_A2_y)
                pen.end_fill()
                pen.write("X", font=('Arial', 110, 'bold'))
                counter += 1
                board[1] = "X"
            else:
                pen.fillcolor('red')
                pen.begin_fill()
                pen.goto(Button_A2_x, Button_A2_y)
                pen.goto(Button_A2_x + ButtonLength, Button_A2_y)
                pen.goto(Button_A2_x + ButtonLength, Button_A2_y + ButtonWidth)
                pen.goto(Button_A2_x, Button_A2_y + ButtonWidth)
                pen.goto(Button_A2_x, Button_A2_y)
                pen.end_fill()
                pen.write("O", font=('Arial', 110, 'bold'))
                counter += 1
                board[1] = "O"
    if Button_A3_x <= x <= Button_A3_x + ButtonLength:
        if Button_A3_y <= y <= Button_A3_y + ButtonWidth:
            if counter % 2 == 0:
                pen.fillcolor('green')            
                pen.begin_fill()
                pen.goto(Button_A3_x, Button_A3_y)
                pen.goto(Button_A3_x + ButtonLength, Button_A3_y)
                pen.goto(Button_A3_x + ButtonLength, Button_A3_y + ButtonWidth)
                pen.goto(Button_A3_x, Button_A3_y + ButtonWidth)
                pen.goto(Button_A3_x, Button_A3_y)
                pen.end_fill()
                pen.write("X", font=('Arial', 110, 'bold'))
                counter += 1
                board[2] = "X"
            else:
                pen.fillcolor('red')
                pen.begin_fill()
                pen.goto(Button_A3_x, Button_A3_y)
                pen.goto(Button_A3_x + ButtonLength, Button_A3_y)
                pen.goto(Button_A3_x + ButtonLength, Button_A3_y + ButtonWidth)
                pen.goto(Button_A3_x, Button_A3_y + ButtonWidth)
                pen.goto(Button_A3_x, Button_A3_y)
                pen.end_fill()
                pen.write("O", font=('Arial', 110, 'bold'))
                counter += 1
                board[2] = "O"

    if Button_B1_x <= x <= Button_B1_x + ButtonLength:
        if Button_B1_y <= y <= Button_B1_y + ButtonWidth:
            if counter % 2 == 0:
                pen.fillcolor('green')            
                pen.begin_fill()
                pen.goto(Button_B1_x, Button_B1_y)
                pen.goto(Button_B1_x + ButtonLength, Button_B1_y)
                pen.goto(Button_B1_x + ButtonLength, Button_B1_y + ButtonWidth)
                pen.goto(Button_B1_x, Button_B1_y + ButtonWidth)
                pen.goto(Button_B1_x, Button_B1_y)
                pen.end_fill()
                pen.write("X", font=('Arial', 110, 'bold'))
                counter += 1
                board[3] = "X"
            else:
                pen.fillcolor('red')
                pen.begin_fill()
                pen.goto(Button_B1_x, Button_B1_y)
                pen.goto(Button_B1_x + ButtonLength, Button_B1_y)
                pen.goto(Button_B1_x + ButtonLength, Button_B1_y + ButtonWidth)
                pen.goto(Button_B1_x, Button_B1_y + ButtonWidth)
                pen.goto(Button_B1_x, Button_B1_y)
                pen.end_fill()
                pen.write("O", font=('Arial', 110, 'bold'))
                counter += 1
                board[3] = "O"

    if Button_B2_x <= x <= Button_B2_x + ButtonLength:
        if Button_B2_y <= y <= Button_B2_y + ButtonWidth:
            if counter % 2 == 0:
                pen.fillcolor('green')            
                pen.begin_fill()
                pen.goto(Button_B2_x, Button_B2_y)
                pen.goto(Button_B2_x + ButtonLength, Button_B2_y)
                pen.goto(Button_B2_x + ButtonLength, Button_B2_y + ButtonWidth)
                pen.goto(Button_B2_x, Button_B2_y + ButtonWidth)
                pen.goto(Button_B2_x, Button_B2_y)
                pen.end_fill()
                pen.write("X", font=('Arial', 110, 'bold'))
                counter += 1
                board[4] = "X"
            else:
                pen.fillcolor('red')
                pen.begin_fill()
                pen.goto(Button_B2_x, Button_B2_y)
                pen.goto(Button_B2_x + ButtonLength, Button_B2_y)
                pen.goto(Button_B2_x + ButtonLength, Button_B2_y + ButtonWidth)
                pen.goto(Button_B2_x, Button_B2_y + ButtonWidth)
                pen.goto(Button_B2_x, Button_B2_y)
                pen.end_fill()
                pen.write("O", font=('Arial', 110, 'bold'))
                counter += 1
                board[4] = "O"

    if Button_B3_x <= x <= Button_B3_x + ButtonLength:
        if Button_B3_y <= y <= Button_B3_y + ButtonWidth:
            if counter % 2 == 0:
                pen.fillcolor('green')            
                pen.begin_fill()
                pen.goto(Button_B3_x, Button_B3_y)
                pen.goto(Button_B3_x + ButtonLength, Button_B3_y)
                pen.goto(Button_B3_x + ButtonLength, Button_B3_y + ButtonWidth)
                pen.goto(Button_B3_x, Button_B3_y + ButtonWidth)
                pen.goto(Button_B3_x, Button_B3_y)
                pen.end_fill()
                pen.write("X", font=('Arial', 110, 'bold'))
                counter += 1
                board[5] = "X"
            else:
                pen.fillcolor('red')
                pen.begin_fill()
                pen.goto(Button_B3_x, Button_B3_y)
                pen.goto(Button_B3_x + ButtonLength, Button_B3_y)
                pen.goto(Button_B3_x + ButtonLength, Button_B3_y + ButtonWidth)
                pen.goto(Button_B3_x, Button_B3_y + ButtonWidth)
                pen.goto(Button_B3_x, Button_B3_y)
                pen.end_fill()
                pen.write("O", font=('Arial', 110, 'bold'))
                counter += 1
                board[5] = "O"

    if Button_C1_x <= x <= Button_C1_x + ButtonLength:
        if Button_C1_y <= y <= Button_C1_y + ButtonWidth:
            if counter % 2 == 0:
                pen.fillcolor('green')            
                pen.begin_fill()
                pen.goto(Button_C1_x, Button_C1_y)
                pen.goto(Button_C1_x + ButtonLength, Button_C1_y)
                pen.goto(Button_C1_x + ButtonLength, Button_C1_y + ButtonWidth)
                pen.goto(Button_C1_x, Button_C1_y + ButtonWidth)
                pen.goto(Button_C1_x, Button_C1_y)
                pen.end_fill()
                pen.write("X", font=('Arial', 110, 'bold'))
                counter += 1
                board[6] = "X"
            else:
                pen.fillcolor('red')
                pen.begin_fill()
                pen.goto(Button_C1_x, Button_C1_y)
                pen.goto(Button_C1_x + ButtonLength, Button_C1_y)
                pen.goto(Button_C1_x + ButtonLength, Button_C1_y + ButtonWidth)
                pen.goto(Button_C1_x, Button_C1_y + ButtonWidth)
                pen.goto(Button_C1_x, Button_C1_y)
                pen.end_fill()
                pen.write("O", font=('Arial', 110, 'bold'))
                counter += 1
                board[6] = "O"

    if Button_C2_x <= x <= Button_C2_x + ButtonLength:
        if Button_C2_y <= y <= Button_C2_y + ButtonWidth:
            if counter % 2 == 0:
                pen.fillcolor('green')            
                pen.begin_fill()
                pen.goto(Button_C2_x, Button_C2_y)
                pen.goto(Button_C2_x + ButtonLength, Button_C2_y)
                pen.goto(Button_C2_x + ButtonLength, Button_C2_y + ButtonWidth)
                pen.goto(Button_C2_x, Button_C2_y + ButtonWidth)
                pen.goto(Button_C2_x, Button_C2_y)
                pen.end_fill()
                pen.write("X", font=('Arial', 110, 'bold'))
                counter += 1
                board[7] = "X"
            else:
                pen.fillcolor('red')
                pen.begin_fill()
                pen.goto(Button_C2_x, Button_C2_y)
                pen.goto(Button_C2_x + ButtonLength, Button_C2_y)
                pen.goto(Button_C2_x + ButtonLength, Button_C2_y + ButtonWidth)
                pen.goto(Button_C2_x, Button_C2_y + ButtonWidth)
                pen.goto(Button_C2_x, Button_C2_y)
                pen.end_fill()
                pen.write("O", font=('Arial', 110, 'bold'))
                counter += 1
                board[7] = "O"

    if Button_C3_x <= x <= Button_C3_x + ButtonLength:
        if Button_C3_y <= y <= Button_C3_y + ButtonWidth:
            if counter % 2 == 0:
                pen.fillcolor('green')            
                pen.begin_fill()
                pen.goto(Button_C3_x, Button_C3_y)
                pen.goto(Button_C3_x + ButtonLength, Button_C3_y)
                pen.goto(Button_C3_x + ButtonLength, Button_C3_y + ButtonWidth)
                pen.goto(Button_C3_x, Button_C3_y + ButtonWidth)
                pen.goto(Button_C3_x, Button_C3_y)
                pen.end_fill()
                pen.write("X", font=('Arial', 110, 'bold'))
                counter += 1
                board[8] = "X"
            else:
                pen.fillcolor('red')
                pen.begin_fill()
                pen.goto(Button_C3_x, Button_C3_y)
                pen.goto(Button_C3_x + ButtonLength, Button_C3_y)
                pen.goto(Button_C3_x + ButtonLength, Button_C3_y + ButtonWidth)
                pen.goto(Button_C3_x, Button_C3_y + ButtonWidth)
                pen.goto(Button_C3_x, Button_C3_y)
                pen.end_fill()
                pen.write("O", font=('Arial', 110, 'bold'))
                counter += 1
                board[8] = "O"
                
    checkIfWin(board)
    checkIfTie(board)

win.onclick(buttonClicks)

turtle.done()