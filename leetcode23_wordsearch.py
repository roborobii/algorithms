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


'''
Above is code that is implemented from scratch

Below is a more efficient algorithm in C++
class Solution {
private:
    bool dfs(vector<vector<char>>& board, int row, int col, const string &word, int start, int M, int N, int sLen)
    {
        char curC;
        bool res = false;
        if( (curC = board[row][col]) != word[start]) return false;
        if(start==sLen-1) return true;
        board[row][col] = '*';
        if(row>0) res = dfs(board, row-1, col, word, start+1, M, N, sLen);
        if(!res && row < M-1) res = dfs(board, row+1, col, word, start+1, M, N, sLen);
        if(!res && col > 0)   res = dfs(board, row, col-1, word, start+1, M, N, sLen);
        if(!res && col < N-1) res = dfs(board,  row, col+1, word, start+1, M, N, sLen);
        board[row][col] = curC;
        return res;
    }
    
public:
    bool exist(vector<vector<char>>& board, string word) {
        int M,N,i,j,sLen = word.size();
        if( (M=board.size()) && (N=board[0].size()) && sLen)
        {
            for(i=0; i<M; ++i)
                for(j=0; j<N; ++j)
                    if(dfs(board, i, j, word, 0, M, N, sLen)) return true;
        }
        return false;
    }
};

'''