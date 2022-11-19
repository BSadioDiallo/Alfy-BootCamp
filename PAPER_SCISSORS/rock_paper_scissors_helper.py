MACHINE = '1'
USER = '2'
QUIT = '3'
PLAYER1 = 'Player 1'
PLAYER2 = 'Player 2'
STOP = 'STOP'
POSE = { 1: 'PAPER', 2: 'SCISSOR', 3: 'ROCK' }
PAPER = 1
SCISSOR = 2 
ROCK = 3



# this is because i am not casting the value in the menu function
#i dont know if its a good thing or not but i thought it will make the code smaller, yeah 1 line :) haha
def display_state(score_1, score_2):
    '''this function display the state of the current round
    param: input of players
    return: nothing
    '''
    print('> Here is the score')
    print(f'{PLAYER1} : {score_1}\n{PLAYER2} : {score_2} ')
    input('Type ENTER to continue...')

def menu():
    print('''Welcome to the paper scissors game :)
             Choose one playing mode :
             1. User vs Machine
             2. User vs User
             3. Quit''')
    while True:
        choice = input('Which mode do you want to play ? > ')
        if choice.isdecimal() and len(choice) == 1:
            if choice == MACHINE:
                return choice
            elif choice == USER:
                return choice
            elif choice == QUIT:
                return choice
        else:
            print('> You entered an unknow option, restart')

def user_input(msg=''):
    '''This function handle the user inputs through the game
        param: a user input
        return: dont know yet'''
    while True:
        print(f'Make your choice {msg}')
        print("- s for Scissors \n- p for Paper \n- r for Rock")
        choice = input('> ')
        if choice.isalpha() and len(choice) == 1:
            if choice and choice in 'sS':
                return SCISSOR
            elif choice and choice in 'pP':
                return PAPER
            elif choice and choice in 'rR':
                return ROCK
            else:
                print('# Invalid input')
        elif choice == '!' and len(choice) == 1:
            choice = input('Are you sure you want to quit ? (y/n) > ')
            if choice in 'yY':
                return STOP
            elif choice in 'nN':
                print('Waiting for your choice')
            
    
def the_round(player1, player2):
    if player1 == PAPER:
        if player2 == SCISSOR:
            print(f'{PLAYER1} \t {POSE[player1]}  <-  {POSE[player2]} \t {PLAYER2}\nWINNER {PLAYER2}')
            return PLAYER2
        elif player2 == ROCK:
            print(f'{PLAYER1} \t {POSE[player1]}  ->  {POSE[player2]} \t {PLAYER2}\nWINNER {PLAYER1}')
            return PLAYER1
        else:
            print(f'{PLAYER1} {POSE[player1]} draw {POSE[player2]} {PLAYER2}')
        return
    elif player1 == SCISSOR:
        if player2 > SCISSOR: # another way to solve,i prefer the first one
            print(f'{PLAYER1} \t {POSE[player1]}  <-  {POSE[player2]} \t {PLAYER2}\nWINNER {PLAYER2}')
            return PLAYER2
        elif player2 < SCISSOR:
            print(f'{PLAYER1} \t {POSE[player1]}  ->  {POSE[player2]} \t {PLAYER2}\nWINNER {PLAYER1}')
            return PLAYER1
        else:
            print(f'{PLAYER1} \t {POSE[player1]}  draw  {POSE[player2]} \t {PLAYER2}')
    else:
        if player2 == PAPER:
            print(f'{PLAYER1} \t {POSE[player1]}  <-  {POSE[player2]} \t {PLAYER2}\nWINNER {PLAYER2}')
            return PLAYER2
        elif player2 == SCISSOR:
            print(f'{PLAYER1} \t {POSE[player1]}  ->  {POSE[player2]} \t {PLAYER2}\nWINNER {PLAYER1}')
            return PLAYER1
        else:
            print(f'{PLAYER1} \t {POSE[player1]}  draw  {POSE[player2]} \t {PLAYER2}')
            return 

def point_distributor(round_result,score_1,score_2):
    if round_result == PLAYER1:
        score_1 += 1
    elif round_result == PLAYER2:
        score_2 += 1
    
    return score_1, score_2

'''def stop_game(instruction):
    if STOP in instruction:
        
        '''
