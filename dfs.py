class Graph(object):
	def __init__(self):
		self.nodes = [] # stores all reference to all nodes

class Node(object):
	def __init__(self, data):
		self.data = data
		self.neighbors = [] # stores Neighboring nodes

def dfs(node):
	# mark node visited / put it in a visited hashset
	# process node
	# for each neighbor of node that is unvisited
		# recursively call dfs on each neighbor
	pass

def dfs_print(node, visited):
	if node == None: return
	# mark node visited / put it in a visited hashset
	visited.add(node)
	print(node.data)
	for neighbor in node.neighbors:
		if neighbor not in visited:
			dfs_print(neighbor,visited)
	return

def exists_dfs(node, target, visited): # boolean
	visited.add(node) # mark visited
	if node.data == target: return True # process
	for neighbor in node.neighbors: # recursive on neighbors
		if neighbor not in visited and exists_dfs(neighbor, target, visited):
			return True
	return False

def all_nodes_in_graph_exists(graph, target, visited): # if any unconnected nodes
	if graph == None: return False
	for node in graph.nodes:
		if exists_dfs(node, target, visited):
			return True
	return False

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n1.neighbors.append(n2)
n1.neighbors.append(n3)
n2.neighbors.append(n4)
n4.neighbors.append(n6)
n3.neighbors.append(n4)
n3.neighbors.append(n5)
n5.neighbors.append(n6)
visited = set()
# print(exists_dfs(n1,5,visited))
dfs_print(n1, visited)

# ----------------------------------------------------------------------

from collections import defaultdict

def calcEquation(equations, values, queries):
    graph = make_graph(equations, values)
    result = []
    for query in queries:
        result.append(dfs_helper(graph, query[0], query[1], set()))
    return result
def make_graph(equations, values):
    graph = defaultdict(list)
    for i in range(len(equations)):
        edge = equations[i]
        weight = values[i]
        start, end = edge
        graph[start].append((end,weight))
        graph[end].append((start,1/weight))
    return graph

def dfs_helper(graph, start, end, seen):
    for k,v in graph[start]:
        if k == end:
            return v
    seen.add(start)
    for entry in graph[start]:
        if entry[0] in seen:
            continue
        result = dfs_helper(graph, entry[0], end, seen)
        if result == -1.0:
            continue
        return result*entry[1]
    return -1.0
    

# ----------------------------------------

def restoreIpAddresses(s):
    ips = []
    dfs_helper(s, 0, ips,"")
    return ips

def dfs_helper(s, curr_length, ips, ip):
    if curr_length == 4:
        if s == '':
            ips.append(ip[1:])
        return
    for i in range(1,4):
        if i <= len(s):
            if int(s[:i]) <= 255:
                dfs_helper(s[i:], curr_length+1, ips, ip+"."+s[:i])
            if s[0] == '0':
                break
    return


# -------------------------------------------

def make_mapping(): # O(1) time, O(1) space since always the same numbers
    mapping = dict()
    mapping["2"] = list("abc")
    mapping["3"] = list("def")
    mapping["4"] = list("ghi")
    mapping["5"] = list("jkl")
    mapping["6"] = list("mno")
    mapping["7"] = list("pqrs")
    mapping["8"] = list("tuv")
    mapping["9"] = list("wxyz")
    return mapping

def letterCombinations(digits):
    results = []
    letterCombinations_helper(0, make_mapping(), digits, len(digits), "", results)
    return results

def letterCombinations_helper(start, mapping, digits, size, current, results):
    if start == size:
        results.append(current)
        return
    for letter in mapping[digits[start]]:
        letterCombinations_helper(start+1, mapping, digits, size, current+letter, results) 



# ------------------------------------------

def get_neighbors(i, j):
    return [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

def exist(board, word):
    if board == [] or board == [[]]: return False
    rows = len(board)
    cols = len(board[0])
    valid_unvisited = set()
    for i in range(rows):
        for j in range(cols):
            valid_unvisited.add((i,j))
    flag = False
    for i in range(rows):
        for j in range(cols):
            if (i,j) in valid_unvisited:
                valid_unvisited.remove((i,j))
                flag = dfs_helper(i, j, valid_unvisited, 1, word, board[i][j], board)
                if flag:
                    return True
    return False

def dfs_helper(i, j, valid_unvisited, word_pointer, word, result,board):
    if word_pointer == len(word):
        return True

    neighbors = get_neighbors(i,j)
    for neighbor in neighbors:
        if neighbor in valid_unvisited and board[neighbor[0]][neighbor[1]] == word[word_pointer]:
            valid_unvisited.remove(neighbor)
            return dfs_helper(neighbor[0], neighbor[1], valid_unvisited, word_pointer+1, word, result+board[neighbor[0]][neighbor[1]], board)
    
    return False