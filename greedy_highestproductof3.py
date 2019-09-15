def highest_product_of_3(list_of_ints):
	'''
	Method 1 Brute Force
		do bubble/insertion sort iteration 3 times to get the 3 highest numbers
		O(3N)=>O(N) time, O(1) space
		flaw: does not account for negative numbers

	Assumptions: there are negatives, unsorted,
				always atleast 3 integers in the input

	Method 2, Greedy Approach **(looked at the solution, couldn't come up with an answer)
		O(N) time and O(1) space
		How do we keep track of the highest_product_of_3 in each iteration
		* keep track of things that will help calculate a new highest_product of three
		keep track of:
			- highest_product_of_3
			- highest_product_of_2, lowest_product_of_2
			- highest, lowest
		a constant of 5 variables are being kept track of with any given input/length of input => O(1) space
		we need to access every possible value in any given list => O(N) time to traverse the list lenght of N

	'''
	highest = max(list_of_ints[0],list_of_ints[1])
	lowest = min(list_of_ints[0],list_of_ints[1])
	lowest_product_of_2 = list_of_ints[0]*list_of_ints[1]
	highest_product_of_2 = list_of_ints[0]*list_of_ints[1]
	highest_product_of_3 = list_of_ints[0]*list_of_ints[1]*list_of_ints[2]

	for i in range(2,len(list_of_ints)):
		current = list_of_ints[i]
		highest_product_of_3 = max(highest_product_of_3, current*highest_product_of_2, current*lowest_product_of_2)
		highest_product_of_2 = max(highest_product_of_2, current*highest, current*lowest)
		lowest_product_of_2 = min(lowest_product_of_2, current*highest, current*lowest)
		highest = max(highest,current)
		lowest = min(lowest,current)

	return highest_product_of_3

print(highest_product_of_3([2,-7,3,5]))