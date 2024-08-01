# N queens

[Problem link](https://leetcode.com/problems/n-queens)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/n-queens

class Solution {
 public:
  vector<vector<string>> solveNQueens(int n) {
    vector<string> boardbase(n, string(n, '.'));

    vector<vector<string>> ret;
    vector<int> perm(n);
    iota(perm.begin(), perm.end(), 0);
    do {
      int flag = true;
      for (int i = 0; flag and i < n; ++i)
        for (int j = 0; flag and j < i; ++j)
          if (abs(perm[i] - perm[j]) == i - j) flag = false;
      if (flag) {
        vector<string> board = boardbase;
        for (int i = 0; i < n; ++i) board[i][perm[i]] = 'Q';
        ret.push_back(board);
      }
    } while (next_permutation(perm.begin(), perm.end()));
    return ret;
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/n-queens

class Solution:
    def backtrack(self, n, i, blocked, board, ret):
        if i == n:
            ret.append([''.join(row) for row in board])
            return
        
        for j in range(n):
            if blocked[i][j]: continue

            board[i][j] = 'Q'
            for k in range(1, n-i):
                blocked[i+k][j] += 1
                if j+k < n: blocked[i+k][j+k] += 1
                if j-k >= 0: blocked[i+k][j-k] += 1

            self.backtrack(n, i+1, blocked, board, ret)
            board[i][j] = '.'
            for k in range(1, n-i):
                blocked[i+k][j] -= 1
                if j+k < n: blocked[i+k][j+k] -= 1
                if j-k >= 0: blocked[i+k][j-k] -= 1
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        blocked = [[0 for i in range(n)] for j in range(n)]
        board = [['.' for i in range(n)] for j in range(n)]
        ret = []
        self.backtrack(n, 0, blocked, board, ret)
        return ret
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)
* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
