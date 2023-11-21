import hangman_helper as hang

def run_single_game(list_words, score):
    '''this function keep a single round
        
        param: a list of words, a initial score
        return: the current score after the end of the round'''
    
    ''' zaWardo its the random word from the list of words and a reference to dio's stand 'the world' in jojo's BA
    but with japan accent 'zawardo' go google this 'dio stand name' if you wanna see :)'''
    
    zaWardo, pattern, wrong_guess_list = game_initializer(list_words)
    
    hang.display_state(pattern, wrong_guess_list, score,'> Try to find out the hidden word')
    
    while '_' in pattern and score > 0:
        choice = hang.get_input()
        if choice[0] == hang.LETTER:
            if not choice[1].isalpha() or not choice[1].islower() or len(choice[1]) != 1: #verifying possible input error
                print('> Sorry but the input is incorrect')
                hang.display_state(pattern, wrong_guess_list, score)
                continue
            
            score = scoring(zaWardo, pattern, choice, score)
            pattern = update_word_pattern(zaWardo, pattern, choice)
            wrong_guess_list, score = wrong_guess_handler(zaWardo, wrong_guess_list, choice[1], score)
        elif choice[0] == hang.WORD:
            score = scoring(zaWardo,pattern, choice, score)
            pattern = update_word_pattern(zaWardo, pattern, choice)
        else:
            hints = filter_words_list(list_words, pattern, wrong_guess_list)
            hang.show_suggestions(hints)
            score -= 1
        hang.display_state(pattern, wrong_guess_list, score)

    if score < 1:
        hang.display_state(pattern, wrong_guess_list, score,f'It was [{zaWardo}].')
    
    return score

def wrong_guess_handler(word, wrong_list, letter, score):
    '''this function is for handling the wrong guesses list

        parameter: the word , the wrong_list, and the letter
        return: a updated wrong_list
        '''
    if letter not in word and letter not in wrong_list :
        wrong_list.append(letter)
        score -= 1
    elif letter not in word and letter in wrong_list:
        print('> You have already tried this letter')
    
    return wrong_list, score


def game_initializer(words):
    '''this function initialize the game
    
        param: a list containing words
        return One word, the pattern of the word and a empty list for wrong_guesses
        '''
    zaWardo = hang.get_random_word(words)
    pattern = '_' * len(zaWardo)
    wrong_guess_list = []
    return zaWardo, pattern, wrong_guess_list
def scoring(word, pattern, choice, score):
    ''' this function handle scoring problem for both letter and word input

        param: the word, the pattern, the input tuple and the current score
        return: a updated score
    '''
    if choice[0] == hang.LETTER:
        if choice[1] in word and choice[1] not in pattern:
            n = 0
            for letter in word:
                if letter == choice[1]:
                    n += 1
            score += n*(n+1)//2 - 1
    elif choice[0] == hang.WORD:
        if choice[1] == word:
            n = 0
            for letter in pattern:
                if letter == '_':
                    n += 1
            score += n*(n+1)//2 - 1
        else:
            score -= 1
    
    return score

def update_word_pattern(word, pattern, choice):
    ''' this function update the pattern

        param: the word, the current pattern, the input tuple
        return: a updated pattern
    '''
    if choice[0] == hang.LETTER:
        if choice[1] in word and choice[1] not in pattern:
            pattern_as_list = []
            for i in range(len(word)):
                pattern_as_list.append(pattern[i])
                if word[i] == choice[1]:
                    pattern_as_list[i] = choice[1]
            pattern = "".join(pattern_as_list)
        elif choice[1] not in word:
            return pattern
        else:
            print('> You have already finded this letter')
    elif choice[0] == hang.WORD:
        if word == choice[1]:
            pattern = choice[1]
            print('Yeah it was that !')
    return pattern

def filter_words_list(words, pattern, wrong_guess_list):
    passed = True
    hint = []
    for word in words:
        if len(word) == len(pattern):
            if len(wrong_guess_list) != 0:
                for char in wrong_guess_list:
                    if char in word:
                        passed = False
                        break
            if passed == True:
                for i in range(len(pattern)):
                    if pattern[i] != '_' and pattern[i] == word[i]:
                        continue
                    elif pattern[i] != '_' and pattern[i] != word[i]:
                        passed = False
                        break
            if passed == True:
                hint.append(word)
            passed = True
    return hint

def main():
    word_list = hang.load_words()
    round = 0

    score = run_single_game(word_list, hang.POINTS_INITIAL)
    round += 1
    while True:
        if score > 1:
            msg = f'Good job You won, played round : {round} current score {score}!\n'
            msg += f'Do you want to keep playing ?'
            if hang.play_again(msg):
                score = run_single_game(word_list, score)
                round += 1
            else: break
        else:
            msg = f'You Loose, played round : {round}. '
            msg += f'Do you want to try again ?'
            if hang.play_again(msg):
                score = run_single_game(word_list, hang.POINTS_INITIAL)
                round += 1
            else: break

if __name__ == '__main__':
    main()


        
    
    