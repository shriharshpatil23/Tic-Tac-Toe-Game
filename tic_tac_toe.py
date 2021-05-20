board = [' ' for x in range(10)]


def insertLetter(letter,pos):
    board[pos] = letter                 #to insert letter


def print_board(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '  ')
    print('   |   |   ')
    print('____________')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '  ')
    print('   |   |   ')
    print('____________')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '  ')
    print('   |   |   ')                        #to print the board i.e Game interface


def isSpaceFree(pos):
    return board[pos] == ' '                        #to check if desired  space is free or not


def isSpaceFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True                         #to check if the board is full for not



def isWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))                                #to check who is winner


def playerMove():
    run = True
    while run:
        move = input('Select the position between 1 to 9 for X')
        try:
            move = int(move)
            if move > 0 and move <10:
                if isSpaceFree(move):
                    run = False
                    insertLetter('X',move)
                else:
                    print('Space is already occupied , Please select some another position.!!!!')
            else:
                print('Please selct number between 1 to 9 !!!!!!!')
        except:
            print('Please type another Number!!!!')                                #to grt the players move


def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move                                 #very Imp to get the input from Simple AI

def selectRandom(li):                               #to select the random value from given data
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game!")
    print_board(board)

    while not(isSpaceFull(board)):
        if not(isWinner(board , 'O')):
            playerMove()
            print_board(board)
        else:
            print("sorry you loose!")
            break

        if not(isWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('computer placed an o on position' , move , ':')
                print_board(board)
        else:
            print("you win!")
            break




    if isSpaceFull(board):
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
