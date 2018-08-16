#!/usr/bin/python

# Please be careful about coding standard while solving exercises

# donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
    # +++your code here+++
	result = ''
	if count < 10:
		result = "Number of donuts: " + repr(count)
	else:
		result = "Number of donuts: many"
		
    	return result


# MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
#('mix', 'pod'), 'pox mid')
def mix_up(a, b):
    # +++your code here+++
	
	str1 = a
	list1 = list(str1)
	list1[0] = b[0]
	list1[1] = b[1]
	str1 = ''.join(list1)

	str2 = b
	list2 = list(str2)
	list2[0] = a[0]
	list2[1] = a[1]
	str2 = ''.join(list2)
	
    	return str1 + " " + str2


# not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    # +++your code here+++
	str1 = "not";
	str2 = "bad";
	
	sira1 = s.find(str1)
	sira2 = s.find(str2)
	
	str3 = s
	sira3 = sira2 + 1
	list1 = list(str3)


	if sira1 != -1 and sira2 != -1:
		if sira1 < sira2:
			while sira1 < sira2+3:
				list1[sira1] = ""
				sira1 = sira1 + 1
				str2 = ''.join(list1)
			print str2
			list1[sira3] = "good"
			str2 = ''.join(list1)	
			return str2
		else:
			return s
	else:
		return s

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
    print 'donuts'
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
