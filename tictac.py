#global variables

board = ['-' ,'-' ,'-' ,
        '-' ,'-' ,'-' ,
        '-' ,'-' ,'-']


game_still_running = True
current_player = 'X'
winner = None
#function for game
def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():

    #display initial board
    displayBoard()
    count  = 0
    while game_still_running and count<9:    
        count+=1
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    
    #the game ends here
    if winner == 'X' or winner == 'Y':
        print(winner + '  won!!!')
    elif winner == None:
        print("it's a tie")

def flip_player():
    global current_player
    if(current_player == 'X'):
        current_player = 'Y'
    else:
        current_player = 'X'
    

def handle_turn(player):
    print(player + "turn")
    position = input("Input the position : ")
    valid = False
    while not valid:
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input("Invalid input \n Input the position : ")
        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print("you can't overwrite there :(")
    board[position] = player
    displayBoard()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    #check_row_win
    row_winner = check_rows()
    #check_column_win
    column_winner = check_columns()
    #chekc_diagonal_win
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner 
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return 

def check_rows():
    global game_still_running
    row_1 = board[0] == board[1] == board[2]!='-'
    row_2 = board[3] == board[4] == board[5]!='-'
    row_3 = board[6] == board[7] == board[8]!='-'
    if row_1 or row_2 or row_3:
        game_still_running = False 
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_running
    column_1 = board[0] == board[3] == board[6]!='-'
    column_2 = board[1] == board[4] == board[7]!='-'
    column_3 = board[2] == board[5] == board[8]!='-'
    if column_1 or column_2 or column_3:
        game_still_running = False 
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_running
    diagonal_1 = board[0] == board[4] == board[8]!='-'
    diagonal_2 = board[2] == board[4] == board[6]!='-'
    if diagonal_1 or diagonal_2:
        game_still_running = False 
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return

def check_if_tie():
    return

play_game()



