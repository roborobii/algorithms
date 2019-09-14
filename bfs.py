from collections import deque

class Graph(object):
	def __init__(self):
		self.nodes = [] # stores all reference to all nodes

class Node(object):
	def __init__(self, data):
		self.data = data
		self.neighbors = [] # stores Neighboring nodes


def bfs(node):
	# start queue and visited set, initiate node in both
	# while queue is not empty we can process bfs
		# pop a node off queue
		# process popped node
		# add all unvisited neighbors onto queue and visited
	pass

def bfs_print(node):
	if node == None: return
	bfsvisited = set([node])
	queue = deque([node]) # start queue, initiate root in it
	while queue: # while queue is not empty
		current = queue.popleft() # pop queue
		bfsvisited.add(current) # mark visited
		print(current.data) # process
		for neighbor in current.neighbors: # add popped node's neighbors into queue
			if neighbor not in bfsvisited:
				bfsvisited.add(neighbor)
				queue.append(neighbor)
	return

bfs_print(n1)
