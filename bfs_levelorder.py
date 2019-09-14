from collections import deque

def levelOrder(root):
	if not root:
		return []
	# 1. make queue
	queue, result = deque([root]), []

	# 2. iterate over the queue
	while queue:

		# 3. keep queue size
		current_level, size = [], len(queue)

		# 4. expand the children
		for i in range(size):
			node = queue.popleft()
			current_level.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		result.append(current_level)

	return result