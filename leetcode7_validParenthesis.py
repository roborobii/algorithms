from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
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