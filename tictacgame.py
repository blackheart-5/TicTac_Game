# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 00:33:21 2023

@author: nana
"""

from IPython.display import clear_output
clear_output()

#board positions
mydata = [
	["row_0","1 ", "2 ", "3 "],
	["row_1","4 ", " 5"," 6"],
	["row_2"," 7", " 8"," 9"]
]

#board prints
mydata1 = [
	["","",""],
	["","",""],
	["","",""]
]

#win patterns
w_patterns = [['X','X','X'], ['O','O','O']] 

def display_board(mydata):
    
    # import module
    from tabulate import tabulate
    print('Welcome to Tic TAc Toe\n'
          '\nGame Instructions:\n '
          '1. Select the row(0,1,2) you want to play in.\n '
         '2. Then select the box number(1-9) in that respective row.\n')
    print(tabulate(mydata,tablefmt="grid"))
    
    

def display_board1(mydata1):
    
# import module
    from tabulate import tabulate
    
# display table
    print(tabulate(mydata1,tablefmt="grid"))
    
    
def players_choice():
    
    row_input = 'not'
    rowinput = ['0','1','2']

    while row_input not in rowinput:
        #select the row you would like to be in 
        row_input = input('\n Please select row where you want to choose (0,1,2):')
        
        if row_input not in rowinput:
            print('Sorry but your input is not in the range, try again.')
            
    return int(row_input)


def position_x():
    
    pseudo_pos = 'wrong'
    
    if int(row_input) == 0:
        while pseudo_pos not in ['1','2','3']:
            pseudo_pos = input('For row 0, Please choose your position on that row(1,2,3): ')
            if pseudo_pos not in ['1','2','3']:
                print('Sorry your input is not in the range, try again.')
       
    elif int(row_input) == 1:
        while pseudo_pos not in ['4','5','6']:
            pseudo_pos = input('For row 1, Please choose your position on that row(4,5,6): ')
            if pseudo_pos not in ['4','5','6']:
                print('Sorry your input is not in the range, try again.')
            
    elif int(row_input) == 2:
        while pseudo_pos not in ['7','8','9']:
            pseudo_pos = input('For row 2, Please choose your position on that row(7,8,9): ')
            if pseudo_pos not in ['7','8','9']:
                print('Sorry your input is not in the range, try again.')
            
        
  #create a dictionary that matches the key to the value
    mydict = {'1':0, '2':1, '3':2, '4':0, '5':1, '6':2, '7':0, '8':1, '9':2}
  #assign the index position of number
    position = mydict[pseudo_pos]
    
    return int(position)    


def replacement_choice(mydata1, position,row_input):
    choice = 'pp'
    while choice not in ['X', 'O']:
        choice = input('What letter do you choose (X or O): ').capitalize()

    #assign change in the list
    mydata1[row_input][position] = choice 
    
    return mydata1


def winner_chk(mydata1,w_patterns):
    
        
    #w_patterns = [['X','X','X'], ['O','O','O']]
    
    i = 0 #rows
    for pattern in w_patterns:
        if [mydata1[0][0], mydata1[1][0], mydata1[2][0]] == pattern:
            print(f'Congratulations player {pattern[i]} won')
            return True
        
        elif [mydata1[0][1], mydata1[1][1], mydata1[2][1]] == pattern:
            print(f'Congratulations player {pattern[i]} won')
            return True
        
        elif [mydata1[0][2], mydata1[1][2], mydata1[2][2]] == pattern:
            print(f'Congratulations player {pattern[i]} won')
            return True
        i += 1
    
    i = 0 #column    
    for pattern in w_patterns:
        if [mydata1[0][0], mydata1[1][0], mydata1[2][0]] == pattern:
            print(f'Congratulations player {pattern[i]} won')
            return True

        elif [mydata1[0][1], mydata1[1][1], mydata1[2][1]] == pattern:
            print(f'Congratulations player {pattern[i]} won')
            return True
        
        elif [mydata1[0][2], mydata1[1][2], mydata1[2][2]] == pattern:
            print(f'Congratulations player {pattern[i]} won')
            return True      
        i += 1
    
    i = 0 #diagonals
    for pattern in w_patterns:
        if [mydata1[0][0], mydata1[1][1], mydata1[2][2]] == pattern:
            print(f'Congratulations player {pattern[i]} won')
            return True
        
        elif [mydata1[0][2], mydata1[1][1], mydata1[2][0]] == pattern:
            print(f'Congratulations player {pattern[i]} won')
            return True
        i += 1
    
    #for draw
    if "" not in mydata1[0] and "" not in mydata1[1] and "" not in mydata1[2]:
        print("It's a draw or stalemate")
        return True  

def gme_chk():
    game_choice = input('Would you like to play again (Yes or No):\n').capitalize()
    
    if game_choice not in ['Yes', 'No']:
        print('Please you entered the wrong input')
    else:
        if game_choice == 'Yes':
            return True
        else:
            return False
   
        
  
                        #GAME LOGIC

#display initial board with numbers
display_board(mydata)


#keep game at play
game_on = True

#MAIN GAME
while game_on:
    
#assign index position for list assignment
    row_input = players_choice()
    position = position_x()
    mydata1 = replacement_choice(mydata1, position, row_input)
    
#prints board after each play
    display_board1(mydata1)
    

 #check winner
    win = winner_chk(mydata1,w_patterns)
    if win != True:
        print("\n Next player's turn!! \n")
    else:
        game_on = gme_chk()
        if game_on == True:
            mydata1 = [
                ["", "", ""],
                ["", "",""],
                ["", "",""]
            ]
        else:
            break