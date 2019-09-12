'''
# O(n^2) time
maximum_area keep track # 0, 1, 2, 6,

width * height
a1 to a2
1*1 = (a1 to a2 distance = 1)*min(a1 height, a2 height)

a1 to a3
2*1 = (a1 to a3 distance = 2)*min(a1 height, a3 height)
1*6 = (a2 to a3 distance = 1)*min(a2 height, a3 height)

a1 to a4
(a1 to a4 distance = 3) * min(a1, a4 height) = 3*1
(a2 to a4 distance = 2) * min(a2, a4 height) = 2*2
(a3 to a4 distance = 1) * min(a3, a4 height) = 1*2

1*1 or 1*2 or 6*1
----------------------------
# O(n) time

height a1 < height a9 move left pointer to right
height a1 > height a9 move right pointer to left
1*8 = min(height a1, height a9) * distance of a9 to a1

7*7 = min(height a2, height )


'''

def max_area(heights): # O(N^2) time, O(1) space
	maximum = 0
	for i in range(1,len(heights)):
		for j in range(i):
			current_area = (i - j) * min(heights[i], heights[j])
			maximum = max(maximum, current_area)
	return maximum
print(max_area([1,8,6,2,5,4,8,3,7]))

def max_area_one_pass(heights): # O(N), O(1) space
'''
You have two heights H_left and H_right, and H_right < H_left, then we know we have two choices, we want to move one of them. If we move the larger one, we cannot increase the height for the simple reason that we are always limited by the shortest, and we would be decreasing j-i, the width as well.

To clarify: let's say we kept the shortest forever, what would happen? Well, j-i would decrease, and either we come across a taller block, which doesn't matter because our shorter one we kept only mattered, or we find a shorter one, in which case that one matters.

Either way we end up with a smaller area, so we must move the shorter one because moving the larger one cannot give an increase in area.
'''
	maximum = 0
	left, right = 0, len(heights) - 1
	while left < right:
		current_area = (right - left) * min(heights[right], heights[left])
		maximum = max(current_area, maximum)
		if heights[left] >= heights[right]:
			right -= 1
		elif heights[left] < heights[right]:
			left += 1
	return maximum

print(max_area_one_pass([1,8,6,2,5,4,8,3,7]))