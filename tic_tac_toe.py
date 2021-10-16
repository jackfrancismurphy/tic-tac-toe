
index_positions = [1,2,3,4,5,6,7,8,9]

# Making the board

def the_board(index_positions):
    
    content_line_one = f"{index_positions[0]}   ┃ {index_positions[1]}   ┃ {index_positions[2]}"
    line_one_point_5 = '━━━━━━━━━━━━━━━━━━'
    content_line_two = f"{index_positions[3]}   ┃ {index_positions[4]}   ┃ {index_positions[5]}" 
    line_two_point_5 = '━━━━━━━━━━━━━━━━━━'
    content_line_3__ = f"{index_positions[6]}   ┃ {index_positions[7]}   ┃ {index_positions[8]}" 

    
    print(content_line_one)
    print(line_one_point_5)
    print(content_line_two)
    print(line_two_point_5)
    print(content_line_3__)

the_board(index_positions)


from IPython.display import clear_output


# Asking for User Input
def first_stage_p1():
    # at some point the grid needs to go here
    
    check_player_choice = input('Player 1: Would you like to play as X or O?\n') 
    
    while check_player_choice != 'X' and check_player_choice != 'O':
        check_player_choice = input('Player 1: Please pick X or O ')
        
    return check_player_choice




#Testing that User input is okay, and that the game has not completed
def user_input_player(player,index_positions,icons):

    legit_choices = [1,2,3,4,5,6,7,8,9]
     
    

    player_position = int(input(player + ': Choose a position (1-9)'))
    
    if player_position in index_positions:
        index_positions[player_position-1] = icons
        return index_positions 

    
    elif player_position not in legit_choices:
        player_position = int(input(player + ': Sorry, choose a position (1-9)'))
        index_positions[player_position-1] = icons
        return index_positions
          #error reason 2: what they picked was invalid 
        
    elif player_position in legit_choices and player_position not in index_positions:
        player_position = int(input('Sorry, please choose available position between 1-9\n'))
        index_positions[player_position-1] = icons
        return index_positions
    #error reason 3: they picked a number already in list
                


# winning conditions checker

def winning_conditions_checker(index_positions):
   
    result_list = []
        
    result_list.append(set(index_positions[0:3]) == {'O'} or set(index_positions[0:3]) == {'X'})
    result_list.append(set(index_positions[3:6]) == {'O'} or set(index_positions[3:6]) == {'X'})
    result_list.append(set(index_positions[6:9]) == {'O'} or set(index_positions[6:9]) == {'X'})
    result_list.append(set(index_positions[::3]) == {'O'} or set(index_positions[::3]) == {'X'})
    result_list.append(set(index_positions[1:7:3]) == {'O'} or set(index_positions[1:7:3]) == {'X'})
    result_list.append(set(index_positions[2::3]) == {'O'} or set(index_positions[2::3]) == {'X'})
    result_list.append(set(index_positions[0::4]) == {'O'} or set(index_positions[0::4]) == {'X'})
    result_list.append(set(index_positions[2:7:2]) == {'O'} or set(index_positions[2:7:2]) == {'X'})
                       
    if True in result_list:
        return True
                       
    else:
        return False


##### The Game

winning_conditions = False 
player_one_icon = first_stage_p1()
clear_output()


#prelim variables and player icon definition

index_positions = [1,2,3,4,5,6,7,8,9]

is_board_full = 'No'

if set(index_positions) == {'O', 'X'}:
    is_board_full = 'Yes'

if player_one_icon == 'X':
    player_two_icon = 'O'
    
elif player_one_icon == 'O':
    player_two_icon = 'X'    

the_board(index_positions)


# Game logic

while winning_conditions == False:
    
    
    index_positions =(user_input_player('Player 1',index_positions,player_one_icon))
    clear_output()
    the_board(index_positions) #board printing 
    
    winning_conditions = winning_conditions_checker(index_positions)
    
    if set(index_positions) == {'O', 'X'}:
        is_board_full = 'Yes'
        break
    
    if winning_conditions == True:
        break

    index_positions =(user_input_player('Player 2',index_positions,player_two_icon))
    clear_output()
    the_board(index_positions) #board printing 
    
    winning_conditions = winning_conditions_checker(index_positions)

    if set(index_positions) == {'O', 'X'}:
        is_board_full = 'Yes'
        break

if is_board_full == 'Yes':
    print('It\'s a draw!')

else: 
    print('You\'re the winner!')
          

        
    
        

# winning conditions
# hard mode - code in which player has won
# hard mode - loop the game, instead of running file again?
# Set a condition for breaking out of the loop when all numbers have been exhausted

winning_conditions_checker(index_positions)