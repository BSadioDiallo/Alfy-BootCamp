def input_list_helper():
    print('Enter numbers here, just press enter when you have done')
    numbers = []
    while True:
        value = input()
        if value == "" or value == " ":
            print('input stream closed\n')
            break
        else:
            numbers.append(int(value))

    return numbers

def input_list():
    """ the user_list() function
    collects numbers from user input,
    calculate their sum and return it as a list
		(We recommend creating a helper function named 
		input_list_helper for collecting the user input
    :return: list of numbers that were given
    by the user, the last object is the sum of all the others
    """
    numbers = input_list_helper()

    if len(numbers) >= 1:
        the_sum = 0
        for value in numbers:
            the_sum += value
        numbers.append(the_sum)
    else:
        numbers.append(0)
        
    return numbers

def check_monotonic_sequence(sequence):
    """ get a sequence (list) of numbers and determine its
    monotonicity type

    :return: list of 4 booleans that represent 4 different
             monotonicity characters
    - At the 0 indexes: monotonicity up
    - At the 1 index: monotonicity up strong
    - At the 2 indexes: monotonicity down
    - At the 3 indexes: monotonicity down strong """
    
    if len(sequence) == 0 or len(sequence) == 1:
        return [True, True, True, True]

    result = monotonicity_up_handler(sequence)
    resultDown = monotonicity_down_handler(sequence)
    
    return  result + resultDown

def monotonicity_up_handler(sequence):
    one = 0
    two = 0
    up = False
    strongUp = True

    for i in range( len(sequence) -1 ):
        j = i + 1
        one = sequence[i]
        two = sequence[j]
        
        if one < two:
            up = True
        elif one == two:
            if one <= two:
                up = True
            strongUp = False
        else:
            up = False
            strongUp = False
            break

    return [ up, strongUp ]

def monotonicity_down_handler(sequence):
        one = 0
        two = 0
        down = False
        strongDown = True

        for i in range( len(sequence) -1 ):
            j = i + 1
            one = sequence[i]
            two = sequence[j]
            
            if one > two:
                down = True
            elif one == two:
                if one >= two:
                    down = True
                strongDown = False
            else:
                down = False
                strongDown = False
                break
        
        return [ down, strongDown ]

def check_monotonic_sequence_inverse(bool_list):
    """ The function that gets a boolean list, and checks if it 
	  matches any of the valid monotonicity cases, if it does,
    it will return a matching list, 
		else (if such doesn't exist such a sequence), 
		it will return None    

    :param def_bool: a list of 4 booleans
    :return: matching sequence to the booleans
						 monotonicity_inverse value
    """
    if len(bool_list) != 4:
        print('invalid input')
        return
    up_monocity = bool_list[:2]
    down_monocity = bool_list[2:]
    true_times_up = 0
    true_times_down = 0
    for i in range(2):
        if up_monocity[i] == True:
            true_times_up += 1
        if down_monocity[i] == True:
            true_times_down += 1
            
    if true_times_up == 2 and true_times_down == true_times_up:
        return [ 100 ]
    if true_times_up == 0 and true_times_down == true_times_up:
        return [ 14, 3, 8, 9 ]
    if true_times_up > 0 and true_times_down == 0:
        if true_times_up == 2:
            return [ 2, 13, 14, 17 ]
        elif true_times_up == 1 and up_monocity[1] == False:
            return [ 4 , 8 , 9, 9, 25 ]
    if true_times_down > 0 and true_times_up == 0:
        if true_times_down == 2:
            return [ 13, 11, 9, 5, 1 ]
        elif true_times_down == 1 and down_monocity[1] == False:
            return [ 5, 4, 4, 3, 2, 1 ]
    if true_times_up == true_times_down == 1 and up_monocity[0] == down_monocity[0]:
        return [ 1, 1, 1, 1 ]

    return None

def primes_generator(n):
    """ the functions find and return a list of prime numbers
            with n primes in it.

    :param n: number of primes the function needs to return
    :return: list that contains the amount of n prime numbers.
    """
    if n < 1:
        return []
    primes = []
    check = 0
    i = 2
    while len(primes) < n:
        
        for j in range(1, i+1):
            if i % j == 0:
                check += 1
        if check == 2 :
            primes.append(i)
        check = 0
        i += 1
    
    return primes

def is_empty_vector(vec_lst):
    """
    being called by vectors_list_sum() 
		to check if a vector list is empty

    :param vec_lst: a list with lists inside of it,
					 each sublist     is a vector
    :return: True when empty and False when not.
    """
    if len(vec_lst) == 0:
        return True
    return False

def can_have_sum(vec_lst):
    for i in range(len(vec_lst)-1):
        j = i + 1
        if len(vec_lst[i]) != len(vec_lst[j]):
            return False
    return True

def vectors_list_sum(vec_lst):
    """ get a list of vectors, add them to each other
    and returns a vector of their sum.

    :param vec_lst: a list with lists inside of it, 
					each sublist is a vector

    :return: list of the total vectors sum.
    """
    if not is_empty_vector(vec_lst) and can_have_sum(vec_lst):
        sum = [ 0 ] * len(vec_lst[0])
        for i in range(len(vec_lst[0])):
            for k in range(len(vec_lst)):
                sum[i] = sum[i] + vec_lst[k][i]
        return sum
    return 

def calc_the_inner_product(vec_1, vec_2):
    """ gets two list, calculates their inner
        product and returns it

    :param vec_1: list of numbers
    :param vec_2: list of numbers
    :return: the inner product of the two lists.
    """
    if len(vec_1) == len(vec_2):
        innerProduct = 0
        for i in range(len(vec_1)):
            innerProduct = innerProduct + vec_1[i] * vec_2[i]
        return innerProduct
    
def orthogonal_number(vectors):
    """ get a list of vectors, and check how many pairs in
    the list are orthogonal
		 then it returns the amount of pairs as int.
     You should use the calc_the_inner_product() helper function
		 for calculations.

    :param vectors: list of lists, with numbers in it
    :return: number (float), of the amount of orthogonal pairs
    """
    amount = 0
    for i in range(len(vectors)):
        for k in range(i+1,len(vectors)):
            if calc_the_inner_product(vectors[i],vectors[k]) == 0:
                amount += 1
    return amount
