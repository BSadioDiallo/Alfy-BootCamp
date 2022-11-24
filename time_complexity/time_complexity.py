def func(n):
	"""
	time complexity : O(n * n)
	description : because the nested loop loops n times for each iteration of the main loop
	which one also loops n times so n * n
    """
	for i in range(n):
		for j in range(n):
			if j < I:
				break

def func(L):
	"""
	time complexity : O(n + n)
	description : we have a in operator so L is a iterable, for each v in L we will use helper_func
	wich one is O(n) so we will iterate n times and we will use the helper_func n times
	"""
	for v in L:
		# helper_func time complexity is O(n)
		helper_func(v)

def func(n):
	"""
	time complexity : O(logn)
	descpriton : in the first loop j is devided by 2 on each iteration so logn
    """
	j = n
	while j > 0:
		j = j // 2
	while j < n:
		j = j + 3
		n = n - 5
	return j

def func(n):
	"""
    time complexity : O(nlogn)
    description : because n is divided by 2 on each iteration and then we run sum() and range()
    """
	total = 0
	while n > 5:
		n = n // 2
		# Remember the time complexity of the sum and range methods
		total += sum(range(n))
	return total

def func(n):
	"""
    time complexity : O(n)
    description : because whe have for loop used with range of 2 to n
    """
	for i in range(2,n):
		if n % i == 0:
			return True
		if i > n/i:
			return False

def func(n):
	"""
    time complexity : n(n-1)
    description : the first loop will run for n times and for each iteration the second one 
    will run for n-1 times 
    """
	for i in range(n):
		for j in range(i):
			if j * j > I:
				break

def func(n) :
    """
    time complexity : n^n
    description : firt loop iterate n/2 times and in each iteration the while loop
    iterate n/2 times so
    """
    k = 0
    for i in range(n//2, n): 
        j = 1
        while j <= n:
            k += 1
            j *= 2
    return k

#------------------------------------------------------ one block
""" time complexity : O(n+m)
    description : because we have linear helper_func :(
"""
def helper_func(x):
	for i in range(x): 
		print(i)
	return x
def func(n):
	if n == 2:
		return 0
	else:
		return helper_func(n - 1) + helper_func(n - 2)
#------------------------------------------------------
	
#------------------------------------------------------ another block
"""
	time complexity : O( (n^2)*100^2 )
	description : in func() for i in range n**2 so n^2, for the helper_func() we have (100)^2 so that's it
"""
def helper_func(n):
	for i in range(n**2):
		print(i)
def func(n):
	for i in range(n**2): 
		print(helper_func(100))
	return 0
