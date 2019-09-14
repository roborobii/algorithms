def valid_permutation(n):
	result = []
	valid_permutation_helper(2*n, "", result)
	return result

def valid_permutation_helper(n, current, result):
	if n < 0:
		if len(current) != 0 and len(current) % 2 == 0 and current not in result and valid(current): # checks whether current string is valid permutation of paren
			result.append(current)
	else:
		valid_permutation_helper(n-1, current, result)
		valid_permutation_helper(n-1, current + "(", result)
		valid_permutation_helper(n-1, current + ")", result)

from collections import deque

def valid(s):
    stack = deque()
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif stack and c == ')' and stack[-1] == '(':
            stack.pop()
        elif stack and c == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and c == ']' and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return len(stack) == 0
print(valid_permutation(3))

class Solution(object):
    def validParentheses(self, n):
        result = []
        left_remain = right_remain = n
        self.helper(left_remain, right_remain, 2 * n, result, [])
        return result
  
    def helper(self, left_remain, right_remain, size, result, temp):
        if len(temp) == size:
            result.append(''.join(temp))

        if left_remain > 0:
        	self.helper(left_remain-1, right_remain, size, result, temp + ["("])
    	if right_remain > 0 and right_remain > left_remain:
    		self.helper(left_remain, right_remain-1, size, result, temp + [")"])

a = Solution()
print(a.validParentheses(3))