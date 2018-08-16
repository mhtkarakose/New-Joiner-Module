#!/usr/bin/python

# Please be careful about coding standard while solving exercises
# http://rdwiki/confluence/display/INFRA/Python+Coding+Standards

# monkey trouble
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling.
# Return True if we are in trouble. 
def monkey_trouble(a_smile, b_smile):
    # +++your code here+++

	if a_smile == True and b_smile == True:
	   result= True
	elif a_smile == False and b_smile == False:
	   result= True
	else:
	   result = False
	return result
    

# positive negative
# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    # +++your code here+++

	if a < 0 and b > 0:
	   result= True
	elif a > 0 and b < 0:
	   result= True
	elif a < 0 and b < 0:
	   result= True
	return result

# count nine
# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    # +++your code here+++
	i = 0
	for x in nums:
        	if x == 9:
	   		i = i+ 1
    	return i

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
    print 'monkey_trouble'
    test(monkey_trouble(True, True), True)
    test(monkey_trouble(False, False), True)
    test(monkey_trouble(True, False), False)
    
    print
    print 'pos_neg'
    test(pos_neg(1, -1, False), True)
    test(pos_neg(-1, 1, False), True)
    test(pos_neg(-4, -5, True), True)
    
    print
    print 'array_count9'
    test(array_count9([1, 2, 9]), 1)
    test(array_count9([1, 9, 9]), 2)
    test(array_count9([1, 9, 9, 3, 9]), 3)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
