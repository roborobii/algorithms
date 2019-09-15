'''
(from geeksforgeeks)
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

'''

def missing_num(c, n):
	i = 1
	while (i < n):
		if (i != c[i-1]):
			return i
		i+=1
	return None

print(missing_num([1,2,3,5], 5)) # output 4
print(missing_num([1,2,3,4,5,6,7,8,10], 10)) # output 9