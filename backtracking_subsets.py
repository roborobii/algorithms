'''
Given a set of distinct integers, return all possible subsets (powerset)
Note: Solution musn't contain duplicate subsets

i/p: nums = [1,2,3]
o/p:
[
[3],
[1],
[2],
[1,2,3],
[1,3],
[2,3],
[1,2],
[]
]

'''

def powerset(nums):
	subsets = []
	powerset_helper(0, [], nums, subsets)
	return subsets

def powerset_helper(start, current, nums, subsets): # O(2^N); dfs on tree/graph == backtracking
	if start >= len(nums):
		subsets.append(current)
	else:
		powerset_helper(start+1, current + [nums[start]], nums, subsets)
		powerset_helper(start+1, current, nums, subsets)

print(powerset([1,2,3]))

# DFS: total time complexity = O(# of nodes * time complexity at each node)
# 	   space complexity = O(Height) or O(Max Depth) of tree or graph (calls on recursion stack)


class Solution:
    def subsets(self, nums): # O(2^N)
        if not nums: return []
        self.res = []
        self.dfs(nums, [], 0)
        return self.res
    
    
    def dfs(self, nums, temp, index):
        if index == len(nums):
            self.res.append(temp[:])
            return
        
        temp.append(nums[index])        
        self.dfs(nums, temp, index + 1)
        temp.pop()
        self.dfs(nums, temp, index + 1)
a = Solution()
print(a.subsets([1,2,3]))