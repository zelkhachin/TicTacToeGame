'''
Author  : zelkhachin
File    : TicTacToeGame.py 
'''

# Global variables
board = [' '] * 10
game_state = True
result = ''


def clear(): print("\n" * 100)


def reset_board():
    global board, game_state
    board = [' '] * 10
    game_state = True


def draw_board():
    '''
    This functions draws board so the numpad can be used as a reference
    '''

    print("\n")
    print("\t\t  "+board[7]+" |"+board[8]+" | "+board[9]+" ")
    print("\t\t------------")
    print("\t\t  "+board[4]+" |"+board[5]+" | "+board[6]+" ")
    print("\t\t------------")
    print("\t\t  "+board[1]+" |"+board[2]+" | "+board[3]+" ")
    
# Initial menu
def game_menu():

    while True:
        
        print('''
              #####################################
              
                  Welcome to TicTacToe Game Menu
                  
              #####################################
              
                  1. Enter 'N' to start new game
                  2. Enter 'Q' to quit game\n

                  
              ''')
        
        inputVal = input("Enter your command here: \t")

        if inputVal == 'q' or inputVal == 'Q':

            while True:
                
                inputCheck = input("Are you sure you want to quit? Y/N:\t")
                
                if inputCheck == 'y' or inputCheck == 'Y':
                    quit()
                    break
                                   
                elif inputCheck == 'n' or inputCheck == 'N':
                    game_menu()
                    break

                else:
                    print("Error! Inadequate command entered!\n ")
                    
                            
        
        elif inputVal == 'n' or inputVal == 'N':
            print('\n')
            game_play_menu()
            break
        
        else:
            print("Error! Inadequate character entered!\n ")
            


# Second menu
def game_play_menu():   
    
    while True:
        print("""
            ####################################

            \t   TicTacToe Game
            
            ####################################
            
              #Rules#:
              
              #Player One is X and starts first
              
              #Player Two is O and starts second
              
              #Enter your position. Use numbers 
              from 1 to 9 to write value to 
              desired position
              
              #Enter S to start

              #Enter M to back to main menu

              #Enter Q to quit game\n""")
        

        inputVal = input("\nEnter your command here: \t")

        if inputVal == 's' or inputVal == 'S':
            reset_board()
            game_play()
            break

        elif inputVal == 'm' or inputVal == 'M':
            game_menu()
            break

        elif inputVal == 'q' or inputVal == 'Q':
            
            while True:
                
                inputCheck = input("Are you sure you want to quit? Y/N:\t")
                
                if inputCheck == 'y' or inputCheck == 'Y':
                    quit()
                    break
                                   
                elif inputCheck == 'n' or inputCheck == 'N':
                    game_play_menu()
                    break

                else:
                    print("Error! Inadequate command entered!\n ")

        else:
            print("Error! Inadequate character entered!\n ")



def victory_check(board, player):
    ''' Check Horizontal, Vertical and Diagonal combinations '''

    if (board[7]  ==  board[8] ==  board[9] == player) or \
        (board[4] ==  board[5] ==  board[6] == player) or \
        (board[1] ==  board[2] ==  board[3] == player) or \
        (board[7] ==  board[4] ==  board[1] == player) or \
        (board[8] ==  board[5] ==  board[2] == player) or \
        (board[9] ==  board[6] ==  board[3] == player) or \
        (board[1] ==  board[5] ==  board[9] == player) or \
        (board[3] ==  board[5] ==  board[7] == player):
        return True
    else:
        return False


def board_check(board):
    ''' Check if there is any free spot on board '''
    if " " in board[1:]:
        return False
    else:
        return True


def select_position(player):
    ''' Asks player where to place X or O mark '''
    global board
    req = 'Choose where to place your ' + player + ':\t'
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print("Wrong value! Please select a number between 1 and 9!")
            continue

        if choice not in range(1,10):
            print("Wrong value! Please select a number between 1 and 9!")
            continue

        if board[choice] == " ":
            board[choice] = player
            break
        else:
            print("Desired space isn't empty! Try again!")
            continue


def player_choice(player):
    global board, game_state, result
    result = ''

    # Get Player input
    player = str(player)
    # Validate input
    select_position(player)

    # Check for player win
    if victory_check(board, player):
        draw_board()
        result = "\n" + player + "wins! Congratulations!"
        game_state = False

    # Draw board
    draw_board()

    # Check for a tie
    if board_check(board):
        result = "\nTie!"
        game_state = False

    return game_state, result


def game_play():
    global result

    # Set players
    X = 'X'
    O = 'O'

    while True:
        # Show board
        draw_board()

        # Player X turn
        game_state, result = player_choice(X)
        print(result)
        if game_state == False:
            break

        # Player O turn
        game_state, result = player_choice(O)
        print(result)
        if game_state == False:
            break

    game_play_menu()

        
def main():

    game_menu()

  
if __name__== "__main__":
  main()
