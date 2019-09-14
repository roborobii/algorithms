from collections import deque

def calcEquation(equations, values, queries):
    def makeGraph(equations, values):
        adjacency_list = dict()
        for index,equation in enumerate(equations):
            if equation[0] in adjacency_list:
                adjacency_list[equation[0]].append((equation[1],values[index]))
            else:
                adjacency_list[equation[0]] = [(equation[1],values[index])]
        return adjacency_list
    def bfs_helper(graph, start, end):
        # Step1: Initialize Queue + Set       
        queue = deque([(start, 1.0)])
        visited = set([start])

        # Step2: Iterate through queue
        while queue:
            node, cur_val = queue.popleft()
            # Step3: Terminating Condition
            if node == end:
                return cur_val

            # Step 4: Add expansion into visited set
            visited.add(node)

            # Step 5: Check visited set and enqueue neighbor
            for neighbor, value in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, cur_val * value))
        return -1.0
    result = []
    graph = makeGraph(equations,values)
    for query in queries:
        result.append(bfs_helper(graph,query[0],query[1]))
   	return result

def calcEquation2(equations, values, queries):
    def make_graph(equations, values):
        graph = {}
        def add_edge(n1, n2, value):
            if n1 in graph:
                graph[n1].append((n2, value))
            else:
                graph[n1] = [(n2, value)]
        
        for i in range(len(values)):
            n1, n2 = equations[i][0] , equations[i][1]
            add_edge(n1, n2, values[i])
            add_edge(n2, n1, 1 / values[i])
            
        return graph

    def bfs_helper(graph, start, end):
        # Step1: Initialize Queue + Set       
        queue = deque([(start, 1.0)])
        visited = set([start])

        # Step2: Iterate through queue
        while queue:
            node, cur_val = queue.popleft()
            # Step3: Terminating Condition
            if node == end:
                return cur_val

            # Step 4: Add expansion into visited set
            visited.add(node)

            # Step 5: Check visited set and enqueue neighbor
            for neighbor, value in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, cur_val * value))
        return -1.0

    result = []
    graph = make_graph(equations,values)
    for query in queries:
        result.append(bfs_helper(graph,query[0],query[1]))
    return result
