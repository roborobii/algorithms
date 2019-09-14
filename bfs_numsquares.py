from collections import deque

def numSquares(n):
    squares = []
    for i in range(1, n+1):
        squares.append(i*i)
    
    unique = set()
    queue = deque([n])

    levels = 0

    while queue:
        levels += 1
        size = len(queue)
        for i in range(size):
            current = queue.popleft()
            for element in squares:
                value = current - element
                if value < 0:
                    break
                if value == 0:
                    return levels
                if value in unique:
                    continue
                queue.append(value)
                unique.add(value)
    return -1