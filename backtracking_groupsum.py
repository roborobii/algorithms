def groupSum(start, nums, target):
	if start >= len(nums):
		return target == 0
	if (groupSum(start+1, nums, target - nums[start])):
		return True
	if (groupSum(start+1, nums, target)):
		return True
	return False
print(groupSum(0, [2, 4, 8], 10))


def groupSum6(start, nums, target):
    if (start >= len(nums)):
        return target == 0
    if (nums[start] == 6):
        return groupSum6(start+1, nums, target - nums[start])
    else:
        if (groupSum6(start+1, nums, target - nums[start])):
            return True
        if (groupSum6(start+1, nums, target)):
            return True
        return False
print(groupSum6(0, [2, 4, 6, 6], 13))
print(groupSum6(0, [5, 6, 2], 8))


def groupNoAdj(start, nums, target):
    if (start >= nums.length):
        return target == 0;
    if (groupNoAdj(start+2, nums, target - nums[start])):
        return True
    if (groupNoAdj(start+1, nums, target)):
        return True
    return False

'''
public boolean groupNoAdj(int start, int[] nums, int target) {
    if (start >= nums.length) return target == 0;
    if (groupNoAdj(start+2, nums, target - nums[start])) return true;
    if (groupNoAdj(start+1, nums, target)) return true;
    return false;
}

// splitArray
public boolean splitArray(int[] nums) {
  int start = 0;
  int a = 0;
  int b = 0;
  return splitArrayHelper(start, nums, a, b);
}
public boolean splitArrayHelper(int start, int[] nums, int a, int b) {
  if (start >= nums.length) return a == b;
  // if (splitArrayHelper(start+1, nums, a+nums[start], b)) return true;
  // if (splitArrayHelper(start+1, nums, a, b+nums[start])) return true;
  // return false;
  return splitArrayHelper(start+1, nums, a+nums[start], b) || splitArrayHelper(start+1, nums, a, b+nums[start]);
}


// splitOdd10
public boolean splitOdd10(int[] nums) {
  int start = 0;
  int a = 0;
  int b = 0;
  return splitOdd10Helper(start, nums, a, b);
}
public boolean splitOdd10Helper(int start, int[] nums, int a, int b) {
  if (start >= nums.length) {
    if ((a % 10 == 0 && b % 2 == 1) || (b % 10 == 0 && a % 2 == 1)) return true;
    return false;
  }
  // if (splitOdd10Helper(start+1, nums, a+nums[start], b)) return true;
  // if (splitOdd10Helper(start+1, nums, a, b+nums[start])) return true;
  // return false;
  return splitOdd10Helper(start+1, nums, a+nums[start], b) || splitOdd10Helper(start+1, nums, a, b+nums[start]);
}


// split53
public boolean split53(int[] nums) {
  int start = 0;
  int a = 0;
  int b = 0;
  return split53Helper(start, nums, a, b);
}
public boolean split53Helper(int start, int[] nums, int a, int b) {
  if (start >= nums.length) return a == b;
  // if (nums[start] % 5 == 0 && split53Helper(start+1, nums, a+nums[start], b)) return true;
  // else if (nums[start] % 3 == 0 && split53Helper(start+1, nums, a, b+nums[start])) return true;
  // else if (split53Helper(start+1, nums, a+nums[start], b)) return true;
  // else if (split53Helper(start+1, nums, a, b+nums[start])) return true;
  // return false;
  
  if (nums[start] % 5 == 0)
    return split53Helper(start+1, nums, a+nums[start], b);
  else if (nums[start] % 3 == 0)
    return split53Helper(start+1, nums, a, b+nums[start]);
  else
    return split53Helper(start+1, nums, a+nums[start], b) || split53Helper(start+1, nums, a, b+nums[start]);
}


'''