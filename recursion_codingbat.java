public int factorial(n) {
  if (n == 1) return 1;
  return n * factorial(n-1);
}
public int bunnyEars(n) {
  if (n == 0) return 0;
  return 2 + bunnyEars(bunnies - 1);
}
public int fibonacci(n) {
  if (n <= 0) return 0;
  if (n <= 2) return 1;
  return fibonacci(n-1) + fibonacci(n-2);
}
// def fibonacci_dp(n):
//   memo = [0,1,1]
//   if n == 0 or n == 1 or n == 2:
//     return memo[n]
//   for i in range(3, n+1):
//     memo.append(memo[i-1] + memo[i-2])
//   return memo[n]
public int bunnyEars2(int bunnies) {
  if (bunnies == 0) return 0;
  if (bunnies % 2 == 1) return 2 + bunnyEars2(bunnies-1);
  else // (bunnies % 2 == 0) => evens
  return 3 + bunnyEars2(bunnies-1);
}
public int triangle(int rows) {
  if (rows == 0) return 0;
  return rows + triangle(rows - 1);
}

// Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), 
//   while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
public int sumDigits(int n) {
  if (n == 0) return 0;
  return n % 10 + sumDigits(n / 10);
}
public int count7(int n) {
  if (n == 0) return 0;
  if (n % 10 == 7) return 1 + count7(n / 10);
  return count7(n / 10);
}
public int count8(int n) {
  if (n == 0) return 0;
  if (n % 10 == 8 && (n / 10) % 10 == 8) return 2 + count8(n / 10);
  if (n % 10 == 8) return 1 + count8(n / 10);
  return count8(n / 10);
}

public int powerN(int base, int n) {
  if (n == 0) return 1;
  return base * powerN(base, n-1);
}

public int countX(String str) {
  int size = str.length();
  return countX_helper(str, 0, size);
}
public int countX_helper(String str, int pointer, int size) {
  if (size == pointer) return 0;
  if (str.charAt(pointer) == 'x') return 1 + countX_helper(str, pointer+1, size);
  return countX_helper(str, pointer+1, size);
}
public int countX_noHelper(String str) {
  if (str.length() == 0) return 0;
  if (str.charAt(0) == 'x') return 1 + countX(str.substring(1));
  return countX(str.substring(1));
}

public int countHi(String str) {
  return countHi_helper(str, 0, str.length());
}
public int countHi_helper(String str, int pointer, int size) {
  if (size == pointer) return 0;
  if (str.charAt(pointer) == 'h' && pointer+1 < size && str.charAt(pointer+1) == 'i') 
    return 1 + countHi_helper(str, pointer+2, size);
  return countHi_helper(str, pointer+1, size);
}
public int countHi_noHelper(String str) {
  if (str.length() < 2) return 0;
  if (str.substring(0, 2).equals("hi")) return 1 + countHi(str.substring(2));
  return countHi(str.substring(1));
}

public String changeXY(String str) {
  return changeXY_helper(str, "");
}
public String changeXY_helper(String str, String result) {
  if (str.length() == 0) return result;
  if (str.charAt(0) == 'x') return changeXY_helper(str.substring(1), result + 'y');
  return changeXY_helper(str.substring(1), result + str.charAt(0));
}
public String changeXY_noHelper(String str) {
  if (str.length() == 0) return str;
  if (str.charAt(0) == 'x') return 'y' + changeXY(str.substring(1));
  return str.charAt(0) + changeXY(str.substring(1));
}

public String changePi(String str) {
  return changePi_helper(str, "");
}
public String changePi_helper(String str, String result) {
  if (str.length() == 0) return result;
  if (str.charAt(0) == 'p' && str.length() > 1 && str.charAt(1) == 'i')
    return changePi_helper(str.substring(2), result + "3.14");
  return changePi_helper(str.substring(1), result + str.charAt(0));
}
public String changePi_noHelper(String str) {
  if (str.length() < 2) return str;
  if (str.substring(0, 2).equals("pi")) return "3.14" + changePi_noHelper(str.substring(2));
  return str.charAt(0) + changePi_noHelper(str.substring(1));
}

public String noX(String str) {
  if (str.length() == 0) return str;
  if (str.charAt(0) == 'x') return noX(str.substring(1));
  return str.charAt(0) + noX(str.substring(1));
}

public boolean array6(int[] nums, int index) {
  if (index == nums.length) return false;
  if (nums[index] == 6) return true;
  return array6(nums, index+1);
}
public int array11(int[] nums, int index) {
  if (nums.length == index) return 0;
  if (nums[index] == 11) return 1 + array11(nums, index+1);
  return array11(nums, index+1);
}
public boolean array220(int[] nums, int index) {
  if (index + 1 >= nums.length) return false;
  if (nums[index] * 10 == nums[index + 1])
    return true;
  return array220(nums, index + 1);
}

public String allStar(String str) {
  if (str.length() <= 1) return str;
  return str.charAt(0) + "*" + allStar(str.substring(1));
}
public String pairStar(String str) {
  if (str.length() <= 1) return str;
  if (str.charAt(0) == str.charAt(1)) return str.charAt(0) + "*" + pairStar(str.substring(1));
  return str.charAt(0) + pairStar(str.substring(1));
}
public String endX(String str) {
  if (str.length() == 0) return str;
  if (str.charAt(0) == 'x') return endX(str.substring(1)) + "x";
  return str.charAt(0) + endX(str.substring(1));
}
public int countPairs(String str) {
  if (str.length() <= 2) return 0;
  if (str.charAt(0) == str.charAt(2)) return 1 + countPairs(str.substring(1));
  return countPairs(str.substring(1));
}
public int countAbc(String str) {
  if (str.length() <= 2) return 0;
  if (str.substring(0,3).equals("abc") || str.substring(0,3).equals("aba"))
    return 1 + countAbc(str.substring(1));
  return countAbc(str.substring(1));
}
public int count11(String str) {
  if (str.length() <= 1) return 0;
  if (str.substring(0,2).equals("11")) return 1 + count11(str.substring(2));
  return count11(str.substring(1));
}
public String stringClean(String str) {
  if (str.length() <= 1) return str;
  if (str.charAt(0) == str.charAt(1)) return stringClean(str.substring(1));
  return str.charAt(0) + stringClean(str.substring(1));
}
public int countHi2(String str) {
  if (str.length() <= 1) return 0;
  if (str.charAt(0) == 'x' && str.charAt(1) == 'h') return countHi2(str.substring(2));
  if (str.substring(0,2).equals("hi")) return 1 + countHi2(str.substring(2));
  return countHi2(str.substring(1));
}

// after finding the first open paren, 
//   start recursing and decrementing to find the closing paren
public String parenBit(String str) {
  if (str.length() == 0) return str;
  if (str.charAt(0) == '(') {
    if (str.charAt(str.length()-1) == ')') return str;
    return parenBit(str.substring(0, str.length()-1));
  }
  return parenBit(str.substring(1));
}

// find pairing open/close paren recursively, until the mid point
//  midpoint is when length of the string is 0
public boolean nestParen(String str) {
  if (str.length() == 0) return true;
  if (str.charAt(0) == '(' && str.charAt(str.length()-1) == ')')
    return nestParen(str.substring(1,str.length()-1));
  return false;
}

public int strCount(String str, String sub) {
  if (str.length() < sub.length()) return 0;
  if (str.substring(0, sub.length()).equals(sub)) 
    return 1 + strCount(str.substring(sub.length()), sub);
  return strCount(str.substring(1), sub);
}

public boolean strCopies(String str, String sub, int n) {
  if (str.length() < sub.length()) return n == 0;
  if (str.substring(0, sub.length()).equals(sub))
    return strCopies(str.substring(1), sub, n-1);
  return strCopies(str.substring(1), sub, n);
}

public int strDist(String str, String sub) {
  if (str.length() < sub.length()) return 0;
  if (str.substring(0, sub.length()).equals(sub)) {
    if (str.substring(str.length() - sub.length()).equals(sub))
      return str.length();
    else
      return strDist(str.substring(0, str.length() - 1), sub);
  }
  return strDist(str.substring(1), sub);
}

public boolean groupSum(int start, int[] nums, int target) {
  if (start == nums.length) return target == 0;
  if (groupSum(start+1, nums, target-nums[start])) return true; // choose
  if (groupSum(start+1, nums, target)) return true; // not choose
  return false;
}

public boolean groupSum(int start, int[] nums, int target) {
  // Base case: if there are no numbers left, then there is a
  // solution only if target is 0.
  if (start >= nums.length) return (target == 0);
  
  // Key idea: nums[start] is chosen or it is not.
  // Deal with nums[start], letting recursion
  // deal with all the rest of the array.
  
  // Recursive call trying the case that nums[start] is chosen --
  // subtract it from target in the call.
  if (groupSum(start + 1, nums, target - nums[start])) return true;
  
  // Recursive call trying the case that nums[start] is not chosen.
  if (groupSum(start + 1, nums, target)) return true;
  
  // If neither of the above worked, it's not possible.
  return false;
}

public boolean groupSum6(int start, int[] nums, int target) {
  if (start == nums.length) return target == 0;
  if (nums[start] == 6) return groupSum6(start+1, nums, target - 6);
  if (groupSum6(start+1, nums, target - nums[start])) return true;
  if (groupSum6(start+1, nums, target)) return true;
  return false;
}

public boolean groupNoAdj(int start, int[] nums, int target) {
  if (start >= nums.length) return target == 0;
  if (groupNoAdj(start+2, nums, target - nums[start])) return true;
  if (groupNoAdj(start+1, nums, target)) return true;
  return false;
}

public boolean groupSum5(int start, int[] nums, int target) {
  if (start >= nums.length) return target == 0;
  if (nums[start] % 5 == 0 && start + 1 < nums.length && nums[start + 1] != 1)
    return groupSum5(start + 1, nums, target - nums[start]);  
  if (nums[start] % 5 == 0 && start + 1 < nums.length && nums[start + 1] == 1)
    return groupSum5(start + 2, nums, target - nums[start]);
  if (nums[start] % 5 == 0 && start + 1 >= nums.length)
    return groupSum5(start + 1, nums, target - nums[start]);
  if (groupSum5(start + 1, nums, target - nums[start])) return true;
  if (groupSum5(start + 1, nums, target)) return true;
  return false;
}

public boolean groupSum5(int start, int[] nums, int target) {
  if (start >= nums.length) return target == 0;
  if (nums[start] % 5 == 0 && start + 1 < nums.length) {
    if (nums[start + 1] == 1) return groupSum5(start + 2, nums, target - nums[start]);
    if (nums[start + 1] != 1) return groupSum5(start + 1, nums, target - nums[start]);
  } else if (nums[start] % 5 == 0 && start + 1 >= nums.length) {
    return groupSum5(start + 1, nums, target - nums[start]);
  }
  if (groupSum5(start + 1, nums, target - nums[start])) return true;
  if (groupSum5(start + 1, nums, target)) return true;
  return false;
}

public boolean groupSumClump(int start, int[] nums, int target) {
  if (start >= nums.length) return target == 0;
  int currentIndex = start;
  int currentTotal = 0;
  int currentElement = nums[currentIndex];
  while (currentIndex < nums.length) {
    if (nums[currentIndex] == currentElement) {
      currentTotal += currentElement;
      currentIndex += 1;
    } else {
      break;
    }
  }
  if (groupSumClump(currentIndex, nums, target - currentTotal)) return true;
  if (groupSumClump(currentIndex, nums, target)) return true;
  return false;
}

public boolean splitArray(int[] nums) {
  return splitArrayHelper(nums, 0, 0, 0);
}
public boolean splitArrayHelper(int[] nums, int left, int right, int start) {
  if (start >= nums.length) return left == right;
  if (splitArrayHelper(nums, left + nums[start], right, start + 1)) return true;
  if (splitArrayHelper(nums, left, right + nums[start], start + 1)) return true;
  return false;
}

public boolean splitOdd10(int[] nums) {
  return splitOdd10Helper(nums, 0, 0, 0);
}
public boolean splitOdd10Helper(int[] nums, int left, int right, int start) {
  if (start >= nums.length) return left % 10 == 0 && right % 2 == 1;
  if (splitOdd10Helper(nums, left + nums[start], right, start + 1)) return true;
  if (splitOdd10Helper(nums, left, right + nums[start], start + 1)) return true;
  return false;
}

public boolean split53(int[] nums) {
  return split53Helper(nums, 0, 0, 0);
}
public boolean split53Helper(int[] nums, int left, int right, int start) {
  if (start >= nums.length) return left == right;
  if (nums[start] % 5 == 0 && nums[start] % 3 != 0) return split53Helper(nums, left + nums[start], right, start + 1);
  if (nums[start] % 3 == 0 && nums[start] % 5 != 0) return split53Helper(nums, left, right + nums[start], start + 1);
  if (split53Helper(nums, left + nums[start], right, start + 1)) return true;
  if (split53Helper(nums, left, right + nums[start], start + 1)) return true;
  return false;
}
