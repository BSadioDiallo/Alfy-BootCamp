import math

def calc_math_expression(num1, num2, operator):
    if operator == '+':
        return num1 + num2

    elif operator == '-':
            return num1 - num2
    
    elif operator == '*':
        return num1 * num2
    
    elif operator ==':':
        if num2 != 0:
            return num1 / num2
    
    else:
        return None

def calc_math_expression_from_str(str_input):
    parameters = str_input.split(' ')
    return calc_math_expression(float(parameters[0]), float(parameters[2]), operator = parameters[1])

def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    numbers = [ num1, num2, num3 ]
    numbers.sort()
    return ( numbers[2], numbers[0] )

def quadratic_equation_solver(a, b, c):
    if a != 0:
        delta = (b*b) - (4*a*c)
        if delta < 0:
            return (None, None)
        elif delta == 0:
            x = (-b) / (2 * a)
            return (x, None)
        elif delta > 0:
            x1 = ( (-b) + math.sqrt(delta) ) / 2*a
            x2 = ( (-b) - math.sqrt(delta) ) / 2*a
            return (x1, x2)
        
    print('a must be higher than 0')

def quadratic_equation_solver_from_user_input():
    parameters = input('give 3 numbers (a b c) : ')
    parameters = parameters.split()
    
    if len(parameters) != 3:
        print('invalid input')
        return False
    
    return quadratic_equation_solver(float(parameters[0]), float(parameters[1]), float(parameters[2]))

def temp_checker(min_temp, temp_1, temp_2, temp_3):
    numberOfDay = 0
    temps = [temp_1, temp_2, temp_3]
    for i in range(len(temps)):
        if temps[i] > min_temp:
            numberOfDay += 1
    
    if numberOfDay >= 2:
        return True
    
    return False
