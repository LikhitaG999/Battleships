"""
Battleship Project

Name:Sai Likhita Gade

Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["board_size"]=500
    data["cell_size"]=data["board_size"]//data["cols"]
    print(data["cell_size"])
    data["ships"]=5
    data["computer"]= emptyGrid(data["rows"],data["cols"])
    data["computer"]=addShips(data["computer"],data["ships"])
    data["user"]= emptyGrid(data["rows"],data["cols"])
    # data["user"]=addShips (data["computer"],data["ships"])
    #data["user"]=test.testGrid()
   # data["temp"]=test.testShip()
    data["temp"]=[]
    data["user-ships"]=0
    data["winner"]=None
    data["max"]=50
    data["current_turn"]=0
    #data["winner"]="draw"
    #data["winner"]="user"    
    return 


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas, data["user"],True)
    drawGrid(data,compCanvas,data["computer"],False)
    drawShip(data,userCanvas,data["temp"])
   # if((data["winner"])=="user"):
       # drawGameOver(data,userCanvas)
   # elif((data["winner"])=="comp"):
       # drawGameOver(data,userCanvas)
   # elif((data["winner"])=="draw"):
    drawGameOver(data,userCanvas)
    drawGameOver(data,compCanvas)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    print(event)
    makeModel(data)
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if data["winner"]==None:
        cell=getClickedCell(data,event)
        if board =="user":
           clickUserBoard(data,cell[0],cell[1])
        if board=="comp":
           clickUserBoard(data,cell[0],cell[1])
           runGameTurn(data,cell[0],cell[1])
    return
    

#else:
#data["computer"](cell[0],cell[1])

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''

def emptyGrid(rows, cols):

    Grid=[]
    for i in range(rows):
        column=[]
        for j in range(cols):
            column.append(1)
        Grid.append(column)
    return Grid



'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row=random.randint(1,8)
    col = random.randint(1,8)
    number=random.randint(0,1)
    if number == 0:
        ship = [[row,col-1],[row,col],[row,col+1]]
    else:
        ship=[[row-1,col],[row,col],[row+1,col]]
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    count=0
    for i in range(len(ship)):
        row=ship[i][0]
        col=ship[i][1]
        if grid[row][col]==EMPTY_UNCLICKED:
            count=count+1
    if count != 3:
        return False
    else:
        return True




'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints 
'''
def addShips(grid, numShips):
    while (numShips>0):
        ship=createShip()
        A_ship = checkShip(grid,ship)
        if (A_ship == True ):
            for i in range(len(ship)):
                row=ship[i][0]
                col=ship[i][1]
                grid[row][col] = SHIP_UNCLICKED
            numShips -= 1
    return grid



'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(data["rows"]):
        for j in range(data["cols"]):
            if grid[i][j]==SHIP_UNCLICKED:
                if(showShips==True):
                   canvas.create_rectangle(j*data["cell_size"],i*data["cell_size"],(j+1)*data["cell_size"],(i+1)*data["cell_size"],fill="yellow")
                elif(showShips==False):
                   canvas.create_rectangle(j*data["cell_size"],i*data["cell_size"],(j+1)*data["cell_size"],(i+1)*data["cell_size"],fill="blue")
            elif(grid[i][j]==EMPTY_UNCLICKED):
                canvas.create_rectangle(j*data["cell_size"],i*data["cell_size"],(j+1)*data["cell_size"],(i+1)*data["cell_size"],fill="blue")       
            elif grid[i][j]==SHIP_CLICKED:
                canvas.create_rectangle(j*data["cell_size"],i*data["cell_size"],(j+1)*data["cell_size"],(i+1)*data["cell_size"],fill="red")  
            elif grid[i][j]==EMPTY_CLICKED:
                canvas.create_rectangle(j*data["cell_size"],i*data["cell_size"],(j+1)*data["cell_size"],(i+1)*data["cell_size"],fill="white") 
    return
    


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    if ((ship[0][1])==(ship[1][1])==(ship[2][1])):
        if((ship[0][0]+2)==(ship[1][0]+1)==(ship[2][0])):
            return True
        elif((ship[0][0])==(ship[1][0]+1)==(ship[2][0]+2)):
            return True
        elif((ship[0][0])==(ship[1][0]+2)==(ship[2][0]+1)):
            return True
        else:
            return False
    else:
        return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    if ((ship[0][0])==(ship[1][0])==(ship[2][0])):
        if ((ship[0][1]+2)==(ship[1][1]+1)==(ship[2][1])):
            return True
        elif((ship[0][1])==(ship[1][1]+1)==(ship[2][1]+2)):
            return True
        elif((ship[0][1])==(ship[1][1]+2)==(ship[2][1]+1)):
            return True
        else:
            return False
    else:
        return False

'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    return[int(event.y//data["cell_size"]),int(event.x//data["cell_size"])]
    


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in ship:
        canvas.create_rectangle(i[1]*data["cell_size"],i[0]*data["cell_size"],(i[1]+1)*data["cell_size"],(i[0]+1)*data["cell_size"],fill="white")
    return 


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
   return checkShip(grid,ship) and isVertical(ship) or isHorizontal(ship)


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["user"],data["temp"]):
        for i in range(len(data["temp"])):
            c=data["temp"][i][0]
            r=data["temp"][i][1]
            data["user"][c][r] = SHIP_UNCLICKED
        data["user-ships"]+=1
    else:
        print("ship not valid")  
    data["temp"]=[] 
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["user-ships"]==5:
        print("you can start the game")
        return
    for i in data["temp"]:
        if (row,col)==i:
            return
    data["temp"].append([row,col])
    if len(data["temp"])==3:
        placeShip(data)
    return




  #  for (temp)
#row,col==i    return

#if =5
#print(you can start the game)


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col]==SHIP_UNCLICKED:
        board[row][col]=SHIP_CLICKED
    if board[row][col]==EMPTY_UNCLICKED:
        board[row][col]=EMPTY_CLICKED
    winner=isGameOver(board)
    if(winner==True):
        data["winner"]=player
'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if (data["current_turn"])<=(data["max"]):
        if data["computer"][row][col]==SHIP_CLICKED or data["computer"][row][col]==EMPTY_CLICKED:
           return  
        else:
           updateBoard(data,data["computer"],row,col,"user")
        row,col=getcomputerGuess(data["user"])
        updateBoard(data,data["user"],row,col,"comp")
        data["current_turn"]+=1
    else:
        data["winner"]="draw"

'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getcomputerGuess(board):
    while True:
        row=random.randint(0,9)
        col=random.randint(0,9)
        if board[row][col]==EMPTY_UNCLICKED or board[row][col]==SHIP_UNCLICKED:
           return [row,col]


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col]==SHIP_UNCLICKED:
                return False
            else:
                pass
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if(data["winner"])=="user":
        canvas.create_text(250,200,text="Congratulations,you have won!",fill="black",font=('Helvetica 20 italic'))
        canvas.create_text(250,400,text="Play again",fill="black",font=('Helvetica 20 italic'))
    elif(data["winner"])=="comp":
        canvas.create_text(250,200,text="you Lost!",fill="black",font=('Helvetica 20 italic'))
        canvas.create_text(250,400,text="play again",fill="black",font=('Helvetica 20 italic'))
    elif((data["winner"])=="draw"):
         canvas.create_text(250,200,text="Draw match!",fill="black",font=('Helvetica 20 italic'))
         canvas.create_text(250,400,text="play again",fill="black",font=('Helvetica 20 italic'))
    return

    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    test.testEmptyGrid()
    test.testCreateShip()
    test.testCheckShip()
    test.testAddShips()
    test.testMakeModel()
    test.testShip()
    test.testIsHorizontal()
    test.testIsVertical()
    test.testGetClickedCell()
    test.testDrawShip()
    test.testShipIsValid()
    test.testUpdateBoard()
    test.testGetcomputerGuess()
    test.testIsGameOver()

    
    




    ## Finally, run the simulation to test it manually ##
    runSimulation(500,500) 