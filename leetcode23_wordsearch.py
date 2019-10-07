class Solution:
    def exist(self, board, word):
        # depth first search/backtracking
        # go through every element in the 2d array board
            # get all the valid neighboring, visited set in the current iteration
            # recursively call (depth first search on that)
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                visited = set()
                if word[0] == board[row][col]:
                    visited.add((row,col))
                    if (self.exists_helper(board, row, col, word,1, visited)): return True
        return False
    
    def exists_helper(self, board, row, col, word, current, visited):
        # get valid neighboring, and recursively call (depth first/backtrack)
        def valid(row, col):
            return -1 < row and row < len(board) and -1 < col and col <len(board[0]) # within bounds
            
        def get_neighbors(i, j):
            result = []
            if valid(i,j-1): result.append((i,j-1))
            if valid(i,j+1): result.append((i,j+1))
            if valid(i-1,j): result.append((i-1,j))
            if valid(i+1,j): result.append((i+1,j))
            return result
        
        if current >= len(word):
            return True
        else:
            for neighbor in get_neighbors(row, col):
                if neighbor not in visited and board[neighbor[0]][neighbor[1]] == word[current]:
                    visited.add(neighbor)
                    if self.exists_helper(board, neighbor[0], neighbor[1], word, current+1, visited): return True
                    visited.remove(neighbor)
            return False

a = Solution()
a.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCED")
