'''
tic-tac-toe for two players
'''

#from IPython.display import clear_output
import random

def display_board(board):
    #clear_output()
    horlines = "---------"
    print(" " + board[1] +" | "+ board[2]+ " | " + board[3])
    print(" " + horlines)
    print(" " + board[4] +" | "+ board[5]+ " | " + board[6])
    print(" " + horlines)
    print(" " + board[7] +" | "+ board[8]+ " | " + board[9])

def clear_board(board):
    for p in board:
        board[p] = ' '
    return board

def player_marker():
    marker = ''
    #choose betwen x or o
    while not (marker == 'x' or marker == 'o'):
        marker = input('Please select x or o: ').lower()
    
    if (marker == 'x'):
        return ('x', 'o')
    else:
        return ('o', 'x')

def place_marker(board, marker, position):
    board[position] = marker
        
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #line 1 horizontally
            (board[4] == mark and board[5] == mark and board[6] == mark) or #line 2 horizontally
            (board[7] == mark and board[8] == mark and board[9] == mark) or #line 3 horizontally
            (board[1] == mark and board[4] == mark and board[7] == mark) or #line 1 vertically
            (board[2] == mark and board[5] == mark and board[8] == mark) or #line 2 vertically
            (board[3] == mark and board[6] == mark and board[9] == mark) or #line 3 vertically
            (board[1] == mark and board[5] == mark and board[9] == mark) or #line 1 diagonally
            (board[3] == mark and board[5] == mark and board[7] == mark))   #line 2 diagonally

def choose_first():
    player = ("Player", str(random.randint(1,2)))
    return " ".join(player)

def space_check(board, position):
    return (board[position] == " ")

def full_board_check(board):
    for pos in range(0, 9):
        if(space_check(board, pos)):
            return False
    return True

def player_choice(board):
    player_pos = 0
    while (player_pos not in [1,2,3,4,5,6,7,8, 9] or not space_check(board, player_pos)):
        player_pos = int(input("Your turn, pos: "))
    return player_pos

def replay():
    replay_ch = " "
    while (replay_ch not in ['yes', 'y', 'no', 'n']):
        replay_ch = input("Would you like to play again?: ").lower()
    if (replay_ch == 'yes' or replay_ch == 'y'):
        return True
    else:
        return False
    
print('Welcome to Tic Tac Toe!')

game_board = [' ']*10
player = choose_first()
print('Okay {} goes first. '.format(player))

if player == 'Player 1':
    (p1, p2) = player_marker()
else:
    (p2, p1) = player_marker()
    
print('Player 1: {}, Player 2: {}'.format(p1, p2))

ready_to_start = input('Are you ready to play? ').lower()
if ready_to_start == 'y' or ready_to_start == 'yes':
    game_on = True
else:
    game_on = False

while game_on:
    if(player == 'Player 1'):
        #Player 1's turn
        
        #Player 1 Turn
        display_board(game_board)
        print('Player 1')
        pos1 = player_choice(game_board)
        place_marker(game_board, p1, pos1)
 
        if win_check(game_board, p1):
            display_board(game_board)
            print('Congratulations Player 1! You have won the game!')
            game_on = False
        else:
            if full_board_check(game_board):
                display_board(game_board)
                print('The game is a draw!')
                break
            else:
                player = 'Player 2'
    else:
        #Player 2's turn
        display_board(game_board)
        print('Player 2')
        pos2 = player_choice(game_board)
        place_marker(game_board, p2, pos2)

        if win_check(game_board, p2):
            display_board(game_board)
            print('Player 2 has won!')
            game_on = False
        else:
            if full_board_check(game_board):
                display_board(game_board)
                print('The game is a draw!')
                break
            else:
                player = 'Player 1'
'''
    if not replay():
        break
        '''