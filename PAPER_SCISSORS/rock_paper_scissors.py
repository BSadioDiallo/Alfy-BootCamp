from os import name as os_name, system
import rock_paper_scissors_helper as helper
from random import randint

WINDOWS = 'nt'
UNIX = 'posix'

def clear_screen(os_name):
    if os_name == WINDOWS:
        system('cls')
    elif os_name == UNIX:
        system('clear')

#This function handles game for user versu machine party
def user_and_machine():
    print('USER VS MACHINE')
    score_1, score_2 = 0 , 0 
    helper.display_state(score_1,score_2)
    clear_screen(os_name)
    
    # you can stop the game bye typing [!]
    while score_1 != 3 and score_2 != 3 and score_1 != '!':
        player_1 = helper.user_input(helper.PLAYER1)
        player_2 = randint(1,3)
        if player_1 != helper.STOP:
            clear_screen(os_name)
            round_result = helper.the_round(player_1, player_2)
            score_1, score_2 = helper.point_distributor(round_result, score_1, score_2)
            helper.display_state(score_1, score_2)
        else:
            return
    clear_screen(os_name)
    if score_1 == 3:
        print('You are the winner')
    else:
        print('You lose!')
   
def user_and_user():
    print('USER VS USER')
    score_1, score_2 = 0 , 0
    helper.display_state(score_1,score_2)
    clear_screen(os_name)
    while score_1 != 3 and score_2 != 3:
        player_1 = helper.user_input(helper.PLAYER1)
        clear_screen(os_name)
        player_2 = helper.user_input(helper.PLAYER2)
        if helper.STOP not in [ player_1, player_2]:
            clear_screen(os_name)
            round_result = helper.the_round(player_1, player_2)
            score_1, score_2 = helper.point_distributor(round_result, score_1, score_2)
            helper.display_state(score_1, score_2)
            clear_screen(os_name)
        else:
            return
    if score_1 > score_2:
        print(f'{helper.PLAYER1} You are the winner ')
    else:
        print(f'{helper.PLAYER2} You are the winner ')

def main():
    mode = helper.menu()
    if mode == helper.MACHINE:
        clear_screen(os_name)
        user_and_machine()
    elif mode == helper.USER:
        clear_screen(os_name)
        user_and_user()
    
    print('GOOD BYE')
    
if __name__ == '__main__':
    main()
