def word_split(phrase, list_of_words, output = []):
	return word_split_helper(phrase, set(list_of_words), output) 

def word_split_helper(phrase, words_set, output):
	if len(phrase) == 0: return output

	substring = ""
	for i, char in enumerate(phrase):
		substring += char
		if substring in words_set:
			output.append(substring)
			if i+1 == len(phrase): return output
			return word_split_helper(phrase[i+1:], words_set, output)
	return output

print(word_split("themanran", ["clown", "ran", "man"], []))
print(word_split("themanran", ["the", "ran", "man"], []))
print(word_split("ilovehotdogJohn", ["i", "John", "am", "a", "super", "hotdog", "love"], []))