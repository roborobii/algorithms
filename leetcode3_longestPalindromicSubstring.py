def longest_palindromic_substring(s): # banana
	if len(s) == 0: return s

	length = len(s) # 6
	mid = 0
	max_substring_length = 0
	final_palindrome = ""

	while mid < length: # 0 < 6  # 1 < 6 # 2
		current_palindrome = longest_palindrome(s, mid) # b # a
		if len(current_palindrome) > max_substring_length: # 1 > 0
			max_substring_length = len(current_palindrome) # 1
			final_palindrome = current_palindrome # "b"
		mid += 1

	return final_palindrome

def longest_palindrome(s, mid): # s, 0 # s, 1, # s, 2
	final_palindrome = s[mid] # "b" # a # n # ana
	start = mid - 1 # -1 # 0 # 1
	end = mid + 1 # 1 # 2 # 3
	while start >= 0 and end < len(s):
		palindrome = s[start:end+1] # ana
		# if is_palindrome(palindrome): 
		if s[start] == s[end]:
			# final_palindrome = palindrome # ana
			final_palindrome = s[start:end+1]
			start -= 1 # 0
			end += 1 # 4
		else:
			break
	return final_palindrome # b # a 

# def is_palindrome(s):
# 	i, j = 0, len(s) - 1
# 	while i < j:
# 		if s[i] != s[j]:
# 			return False
# 		i+=1
# 		j-=1
# 	return True
		
print(longest_palindromic_substring("banana"))

# solve it using dynamic programming