#!/usr/bin/python
# -*- coding: utf-8 -*-

# prime
# Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself. 
def prime(n):
    # +++your code here+++
	result = False
	if n > 1:
	   for i in range(2,n):
	       if (n % i) == 0:
	   	result = False
	   else:
	   	result= True
	else:
	   result = False
   	return result


# multiply_3_5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below n.
def multiply_3_5(n):
    # +++your code here+++
	count = 0
	result = 0
	while count < 10:
	    if count % 3 == 0:
		result = result + count
	    elif count % 5 == 0:
		result = result + count
	    
	    count = count + 1	
    
    	return result

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print 'prime'
    test(prime(1), False)
    test(prime(23), True)
    test(prime(77), False)
    
    print
    print 'multiply_3_5'
    test(multiply_3_5(10), 23)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
