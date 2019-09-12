class Solution:
    def two_sum_sorted_input(self, numbers: List[int], target: int) -> List[int]: # O(N) time, O(1) space
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l, r]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return []

    def two_sum(self, numbers: List[int], target: int) -> List[int]: # O(N) time, O(N) space
        # save a hashmap of the element as key and index as its value
        table = dict()
        for i, num in enumerate(numbers):
            if target - num in table:
                return [table[target - num], i]
            else:
                table[num] = i
        return []

    def threeSum_initial_attempt(self, nums: List[int]) -> List[List[int]]:
        # are the numbers in the input array unique?
        # use a twoSum? which is implemented with a hash set to find a target to yield O(n)
        
        # O(n^3) approach where a number will go for every other number and those will go for every other number
        nums.sort() # O(nlogn)
        result = []
        size = len(nums)
        unique_triplets = set()
        for i in range(size):
            for j in range(i, size):
                for k in range(j,size):
                    if i != j and j != k and k != i and (nums[i] + nums[j] + nums[k] == 0):
                        if [nums[i], nums[j], nums[k]] not in unique_triplets.add([nums[i], nums[j], nums[k]])
                        result.append([nums[i], nums[j], nums[k]])
        return result
        # target = 0
        # twoSum(nums, target) # find two numbers that sum up to a number in the array
    def three_sum_final(self, numbers: List[int]): # O(N^2) time, O(N) space to store result
        # sort numbers
        # use two pointers

        # numbers.sort() # inplace O(nlogn) sort, will change the input; O(1) space
        nums = sorted(numbers) # out of place O(nlogn) sort, will NOT change input; creates new list O(N) space
        result = []
        length = len(nums)

        for i in range(length-2): # O(N^2)
            if nums[i] > 0: return result
            if i > 0 and nums[i-1] == nums[i]: continue

            l, r = i + 1, length - 1
            while l < r: # O(N)
                current = nums[i] + nums[l] + nums[r]
                if current > 0:
                    r -= 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                elif current < 0:
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                else: # current == 0
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    r -= 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1

        return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort numbers
        # use two pointers

        nums.sort()
        result = []
        length = len(nums)

        for i in range(length-2): # O(N^2)
            if nums[i] > 0: return result
            if i > 0 and nums[i-1] == nums[i]: continue

            l, r = i + 1, length - 1
            while l < r: # O(N)
                current = nums[i] + nums[l] + nums[r]
                if current > 0:
                    r -= 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                elif current < 0:
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                else: # current == 0
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    r -= 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1

        return result