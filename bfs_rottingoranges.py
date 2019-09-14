from collections import deque

def find_neighbors(coordinate):
    i,j = coordinate
    return [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

def orangesRotting(grid):
    if grid == [[]]:
        return -1
    rotten_queue, minute_counter, fresh_set = deque([]), 0, set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh_set.add((i,j))
            elif grid[i][j] == 2:
                rotten_queue.append((i,j))
    
    while rotten_queue and len(fresh_set) != 0:
        rot_flag = False
        size = len(rotten_queue)
        for _ in range(size):
            current = rotten_queue.popleft()
            valid_neighbors = find_neighbors(current) # give all 4 directions
            for valid_neighbor in valid_neighbors:
                if valid_neighbor in fresh_set:
                    rot_flag = True
                    fresh_set.remove(valid_neighbor)
                    rotten_queue.append(valid_neighbor)
        if rot_flag == False and len(fresh_set) != 0:
            return -1
        minute_counter += 1
        
    return minute_counter