def balance_check(s):
	stack = []
	for char in s:
		if char == '(' or char == '[':
			stack.append(char)
		elif char == ']':
			popped = stack.pop()
			if popped != '[':
				return False
		elif char == ')':
			popped = stack.pop()
			if popped != '(':
				return False
		else:
			continue
	return len(stack) == 0