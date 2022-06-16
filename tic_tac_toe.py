
from operator import truth
from random import choices


import random
from IPython.display import clear_output



# Asking for User Input
def icon():
    # at some point the grid needs to go here
    
    check_player_choice = input('Player 1: Would you like to play as X or O?\n')
    
    while check_player_choice != 'X' and check_player_choice != 'O':
        check_player_choice = input('Player 1: Please pick X or O')
        
    return check_player_choice

# Making the board
def pp_board(board_positions):
    
    content_line_one = f"{board_positions[0]}   ┃ {board_positions[1]}   ┃ {board_positions[2]}"
    content_line_two = f"{board_positions[3]}   ┃ {board_positions[4]}   ┃ {board_positions[5]}"
    content_line_3__ = f"{board_positions[6]}   ┃ {board_positions[7]}   ┃ {board_positions[8]}"
    line = '━━━━━━━━━━━━━━━━━━'
    
    print(content_line_one)
    print(line)
    print(content_line_two)
    print(line)
    print(content_line_3__)
    print("              ")



#Taking input, checking input, and returning result
def player_turn(player,board_positions,icons):

    player_input = input(player + ': Choose a position (1-9)')
    
    while player_input.isdigit() != True:
        if input("Do you want to stop playing? ") == "yes":
            quit()
        else:
            player_input = input("Please pick a digit between 1-9\n")
    #error 1: what they picked was not a number

    player_position = int(player_input)

    if player_position in board_positions:
        board_positions[player_position-1] = icons
        return board_positions 

    elif player_position not in board_positions:
        player_position = int(input(player + ': Sorry, choose an available position (1-9)'))
        board_positions[player_position-1] = icons
        return board_positions
          #error 2: what they picked was invalid or taken.

#ai input

def utility_function(current_board):
    max_wins = ai_wins(current_board)[0]
    min_wins = ai_wins(current_board)[1]


    if True in max_wins:
        return 1

    elif True in min_wins:
        return -1

    else:
        return 0


# Options generator for next board

def options_genr(current_board) -> list:
    m_choices_list = []
    for x in current_board:
        if type(x) != str:
            m_choices_list.append(x)
    return m_choices_list

def next_boards(current_board, current_player):
    board_lists = []
    potential_move = []
    choices = options_genr(current_board)
    for moves in choices:
        potential_move = current_board.copy()
        potential_move[moves -1] = current_player
        board_lists.append(potential_move)
    return board_lists




def minimax(current_board, current_player):

    #this is a list of lists containing potential boards
    moves = next_boards(current_board, current_player)

    #each potential board is assessed for its utility

    if utility_function(current_board) != 0:
        return current_board, utility_function(current_board), []
        
    elif moves == []:
        return current_board, 0, []
    
    else:
        max_evaluation = -2
        min_evaluation = 2

        if current_player == "X":
            current_player = "O"
            for board in moves:
                if minimax(board, current_player)[1] > max_evaluation:
                    max_evaluation = minimax(board, current_player)[1]
                    triple = current_board, max_evaluation, [board]
            return triple

        if current_player == "O":
            current_player = "X"
            for board in moves:
                if minimax(board, current_player)[1] < min_evaluation:
                    min_evaluation = minimax(board, current_player)[1]
                    triple = current_board, min_evaluation, [board]
            return triple


def unbeatable_ai(current_board, current_player) -> list:
    print("AI's move:")
    board_lists = []
    potential_move = []
    choices = options_genr(current_board)
    for moves in choices:
        potential_move = current_board.copy()
        potential_move[moves -1] = current_player
        board_lists.append(potential_move)
    ai_choice = random.choice(board_lists)
    return ai_choice
                


# winning conditions checker

def winning_conditions_checker(board_positions):
   
    result_list = []
        
    result_list.append(set(board_positions[0:3]) == {'O'} or set(board_positions[0:3]) == {'X'})
    result_list.append(set(board_positions[3:6]) == {'O'} or set(board_positions[3:6]) == {'X'})
    result_list.append(set(board_positions[6:9]) == {'O'} or set(board_positions[6:9]) == {'X'})
    result_list.append(set(board_positions[::3]) == {'O'} or set(board_positions[::3]) == {'X'})
    result_list.append(set(board_positions[1:8:3]) == {'O'} or set(board_positions[1:8:3]) == {'X'})
    result_list.append(set(board_positions[2::3]) == {'O'} or set(board_positions[2::3]) == {'X'})
    result_list.append(set(board_positions[0::4]) == {'O'} or set(board_positions[0::4]) == {'X'})
    result_list.append(set(board_positions[2:7:2]) == {'O'} or set(board_positions[2:7:2]) == {'X'})
                       
    if True in result_list:
        return True
                       
    else:
        return False



def ai_wins(current_board):
   
    max_win_boards = []
    min_win_boards = []
    
    max_win_boards.append(set(current_board[0:3]) == {'X'})
    max_win_boards.append(set(current_board[3:6]) == {'X'})
    max_win_boards.append(set(current_board[6:9]) == {'X'})
    max_win_boards.append(set(current_board[::3]) == {'X'})
    max_win_boards.append(set(current_board[1:8:3]) == {'X'})
    max_win_boards.append(set(current_board[2::3]) == {'X'})
    max_win_boards.append(set(current_board[0::4]) == {'X'})
    max_win_boards.append(set(current_board[2:7:2]) == {'X'})

    min_win_boards.append(set(current_board[0:3]) == {'O'})
    min_win_boards.append(set(current_board[3:6]) == {'O'})
    min_win_boards.append(set(current_board[6:9]) == {'O'})
    min_win_boards.append(set(current_board[::3]) == {'O'})
    min_win_boards.append(set(current_board[1:8:3]) == {'O'})
    min_win_boards.append(set(current_board[2::3]) == {'O'})
    min_win_boards.append(set(current_board[0::4]) == {'O'})
    min_win_boards.append(set(current_board[2:7:2]) == {'O'})


    return max_win_boards, min_win_boards


##### The Game

#prelim variables, player icon definition, and first board printed

winning_conditions = False

ai_mode = ""

ai_mode = input("Would you like to play against an A.I? (yes or no)\n").lower()

player_one_icon = icon()

clear_output()

board_positions = [1,2,3,4,5,6,7,8,9]

is_board_full = 'No'

if player_one_icon == 'X':
    player_two_icon = 'O'
    
elif player_one_icon == 'O':
    player_two_icon = 'X'

pp_board(board_positions)


# Game logic

while winning_conditions == False:
    
    
    board_positions = (player_turn('Player 1',board_positions,player_one_icon))
    clear_output()
    pp_board(board_positions) #board printing 
    
    winning_conditions = winning_conditions_checker(board_positions)
    
    if winning_conditions == True:
        if ai_mode == "yes":
            print("You win!")
        else: 
            print("Player 1 wins!")
        break

    if set(board_positions) == {'O', 'X'}:
        is_board_full = 'Yes'
        break

    if ai_mode == 'no':

        board_positions = (player_turn('Player 2',board_positions,player_two_icon))
        clear_output()
        pp_board(board_positions) #board printing 
        
        winning_conditions = winning_conditions_checker(board_positions)

        if winning_conditions == True:
            print("Player 2 wins!")
            break
    
        if set(board_positions) == {'O', 'X'}:
            is_board_full = 'Yes'
            break
    
    else:
        board_positions = minimax(board_positions, player_two_icon)[2][0]
        clear_output()
        pp_board(board_positions)
        
        winning_conditions = winning_conditions_checker(board_positions)

        if winning_conditions == True:
            print("The AI wins! :(")
            break
    
        if set(board_positions) == {'O', 'X'}:
            is_board_full = 'Yes'
            break

if is_board_full == 'Yes':
    print('It\'s a draw!')         

