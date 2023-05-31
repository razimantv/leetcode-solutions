# Surrounded regions

[Problem link](https://leetcode.com/problems/surrounded-regions)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/surrounded-regions

class Solution {
 public:
  void dfs(vector<vector<char>>& board, int i, int j, int M, int N) {
    board[i][j] = 'P';
    if (i + 1 < M and board[i + 1][j] == 'O') dfs(board, i + 1, j, M, N);
    if (i - 1 > 0 and board[i - 1][j] == 'O') dfs(board, i - 1, j, M, N);
    if (j + 1 < N and board[i][j + 1] == 'O') dfs(board, i, j + 1, M, N);
    if (j - 1 > 0 and board[i][j - 1] == 'O') dfs(board, i, j - 1, M, N);
  }
  void solve(vector<vector<char>>& board) {
    if (board.empty()) return;
    int M = board.size(), N = board[0].size();
    for (int i = 0; i < M; i++) {
      if (board[i][0] == 'O') dfs(board, i, 0, M, N);
      if (board[i][N - 1] == 'O') dfs(board, i, N - 1, M, N);
    }
    for (int i = 0; i < N; i++) {
      if (board[0][i] == 'O') dfs(board, 0, i, M, N);
      if (board[M - 1][i] == 'O') dfs(board, M - 1, i, M, N);
    }

    for (auto& r : board)
      for (auto& c : r) {
        if (c == 'P')
          c = 'O';
        else
          c = 'X';
      }
  }
};
```