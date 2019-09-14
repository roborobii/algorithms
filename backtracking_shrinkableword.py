'''
def backtracking_template(choices, other_params):
	if base_case():
		return whether_solvable
	else:
		for choice in choices:
			# edit choice or other params to try out 
			if is_valid(choice) && backtracking_template(choice, other_params):
				return success
			# may need to undo
	return failure
'''

def is_shrinkable(string, dictionary): # O(2^N) time, backtracking is exponential because it's an exhaustive search algo
	if len(s) == 0:
		return True
	else:
		for i, letter in enumerate(string):
			# EDIT CHOICE OR OTHER PARAMS  choice or other params to try out 
			# delete the chosen letter from the string
			new_string = delete_letter(i, string) # deletes letter at i
			if choice_in_dictionary(new_string, dictionary) and is_shrinkable(new_string, dictionary):
				return True
			# may need to undo
			# add the letter back from choice
	return False
	

def is_shrinkable(word, lexicon):
	if word not in lexicon:
		return False
	if len(word) == 1:
		return True
	else:
		for letter_index in range(len(word)):
			shrunken_word = word[:letter_index] + word[letter_index+1:]
			if shrunken_word in lexicon and is_shrinkable(shrunken_word, lexicon):
				return True
		return False


def sudoku(board, row, col):
	if correct(board):
		print(board)
		return True
	else:
		rows = len(board)
		cols = len(board[0])
		for r in range(row, rows):
			for c in range(col, cols):
				# edit choice or other params to try out 
				board[row][col] = 
				if is_valid(board, row, col) && backtracking_template(board, row, col):
					return True
				# may need to undo
	return False

'''
not optimal but a way/potential solution

identifying Backtracking problems: (exhaustive search!)
- find all possible ... 
- find any such that ...
- count total number that ...
- determine if a solution exists ...
- find the best solution to ...

'''
