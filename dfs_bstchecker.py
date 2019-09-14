class BinaryTree(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def bst_check(binary_tree):
	# base case(s)
	if binary_tree == None: return True

	if binary_tree.left != None and binary_tree.left.value > binary_tree.value:
		return False
	if binary_tree.right != None and binary_tree.right.value < binary_tree.value:
		return False

	# request left,right children
	left = bst_check(binary_tree.left)
	right = bst_check(binary_tree.right)

	# response
	return left and right

root = BinaryTree(2)
root.left = BinaryTree(1)
root.left.left = BinaryTree(0)

root.right = BinaryTree(4)
root.right.left = BinaryTree(3)
root.right.right = BinaryTree(100)

print(bst_check(root))