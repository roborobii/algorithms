class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1. have a hashtable/dictionary
        2. store key each word sorted, and values as indices from strs
        3. use those anagrams and indices to create result
        '''
        # result = []
        # anagrams = dict()
        # for i,word in enumerate(strs):
        #     temp = str(sorted(word))
        #     if temp in anagrams:
        #         anagrams[temp].append(i)
        #     else:
        #         anagrams[temp] = [i]
        # for anagram, indices in anagrams.items():
        #     temp2 = []
        #     for i in indices:
        #         temp2 += [strs[i]]
        #     result.append(temp2)
        # return result

        '''
        Shorter (one loop): 
        1. store hashtable with sorted word as key, 
        	store list of the anagram words as list for value
		2. return value which is the last of anagram words 
        '''
        anagrams = dict()
        for word in strs:
        	temp = str(sorted(word))
        	if temp in anagrams:
        		anagrams[temp].append(word)
        	else:
        		anagrams[temp] = [word]
        return [anagrams.values()]