board = [[0,0,0],[0,0,0],[0,0,0]]
toure = 0
player1 = 1
player2 = 4
joueur = 0
win = 0

def Moov(ligne, colone):
    Toure()
    board[ligne-1][colone-1] = joueur
    VerifAll()

def VerifAll():
    VerifLigne()
    VerifColone()
    VerifDiagonalD()
    VerifDiagonalG()

def VerifLigne():
    global win
    for n in range(3):
        count = 0
        for i in range(3):
            if board[n][i] != 0:
                count += board[n][i]
            if count == 3:
                win = player1
            elif count == 12:
                win = player2

def VerifColone():
    global win
    for n in range(3):
        count = 0
        for i in range(3):
            if board[i][n] != 0:
                count += board[i][n]
            if count == 3:
                win = player1
            elif count == 12:
                win = player2

def VerifDiagonalD():
    global win
    count = 0
    for n in range(3):
        if board[n][n] != 0:
            count += board[n][n]
        if count == 3:
            win = player1
        elif count == 12:
            win = player2

def VerifDiagonalG():
    global win
    count = 0
    if board[0][2] != 0 and board[1][1] != 0 and board[2][0] != 0:
        count += board[0][2]+board[1][1]+board[2][0]
        if count == 3:
            win = player1
        elif count == 12:
            win = player2

def Toure():
    global toure, joueur
    joueur = player1 if toure % 2 == 0 else player2
    toure += 1

def ResetGame():
    global board, toure, win
    board = [[0,0,0], [0,0,0], [0,0,0]]
    toure = 0
    win = 0