def topKFrequent(words, k):
    # Write your code here
    # 1) count the number of occurences, use a hashtable 
    # this will run O(N) time where N is length of the words array
    frequency_count = dict()
    for word in words:
        if word in frequency_count:
            frequency_count[word] += 1
        else:
            frequency_count[word] = 1
    
    # 2) have a unique word list, this is just the keys in the dictionary
    unique_words = []
    for word in frequency_count.keys():
        unique_words.append(word)

    print(unique_words)

    # 3) sort it by freq first but at equal frequency then by alphabetically for those
    unique_words.sort(key = lambda word: (-frequency_count[word], word))

    return unique_words[:k]


def findWords(words):
    # Write your code here
    result = []
    row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
    for word in words:
        add_to_result = True
        if len(word) == 0:
            continue
        lowercase_word = word.lower()
        if lowercase_word[0] in row1:
            for char in lowercase_word:
                if char not in row1:
                    add_to_result = False
                    break
        elif lowercase_word[0] in row2:
            for char in lowercase_word:
                if char not in row2:
                    add_to_result = False
                    break
        elif lowercase_word[0] in row3:
            for char in lowercase_word:
                if char not in row3:
                    add_to_result = False
                    break
        if add_to_result:
            result.append(word)
        
    return result

def anagramMappings(arr1, arr2):
    # Write your code here
    indices = dict()
    result = []
    for i,num in enumerate(arr2):
        indices[num] = i
    for num in arr1:
        result.append(indices[num])
    return result

def numJewelsInStones(J, S):
    # Write your code here
    counter = 0
    unique_jewels = set(J)
    # print(unique_jewels)
    for stone in S:
        if stone in unique_jewels:
            counter += 1
    return counter

def singleNumber(nums):
    # Write your code here
    # Read question
    # Ask clarifying questions: are the elements only single digits? is the given input array sorted?
    # Confirm i/o: what do you want for inputs? what about for outputs?
    # Hack brute force
    unique_dictionary = dict()
    for num in nums:
        if num in unique_dictionary:
            unique_dictionary[num] += 1
        else:
            unique_dictionary[num] = 1
    for key,value in unique_dictionary.items():
        if (value == 1):
            return key