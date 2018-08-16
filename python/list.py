#!/usr/bin/python

# Please be careful about coding standard while solving exercises

# match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    # +++your code here+++
	count = 0
	result = 0
	ListSize = len(words)

	while count < ListSize:
	    if len(words[count]) >= 2:
		word = words[count]
		wordCount = len(word)
		if(word[0] == word[wordCount-1]):
			result = result + 1   
	    count = count + 1	
    	return result

def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

# Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    # +++your code here+++
	NormalList = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
	
	TotalArrSize = len(list1) + len(list2)
	ResultList = []
	List = []
	ListCount = 0
	count = 0
	#sorted(list1 + list2)
	while count < len(list1):
		buff1 = list1[count]
		buff1First = buff1
		buff1Num = 0
		#finding 1 normal num
		count2 = 0
		while count2 < len(NormalList):
			if buff1First == NormalList[count2]:
				buff1Num = count2
				ResultList.append(buff1Num)

			count2 = count2 + 1
		
		#print buff1Num
		count = count + 1
	count3 = 0
	while count3 < len(list2):
		buff2 = list2[count3]
		buff2First = buff2
		buff2Num = 0
		#finding 2 normal num
		count2 = 0
		while count2 < len(NormalList):
			if buff2First == NormalList[count2]:
				buff2Num = count2
				ResultList.append(buff2Num)

			count2 = count2 + 1
		
		#print buff2Num
		count3 = count3 + 1
	#print "SORT"
	bubbleSort(ResultList)
	count2 = 0
	while count2 < len(ResultList):
		buff = ResultList[count2]
		buff = NormalList[buff]
		List.append(buff)
		
		count2 = count2 + 1
	
    	return List




# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
